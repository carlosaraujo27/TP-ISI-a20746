from icalendar import Calendar
import csv
import warnings

# Supressão do aviso
warnings.filterwarnings("ignore", category=FutureWarning)

def ics_to_csv(ics_file_path, csv_file_path):
    # Lê o ficheiro .ics com encoding UTF-8
    with open(ics_file_path, 'r', encoding='utf-8') as ics_file:
        calendar = Calendar.from_ical(ics_file.read())

    # Abre o ficheiro .csv para escrita com encoding UTF-8
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        # Escreve o cabeçalho do CSV
        writer.writerow(['Conteúdo do Evento'])

        # Percorre cada evento no calendário
        for component in calendar.walk():
            if component.name == "VEVENT":
                # Serializar o evento completo
                event_content = component.to_ical().decode('utf-8')

                # Verificar se o campo LOCATION existe e, caso não exista, adicioná-lo vazio
                if 'LOCATION' not in event_content:
                    # Inserir LOCATION logo após o DTSTART, para manter o formato
                    event_content = event_content.replace('DTSTART', 'LOCATION:\r\nDTSTART')

                # Escreve o conteúdo do evento no CSV
                writer.writerow([event_content])

    print(f"Ficheiro .ics foi convertido para {csv_file_path} com sucesso.")

# Caminhos dos ficheiros
ics_file_path = 'C:/Users/Carlos/knime-workspace/TP-ISI-a20746/scripts/meu_calendario_google.ics'
csv_file_path = 'C:/Users/Carlos/knime-workspace/TP-ISI-a20746/scripts/meu_calendario_google.csv'

# Executa a função de conversão
ics_to_csv(ics_file_path, csv_file_path)
