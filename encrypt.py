import base64
import hashlib
import key
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
import easygui

def encrypt_file():
    
    msg = "W celu utworzenia podpisu, podaj ściezki:"
    title = "Maciej Piotrowski- Podpis"
    fieldNames = ["Plik do podpisu:","Podaj plik z podpisem:","Podaj nazwę źródła szyfrowania:","Podaj ściezke do klucza publicznego:"]
    fieldValues = [] 
    fieldValues = easygui.multenterbox("", title, fieldNames, fieldValues)
    print ("Reply was:", fieldValues)


    print(fieldValues)

    #otwieramy pliki
    #print('Podaj plik do podpisania:')
    #x = input()
    #x="files/toEncrypt.txt"
    x=fieldValues[0]
    file=open(str(x),"rb")
    readFile = file.read()

    #print('Podaj plik z podpisem')
    #x = input()
    #x="files/cert.txt"
    x=fieldValues[1]
    certyfikat=open(str(x),"wb")



    #pobieramy klucz korzystając z algorytmu
    print('Podaj nazwę źródła szyfrowania:')
    #x = input()

    #x="lena.png"
    x=fieldValues[2]
    #Podajemy źródło losowości do naszego algorytmu i generujemy ciąg
    key.getKey(x)
    source=open("temp.png","rb")



    #Tworzę klucz
    key_p = RSA.generate(1024,source.read)
    prywatny=key_p.export_key('PEM')
    publiczny=key_p.publickey().export_key('PEM')


    #zapisanie klucza publicznego

    print('Podaj ściezke do klucza publicznego:')
    #x = input()
    #x='files/pubkey.pem'
    x=fieldValues[3]
    klucz=open(x, 'wb')
    klucz.write(publiczny)
    klucz.close()

    #haszowanie pliku
    fileSHA=hashlib.sha3_256(readFile) 
    print("SHA: : ",fileSHA.hexdigest())

    #tworzenie podpisu
    haszowanie = SHA256.new(readFile)
    podpis = PKCS1_v1_5.new(key_p)
    podpisanie = podpis.sign(haszowanie)
    certyfikat.write(base64.b64encode(podpisanie))

    easygui.msgbox("Podpisane!  "+"SHA: "+fileSHA.hexdigest(),image= "sources/signature.jpeg")



