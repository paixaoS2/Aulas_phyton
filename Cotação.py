import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    cotacao = json.loads(requisicao.text)

    print('     Cotação', datetime.datetime.now())
    print('Dolar: R$',cotacao['USDBRL']['ask'])
    print('Euro: R$',cotacao['EURBRL']['ask'])
    print('Bitcoin: R$',cotacao['BTCBRL']['ask'])
    time.sleep(2)