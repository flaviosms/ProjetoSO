# Trabalho 1
Esse trabalho trata-se de um simulador de escalonador de processos,ele simuala a execucao de processos em três algoritmos de escalonamento diferentes First Come First Served(FCFS), Shortest Job First(SJF) e Round Robin(RR) e sua saída são metricas dessas simulações:
Media do tempo de retorno , do tempo de resposta e do tempo de espera.
Alguns parâmetros podem ser alterados no programa como o Quantum do RR , se o SJF tem preempção ou não e se quer sejam printadas na tela informações adicionais sobre a fila de execução ou métricas completas sem ser as médias apenas.
Esse programa usa como entrada o arquivo entrada.txt contido na mesma pasta do codigo fonte no padrão:
[tempo_de_chegada]" "[tempo_de_pico]
[tempo_de_chegada]" "[tempo_de_pico]
...

# Trabalho 2 
Já nesse trabalho simulamos como o funcionam 3 algoritmos de substituição de páginas para alocar dados na memória RAM a partir da memória virtual, esses três são First-in First-out(FIFO), Algorítmo Ótimo(OTM) e Least Recently Used(LRU):
O retorno desse programa é o número de Page Faults ocorridas durante a simulação para cada algoritmo.
Esse programa usa como entrada o arquivo entrada2.txt contido na mesma pasta do codigo fonte no padrão:
[Quadros_disponíveis_na_RAM]
[Pagina]
[Pagina]
[Pagina]
[Pagina]
[Pagina]
...
