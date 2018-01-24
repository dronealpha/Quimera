################################################
#Autor:Diego Lopes da Silva                    #
#Data:09/01/2018                               #
#Descrição:Script para carregar modulos        #
################################################

import sys #Biblioteca para chamar modulos em suas devidas pastas
sys.path.append('/home/diego/Codigos/Quimera/scripts')

import os#biblioteca para interação com o sistema operacional
import writelogs #Modulo para escripta de log
import ConnectDevice #Modulo para conexão do dispositivo wi-fi
import time #Modulo de função de tempo
import letreiro #Modulo de letreiro com vesão do sistema 
import ConnectDB #Modulo para conexão do sqlite que armazena comandos



#Função para criar interface do sistema
def TelaQuimera():

    listcmd = ConnectDB.CarregaComandos()
    index = 0
    menu = 1
    for linha in listcmd:
        dados = str(menu) + str(list(linha))
        menu = menu + 1
        print(dados)
        index = index + 1
    
    op = int(input("Escolha um Comando->"))
    
    return listcmd[op - 1]


#tratamento para comandos vindos do banco
def TratCommand(dado):
    lt = str(dado)
    lt = lt.replace("'","")
    lt = lt.replace("(","")
    lt = lt.replace(")","")
    lt = lt.replace(",","")

    return lt


#execução de comando para o dispositivo
def execCommand():
    dado = TelaQuimera()
    print(dado)

    #Tratamento para comando
    lt = TratCommand(dado)
    com = lt+" \r"
    lt = lt.replace(" ","")
    stdata = "Comando ativado foi"+lt
    loglista = [lt]


    #Separando comandos para seta protocolo/comandos de interação
    print("Comando limpo {}".format(lt))
    if((lt == "ATDP") or (lt == "ATSP3")):
	    dado = ConnectDevice.Communication(com)
	    
	    #Data para log
	    data = writelogs.RetDateTime()
	    data = str(data)

            #Gera Lista Para Log
	    loglista.append(data+str(dado))
	    writelogs.OpenLog(lt, loglista)
    else:
       for x in range(1,100):
          dado1 = ConnectDevice.Communication(com)

          #Data para log
          dado1 = writelogs.TraDadosComando(dado1)
          data = writelogs.RetDateTime()
          data = str(data)

          
          loglista.append(data+dado1)
          time.sleep(1)
       writelogs.OpenLog(lt, loglista)


#função principa para executar os modulos       
if __name__ == "__main__":
	msg ="Operação realizada com sucesso"
	try:
	   stname="Quimera interface OBD2"
	   stversion=": "+ConnectDB.CarregaVersionApp()
	   stdbversion = ": "+ConnectDB.CarregaVersionDB()
	   letreiro.Let(stname,stversion,stdbversion)
	   execCommand()
	except:
		msg ="Erro de conexão com o dispositivo"
	finally:
		print(msg)            
    
		
 
