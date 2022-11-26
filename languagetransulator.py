import googletrans #https://pypi.org/project/googletrans/   its library in python
#we should install googletrans on our system using command pip install googletrans
translator=googletrans.Translator() #Transulator is a module in googletrans


print(googletrans.LANGUAGES)#languages is a dictionary
print(googletrans.LANGUAGES.values())
for values in googletrans.LANGUAGES.values():
    print(values)


transulated=translator.translate("hello,this is a boy ",dest="german")
print(transulated.text)
