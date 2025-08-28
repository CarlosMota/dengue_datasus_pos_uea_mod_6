from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Exames(BaseModel):
    dt_coleta: Optional[date]
    resul_soro: Optional[str]
    dt_ns1: Optional[date]
    resul_ns1: Optional[str]
    dt_viral: Optional[date]
    resul_vi_n: Optional[str]
    dt_pcr: Optional[date]
    resul_pcr: Optional[str]
    sorotipo: Optional[str]
    histopa_n: Optional[str]
    imunoh_n: Optional[str]

    