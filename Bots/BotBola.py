from Bots.Bot import Bot

class BotBola(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__nome = nome
        self.comandos['1'] = ("Bom dia!", "FAAALA FIO, TÁ BÃO??")
        self.comandos['2'] = ("[insira um comentário engraçado aqui]", "HAHAHA!!")
        self.comandos['3'] = ("Qual é o seu nome mesmo?", "Boa! Tá sabendo legal")
        self.comandos['4'] = ("Adeus", "Boa! Falô fio!!!")

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f"FAALA FIOTE!"
 
    #def mostra_comandos(self):
    #    return self.comandos['a']
    
    def executa_comando(self,cmd):
        if cmd in self.comandos:
            return f"\nVocê --> {self.comandos[cmd][0]}\n{self.__nome} --> {self.comandos[cmd][1]}\n"
        else:
            return "FALA DEREITO, JUMENTO!!"

    def boas_vindas(self):
        return self.executa_comando('1')

    def despedida(self):
        return self.executa_comando('4')
