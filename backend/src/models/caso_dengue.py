from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from src.models.comorbidades import Comorbidades
from src.models.encerramento import Encerramento
from src.models.exames import Exames
from src.models.hospitalizacao import Hospitalizacao
from src.models.sinais_sintomas import SinaisSintomas
from src.models.residencia import Residencia
from src.models.paciente import Paciente
from src.models.identificacao_notificacao import IdentificacaoNotificacao


class CasoDengue(BaseModel):
    identificacao: IdentificacaoNotificacao
    paciente: Paciente
    residencia: Residencia
    sinais: Optional[SinaisSintomas]
    comorbidades: Optional[Comorbidades]
    exames: Optional[Exames]
    hospitalizacao: Optional[Hospitalizacao]
    encerramento: Optional[Encerramento]