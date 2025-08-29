"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 

O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 

máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.

"""

import requests
from datetime import datetime
import locale

def formatar_moeda(valor):
    """Formata um valor numérico para o padrão de moeda brasileiro."""
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(float(valor), grouping=True, symbol=True)
    except (ValueError, locale.Error):
        try:
            valor_float = float(valor)
            return f"R$ {valor_float:.2f}".replace('.', ',')
        except ValueError:
            return valor

def consultar_cotacao():
    """
    Consulta a cotação de uma moeda estrangeira em relação ao BRL
    e exibe os detalhes para o usuário.
    """
    codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

    if not codigo_moeda:
        print("\nErro: Nenhum código de moeda foi informado.")
        return

    url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"

    print(f"\nBuscando cotação para {codigo_moeda}...")

    try:
        response = requests.get(url)
        response.raise_for_status() 

        dados = response.json()
        chave_cotacao = f"{codigo_moeda}BRL"

        if chave_cotacao not in dados:
             print(f"\nErro: A moeda '{codigo_moeda}' não foi encontrada ou não possui cotação para BRL.")
             return

        cotacao_info = dados[chave_cotacao]

        nome = cotacao_info.get('name')
        valor_atual = cotacao_info.get('bid')
        valor_maximo = cotacao_info.get('high')
        valor_minimo = cotacao_info.get('low') 
        timestamp = int(cotacao_info.get('timestamp'))

        data_atualizacao = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        print("\n--- Cotação Encontrada ---")
        print(f"Moeda: {nome}")
        print(f"Valor Atual: {formatar_moeda(valor_atual)}")
        print(f"Máxima do Dia: {formatar_moeda(valor_maximo)}")
        print(f"Mínima do Dia: {formatar_moeda(valor_minimo)}")
        print(f"Última Atualização: {data_atualizacao}")
        print("--------------------------")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"\nErro: Código de moeda '{codigo_moeda}' inválido ou não encontrado na API.")
        else:
            print(f"\nErro HTTP ao consultar a API: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"\nErro de conexão: Não foi possível acessar a API. Verifique sua internet. Detalhes: {req_err}")
    except KeyError:
        print("\nErro: A resposta da API não continha os dados esperados. Tente novamente mais tarde.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")


if __name__ == "__main__":
    consultar_cotacao()