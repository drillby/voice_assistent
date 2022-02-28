import modules.VoiceAssistent.voice_assistent as voice_assistent
import random
import modules.VoiceAssistent.errors.custome_errors as custome_errors

va = voice_assistent.VoiceAssistent("hello")


def list_to_str(arr) -> str:
    str = ""
    for word in arr:
        str += word

    return str


while True:
    print("listening")
    text = va.get_audio()
    print(text)
    if text.count(va.wake_word) > 0:
        va.speak(random.choice(va.speach_responses["on_start"]))
        text = None
        while not text:
            text = va.get_audio()

        text_arr = text.split()
        if text in va.key_words["kill_bot"]:
            va.speak(random.choice(va.speach_responses["confirmation"]))

        elif text_arr[0] in va.key_words["open"]:
            text_arr.pop(0)
            text = list_to_str(text_arr)
            if text in va.key_words["apps"]["spotify"]:
                try:
                    va.open_spotify()
                    va.speak(random.choice(va.speach_responses["confirmation"]))
                except Exception:
                    va.speak(custome_errors.CannotOpenApplication().__str__())

            elif text in va.key_words["apps"]["google_chrome"]:
                try:
                    va.speak(random.choice(va.speach_responses["confirmation"]))
                    va.open_chrome()
                except Exception:
                    va.speak(custome_errors.CannotOpenApplication().__str__())

            elif text in va.key_words["apps"]["code"]:
                va.speak(random.choice(va.speach_responses["code"]))
                text = None
                while not text:
                    text = va.get_audio()

                if text in va.key_words["code_project"]["smart_bedroom"]:
                    try:
                        va.speak(random.choice(va.speach_responses["confirmation"]))
                        va.open_code(va.paths["linux"]["smart_bedroom"])
                    except Exception:
                        va.speak(custome_errors.CannotOpenApplication().__str__())

                elif text in va.key_words["code_project"]["voice_assistent"]:
                    try:
                        va.speak(random.choice(va.speach_responses["confirmation"]))
                        va.open_code(va.paths["linux"]["voice_assistent"])
                    except Exception:
                        va.speak(custome_errors.CannotOpenApplication().__str__())

                elif text in va.key_words["code_project"]["automatization_of_pc"]:
                    try:
                        va.speak(random.choice(va.speach_responses["confirmation"]))
                        va.open_code(va.paths["linux"]["automatization_of_pc"])
                    except Exception:
                        va.speak(custome_errors.CannotOpenApplication().__str__())

                elif text in va.key_words["code_project"]["side_job"]:
                    try:
                        va.speak(random.choice(va.speach_responses["confirmation"]))
                        va.open_code(va.paths["linux"]["Holecek_brigada"])
                    except Exception:
                        va.speak(custome_errors.CannotOpenApplication().__str__())

        elif text_arr[0] in va.key_words["close"]:
            text_arr.pop(0)
            text = list_to_str(text_arr)
            if text in va.key_words["apps"]["spotify"]:
                try:
                    va.close_spotify()
                    va.speak(random.choice(va.speach_responses["confirmation"]))
                except Exception:
                    va.speak(custome_errors.CannotCloseApplication().__str__())

            elif text in va.key_words["apps"]["google_chrome"]:
                try:
                    va.close_chrome()
                    va.speak(random.choice(va.speach_responses["confirmation"]))
                except Exception:
                    va.speak(custome_errors.CannotCloseApplication().__str__())

            elif text in va.key_words["apps"]["code"]:
                try:
                    va.close_code()
                    va.speak(random.choice(va.speach_responses["confirmation"]))
                except Exception:
                    va.speak(custome_errors.CannotCloseApplication().__str__())

        elif text_arr[0] in va.key_words["search"]:
            text_arr.pop(0)
            text = list_to_str(text_arr)
            try:
                va.search_on_internet(text)
            except Exception:
                va.speak(custome_errors.CannotSearchOnInternet.__str__())
