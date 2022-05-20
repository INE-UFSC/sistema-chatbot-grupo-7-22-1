from Bots.Bot import Bot

class BotIngles(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__nome = nome
        self.comandos['1'] = ("Bom dia!", "Good morning! How can I help you?")
        self.comandos['2'] = ("Você prefere futebol americano ou baseball?", "I prefer baseball")
        self.comandos['3'] = ("Qual a sua cor favorita?", "My favorite color is blue")
        self.comandos['4'] = ("Adeus", "Goodbye! I hope to see you again soon")

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f"Hi! I'm {self.__nome}"
 
    #def mostra_comandos(self):
    #    return self.comandos['a']
    
    def executa_comando(self,cmd):
        if cmd in self.comandos:
            return f"\nVocê --> {self.comandos[cmd][0]}\n{self.__nome} --> {self.comandos[cmd][1]}\n"
        else:
            return "I don't understand"

    def boas_vindas(self):
        return self.executa_comando('1')

    def despedida(self):
        return self.executa_comando('4')
