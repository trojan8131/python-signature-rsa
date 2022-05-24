from easygui import *
import encrypt
import Check_signature
try:
    while(1):
        title = "Maciej Piotrowski- tworzenie podpisu cyfrowego"


        button_list = []
        button1 = "Utwórz podpis"
        button2 = "Sprawdź podpis"

        button_list.append(button1)
        button_list.append(button2)


        img = "sources/rsa.png"

        # creating a button box
        output = buttonbox("",title, image = img, choices = button_list)

        if output=="Utwórz podpis":

            encrypt.encrypt_file()
        else:
            Check_signature.check_signature()

        # creating a message box 
except:
    exceptionbox()
