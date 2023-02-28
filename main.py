import speech_recognition as sr
import pyttsx3


def speak(voice):
    engine = pyttsx3.init()
    engine.say(voice)


def main():
    file = open("webserver.txt", "w")
    r = sr.Recognizer()
    speak("Are you currently in pain?")
    with sr.Microphone() as source:
        print("Recognizing...")
        text = r.recognize_google(r.record(source, duration=int(3)))
        print(text)
    if text == "Yes" or text == "yes":
        speak("What kind of pain is it?")
        with sr.Microphone() as source:
            print("Recognizing...")
            text = r.recognize_google(r.record(source, duration=int(3)))
            print(text)
            str_text = repr(text)
            file.write("Pain Type: \n" + str_text + "\n")
            speak("Is it upper or lower body?")
            with sr.Microphone() as source:
                audio_data = r.record(source, duration=int(3))
                print("Recognizing...")
                text = r.recognize_google(audio_data)
                print(text)
            if text == "upper" or text == "Upper":
                speak("Is it your head, arms, shoulders, chest, or abdomen?")
                with sr.Microphone() as source:
                    print("Recognizing...")
                    text = r.recognize_google(r.record(source, duration=int(3)))
                    print(text)
                if text == "head" or text == "Head":
                    pass
                elif text == "arms" or text == "Arms":
                    speak("Is it your left or right arm?")
                    with sr.Microphone() as source:
                        print("Recognizing...")
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print(text)
                    if text == "left" or text == "Left":
                        pass
                    elif text == "right" or text == "Right":
                        pass
                elif text == "shoulders" or text == "Shoulders":
                    speak("Is it your left or right shoulder?")
                    with sr.Microphone() as source:
                        print("Recognizing...")
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print(text)
                    if text == "left" or text == "Left":
                        pass
                    elif text == "right" or text == "Right":
                        pass
                elif text == "chest" or text == "Chest":
                    speak("Is it to the left or right side of your chest?")
                    with sr.Microphone() as source:
                        print("Recognizing...")
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print(text)
                    if text == "left" or text == "Left":
                        pass
                    elif text == "right" or text == "Right":
                        pass
                elif text == "abdomen" or text == "Abdomen":
                    pass
            elif text == "lower" or text == "Lower":
                speak("Is it your legs, ankles, feet, groin, or posterior?")
                with sr.Microphone() as source:
                    print("Recognizing...")
                    text = r.recognize_google(r.record(source, duration=int(3)))
                    print(text)
                if text == "legs" or text == "Legs":
                    pass
                elif text == "ankles" or text == "Ankles":
                    speak("Is it your left or right ankle?")
                    with sr.Microphone() as source:
                        print("Recognizing...")
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print(text)
                    if text == "left" or text == "Left":
                        pass
                    elif text == "right" or text == "Right":
                        pass
                elif text == "feet" or text == "Feet":
                    speak("Is it your left or right foot?")
                    with sr.Microphone() as source:
                        print("Recognizing...")
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print(text)
                    if text == "left" or text == "Left":
                        pass
                    elif text == "right" or text == "Right":
                        pass
                elif text == "groin" or text == "Groin":
                    pass
                elif text == "posterior" or text == "Posterior":
                    pass
    elif text == "no" or text == "No":
        speak("What is it that you need?")
        with sr.Microphone() as source:
            print("Recognizing...")
            text = r.recognize_google(r.record(source, duration=int(3)))
            print(text)

    elif text != "Yes" or text != "yes" or text != "no" or text != "no":
        speak("Please respond with yes or no.")


if __name__ == "__main__":
    main()
