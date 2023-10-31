import os 
import datetime as dt
import time 
from funcoes import *
import aspose.words as aw
from variaveis import *


teste_de_existencia = os.path.exists(agendas_path)
cwd = os.getcwd()
if teste_de_existencia:
    pass
else:
    os.mkdir(cwd+'\\'+'Agendas')
    
teste_de_existencia_pdf = os.path.exists(pdfs_path)

if teste_de_existencia_pdf:
    pass
else:
    os.mkdir(cwd+'\\'+'PDFs')
 
   
    
carrega_dados(lista_de_agendas) 

print ('Não há nenhuma agenda\n\n Crie uma agenda\n\n')
if not lista_de_agendas:
    pasta_atual = (gerar_agenda()).capitalize()      
    os.system('cls')
            
while True:
    
    

    
    
    ESCOLHAS = ['1','2','3','4','5']
    print ("O que deseja fazer? \n\n [1] - Escrever Relatório \n\n [2] - Exibir Relatório \n\n [3] - Salvar um relatório como PDF \n\n [4] - Deletar Relatório\n\n [5] - Sair\n\n")
    
    escolha = input ('')
    
    if (escolha not in ESCOLHAS) | (escolha.isdigit() == False) | (len(escolha)>1):
        print ("Escolha inválida. \n\n")
        time.sleep(3)
        os.system('cls')
        continue
        
    
    elif escolha == '1':
        os.system ("cls")
        
        

        while True:
            selecao_de_agenda = input ("Selecione a Agenda, Crie ou exclua uma: \n\n [1] - Selecionar uma existente\n\n [2] - Criar uma\n\n [3] - Deletar uma\n\n") 
              
            ESCOLHAS = ['1','2', '3']
            if (selecao_de_agenda not in ESCOLHAS) | (selecao_de_agenda.isdigit() == False) | (len(selecao_de_agenda)>1):
                print ("Escolha inválida. \n\n")
                time.sleep(3)
                os.system('cls')
                continue
            elif selecao_de_agenda == '1':
                os.system('cls')
                opcoes = lista_agendas() 
                print ("\n\n")
                agenda_selecionada = input ("Selecione uma agenda: \n\n")
                pasta_atual = opcoes[f'[{agenda_selecionada}]']
                
                break
            elif selecao_de_agenda == '2':
                gerar_agenda(lista_de_agendas)
                time.sleep(3)
                os.system('cls')
                continue
            elif selecao_de_agenda == '3':
                deletar_agenda()
                time.sleep(3)
                os.system('cls')
 
        
        print ("Escrevendo Relatório. \n\n")
        data_do_rel = datar()
        os.system('cls')
        escrever(data_do_rel, pasta_atual)
        os.system('cls')
        continue
                     
    elif escolha == '2':
        os.system('cls')
        while True:
            for file in os.listdir(agendas_path):
                
                opcoes = []
                numeracao_de_agendas = 0
                numeracao_de_agendas += 1
                print (f"{file}--[{numeracao_de_agendas}]")
                opcao = f'{file} -- [{numeracao_de_agendas}]'
                opcoes.append(opcao)
                escolhas = []
                escolhas.append(str(numeracao_de_agendas))
                
               
            escolha = input ("Qual agenda deseja acessar? \n Digite 'sair' para sair. \n\n" )
            if escolha.lower() == 'sair':
                print ("Saindo ...")
                time.sleep(3)
                os.system('cls')
                break 
            elif (escolha not in escolhas) | (escolha.isdigit() == False) | (len(escolha)>1):
                print ("Escolha inválida. \n\n")
                time.sleep(3)
                os.system('cls')
                continue
            else:
                for arquivo in opcoes:
                    if f'[{escolha}]' in arquivo:
                        pasta_atual = file
                        pasta_atual_path = agendas_path + '\\' + pasta_atual
                        break
            while True:##exibir arquivo
                os.system ("cls")           
                listagem_de_arquivos = lista_arquivos(pasta_atual_path)
                
                arquivo_acessado = input ("Qual arquivo deseja acessar? \n\n")
                os.system ("cls")
                if ((f'[{arquivo_acessado}]') not in listagem_de_arquivos) | (arquivo_acessado.isdigit() == False) | (len(arquivo_acessado)>1):
                    print ("Escolha inválida. \n\n")
                    time.sleep(3)
                    os.system('cls')
                    continue
                
                with open (pasta_atual_path+'\\'+listagem_de_arquivos[f'[{arquivo_acessado}]'], 'r', encoding='UTF-8') as fl:
                    conteudo = fl.read()
                print (conteudo)
                pular = input ("Pressione qualquer Tecla para pular !")
                os.system("cls")
                break
                      
    elif escolha == '3':
        os.system('cls')
        while True:
            opcoes = lista_agendas(lista_de_agendas)
            
            decisao = input ("Qual agenda deseja acessar? \n Digite 'sair' para sair. \n\n" )
            
            if decisao.lower() == 'sair':
                print ("Saindo ...")
                time.sleep(3)
                os.system('cls')
                break
            
            elif (f'[{decisao}]' not in opcoes) | (decisao.isdigit() == False) | (len(decisao)>1):
                print ("Escolha inválida. \n\n")
                time.sleep(3)
                os.system('cls')
                continue
            else:
                while True:
                    os.system('cls')
                    
                    listagem_de_arquivos = lista_arquivos((agendas_path+'\\'+opcoes[f'[{decisao}]']))
                    print ("\n\n")
                    if listagem_de_arquivos == {}:
                        print ("Não há arquivo algum aqui. \n\n")
                        time.sleep(3)
                        os.system('cls')
                        break
                    arquivo_selecionado = input ("Qual arquivo deseja converter? \n\n Ou digite 'sair' para sair\n\n")
                    
                    if arquivo_selecionado.lower() == 'sair':
                        print ("Saindo ...")
                        time.sleep(3)
                        os.system('cls')
                        break   
                    elif (f'[{arquivo_selecionado}]' not in listagem_de_arquivos) | (arquivo_selecionado.isdigit() == False) | (len(arquivo_selecionado)>1):
                        print ("Escolha inválida. \n\n")
                        time.sleep(3)
                        
                        os.system('cls')
                        continue
                    else:
                        
                        converter_em_pdf(agendas_path+'\\'+opcoes[f'[{decisao}]']+'\\'+listagem_de_arquivos[f'[{arquivo_selecionado}]'])

    elif escolha == '4':
        os.system('cls')
        while True: #####Lista as agendas
            c = 0
            for file in os.listdir(agendas_path):
                pastas = {}
                c += 1
                pastas.update({f'[{c}]':file})
                print (f"[{c}] --- {file}\n\n")
            if c == 0:
                print ("Não há nenhuma agenda aqui. \n\n") 
                time.sleep(3)  
                os.system('cls')
                break
            
            escolha = input ("Qual pasta deseja acessar? \n\n Ou digite 'sair' para sair. \n\n")
            
            if escolha.lower() == 'sair':
                time.sleep(3)
                os.system('cls')
                break
            
            if (escolha not in pastas) | (escolha.isdigit() == False) | len(escolha)>1:
                print ("Opção inválida. \n\n")
                time.sleep(3)
                os.system ('cls')
                continue
            else:
                os.system("cls")
                while True: #### Lista os arquivos
                    arquivos = {}
                    for file in os.listdir(agendas_path+'\\'+ pastas[f'[{escolha}]']):
                        c = 0
                        c += 1
                        arquivos.update({f'[{c}]':file})
                        print (f'[{c}] -- {file} \n')
                        
                    if arquivos == {}:
                        print ("Não há nenhum arquivo nesta pasta")
                        time.sleep(3)
                        os.system ('cls')
                        break  
                      
                    arquivo_a_ser_removido = input ("Qual arquivo deseja remover? \n\n Ou digite 'sair' para voltar ao menu \n\n" )  
                    
                    
                    
                    if arquivo_a_ser_removido.lower() == ('sair'):
                        os.system('cls')
                        break
                    elif (arquivo_a_ser_removido not in arquivos) | (arquivo_a_ser_removido.isdigit() == False) | len(arquivo_a_ser_removido)>1:
                        print ("Opção inválida. \n\n")
                        time.sleep(3)
                        os.system ('cls')
                        continue  
                    else:
                        path_do_arquivo = agendas_path+'\\'+ pastas[f'[{escolha}]']+'\\'+arquivos[f'[{arquivo_a_ser_removido}]']
                        deletar_arquivo(path_do_arquivo)
                        teste = lista_arquivos(agendas_path+'\\'+ pastas[f'[{escolha}]'])
                    
    elif escolha == '5':
        
        print ("Encerrando . . .\n\n")
        time.sleep(3)
        os.system ("cls")
        break