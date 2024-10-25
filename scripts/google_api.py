from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from icalendar import Calendar, Event, vDatetime
import os
import datetime
from dateutil.parser import parse as date_parse

# Definir o escopo de acesso ao Google Calendar
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Carregar as credenciais ou gerar nova autorização
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

    # Guardar o token para futuras execuções
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Conectar à API do Google Calendar
service = build('calendar', 'v3', credentials=creds)

# Definir o ID do calendário principal
calendar_id = 'carlosaraujotechnology@gmail.com'

# Obter todos os eventos do Google Calendar (removido o timeMin)
events_result = service.events().list(calendarId=calendar_id,
                                      singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

# Criar ficheiro .ics
cal = Calendar()

# Adicionar informações do calendário
cal.add('prodid', '-//Google Inc//Google Calendar 70.9054//EN')
cal.add('version', '2.0')
cal.add('calscale', 'GREGORIAN')
cal.add('method', 'PUBLISH')
cal.add('X-WR-CALNAME', calendar_id)
cal.add('X-WR-TIMEZONE', 'Europe/Lisbon')

# Adicionar informação de fuso horário neste caso Europe/Lisbon
timezone = """
BEGIN:VTIMEZONE
TZID:Europe/Lisbon
X-LIC-LOCATION:Europe/Lisbon
BEGIN:DAYLIGHT
TZOFFSETFROM:+0000
TZOFFSETTO:+0100
TZNAME:GMT+1
DTSTART:19700329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0100
TZOFFSETTO:+0000
TZNAME:GMT
DTSTART:19701025T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
"""
cal.add_component(Calendar.from_ical(timezone))

# Processar cada evento
for event in events:
    ev = Event()
    ev.add('summary', event.get('summary', 'Sem título'))

    # Tratar data de início e fim
    start = event['start'].get('dateTime', event['start'].get('date'))
    ev.add('dtstart', vDatetime(date_parse(start)))

    end = event['end'].get('dateTime', event['end'].get('date'))
    ev.add('dtend', vDatetime(date_parse(end)))

    # Adicionar outros campos do evento
    ev.add('dtstamp', vDatetime(datetime.datetime.utcnow()))  # Data atual como DTSTAMP
    ev.add('uid', event.get('id'))  # Usar o ID do evento do Google como UID
    ev.add('created', vDatetime(date_parse(event['created'])))
    ev.add('last-modified', vDatetime(date_parse(event['updated'])))
    ev.add('sequence', event.get('sequence', 0))
    ev.add('status', event.get('status', 'CONFIRMED'))
    ev.add('transp', 'OPAQUE')  # Definir como ocupado

    # Adicionar o campo LOCATION, mesmo que esteja vazio
    ev.add('location', event.get('location', ''))

    cal.add_component(ev)

# Guardar num ficheiro .ics
with open('meu_calendario_google.ics', 'wb') as f:
    f.write(cal.to_ical())

print("Ficheiro .ics criado com sucesso!")
