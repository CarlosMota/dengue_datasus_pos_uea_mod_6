from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Comorbidades(BaseModel):
    diabetes: Optional[int]
    hematolog: Optional[int]
    hepatopat: Optional[int]
    renal: Optional[int]
    hipertensa: Optional[int]
    acido_pept: Optional[int]
    auto_imune: Optional[int]