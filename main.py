import os
os.system("cls")


# Importando as bibliotecas necessarias
try:
    
    # Verificando se a biblioteca para a barra de progresso esta em condições
    try:
        from rich.progress import Progress
    except ImportError:
        print("\n033[1;31mExecute: pip install rich")
        
    with Progress() as progress:
        
        # Criando uma barra de progresso para as importações necessarias
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
            

# Caso alguma biblioteca não esteja instalada ou atualizada
except ImportError:
    print("\n\033[1;31mAlgumas bibliotecas estão em falta\n\033[0;32mExecute \033[1;34m'pip install -r requirements.txt'\033[0;32m para instalar/atualizar as bibliotecas necessarias\033[0;0m")



# Classe de usuario do sistema
class Usuario:
    
    def __init__(self, login, senha, privLevel) -> None:
        """Cria um novo usuario do sistema

        Args:
            login (str): Login/Nome do usuario
            senha (str): Senha do usuario
            privLevel (int): Valor do nivel do usuario
        """
        
        self.login = login
        self.senha = senha
        self.privLevel = privLevel
        
        
    def setLogin(self, login) -> None:
        """Define o Login do usuario

        Args:
            login (str): Login do usuario
        """
        self.login = login
    
    def setSenha(self, senha) -> None:
        """Define a Senha do usuario

        Args:
            senha (str): Senha do usuario
        """
        self.senha = senha
    
    def setPrivLevel(self, privLevel) -> None:
        """Define o PrivLevel do usuario

        Args:
            privLevel (str): PrivLevel do usuario
        """
        self.privLevel = privLevel
        
    
    def getLogin(self) -> None:
        """Retorna o Login do usuario

        Returns:
            str: Login do usuario
        """
        return self.login
    
    def getSenha(self) -> None:
        """Retorna a Senha do usuario

        Returns:
            str: Senha do usuario
        """
        return self.senha
    
    def getPrivLevel(self) -> None:
        """Retorna o PrivLevel do usuario

        Returns:
            int: PrivLevel do usuario
        """
        return self.privLevel
        