# Integração de Sistemas de Informação - Projeto ETL com KNIME

Este projeto foi desenvolvido para a unidade curricular **Integração de Sistemas de Informação** do curso de **Licenciatura em Engenharia de Sistemas Informáticos**. O objetivo é demonstrar a aplicação de processos ETL (Extração, Transformação e Carregamento) utilizando o KNIME, com dados de eventos de calendário extraídos de ficheiros ICS.

## Objetivo do Projeto

Desenvolver um workflow que:
- Extrai dados de eventos de calendário via API Google Calendar (em Python).
- Converte ficheiros ICS para CSV para processamento no KNIME.
- Normaliza e armazena dados em bases de dados SQL.
- Gera dashboards e envia notificações automáticas de eventos futuros.

## Estrutura do Projeto

1. **Extração de Dados**: Scripts em Python para extrair e converter ficheiros ICS.
2. **Processamento no KNIME**:
   - Transformações e manipulação de dados com Regex e filtros.
   - Armazenamento em SQL e geração de dashboards.
3. **Notificações Automáticas**: Envio de alertas por e-mail com os próximos eventos.

## Requisitos

- **Python** (para a extração de dados via API e outros scripts)
- **KNIME** (para processamento de dados e criação de dashboards)
- **Base de Dados SQL** (para armazenamento dos dados)

## Como Utilizar

1. Execute o script Python para obter o ficheiro .ICS apartir da API ou use .ICS do seu calendario.
2. Execute o script Python para converter .ICS e em .CSV.
3. Importe o workflow no KNIME e ajuste os parâmetros de conexão, como o caso da base de dados.
4. Execute o workflow para processar os dados e gerar os devidos relatórios.

**Aluno A20746**
