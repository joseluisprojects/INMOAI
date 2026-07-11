import sys
import os
import random

sys.path.append(os.path.abspath("02_AGENTES"))

from playwright.sync_api import sync_playwright
from config import *
from agente_captador import *

def esperar_humano(minimo=1, maximo=3):
    tiempo = random.uniform(minimo, maximo)
    print(f"Esperando {tiempo:.2f} segundos...")
    return tiempo

print("HALCÓN v2 iniciando...")

with sync_playwright() as p:

    browser = p.chromium.launch(headless=not NAVEGADOR_VISIBLE)

    page = browser.new_page()

    page.set_viewport_size({"width": 1366, "height": 768})

    page.set_extra_http_headers({
        "Accept-Language": "es-ES,es;q=0.9"
    })

    print("Abriendo Idealista...")

    tiempo = esperar_humano()

    page.wait_for_timeout(int(tiempo * 1000))

    page.goto("https://www.idealista.com")

    tiempo = esperar_humano(3, 6)

    page.wait_for_timeout(int(tiempo * 1000))

    browser.close()

print("HALCÓN v2 terminó su trabajo.")