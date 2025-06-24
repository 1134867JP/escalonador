from typing import List, Dict
from tarefas import Tarefa

def escalonador_hrrn(tarefas: List[Tarefa], numero_classes: int) -> List[Tarefa]:
    """
    Executa o escalonamento por múltiplas filas com HRRN interno.
    """
    pendentes = sorted(tarefas, key=lambda t: t.chegada)
    filas: Dict[int, List[Tarefa]] = {i: [] for i in range(numero_classes)}
    concluidas: List[Tarefa] = []
    tempo_atual = 0

    while pendentes or any(filas.values()):
        # Enfileira tarefas que chegaram
        while pendentes and pendentes[0].chegada <= tempo_atual:
            t = pendentes.pop(0)
            filas[t.nivel_prioridade].append(t)
            print(f"[Tick {tempo_atual}] Tarefa {t.id} chegou na fila {t.nivel_prioridade}")

        # Seleciona a próxima fila com tarefas
        fila_atual = next((n for n, f in filas.items() if f), None)
        if fila_atual is None:
            tempo_atual = pendentes[0].chegada if pendentes else tempo_atual + 1
            continue

        # Calcula HRRN e seleciona a tarefa
        candidatos = filas[fila_atual]
        rr_list = [((tempo_atual - t.chegada + t.duracao) / t.duracao, idx) for idx, t in enumerate(candidatos)]
        hrnn_max, idx_max = max(rr_list, key=lambda x: x[0])
        tarefa = candidatos.pop(idx_max)

        # Executa a tarefa
        tarefa.tempo_inicio = tempo_atual
        print(f"[Tick {tempo_atual}] Iniciando {tarefa.id} (fila {fila_atual}, HRRN={hrnn_max:.2f})")
        tempo_atual += tarefa.duracao
        tarefa.tempo_termino = tempo_atual
        print(f"[Tick {tempo_atual}] Concluiu {tarefa.id}")
        concluidas.append(tarefa)

    return concluidas