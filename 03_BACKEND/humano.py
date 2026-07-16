import random


def esperar(minimo=1, maximo=3):
    tiempo = random.uniform(minimo, maximo)
    print(f"Esperando {tiempo:.2f} segundos...")
    return tiempo


def mover_raton(page):

    print("Moviendo el ratón...")

    page.mouse.move(300, 200)

    page.wait_for_timeout(500)

    page.mouse.move(500, 350)

    page.wait_for_timeout(400)

    page.mouse.move(700, 250)