import os
import time
import pathlib
from variaveis import *
from fpdf import FPDF 



MESES_30 = ['04', '06', '09', '11']
MESES_31 = ['01', '03', '05', '07', '08', '10', '12']
FEVEREIRO = ['02']




path_main = pathlib.Path('funcoes.py').parent.resolve()

path = (path_main)





        

def gerar_agenda(y=lista_de_agendas): 
    pasta = input ("Digite um nome para a agenda: \n\n")
    try:
        path_novo = os.path.join(agendas_path, pasta)
        
        os.mkdir(path_novo)
        
        lista_de_agendas.update({pasta:''})
    except FileExistsError:
        path_novo = os.path.join(agendas_path, pasta+'(1)')
        
        os.mkdir(path_novo)
        
        lista_de_agendas.update({pasta:''})
        
    return pasta


def lista_agendas(path=agendas_path):
    opcoes = {}
    c = 0
    for file in os.listdir(agendas_path):
            c += 1
            print (f"[{c}]- {file} \n\n")
            opcoes.update({f'[{c}]':file})
    return opcoes
            
def deletar_arquivo(PathDoArquivo):
    try: 
        os.remove(PathDoArquivo)
        print ("O arquivo foi removido. \n\n")
    except FileNotFoundError:
        print ("Arquivo não existe. \n\n")
        time.sleep(3)
        os.system('cls')
    
    


def datar():
    
    while True:
        data = input ("Digite uma data válida: \n\n")
        
        if data.isdigit()!= True:
            print ('Formato de data inválido \n')
            time.sleep(3)
            os.system('cls')
            continue          
        elif (len(data)==8) == False:
            print ('Formato de data inválido \n')
            time.sleep(3)
            os.system('cls')
            continue
        elif (int(data[0:2])<1 | int(data[0:2])> 30) and (data[2:4] in MESES_30):
            print ("Digite uma data válida")
            time.sleep(3)
            os.system('cls')
            continue
        elif (int(data[0:2])<1 | int(data[0:2])> 28) and (data[2:4] in FEVEREIRO):
            print ("Digite uma data válida")
            time.sleep(3)
            os.system('cls')
            continue
        elif (int(data[0:2])<1 | int(data[0:2])> 31) and (data[2:4] in MESES_31):
            print ("Digite uma data válida")
            time.sleep(3)
            os.system('cls')
            continue
        elif (int(data[2:4]) < 1 | int(data[2:4]) > 12):
            print ("Digite um mês válido \n\n")
            time.sleep(3)
            os.system('cls')
            continue

        data_final = (f'{data[0:2]}/{data[2:4]}/{data[4:8]}')    
        
        return data_final 

    
    
    
def escrever(data, pasta):
    
    titulo = input ("Digite um título para o texto: \n")
    
    texto = input ('\n--- ')
    
    with open (agendas_path+'\\'+pasta+'\\'+titulo+'.txt', 'w') as tx:
        tx.write((f'{data} \n\n\n {texto}'))
        tx.close()

def deletar_agenda(lista=lista_de_agendas):
    opcoes = lista_agendas(agendas_path)
    
    
    escolha = input ("Qual agenda deseja remover? \n\n")
    try: 
        os.remove(agendas_path+'\\'+opcoes[f'[{escolha}]'])
        print ("A agenda foi removida. \n\n")
    except FileNotFoundError:
        print ("A agenda não existe. \n\n")
        time.sleep(3)
        os.system('cls')


def carrega_dados(lista=lista_de_agendas, c=0):
        
    for file in os.listdir(agendas_path):
        c =+ 1
        
    if c == 0:
        return lista_de_agendas
    else:
        for file in os.listdir(agendas_path):
            if '.' in file:
                pass
            else:
                for file in agendas_path:
                    lista_de_agendas.update({file:""})
 
 
 
def lista_arquivos(path):
    c = 0
    lista = {}
    for file in os.listdir(path):
        c += 1
        lista.update({f'[{c}]' : f'{file}'})
        print (f'[{c}] -- {file}\n\n')
    return lista


def converter_em_pdf(path):
    nome = input ("Digite o nome do PDF\n\n")
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=15)
    with open(path, 'r', encoding='UTF-8') as tx: 
        for x in tx: 
            pdf.cell(20, 10, txt = x, ln = 1, align = 'C')
          
        pdf.output(agendas_path+ '\\' + nome+'.pdf', 'F')