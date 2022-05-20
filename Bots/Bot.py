##implemente as seguintes classes

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
    def nome(self, nome):
        self.__nome = nome

    def mostra_comandos(self):
        cmds = ''
        for i, cmd in enumerate(self.__comandos):
            cmds.join([i+1,'-',self.__comandos[cmd][0],'\n'])
        return cmds

    @abstractmethod
    def executa_comando(self,cmd):
        return self.__comandos[cmd][1]

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass