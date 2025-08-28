from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Encerramento(BaseModel):
    classi_fin: Optional[str]
    criterio: Optional[str]
    dt_encerra: Optional[date]
    evolucao: Optional[str]
    dt_obito: Optional[date]