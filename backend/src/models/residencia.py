from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Residencia(BaseModel):
    sg_uf: str
    id_mn_resi: str
    id_rg_resi: Optional[str]
    id_pais: Optional[str]
    dt_invest: Optional[date]
    id_ocupa_n: Optional[str]