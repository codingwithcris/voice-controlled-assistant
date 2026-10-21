import speech_recognition as sr
import pyttsx3

class VoiceControlledAssistant:
    def capture_audio(self) -> str:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            self.text_to_speech(
                'Speak into your microphone what command you would like me to do'
            )
            try:
                r.adjust_for_ambient_noise(source)
                audio_data = r.listen(source)
                txt = r.recognize_google(audio_data)
                print(txt)
            except sr.UnknownValueError:
                self.text_to_speech(
                    'Sory, I could not catch what you are trying to say'
                )
            except sr.RequestError:
                self.text_to_speech('Error connecting to speech api')


    def text_to_speech(self, s: str) -> None:
        try:
            engine = pyttsx3.init()
            engine.say(s)
            engine.runAndWait()
        except RuntimeError as e:
            print(f"Error occured when translating text to speech: {e}")

