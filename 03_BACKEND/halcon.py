import sys
import os

sys.path.append(os.path.abspath("02_AGENTES"))
from playwright.sync_api import sync_playwright
from config import *
from agente_captador import *
print("🦅 HALCÓN iniciando...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=not NAVEGADOR_VISIBLE)

    page = browser.new_page()

    print("Abriendo Idealista...")

    page.goto("https://www.idealista.com")

    page.wait_for_timeout(TIEMPO_ESPERA)

    browser.close()

print("✅ HALCÓN terminó su trabajo.")