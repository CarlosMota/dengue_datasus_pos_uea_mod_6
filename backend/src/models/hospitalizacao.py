from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Hospitalizacao(BaseModel):
    hospitaliz: Optional[str]
    dt_interna: Optional[date]
    coufinf: Optional[str]
    municipio: Optional[str]
    tpautocto: Optional[str]

