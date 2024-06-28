import time
import threading
import gpio
from gpiozero import Button, LED

#button.when_pressed = led.on

Przycisk1 = Button(16)
Przycisk2 = Button(18)
Przycisk3 = Button(19)
Przycisk4 = Button(21)
CzujnikC = Button(3) #czujnik cisnienia
CzujnikPMin= Button(5) #czujnik paliwa min
CzujnikPMax = Button(7) #czyjnik paliwa max
Pompa = LED(8) #pompa
GeneratorP = LED(10) #generator paliwa
ZaworAP = LED(11) #zawor awaryjny powietrze
ZaworPa = LED(12) #Zawor paliwa
ZaworPo = LED(13) #Zawor pompy
Fuzja = LED(15) #Fuzja


def Stop():
    Pompa.on()
    GeneratorP.on()
    ZaworAP.on()
    ZaworPa.on()
    ZaworPo.on()
    Fuzja.off()
    #Na ekranie trzeba wyswietlic zatrzymanie awaryjne
    time.sleep(2)
    #Na ekranie trzeba wyswietlić Wybierz dalsze opcje
    while Przycisk2.when_deactivated:
        if Przycisk1.when_held:
            ZaworAP.off()
            #Wyświetlic zawor powietrza otw
            time.sleep(2)
            while Przycisk1.when_deactivated:
                time.sleep(0.1)
        ZaworAP.on()
        #Wyświetlić wysyłanie do menu
        return 1

def On_Stop():
    if Przycisk1.when_activated:
        if Stop() == 1:
            return 1
def Paliwo(ile_razy, x, timer):
    while x <= ile_razy:
        #Wyświetlić napełnianie
        while True:
            time.sleep(0.1)
        if CzujnikPMin.when_held:
            time.sleep(1)
            if CzujnikPMin.when_held:
                break

        time.sleep(0.1)
        #Wyświetlić paliwo maksymalne
        time.sleep(1)
        #Wyświetlić zawor paliwa otwarty
        ZaworPa.off()
        while  CzujnikPMax.when_held:
            time.sleep(0.1)
        ZaworPa.on()
        #wyswietlic zawor paliwa zamkniety
        time.sleep(1)
        #wyswietlic paliwo min
        time.sleep(1)
        #wyswietlic pompa on
        Pompa.off()
        time.sleep(1)
        #wyswietlic zawor pompy otwarty
        ZaworPo.off()
        while CzujnikC.when_deactivated:
            #Wyswietlić regulacja cisnienia
            time.sleep(0.1)
        time.sleep(1)
        #wyswietlić poprawne cisnienie
        time.sleep(1)
        #wyswietlić zawor pompy zamkniety
        Pompa.on()
        ZaworPo.on()
        x = x+1
    return 1

def Reaktor(ti,ile_razy):
    pokaz_menu = True
    Pompa.off()
    #wyswietlic pompa on
    time.sleep(1)
    ZaworPo.off()
    #wyswietlic zawor pompy otwarty
    time.sleep(1)
    #wyswietlic regulacja cisnienia
    while CzujnikC.when_deactivated:
        time.sleep(0.1)
    time.sleep(1)
    #wyswietlic cisnienie poprawne
    time.sleep(1)
    #wyswietlic zawor pompy zamkniety
    ZaworPo.on()
    time.sleep(1)
    #wyswietlic wyłączenie pompy
    Pompa.on()
    time.sleep(1)
    #wyswietlic generator paliwo on
    GeneratorP.off()
    time.sleep(1)
    #wyswietlic funkcja paliwo
    time.sleep(1)
    if Paliwo(ile_razy,1,10)==0:
        return 0;
    time.sleep(1)
    #wyswietlic zawor pompy otwarty
    Pompa.off()
    time.sleep(1)
    ZaworPo.off()
    #wyswietlic generator paliwa off
    GeneratorP.on()
    time.sleep(1)
    #wyswietlic poczekaj 5 minut
    time.sleep(1)
    ta = 3000
    while ta >=1:
        ta = ta -1
        if ta%10 == 0:
            #wyswitlic na ekranie wynik ta/10
        time.sleep(100)
    #wyswietlic na ekranie pompa off
    Pompa.on()
    ZaworPo.on()
    while Przycisk4.when_deactivated:
        #wyswietl na ekranie rozpocznij fuzje
    if CzujnikC.when_deactivated:
        #wyswietlic nieszczelna komora
        time.sleep(1)
        #wyswietlic powrot do startu
        return 0;
    else:
        while ti>1:
            if fuzja() == 0:
                return 0
            ti = ti - 1
        #wyswietlic  wykonano maks fuzji
        time.sleep(1)
        #wyswietlic powrot do startu



