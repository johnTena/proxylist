#!/usr/bin/env python3
import argparse
import requests
from bs4 import BeautifulSoup
def get_args():
    parser = argparse.ArgumentParser(description='Obtener una lista de proxies gratuitos.')
    parser.add_argument('-n','--numero',type=int,help='Numero de proxies a mostrar (por defecto se muestran todos.)')
    args = parser.parse_args()
    if args.numero > 0 and args.numero < 150:
        return args.numero
    else:
        return None
def obtener_proxies(cantidad=None):
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    proxies = []
    table = soup.find('table')
    rows = table.tbody.find_all('tr')
    if cantidad is not None:
        rows = rows[:cantidad]
    for row in rows:
        cols = row.find_all('td')
        ip = cols[0].text
        port = cols[1].text
        https = cols[6].text == 'yes'
        if https:
            proxy = f"https://{ip}:{port}"
        else:
            proxy = f"http://{ip}:{port}"
        proxies.append(proxy)
    return proxies
if __name__ == '__main__':
    nums = get_args()
    proxies = obtener_proxies(nums)
    print("\n[+] Proxies:\n")
    for proxy in proxies:
        print(f"\t{proxy}")
    if nums is None:
        print("[x] Error de argumento, rango: 1-150")
