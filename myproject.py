import streamlit as st 
import googletrans
translator = googletrans.Translator()

st.set_page_config(page_title="My Internship project")
st.sidebar.header('About')
st.sidebar.text('Language transulator internship project by harichselvam') 
st.header("My Projects")
# st.write("language transulator")

st.title("This is a language transulator")#title of the page
st.write("language transulator")
# st.markdown('i used googles transulator library')

option=st.selectbox('Select Language',tuple(googletrans.LANGUAGES.values())) #selectbox method options 
text=st.text_area('Input the text')


def getkey(val):#defining the fucntions
    for key, value in googletrans.LANGUAGES.items():
         if val == value:
                return key
    return "key doesn't exist"


translated = translator.translate(text, dest=getkey(option))
st.write(translated.text)
