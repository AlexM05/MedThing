import speech_recognition as sr
import pyttsx3
import threading


def speak(voice):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 200)
    engine.say(voice)
    engine.runAndWait()


def main():
    file = open("webserver.txt", "w")
    r = sr.Recognizer()
    threading.Thread(target=speak, args=("Are you currently in pain?",)).start()
    with sr.Microphone() as source:
        print("Recognizing...")
        text = r.recognize_google(r.record(source, duration=int(3)))
        print(text)
    if text == "Yes" or text == "yes":
        threading.Thread(target=speak, args=("What kind of pain is it?",)).start()
        with sr.Microphone() as source:
            print("Recognizing...")
            text = r.recognize_google(r.record(source, duration=int(3)))
            print(text)
            str_text = repr(text)
            file.write("Pain Type: \n" + str_text + "\n")
            threading.Thread(target=speak, args=("Is it upper or lower body?",)).start()
            with sr.Microphone() as source:
                audio_data = r.record(source, duration=int(3))
                print("Recognizing...")
                text = r.recognize_google(audio_data)
                print(text)
            if text == "upper" or text == "Upper":
                threading.Thread(target=speak, args=("Is it your head, arms, shoulders, chest, or abdomen?",)).start()
                with sr.Microphone() as source:
                    print("Recognizing...")
                    text = r.recognize_google(r.record(source, duration=int(3)))
                    print(text)
                if text == "head" or text == "Head":
                    pass
                elif text == "arms" or text == "Arms":
                    threading.Thread(target=speak, args=("Is it your left or right arm?",)).start()
                    with sr.Microphone() as source:
                        print("Recognizing...")
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print(text)
                    if text == "left" or text == "Left":
                        pass
                    elif text == "right" or text == "Right":
                        pass
                elif text == "shoulders" or text == "Shoulders":
                    threading.Thread(target=speak, args=("Is it your left or right shoulder?",)).start()
                    with sr.Microphone() as source:
                        print("Recognizing...")
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print(text)
                    if text == "left" or text == "Left":
                        pass
                    elif text == "right" or text == "Right":
                        pass
                elif text == "chest" or text == "Chest":
                    threading.Thread(target=speak, args=("Is it to the left or right side of your chest?",)).start()
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
                threading.Thread(target=speak, args=("Is it your legs, ankles, feet, groin, or posterior?",)).start()
                with sr.Microphone() as source:
                    print("Recognizing...")
                    text = r.recognize_google(r.record(source, duration=int(3)))
                    print(text)
                if text == "legs" or text == "Legs":
                    pass
                elif text == "ankles" or text == "Ankles":
                    threading.Thread(target=speak, args=("Is it upper or lower body?",)).start()
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
                    threading.Thread(target=speak, args=("Is it upper or lower body?",)).start()
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
        threading.Thread(target=speak, args=("What is it that you need?",)).start()
        with sr.Microphone() as source:
            print("Recognizing...")
            text = r.recognize_google(r.record(source, duration=int(3)))
            print(text)

    elif text != "Yes" or text != "yes" or text != "no" or text != "no":
        threading.Thread(target=speak, args=("Please respond with yes or no.",)).start()


if __name__ == "__main__":
    main()
