import speech_recognition as sr
import pyttsx3
import threading


def speak(voice):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.say(voice)
    engine.runAndWait()


def main():
    file = open("webserver.txt", "w")
    r = sr.Recognizer()
    threading.Thread(target=speak, args=("Are you currently in pain?",)).start()
    with sr.Microphone() as source:
        print("Recognizing...")
        text = r.recognize_google(r.record(source, duration=int(3)))
        if text == 'yes' or fl == 'Yes':
            threading.Thread(target=speak, args=("What kind of pain is it?",)).start()
            with sr.Microphone() as source:
                print("Recognizing...")
                text = r.recognize_google(r.record(source, duration=int(3)))
                file.write("Pain Type: \n" + repr(text) + "\n")
                threading.Thread(target=speak, args=("Is it upper or lower body?",)).start()
            with sr.Microphone():
                audio_data = r.record(source, duration=int(3))
                print("Recognizing...")
                text = r.recognize_google(audio_data)
            if text == "upper" or text == "Upper":
                threading.Thread(target=speak, args=("Is it your head, arms, shoulders, chest, or abdomen?",)).start()
                with sr.Microphone():
                    print("Recognizing...")
                    text = r.recognize_google(r.record(source, duration=int(3)))
                if text == "head" or text == "Head":
                    file.write("Location: \n" + repr(text) + "\n")
                    return None
                elif text == "arms" or text == "Arms":
                    file.write("Location: \n" + repr(text))
                    threading.Thread(target=speak, args=("Is it your left or right arm?",)).start()
                    with sr.Microphone():
                        print("Recognizing...")
                        text = r.recognize_google(r.record(source, duration=int(3)))
                    if text == "left" or text == "Left":
                        file.write(": " + repr(text))
                        return None
                    elif text == "right" or text == "Right":
                        file.write(": " + repr(text))
                        return None
                elif text == "shoulders" or text == "Shoulders":
                    file.write("Location: \n" + repr(text))
                    threading.Thread(target=speak, args=("Is it your left or right shoulder?",)).start()
                    with sr.Microphone():
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print("Recognizing...")
                        file.write("Location: \n" + repr(text))
                    if text == "left" or text == "Left":
                        file.write(": " + repr(text))
                        return None
                    elif text == "right" or text == "Right":
                        file.write(": " + repr(text))
                        return None
                elif text == "chest" or text == "Chest":
                    file.write("Location: \n" + repr(text))
                    threading.Thread(target=speak, args=("Is it to the left or right side of your chest?",)).start()
                    with sr.Microphone():
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print("Recognizing...")
                    if text == "left" or text == "Left":
                        file.write(": " + repr(text))
                        return None
                    elif text == "right" or text == "Right":
                        file.write(": " + repr(text))
                        return None
                elif text == "abdomen" or text == "Abdomen":
                    file.write(": " + repr(text))
                    return None
            elif text == "lower" or text == "Lower":
                threading.Thread(target=speak, args=("Is it your legs, ankles, feet, groin, or posterior?",)).start()
                with sr.Microphone():
                    text = r.recognize_google(r.record(source, duration=int(3)))
                    print("Recognizing...")
                    print(text)
                if text == "legs" or text == "Legs":
                    file.write("Location: \n" + repr(text))
                    return None
                elif text == "ankles" or text == "Ankles":
                    file.write("Location: \n" + repr(text))
                    threading.Thread(target=speak, args=("Is it your left or right ankle?",)).start()
                    with sr.Microphone():
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print("Recognizing...")
                        print(text)
                    if text == "left" or text == "Left":
                        file.write(": " + repr(text))
                        return None
                    elif text == "right" or text == "Right":
                        file.write(": " + repr(text))
                        return None
                elif text == "feet" or text == "Feet":
                    file.write("Location: \n" + repr(text))
                    threading.Thread(target=speak, args=("Is it upper or lower body?",)).start()
                    speak("Is it your left or right foot?")
                    with sr.Microphone():
                        text = r.recognize_google(r.record(source, duration=int(3)))
                        print("Recognizing...")
                    if text == "left" or text == "Left":
                        return None
                    elif text == "right" or text == "Right":
                        return None
                elif text == "groin" or text == "Groin":
                    file.write("Location: \n" + repr(text))
                    return None
                elif text == "posterior" or text == "Posterior":
                    file.write("Location: \n" + repr(text))
                    return None
        elif text == 'no' or text == 'No':
            threading.Thread(target=speak, args=("What is it that you need?",)).start()
            with sr.Microphone() as source:
                text = r.recognize_google(r.record(source, duration=int(3)))
                print("Recognizing...")
                file.write("Paictent's request: \n" + repr(text) + "\n")


if __name__ == "__main__":
    main()
    threading.Thread(target=speak, args=("Please wait for assistance.",)).start()
