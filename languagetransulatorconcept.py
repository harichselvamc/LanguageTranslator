import googletrans #pip install googletrans==3.1.0a0
from googletrans import Translator

modules=Translator()#modules
userinput=str(input("Enter the sentences you want to transulate: "))
language=str(input("your language: "))
convertto=str(input("which language:"))

output=modules.translate(userinput,src=language,dest=convertto)#function
print(output.text)

