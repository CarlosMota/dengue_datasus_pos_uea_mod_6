from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# -----------------------------
# Identificação da Notificação
# -----------------------------
class IdentificacaoNotificacao(BaseModel):
    tp_not: str = Field(..., description="Tipo de Notificação (1=Negativa, 2=Individual, 3=Surto, 4=Agregado)")
    id_agravo: str
    dt_notific: date
    sem_not: str
    nu_ano: str
    sg_uf_not: str
    id_municip: str
    id_regiona: Optional[str]
    id_unidade: Optional[str]