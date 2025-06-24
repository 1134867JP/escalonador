from dataclasses import dataclass
from typing import Optional

@dataclass
class Tarefa:
    """
    Representa uma tarefa no escalonador com múltiplas filas e HRRN.
    """
    id: str
    chegada: int
    duracao: int
    nivel_prioridade: int
    tempo_inicio: Optional[int] = None
    tempo_termino: Optional[int] = None
