from playwright.sync_api import sync_playwright


def iniciar_navegador(visible=True):

    playwright = sync_playwright().start()

    context = playwright.chromium.launch_persistent_context(
        user_data_dir="11_PERFILES/HALCON",
        headless=not visible
    )

    page = context.pages[0]

    page.set_viewport_size({
        "width": 1366,
        "height": 768
    })

    page.set_extra_http_headers({
        "Accept-Language": "es-ES,es;q=0.9"
    })

    return playwright, context, page