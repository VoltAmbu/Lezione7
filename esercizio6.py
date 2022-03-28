print("-------ESERCIZIO 6-------- \n il codice è commentato")

"""
Le funzioni lambda sono particolari funzioni senza nome, che svolgono semplici operazioni definite in un'unica linea di comando, restituendo un unico valore.
- lambda a: a+10 
incrementa di 10 unità il valore di a.
Esempio:
f= lambda a: a+10
print(f(2))
Risutato: 12
-f = lambda animale: animale.capitalize()
f è una funzione che rende maiuscola l'iniziale di una stringa di caratteri.
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