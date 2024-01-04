from win32com.client import Dispatch
def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)
# with open("F:\\downloads\\Python apps\\55 language.txt", "r") as f:
#     for item in f.readlines():
#         speak(item)

with open("lang.txt", "rt", encoding="utf8") as f:
    for item in f.readlines():
        # print(item)
        speak(item)