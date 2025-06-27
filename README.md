# Escalonamento com Múltiplas Filas

## Integrantes do Grupo
- Fabricio Panisson  
- Jean Cesare  
- João Pedro Rodrigues  
- Nycolas Fachi  
- Ricardo Basso  
- Ricardo Groth  

## Descrição do Projeto
Este projeto simula um algoritmo de Escalonamento com Múltiplas Filas utilizando a política HRRN (Highest Response Ratio Next) para selecionar a próxima tarefa a ser executada em cada fila. A simulação busca representar cenários reais de sistemas operacionais que precisam lidar com múltiplos processos de diferentes prioridades.

## Linguagem Utilizada
- Python 3

## Algoritmo Simulado
- Escalonamento com Múltiplas Filas (Multi-level Queue Scheduling)
- Política de escalonamento interna: HRRN (Highest Response Ratio Next)

## Preparar Ambiente
```bash
pip install tabulate
```

## Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/1134867JP/escalonador
cd escalonador
```

2. Execute com entrada JSON:
```bash
python escalonador.py --json tarefas_exemplo.json
```

3. Execute com entrada CSV:
```bash
python escalonador.py --csv tarefas_exemplo.csv
```

4. Ou com tarefas geradas aleatoriamente:
```bash
python escalonador.py --aleatorio 5
```

## Análise dos Resultados
O programa imprime as métricas de cada tarefa ao final da execução, incluindo:
- Tempo de início e término
- Tempo de resposta
- Tempo de espera
- Turnaround

Estas informações são úteis para analisar o desempenho do algoritmo em diferentes cenários e prioridades de tarefas.

## Referências
- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts.
- https://en.wikipedia.org/wiki/Scheduling_(computing)
- https://www.geeksforgeeks.org/hrrn-scheduling/

## Dados de Entrada
O repositório inclui arquivos `tarefas_exemplo.json` e `tarefas_exemplo.csv` que podem ser utilizados para testes.

## Código-fonte
O código está modularizado e comentado em:
- escalonador.py
- tarefas.py
- utils.py
