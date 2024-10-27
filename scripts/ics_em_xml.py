from icalendar import Calendar
import xml.etree.ElementTree as ET
import os

def ics_to_xml(ics_file_path, xml_file_path):
    # Ler o ficheiro .ics
    with open(ics_file_path, 'r', encoding='utf-8') as ics_file:
        calendar = Calendar.from_ical(ics_file.read())

    # Criar a raiz do XML
    root = ET.Element("calendar")

    # Inicializar contagem de eventos
    event_count = 0

    # Percorrer cada componente do calendário
    for component in calendar.walk():
        # Verificar se o componente é um evento (VEVENT)
        if component.name == "VEVENT":
            event_count += 1  # Incrementar a contagem de eventos
            event = ET.SubElement(root, "event")
            
            # Extrair campos do evento e adicionar ao XML
            summary = component.get('SUMMARY', 'Sem título')
            dtstart = component.get('DTSTART').dt.isoformat() if component.get('DTSTART') else ''
            dtend = component.get('DTEND').dt.isoformat() if component.get('DTEND') else ''
            dtstamp = component.get('DTSTAMP').dt.isoformat() if component.get('DTSTAMP') else ''
            uid = component.get('UID', '')
            sequence = component.get('SEQUENCE', '0')
            created = component.get('CREATED').dt.isoformat() if component.get('CREATED') else ''
            last_modified = component.get('LAST-MODIFIED').dt.isoformat() if component.get('LAST-MODIFIED') else ''
            location = component.get('LOCATION', '')
            status = component.get('STATUS', 'confirmed')
            transp = component.get('TRANSP', 'OPAQUE')

            # Adicionar elementos ao evento no XML
            ET.SubElement(event, "summary").text = summary
            ET.SubElement(event, "dtstart").text = dtstart
            ET.SubElement(event, "dtend").text = dtend
            ET.SubElement(event, "dtstamp").text = dtstamp
            ET.SubElement(event, "uid").text = uid
            ET.SubElement(event, "sequence").text = sequence
            ET.SubElement(event, "created").text = created
            ET.SubElement(event, "lastModified").text = last_modified
            ET.SubElement(event, "location").text = location
            ET.SubElement(event, "status").text = status
            ET.SubElement(event, "transp").text = transp

    # Verificar se foram encontrados eventos
    if event_count == 0:
        print("Nenhum evento encontrado no ficheiro .ics.")
    else:
        print(f"{event_count} eventos encontrados e convertidos para XML.")

    # Converter a árvore XML para string e salvar no ficheiro .xml
    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)

    print(f"Ficheiro XML criado com sucesso em {xml_file_path}")

# Caminhos para os ficheiros de entrada e saída
ics_file_path = "meu_calendario_google.ics"
xml_file_path = "meu_calendario_google.xml"

# Executar a conversão
ics_to_xml(ics_file_path, xml_file_path)
