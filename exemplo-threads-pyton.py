# -*- coding: utf-8 -*-
#!/usr/bin/python3

import threading
import time
import sys
from datetime import datetime
import os
import random


class Envios(threading.Thread):

    # var1 = obrigatorio, var2 'str' = o 'str' fica valor default mas pode receber outros valores pelo parametro.
    def __init__(self, threadnum, var2=None):

        threading.Thread.__init__(self)

        # Modo 1 de declara variaveis globais da thread atual.
        #global varLocal
        #varLocal = parte[i]

        # Modo 2 de declara variaveis globais da thread atual.
        self.threadNum = threadnum
        self.var2 = var2

    def run(self):

        # Pra cada thread vai rodar o codigo abaixo
        timeSleep = random.randint(0,3)
        time.sleep(timeSleep)
        print(self.threadNum, self.var2, timeSleep)


class Menu:

    def __init__(self):
        #self.name = name
        #self.age = age

        print("olá")

        # <... inicia codigo da tela

        #numero de Threads que vao rodar
        self.numThreads = 5

        #array que organizara as Threads
        self.arrayThreads = []

        for i in range(0, self.numThreads):

            # Organiza Threads?!
            self.varTeste = Envios(i)
            self.arrayThreads.append(self.varTeste)

        for j in self.arrayThreads:
            # Starta a Thread
            j.start()

        for j in self.arrayThreads:
            # ?
            j.join()

        # fim do codigo da tela ...>


'''
p1 = Menu("John", 36)

print(p1.name)
print(p1.age)
'''

#if __name__ == "main":

p1 = Menu()
print(p1.numThreads)


# Exemplo de chamada da classe Threads
#Threads(count,"teste123", var2 = "teste456")

