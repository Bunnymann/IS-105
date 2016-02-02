#!/usr/bin/python
# -*- coding: utf-8 -*-



import random;
from random import shuffle
import sys




#Alle de forskjellige korttypene
kortHjerter =['Hjerter A','Hjerter2','Hjerter3','Hjerter4','Hjerter5','Hjerter6','Hjerter7','Hjerter8','Hjerter9','Hjerter10','Hjerter J','Hjerter Q','Hjerter K'];
kortKloever = ['Kloever A','Kloever2','Kloever3','Kloever4','Kloever5','Kloever6','Kloever7','Kloever8','Kloever9','Kloever10','KloeverJ','Kloever Q','Kloever K'];
kortSpar = ['Spar A','Spar2','Spar3','Sparr4','Spar5','Spar6','Spar7','Spar8','Spar9','Spar10','Spar J','Spar Q','Spar K'];
kortRuter = ['Ruter A','Ruter2','Ruter3','Ruter4','Ruter5','Ruter6','Ruter7','Ruter8','Ruter9','Ruter10','Ruter J','Ruter Q','Ruter K'];

#Alle kort som er i en kortstokk
alleKort = ['Hjerter A','Hjerter 2','Hjerter 3','Hjerter 4','Hjerter 5','Hjerter 6','Hjerter 7','Hjerter 8','Hjerter 9','Hjerter 10','Hjerter J','Hjerter Q','Hjerter K',
            'Kloever A','Kloever 2','Kloever 3','Kloever 4','Kloever 5','Kloever 6','Kloever 7','Kloever 8','Kloever 9','Kloever 10','Kloever J','Kloever Q','Kloever K',
            'Spar A','Spar 2','Spar 3','Spar 4','Spar 5','Spar 6','Spar 7','Spar 8','Spar 9','Spar 10','Spar J','Spar Q','Spar K',
            'Ruter A','Ruter 2','Ruter 3','Ruter 4','Ruter 5','Ruter 6','Ruter 7','Ruter 8','Ruter 9','Ruter 10','Ruter J','Ruter Q','Ruter K'];

#Stokker alle kortene i kortstokken
random.shuffle(alleKort)


def spill ():
#trekker 5 bunker fra kortstokken
    trekkEn = alleKort[0:5]
    trekkTo = alleKort[5:10]
    trekkTre = alleKort[10:15]
    trekkFire = alleKort[15:20]
    trekkFem = alleKort[20:25]
    trekkSeks = alleKort[25:30]

#printer hver person, med en bunke hver
    print 
    
    print "Benjamin trakk:", trekkEn
    print 
    print "Ola trakk:", trekkTo
    print
    print "Christian trakk:", trekkTre
    print
    print "Merethe trakk:", trekkFire
    print
    print "Erlend trakk:", trekkFem
    print
    print "Tommy trakk:", trekkSeks
    print
    #stokker kortene på nytt
    random.shuffle(alleKort)
    
    

   
    spillIgjen()
#funksjon for å spille igjen
def spillIgjen() :
    
    #mulige svar for ja eller nei om å spille på nytt
    svar = raw_input("Vil du Spille igjen? , Ja eller Nei: ")
    jaSvar = ["Yes", "ja", "y","j"]
    neiSvar = ["No","n","nei","n"]
    
    #hvis et svar for nei, avslutt
    for i in  neiSvar :
        if (svar.upper() == i.upper()):
            sys.exit("Bra spill, takk for at du spilte!")

    #hvis et svar for ja, start på nytt
    for i in jaSvar :
        if (svar.upper() == i.upper()):
            spill()
    
   #hvis et svar som ikke er ja eller nei, si at det er feil, og at de skal prøve på nytt
    print (svar),":", " Er desverre ikke et alternativ, Vil du Spille igjen? , Ja eller Nei"
    spillIgjen()
    

#kjører spillet       
spill()

