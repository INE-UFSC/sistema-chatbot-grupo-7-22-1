
  
from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
<<<<<<< HEAD
    def __init__(self, nome):
        self.nome = nome
        self.comandos = {}
=======

    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {}
>>>>>>> 7d4e09002b8bf607eece73a80367671f46f35da0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
<<<<<<< HEAD
    def nome(self, nome:str):
        self.__nome = nome

    def mostra_comandos(self):
        for index, chave in enumerate(self.comandos):
            print(f'{index+1} | {self.comandos[chave][0]}')

    def executa_comando(self,cmd:str):
        return self.comandos[cmd][1]
=======
    def nome(self, nome):
        self.__nome = nome

    def mostra_comandos(self):
        for i, cmd in enumerate(self.__comandos):
            print(i+1,'-',self.__comandos[cmd][0])
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        return self.__comandos[cmd][1]
>>>>>>> 7d4e09002b8bf607eece73a80367671f46f35da0

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass