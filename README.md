# Proxy List Project

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📖 Introducción

Este proyecto es que genera un listado de proxys gratuitos y categorizados para su uso en diferentes escenarios, como pruebas de pentesting, anonimización de tráfico, y más. **Por favor, usa estos proxys de manera ética y legal.**

## 🚀 Características

- ✅ Listado de proxys 
- ✅ Actualizaciones automáticas a través de un script.
- ✅ Integración con herramientas de pentesting.
- ✅ Soporte para múltiples protocolos (HTTP, HTTPS, SOCKS4, SOCKS5).

## 📋 Requisitos

- Python 3.8+
- Requests Library
- Argparse
- BeautifulSoup

## ⚙️ Uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/johnaTena/proxylist.git
   cd proxylist
   ./proxy-list -h

   usage: proxy-list.py [-h] [-n NUMERO]

   Obtener una lista de proxies gratuitos.

   options:
     -h, --help            show this help message and exit
     -n NUMERO, --numero NUMERO
                        Numero de proxies a mostrar (por defecto se muestran todos.)
