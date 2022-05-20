
from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    def mostra_comandos(self):
        cmds = ''
        for cmd in sorted(self.__comandos):
            cmds.join([cmd,'-',self.__comandos[cmd][0],'\n'])
        print(cmds)
        return cmds


    def executa_comando(self,cmd:str):
        return self.comandos[cmd][1]

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass