#encoding: utf-8
from Bots.BotEspelhado import BotEspelhado
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotEndiabrado import BotEndiabrado
from Bots.BotCachorro import BotCachorro
from Bots.BotEspanhol import BotEspanhol
###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Chorão"), BotEndiabrado("Lulu"), BotCachorro("Adolf"), BotEspanhol("Taquito"), BotEspelhado("Caral")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
