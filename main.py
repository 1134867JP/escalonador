import argparse
from escalonador import escalonador_hrrn
from utils import (
    carregar_tarefas_json,
    carregar_tarefas_csv,
    gerar_tarefas_aleatorias,
    exibir_tabela,
    calcular_metricas,  # Adicionada a importação
)
from tarefas import Tarefa

def main():
    parser = argparse.ArgumentParser(description="Simulador de Escalonamento Multinível com HRRN")
    parser.add_argument("-j", "--json", help="Arquivo JSON com tarefas")
    parser.add_argument("-c", "--csv", help="Arquivo CSV com tarefas")
    parser.add_argument("-a", "--aleatorio", type=int, help="Quantidade de tarefas aleatórias")
    parser.add_argument("--seed", type=int, help="Semente para geração aleatória")
    parser.add_argument("-n", "--classes", type=int, default=3, help="Número de filas de prioridade")
    args = parser.parse_args()

    # Carrega tarefas
    if args.json:
        tarefas = carregar_tarefas_json(args.json)
    elif args.csv:
        tarefas = carregar_tarefas_csv(args.csv)
    elif args.aleatorio:
        tarefas = gerar_tarefas_aleatorias(args.aleatorio, seed=args.seed)
    else:
        print("Nenhuma fonte de tarefas fornecida. Use --json, --csv ou --aleatorio.")
        return

    # Executa o escalonador
    resultados = escalonador_hrrn(tarefas, numero_classes=args.classes)

    # Calcula métricas e exibe resultados
    metricas = calcular_metricas(resultados)
    exibir_tabela(metricas)

if __name__ == "__main__":
    main()