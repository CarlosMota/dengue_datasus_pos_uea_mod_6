from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Paciente(BaseModel):
    dt_sin_pri: Optional[date]
    sem_pri: Optional[str]
    ano_nasc: Optional[str]
    nu_idade_n: Optional[int]
    cs_sexo: Optional[str]
    cs_gestant: Optional[str]
    cs_raca: Optional[str]
    cs_escol_n: Optional[str]

