from enum import Enum


class EstadoExpediente(Enum):

    NUEVO = "Nuevo"

    ANALIZADO = "Analizado"

    PENDIENTE_WHATSAPP = "Pendiente WhatsApp"

    WHATSAPP_ENVIADO = "WhatsApp enviado"

    RESPONDIO = "Respondió"

    INTERESADO = "Interesado"

    LLAMADA_PROGRAMADA = "Llamada programada"

    CAPTADO = "Captado"

    DESCARTADO = "Descartado"