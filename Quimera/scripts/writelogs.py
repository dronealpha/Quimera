##########################################
#Autor:Diego Lopes da Silva              #
#Data:11/01/2018                         #
#Descrição:Script para tratamento de Log #
##########################################

import os
from datetime import datetime

#retorna data e hora da execução do comando
def RetDateTime():
	r = datetime.now()
	r1 = str(r)
	r2 = '['+r1[0:19]+']'
	return r2
	
#Tratamento para retorno de dados comando
def TraDadosComando(dadoslogcm):
        d = str(dadoslogcm)
        d = d[10:22]
        return d

#Tratamento para retor de parametrização
def TraDadosConfig(dadoslogst):
       d = str(dadoslogst)
       d = d[10:22]
       return d

#Escreve log do sistema
def OpenLog(namelog,stdata):
        os.system("cd ../logs")
        namelog = namelog+".log"
        arquivo = open("/home/diego/Codigos/Quimera/logs/"+namelog, "w")
        for x in stdata:
                arquivo.write(x+"\n")
        arquivo.close()

