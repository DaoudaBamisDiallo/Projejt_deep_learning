# importation des packages
import streamlit as st
import speech_recognition as sr
# from myinterpreter import Myinterpreter
# generateur de du procecusse de la reconnaissance vocal

def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Parlez maintenat...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcription...")

        try:
            # using Google Speech Recognition
            
            text = r.recognize_google(audio_text,language="fr-FR")
            return text
        except:
            return "Désolé je ne comprends votre langue."
        

#
def main():
    st.title("Application de reconnaisance vocale")

    # add a button to trigger speech recognition
    if st.button("Commencez à parler"):
        text = transcribe_speech()
        st.write("Transcription: ", text)
if __name__ == "__main__":
    main()