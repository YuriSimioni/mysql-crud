import os
os.system('cls')

try:
    try:
        from rich.progress import Progress
    except ImportError:
        print("\n033[1;31mExecute: pip install rich")
        
    with Progress() as progress:
            task = progress.add_task("   [blue]Importando Bibliotecas:", total=100)
            
            
            while not progress.finished:
                import mysql.connector
                progress.update(task, advance=1)
                
                import os
                progress.update(task, advance=1)
                
                import sys
                progress.update(task, advance=1)
                
                import time
                progress.update(task, advance=1)
                
                import pyfiglet
                progress.update(task, advance=1)
                
                import progressbar
                progress.update(task, advance=1)
                
                import inquirer
                progress.update(task, advance=1)
                
                from colorama import Fore, Back, Style
                progress.update(task, advance=1)
                
                from tqdm import tqdm
                progress.update(task, advance=1)
                
                import random
                progress.update(task, advance=1)
                
                import getpass
                progress.update(task, advance=1)
                
                time.sleep(0.1)
    
except ImportError:
    print('\033[1;31mAlgumas bibliotecas estão em falta')


class Usuario:
    
    def __init__(self, id, login, password, privLevel) -> None:
        self.id = id
        self.login = login
        self.password = password
        self.privLevel = privLevel
        
    def getLogin(self):
        return self.login

os.system("cls")

# Configuração da conexão
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud"
)


cursor = conexao.cursor()



# Verificar a conexão
if conexao.is_connected():
    print('\033[1;0m' + Fore.GREEN + Style.BRIGHT +'Conexão estabelicida com sucesso!\033[0;0m')
    time.sleep(1)
else:
    print("Erro ao conectar.")




while True:
    os.system('cls')
    print(Fore.BLUE + pyfiglet.figlet_format('Mysql CRUD', 'big'))
    print('─' * 57)
    user = input(Fore.BLUE  + "Digite o Usuário: " + Fore.WHITE)
    password = getpass.getpass(Fore.BLUE + "Digite sua senha: ")

    sql = "SELECT * FROM usuarios WHERE login = %s AND senha = %s"
    valor = (user, password)  # Sempre use tupla para valores

    # Executa a consulta
    cursor.execute(sql, valor)

    # Obter resultados
    resultados = cursor.fetchall()
    Usuario = Usuario(resultados[0][0], resultados[0][1], resultados[0][2], resultados[0][3])
    # Exibir resultados
    if cursor.rowcount > 0:
        os.system("cls")
        print('\033[1;0m'+Fore.GREEN+'Usuário authenticado com sucesso!')
        
        time.sleep(0.8)
        while True:
            os.system("cls")
            print(Fore.BLUE + pyfiglet.figlet_format('Mysql CRUD', 'big'))
            print('─' * 57)
            print(Usuario.getLogin())
            questions = [
                inquirer.List(
                    "opc1",
                    message='Escolha uma opção',
                    choices=["\033[0;34m[\033[0;0m1\033[0;34m] - \033[0;0mCadastro",
                            "\033[0;34m[\033[0;0m2\033[0;34m] - \033[0;0mListagem",
                            "\033[0;34m[\033[0;0m0\033[0;34m] - \033[0;0mSair",
                            ],
                ),
            ]
            opc = inquirer.prompt(questions)
            if opc["opc1"] == "\033[0;34m[\033[0;0m0\033[0;34m] - \033[0;0mSair":
                os.system('cls')
                break
            
    else:
        print('n tem ')
    
    # Fechar a conexão
    cursor.close()
    conexao.close()

    