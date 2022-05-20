
from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.comandos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    def mostra_comandos(self):
<<<<<<< HEAD
        cmds = ''
        for i, cmd in enumerate(self.__comandos):
            cmds.join([i+1,'-',self.__comandos[cmd][0],'\n'])
        return cmds
=======
        for index, chave in enumerate(self.comandos):
            print(f'{index+1} | {self.comandos[chave][0]}')
>>>>>>> 4b30024a44b43f307c37cfe47e89932da2f9ca91

    def executa_comando(self,cmd:str):
        return self.comandos[cmd][1]

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass