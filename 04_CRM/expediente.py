from dataclasses import dataclass
from datetime import datetime


@dataclass
class Expediente:

    id: str

    portal: str

    url: str

    propietario: str

    telefono: str

    whatsapp: bool

    zona: str

    precio: float

    fecha_publicacion: str

    dias_publicado: int

    rebajas: int

    prioridad: str

    estado: str

    fecha_creacion: datetime

    observaciones: str = ""