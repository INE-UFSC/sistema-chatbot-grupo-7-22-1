
from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome):
        self.__nome = nome
        self.comandos = {}
## Deixa privado
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    def mostra_comandos(self):
        cmds = ''
        for cmd in self.comandos:
            cmds += ' '.join([cmd,'-',self.comandos[cmd][0],'\n'])
        return cmds

    def executa_comando(self,cmd:str):
        return self.comandos[cmd][1]

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass