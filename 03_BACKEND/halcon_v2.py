import sys
import os

sys.path.append(os.path.abspath("02_AGENTES"))

from navegador import iniciar_navegador
from idealista import abrir_inicio
from config import *
from agente_captador import *

print("HALCÓN v2 iniciando...")

playwright, context, page = iniciar_navegador(NAVEGADOR_VISIBLE)

abrir_inicio(page)

context.close()
playwright.stop()

print("HALCÓN v2 terminó su trabajo.")