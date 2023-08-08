# pip install -r requirements.txt => importar as bibliotecas
# pip3 install pyinstaller => Instalando para o Deploy instanciando o AWS/EC2
# A após digitar => pyinstaller --onefile main.py => Para criação do deploy
import speech_recognition as sr
import playsound
from gtts import gTTS, tts
import random
import webbrowser
import pyttsx3
import os

print("\nInicializando a Robot!\n")


# Initialize text to speech engine (Mecanismo de conversão de texto em fala)
class Virtual_assit:
    def __init__(self, assist_name, person):
        self.person = person
        self.assit_name = assist_name

        self.engine = pyttsx3.init("sapi5")
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[0].id)
        self.r = sr.Recognizer()

        self.voice_data = ""

    # Function to speak text (fala da assitente virtual)
    def engine_speak(self, text):
        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()

    # Function to recognize speech (reconhecer a fala)
    def record_audio(self, ask=""):
        with sr.Microphone() as source:
            if ask:
                self.engine_speak(
                    "Hello! I'm Robot, your personal assistant. How can I help?\n"
                )
                print("recording...")
                self.engine_speak(ask)

            audio = self.r.listen(source, 5, 5)  # pega dados de audio
            print("looking at the data base")
            try:
                self.voice_data = self.r.recognize_google(
                    audio
                )  # converte audio para texto

            except sr.UnknownValueError:
                self.engine_speak(
                    "Sorry Master, I did not get what you said. Can you please repeat?"
                )

            except sr.RequestError:
                self.engine_speak(
                    "Sorry Master, my server is down"
                )  # recognizer is not connected

            print(">>", self.voice_data.lower())  # imprime o que vc disse
            self.voice_data = self.voice_data.lower()

            return self.voice_data.lower()

    def engine_speak(self, audio_strig):
        audio_strig = str(audio_strig)
        tts = gTTS(text=audio_strig, lang="en")
        r = random.randint(1, 20000)
        audio_file = "audio" + str(r) + ".mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.assit_name + ":", audio_strig)
        os.remove(audio_file)

    # função para identificar se o termo existe

    def there_exist(self, terms):
        for term in terms:
            if term in self.voice_data:
                return True

    def respond(self, voice_data):
        if self.there_exist(["hey", "hi", "hello", "oi"]):
            greetigns = [
                f"Hi {self.person}, Are you studying Python or Java Script?\n",
                "Hello master, I know you like praise!\n",
                f"Hi {self.person}, Take the Umbrella, because it will rain!\n",
                "Hello master, I know that the team of your heart is Vasco ...\n",
            ]

            greet = greetigns[random.randint(0, len(greetigns) - 1)]
            self.engine_speak(greet)

        # Criar  Lista de Tarefas
        if self.there_exist(["create", "task", "add, reminder"]):
            greetigns = [
                "Task created successfully: Study Python from 18:00!\n",
                "Task created successfully: Report Delivery!\n",
                "Successfully created reminder: Meeting at 16:00!\n",
                "Successfully created reminder: Fuel Car!\n",
                "Task successfully created: Shopping at the supermarket!\n",
                "Successfully created reminder: Mow lawn!\n",
                "Task created successfully: Paying Bills!\n",
            ]

            greet = greetigns[random.randint(0, len(greetigns) - 1)]
            self.engine_speak(greet)

        # google
        if self.there_exist(["google"]):
            search_term = voice_data.split("for")[-1]
            url = "http://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("here is what I found for " + search_term + "on google\n")

        # youtube
        if self.there_exist(["youtube"]):
            search_term = voice_data.split("for")[-1]
            url = "http://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak(
                "Here is what i found for " + search_term + "on youtube\n"
            )

        # github
        if self.there_exist(["projects"]):
            search_term = voice_data.split("for")[-1]
            url = "https://github.com/RafaRz76Dev"
            webbrowser.get().open(url)
            self.engine_speak(f"Here's github/{self.person}\n")

            # portfolio
        if self.there_exist(["search for"]):
            search_term = voice_data.split("for")[-1]
            url = "https://portifolio-rafarz76dev.netlify.app/" + search_term
            webbrowser.get().open(url)
            self.engine_speak(f"Here is the portfolio of {self.person}\n")


assistent = Virtual_assit("Robot", "RafaRz76Dev")

while True:
    voice_data = assistent.record_audio("listening...\n")
    assistent.respond(voice_data)

    if assistent.there_exist(["bye", "goodbye", "seeyou", "see you later", "see you"]):
        assistent.engine_speak("Have a nice day! Good bye!\n")
        break
