from Bots.Bot import Bot

class BotBinario(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__nome = nome
        self.comandos['1'] = ("Bom dia!", "01000010 01101111 01101101 01000100 01101001 01100001")
        self.comandos['2'] = ("Qual seu filme favorito?", "01000101 01110101 01010010 01101111 01100010 11110100")
        self.comandos['3'] = ("Qual o seu estilo musical favorito?", "01001101 11111010 01110011 01101001 01100011 01100001 01000101 01101100 01100101 01110100 01110010 11110100 01101110 01101001 01100011 01100001")
        self.comandos['4'] = ("Adeus", "01000010 01111001 01100101 01000010 01111001 01100101")

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f"01001111 01001001 01000101 01110101 01010011 01101111 01110101 01001111 {self.__nome}"
 
    #def mostra_comandos(self):
    #    return self.comandos['a']
    
    def executa_comando(self,cmd):
        if cmd in self.comandos:
            return f"\nVocê --> {self.comandos[cmd][0]}\n{self.__nome} --> {self.comandos[cmd][1]}\n"
        else:
            return "01001110 01100001 01101111 01000101 01101110 01110100 01100101 01101110 01100100 01101001"

    def boas_vindas(self):
        return self.executa_comando('1')

    def despedida(self):
        return self.executa_comando('4')