def fuzja():
    pozwolenie_na_kont = True
    t =5
    while t>=1:
        #wyswietl na akranie "fuzja za" zmienna t
        t = t-1
        time.sleep(1)
    Fuzja.on()
    t = 1200
    while t>=1:
        t = t-1
        if t%10 == 0:
            #Wyswietl na ekranie "praca" zmienna t
        time.sleep(0.1)
    #wysweitl wyłączenie
    Fuzja.off()
    t = 600
    while t>=1:
        t = t-1
        if t%10 == 0:
            #wyswietl na ekranie"odpoczynek" zmienna t
        time.sleep(0.1)

    Fuzja.on()
    t = 1200
    while t >= 1:
        t = t - 1
        if t % 10 == 0:
        # Wyswietl na ekranie "praca" zmienna t
        time.sleep(0.1)
    # wysweitl wyłączenie
    Fuzja.off()
    time.sleep(1)
    #wyswietl generator paliwa on
    GeneratorP.off()
    time.sleep(1)
    if Paliwo(1,1,10) == 0:
        return 0;
    #wyswietl genrator paliwa off
    GeneratorP.on()
    time.sleep(1)
    #wyswietl zawor pompy otwarty
    Pompa.off()
    ZaworPo.off()
    time.sleep(1)
    while CzujnikC.when_deactivated:
        #wyswietl regulacja cisnienia
        time.sleep(0.1)
    #wyswietl czekaj 5min
    time.sleep(1)
    Pompa.off()
    t = 3000
    while t >= 1:
        t = t - 1
        if t % 10 == 0:
        # wyswitlic na ekranie "odparowywanie" t/10
        time.sleep(100)
    #wyswietlic zawor pompy zamkniety
    ZaworPo.on()
    time.sleep(1)
    #wyswietlic pompa off
    Pompa.on()
    return 1

def zmiana_stanu(urzadzenie):
    zmiana = LED(urzadzenie)
    if zmiana.on():
        zmiana.off()
        time.sleep(0.5)
    else:
        zmiana.on()
        time.sleep(0.5)

def tryb_serwisowy(pozycja, wyswietl):
    time.sleep(1)
    #kwestia z trybem serwisowym jest taka ze funkcje ekranu były połączone z włączaniem danych elementów wiec nie mogłem tego zrobić


pokaz_menu = True
pozwolenie_na_kont = False
while True:
    if pokaz_menu == True:
        #wyswietlic na ekranie "Reaktor fuzyjny v2;
        pokaz_menu = False
    if Przycisk1.when_activated:
        t1 = threading.Thread(target=Reaktor(3,3))
        t2 = threading.Thread(target=On_Stop())
        t1.start()
        t2.start()
        #Wyswietlic na ekranie wykonano fuzje
        time.sleep(2)
        pokaz_menu = True
    elif Przycisk2.when_activated & pozwolenie_na_kont == True:
        t1 = threading.Thread(target=Reaktor(3, 1))
        t2 = threading.Thread(target=On_Stop())
        t1.start()
        t2.start()
        # Wyswietlic na ekranie wykonano fuzje
        time.sleep(2)
        pokaz_menu = True
    elif Przycisk2.when_activated & pozwolenie_na_kont == False:
        # Wyswietlic na ekranie nie wolno kont
        time.sleep(2)
        pokaz_menu = True
    elif Przycisk4.when_activated:
        tryb_serwisowy(1,True)
        Pompa.on()
        GeneratorP.on()
        ZaworAP.on()
        ZaworPo.on()
        ZaworPa.on()
        Fuzja.off()
        pokaz_menu=True
    time.sleep(0.1)



#podsumowanie do zrobienia jest jeszcze tryb serwisowy ale trzeba do tego najprawdopodobniej zaprogramować ekran