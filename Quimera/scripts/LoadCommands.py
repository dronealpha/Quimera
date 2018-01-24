import sqlite3

def TelaQuimera():

    listcmd = CarregaComandos()
    index = 0
    menu = 1
    for linha in listcmd:
        dados = str(menu) + str(list(linha))
        menu = menu + 1
        print(dados)
        index = index + 1
    
    op = int(input("Escolha um Comando"))
    
    return listcmd[op - 1]

#função para carregar comandos e retorna lista
def CarregaComandos():
    #craindo lista para armazenar os comandos
    listcomand = []
    
    # carrega comandos
    con = sqlite3.connect('QuimeraDB.db')
    c = con.cursor()
    for row in c.execute('select qm_com_command from QM_COMMANDS'):
        listcomand.append(row)
    con.close()

    return listcomand


if __name__ == "__main__":
    dado = TelaQuimera()
    print(dado)


