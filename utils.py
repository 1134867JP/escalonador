from typing import List, Dict, Optional
import json
import pandas as pd
from tabulate import tabulate
from tarefas import Tarefa
import random
import os

def carregar_tarefas_json(caminho: str) -> List[Tarefa]:
    """
    Carrega tarefas de um arquivo JSON.
    """
    if not caminho.endswith(".json"):
        raise ValueError(f"O arquivo fornecido '{caminho}' não é um arquivo JSON.")
    with open(caminho, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    return [Tarefa(**item) for item in dados]

def carregar_tarefas_csv(caminho: str) -> List[Tarefa]:
    """
    Carrega tarefas de um arquivo CSV.
    """
    if not caminho.endswith(".csv"):
        raise ValueError(f"O arquivo fornecido '{caminho}' não é um arquivo CSV.")
    df = pd.read_csv(caminho)
    return [Tarefa(
        id=row['id'],
        chegada=int(row['chegada']),
        duracao=int(row['duracao']),
        nivel_prioridade=int(row['nivel_prioridade'])
    ) for _, row in df.iterrows()]

def gerar_tarefas_aleatorias(n: int, max_chegada: int = 20, seed: Optional[int] = None) -> List[Tarefa]:
    if seed is not None:
        random.seed(seed)
    return [
        Tarefa(
            id=f"T{i+1}",
            chegada=random.randint(0, max_chegada),
            duracao=random.randint(1, 10),
            nivel_prioridade=random.randint(0, 2)
        ) for i in range(n)
    ]

def exibir_tabela(metricas: List[Dict]):
    headers = ["ID", "Chegada", "Duração", "Início", "Término", "Turnaround", "Espera", "Resposta", "Prioridade"]
    tabela = [[m[h] for h in headers] for m in metricas]
    print("\n=== Métricas por Tarefa ===")
    print(tabulate(tabela, headers=headers, tablefmt="fancy_grid"))

def calcular_metricas(resultados: List[Tarefa]) -> List[Dict]:
    """
    Calcula métricas como turnaround, tempo de espera e tempo de resposta para cada tarefa.
    """
    metricas = []
    for t in resultados:
        turnaround = t.tempo_termino - t.chegada
        espera = turnaround - t.duracao
        resposta = t.tempo_inicio - t.chegada
        metricas.append({
            "ID": t.id,
            "Chegada": t.chegada,
            "Duração": t.duracao,
            "Início": t.tempo_inicio,
            "Término": t.tempo_termino,
            "Turnaround": turnaround,
            "Espera": espera,
            "Resposta": resposta,
            "Prioridade": t.nivel_prioridade
        })
    return metricas