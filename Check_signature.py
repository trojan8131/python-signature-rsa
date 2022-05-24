import base64
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import easygui


def check_signature():
    msg = "W celu weryfikacji podpisu, podaj ściezki:"
    title = "Maciej Piotrowski- Podpis"
    fieldNames = ["Plik do weryfikacji:","Podaj plik z certyfikatem:","Podaj plik z kluczem publicznym:"]
    fieldValues = []  
    fieldValues = easygui.multenterbox("", title, fieldNames, fieldValues)


    #pobranie pliku
    #print('Podaj plik do sprawdzenia')
    #x = input()
    x=fieldValues[0]
    plik=open(str(x),"rb")
    plik_do_weryfikacji = plik.read()
    #pobranie certyfikatu
    #print('Podaj plik z certyfikatem')
    #x = input()
    x=fieldValues[1]
    certyfikat=open(x,"r")
    certyfikat = certyfikat.read()
    certyfikat=base64.b64decode (certyfikat)
    print(certyfikat)
    #pobranie klucza
    print('Podaj plik z kluczem publicznym')
    #x = input()
    x=fieldValues[2]
    klucz_pub=open(x, 'rb')
    klucz_publiczny = RSA.importKey(klucz_pub.read())


    haszowanie = SHA256.new(plik_do_weryfikacji)
    weryfikatcja = PKCS1_v1_5.new(klucz_publiczny)
    if weryfikatcja.verify(haszowanie, certyfikat):
        easygui.msgbox("Podpis jest poprawny!",image="sources/good.png")
    else:
        easygui.msgbox("Podpis się nie zgadza :(",image="sources/wrong.png")

