from bs4 import BeautifulSoup
import requests
import re

ORDER_BY = {
    'tipo': 'Tipo',
    'valor_unitario': 'Valor Unitário <i class="bi bi-arrow-up"></i>',
    '-valor_unitario': 'Valor Unitário <i class="bi bi-arrow-down"></i>',
    'valor_ultima_venda': 'Valor Última Venda <i class="bi bi-arrow-up"></i>',
    '-valor_ultima_venda': 'Valor Última Venda <i class="bi bi-arrow-down"></i>',
}

URL = 'https://economizaalagoas.sefaz.al.gov.br/exibicaoPrecoCombustivel.htm?codTipoCombustivel=1'


def obter_dados():
    """
    Função para a raspagem de dados. Primeiro obtendo o HTML da página e depois
    extraindo os dados significantes, retornando uma lista com os mesmos.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    cards = soup.find_all(name='div', attrs={'class': 'cartao'})

    dados = []

    for card in cards:
        tipo = card.find(
            name='h6'
        ).text

        valor_unitario = card.find(
            name='span', attrs={'class': 'valor_unitario'}
        ).text.strip().split()[1].replace(',', '.')

        valor_ultima_venda = card.find(
            name='span', attrs={'class': 'valor_ultima_venda'}
        ).text.strip().split()[1].replace(',', '.')

        tempo_ultima_venda = card.find_all(
            name='span', attrs={'class': None}
        )[2].text

        contribuinte = re.sub(r' +', ' ', card.find(
            name='div', attrs={'class': 'cartao_contribuinte_bloco_esquerdo'}
        ).text).strip()

        codigo = card.find_all(
            name='li', attrs={'class': 'menu_item'}
        )[1]['onclick'].split("'")[1]

        dados.append({
            'tipo': tipo,
            'valor_unitario': valor_unitario,
            'valor_ultima_venda': valor_ultima_venda,
            'tempo_ultima_venda': tempo_ultima_venda,
            'contribuinte': contribuinte,
            'codigo': codigo,
        })

    return dados
