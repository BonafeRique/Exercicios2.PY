# -*- coding: utf-8 -*-
"""ExercíciosPY2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b4rW9sPlOHZpPL7ehgu-lXK_pG0HUvS4
"""

#EXERCÍCIO 1

name = str (input('Qual o seu nome?'))
sentence = str(input('Qual é seu maior sonho?'))

print('O maior sonho do {} é {}'.format(name,sentence))

#EXERCÍCIO 2

hora = int(input('Informe a hora'))
minutos = int(input('Informe os minutos'))
segundos  = int(input('Informe os segundos'))

print('De acordo com suas informações são {}h {}m e {}s' .format(hora,minutos,segundos))

#EXERCíCIO 3
ddd = str (input('Informe seu DDD entre parenteses'))
telefone = str (input('Informe seu númro com ífem '))

print ('Seu número é {} {}'.format(ddd,telefone))

#EXERCÍCIO 4

cenoura = ('5 cenouras')
farinha = ('450g de farinha')
ovos = ('4 ovos')
trigo = ('200g de trigo')

print('Para fazer esse delicioso bolo de cenoura você vai precisar de: {}, {}, {} e {}.'.format(cenoura,farinha,ovos,trigo))

#EXERCÍCIO 5

adj = str (input('Me diga um adjetivo que represente o que você gosta de fazer nas horas vagas:'))
ad2 = str (input('Me diga um adjetivo que lhe representa:'))
ad3 = str (input('Me diga um adjetivo que te descreva neste exato momento:'))

print ('Entao... Você gosta de {} e uma palavra que combina com você é {}. Agora, me diga como você está se sentindo: {}.'.format(adj,ad2,ad3))