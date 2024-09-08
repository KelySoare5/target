import json
import xml.etree.ElementTree as ET
import os

def analisa_faturamento(faturamento_diario):

    if not faturamento_diario:
        return 'O vetor de faturamento está vazio.'

    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)
    
    return {
        'menor_valor': menor_valor,
        'maior_valor': maior_valor,
        'dias_acima_media': dias_acima_media
    }

def processa_json(caminho_json):
    if not os.path.exists(caminho_json):
        raise FileNotFoundError(f'Arquivo não encontrado: {caminho_json}')
    with open(caminho_json, 'r') as file:
        dados = json.load(file)
    return [item['valor'] for item in dados]

def processa_xml(caminho_xml):
    if not os.path.exists(caminho_xml):
        raise FileNotFoundError(f'Arquivo não encontrado: {caminho_xml}')
    with open(caminho_xml, 'r') as file:
        xml_content = file.read()
    
    if not xml_content.startswith('<root>'):
        xml_content = f'<root>{xml_content}</root>'
    
    root = ET.fromstring(xml_content)
    return [float(row.find('valor').text) for row in root.findall('row')]

caminho_json = 'dados/dados.json'
caminho_xml = 'dados/dados2.xml'

try:
    faturamento_json = processa_json(caminho_json)
    faturamento_xml = processa_xml(caminho_xml)

except FileNotFoundError as e:
    print(e)
    exit(1)

except ET.ParseError as e:
    print(f'Erro ao analisar o arquivo XML: {e}')
    exit(1)

faturamento_diario = faturamento_json + faturamento_xml

resultados = analisa_faturamento(faturamento_diario)
print(f'Faturamento diário combinado: {faturamento_diario}')
print(f'Menor valor de faturamento: {resultados["menor_valor"]}')
print(f'Maior valor de faturamento: {resultados["maior_valor"]}')
print(f'Número de dias com faturamento acima da média mensal: {resultados["dias_acima_media"]}')
