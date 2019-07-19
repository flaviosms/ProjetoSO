def fcfs(entradas):
	fila=[x[:] for x in entradas]
	tempo_atual=0
	retorno=[]
	resposta=[]
	Nentradas=len(entradas)
	for x in range(0,Nentradas):
		processo=fila.pop(0)
		resposta.append(tempo_atual-int(processo[1]))
		tempo_atual+=int(processo[0])
		retorno.append(tempo_atual-int(processo[1]))
	return (sum(retorno) / float(len(retorno))),(sum(resposta) / float(len(resposta))),(sum(resposta) / float(len(resposta)))
#####################################################################################
def sjf(entradas,preempcao):
	fila=[x[:] for x in entradas]
	Nentradas=len(entradas)
	tempo_atual=0
	retorno=[]
	resposta=[]
	espera=[]
	pronto=[]
	if(preempcao):
		while tempo_atual>=0:
			if(len(fila)>0 and fila[0][1]==tempo_atual):
				pronto.append(fila.pop(0))
			else:
				if(len(pronto)==0):
					if(len(fila)==0):
						break
					else:
						tempo_atual+=1
						continue
				pronto=sorted(pronto, key=lambda tup: tup[0])
				print(pronto)
				if(pronto[0][2]>0):
					resposta.append(tempo_atual-int(pronto[0][1]))
					pronto[0][2]=pronto[0][2]*-1
				
				tempo_atual+=1
				
				pronto[0][0]-=1
				if(pronto[0][0]==0):
					retorno.append(tempo_atual-int(pronto[0][1]))
					espera.append(tempo_atual-int(pronto[0][1])+pronto[0][2])
					pronto.pop(0)
	else:
		while tempo_atual>=0:
			if(len(fila)>0 and fila[0][1]==tempo_atual):
				pronto.append(fila.pop(0))
				if(pronto[0][2]>0):
					pronto=sorted(pronto, key=lambda tup: tup[0])
			else:
				if(len(pronto)==0):
					if(len(fila)==0):
						break
					else:
						tempo_atual+=1
						continue
				if(pronto[0][2]>0):
					resposta.append(tempo_atual-int(pronto[0][1]))
					pronto[0][2]=pronto[0][2]*-1
				tempo_atual+=1
				pronto[0][0]-=1
				if(pronto[0][0]==0):
					retorno.append(tempo_atual-int(pronto[0][1]))
					espera.append(tempo_atual-int(pronto[0][1])+pronto[0][2])
					pronto.pop(0)
					pronto=sorted(pronto, key=lambda tup: tup[0])
	return (sum(retorno) / float(len(retorno))),(sum(resposta) / float(len(resposta))),(sum(espera) / float(len(espera)))
#####################################################################################
def rr(entradas,quantum):
	fila=[x[:] for x in entradas]
	Nentradas=len(entradas)
	tempo_atual=0
	retorno=[]
	resposta=[]
	espera=[]
	pronto=[]
	terminou=1
	while tempo_atual>=0:
		if(len(fila)>0 and fila[0][1]<=tempo_atual):
			pronto.append(fila.pop(0))
		else:
			if(len(pronto)==0):
				if(len(fila)==0 and primeirodafila[0]==0):
					break
				else:
					if(terminou==0):
						pronto.append(primeirodafila)
					else:
						tempo_atual+=1
						continue
			elif(terminou==0):
				pronto.append(primeirodafila)
			print(pronto)
			if(pronto[0][2]>0):
				resposta.append(tempo_atual-int(pronto[0][1]))
				pronto[0][2]=pronto[0][2]*-1
			
			for x in range(0,quantum):
				tempo_atual+=1
				pronto[0][0]-=1
				if(pronto[0][0]==0):
					retorno.append(tempo_atual-int(pronto[0][1]))
					espera.append(tempo_atual-int(pronto[0][1])+pronto[0][2])
					pronto.pop(0)
					terminou=1
				else:
					terminou=0
			if(terminou==0):
				primeirodafila=pronto.pop(0)
	return (sum(retorno) / float(len(retorno))),(sum(resposta) / float(len(resposta))),(sum(espera) / float(len(espera)))


#####################################################################################
f=open("entrada.txt", "r")	
f1 =f.readlines()
entradas = [] 
for x in f1:
	chegada,duracao=x.split()
	entradas.append([int(duracao),int(chegada),int(duracao)])
entradas = sorted(entradas, key=lambda tup: tup[1])
retorno,resposta,espera=fcfs(entradas)
print("FCFS " + str(retorno)+" "+str(resposta)+" "+str(espera))
retorno,resposta,espera=sjf(entradas,False)
print("SJF " + str(retorno)+" "+str(resposta)+" "+str(espera))
retorno,resposta,espera=rr(entradas,2)
print("RR " + str(retorno)+" "+str(resposta)+" "+str(espera))


