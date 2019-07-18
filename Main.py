def fcfs(entradas):
	fila=entradas.copy()
	tempo_atual=0
	retorno=[]
	resposta=[]
	Nentradas=len(entradas)
	for x in range(0,Nentradas):
		processo=fila.pop(0)
		resposta.append(tempo_atual-int(processo[1]))
		tempo_atual+=int(processo[0])
		retorno.append(tempo_atual-int(processo[1]))
	return (sum(retorno) / float(len(retorno))),(sum(resposta) / float(len(resposta)))

def sjf(entradas,preempcao):
	fila=entradas.copy()
	Nentradas=len(entradas)
	tempo_atual=0
	retorno=[0] * Nentradas
	resposta=[0] * Nentradas
	espera=[0] * Nentradas
	while x in range(0,Nentradas):
		if()
		#resposta.append(tempo_atual-int(processo[1]))
		#tempo_atual+=int(processo[0])
		#retorno.append(tempo_atual-int(processo[1]))
	





f=open("entrada.txt", "r")	
f1 =f.readlines()
entradas = [] 
for x in f1:
	chegada,duracao=x.split()
	entradas.append((duracao,chegada))
entradas = sorted(entradas, key=lambda tup: tup[1])
retorno,resposta=fcfs(entradas)
print("FCFS " + str(retorno)+" "+str(resposta)+" "+str(resposta))
sjf(entradas,False)


