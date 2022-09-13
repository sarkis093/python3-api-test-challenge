import schedule
import requests
import json
import sys
import pandas as pd
from config import api_key

header = {'API_KEY': f'{api_key}'}

commodityCode = 801
countryCode = [2010, 5700]
marketYear = 2022

def soybeens(commodity, countrys, year):
    for country in countrys:
        URL = f'https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/{commodity}/countryCode/{country}/marketYear/{year}'
        r = requests.get(url=URL, headers=header)
        arr = r.json()
        country_name = 'china' if int(5700) == country else 'mexico'
        text = json.dumps(arr)
        df = pd.read_json(text)
        df.to_csv(f'{country_name}.csv', index=None)

soybeens(commodityCode, countryCode, marketYear)

## Agendando a próxima execução em uma semana.
ret = schedule.every(1).week.do(soybeens, args=(commodityCode, countryCode, marketYear))

## printa na tela confirmando a próxima execução.
sys.stdout.writelines(f'{ret}\n')
