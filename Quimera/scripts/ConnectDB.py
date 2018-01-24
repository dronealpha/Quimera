##################################################
#Autor:Diego Lopes da Silva                      #
#Data:09/01/2018                                 #
#Descrição:Script para leitura do sqlite3 versão #
##################################################

import sqlite3

#Função para ler comandos da ODB II
def CarregaComandos():
    listcomand = []
    
    con = sqlite3.connect('/home/diego/Codigos/Quimera/database/QuimeraDB.db')
    c = con.cursor()
    for row in c.execute('select qm_com_command from QM_COMMANDS'):
        listcomand.append(row)
    con.close()

    return listcomand


#Função para carrega a versão do banco 
def CarregaVersionDB():
    con = sqlite3.connect('/home/diego/Codigos/Quimera/database/QuimeraDB.db')
    c = con.cursor()
    for row in c.execute("select build from db_version where name='Banco_Quimera'"):
        lcmdversion = row
    con.close()

    vdb = str(lcmdversion)
    vdb = vdb.replace("'","")
    vdb = vdb.replace("(","")
    vdb = vdb.replace(")","")
    vdb = vdb.replace(",","")
    return vdb

#Função para carregar versão da Aplicação
def CarregaVersionApp():
    con = sqlite3.connect('/home/diego/Codigos/Quimera/database/QuimeraDB.db')
    c = con.cursor()
    for row in c.execute("select build from db_version where name='App_Quimera'"):
        lcmdversion = row
    con.close()

    vdb = str(lcmdversion)
    vdb = vdb.replace("'","")
    vdb = vdb.replace("(","")
    vdb = vdb.replace(")","")
    vdb = vdb.replace(",","")
    return vdb
