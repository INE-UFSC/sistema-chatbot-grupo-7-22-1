
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
        cmds = ''
        for i, cmd in enumerate(self.__comandos):
            cmds.join([i+1,'-',self.__comandos[cmd][0],'\n'])
        return cmds


    def executa_comando(self,cmd:str):
        return self.comandos[cmd][1]

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass