print("-------ESERCIZIO 6--------")

"""
Le funzioni lambda sono delle funzioni prive di nome che svolgono operazioni semplici. Una particolarità è che la definizione avviene in una riga di comando e il risultato è unico.

---- lambda a: a+10 ------

aumenta di 10 il valore di a.

---- f = lambda animale: animale.capitalize()-----

trasforma in lettera maiuscola la prima lettera di una stringa

Esempio:
animali = ['cani', 'gatti', 'scoiattoli', 'alci']
f = lambda animale: animale.capitalize()
for animale in animali:
 print(f(animale))
Risultato:
Cani 
Gatti
Scoiattoli
Alci
"""

f= lambda a,b: (a+b)*0.5
media=f(5.0,0.7)
print(media)