import json


def calcular_faturamento(dados):
    # Extrair os valores de faturamento diário
    faturamento_diario = [valor for valor in dados.values() if valor > 0]

    if not faturamento_diario:
        return {
            "menor_valor": None,
            "maior_valor": None,
            "dias_acima_media": 0
        }

    # Calcular o menor e o maior valor de faturamento
    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)

    # Calcular a média mensal
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    # Contar o número de dias com faturamento acima da média
    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_media": dias_acima_media
    }


# Função para ler dados de um arquivo JSON
def ler_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        return json.load(arquivo)


# Exemplo de uso
if __name__ == "__main__":
    caminho_arquivo = 'faturamento.json'  # Substitua pelo caminho do seu arquivo JSON
    dados = ler_dados_json(caminho_arquivo)

    resultado = calcular_faturamento(dados)

    print("Menor valor de faturamento:", resultado["menor_valor"])
    print("Maior valor de faturamento:", resultado["maior_valor"])
    print("Número de dias com faturamento acima da média:", resultado["dias_acima_media"])
