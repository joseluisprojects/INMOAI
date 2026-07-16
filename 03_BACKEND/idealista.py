from humano import esperar, mover_raton


def abrir_inicio(page):

    print("Abriendo Idealista...")

    tiempo = esperar()
    page.wait_for_timeout(int(tiempo * 1000))

    mover_raton(page)

    page.goto("https://www.idealista.com")

    tiempo = esperar(3, 6)
    page.wait_for_timeout(int(tiempo * 1000))