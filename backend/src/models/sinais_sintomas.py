from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


# -----------------------------
# Sinais e Sintomas
# -----------------------------
class SinaisSintomas(BaseModel):
    febre: Optional[int]
    mialgia: Optional[int]
    cefaleia: Optional[int]
    exantema: Optional[int]
    vomito: Optional[int]
    nausea: Optional[int]
    dor_costas: Optional[int]
    conjuntvit: Optional[int]
    artrite: Optional[int]
    artralgia: Optional[int]
    petequia_n: Optional[int]
    leucopenia: Optional[int]
    laco: Optional[int]
    dor_retro: Optional[int]

