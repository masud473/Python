import pyttsx3

speech_engine = pyttsx3.init()
voices = speech_engine.getProperty('voices')
for voice in voices:
    print ('voice', voice.id)
    #speech_engine.setProperty('voice', voice.id)
    #speech_engine.say('The quick brown fox')


# here I find I have installed just 1 eSpeak voice into the Tokens DIR;

anna_voice = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MS-Anna-1033-20-DSK'

male_voice_1 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\eSpeak'
#=====
rate = speech_engine.getProperty('rate')
# the rate should be signed + for faster or - for slower
speech_engine.setProperty('rate', rate-85)
#=====

volume = speech_engine.getProperty('volume')
speech_engine.setProperty('volume', volume+1.0)
#=====
def speak(input_text):
    global talking_yes_or_no
    i = ''
    txt_list = list(input_text)
    if len(txt_list) > 0:
        for i in txt_list:
            if i == '':
                txt_list.remove(i)
    txt = ''.join(txt_list)
    if txt != "":
        speech_engine.say(txt)
        speech_engine.runAndWait()
#=====
def use_anna_voice():
    speech_engine.setProperty('voice', anna_voice)
#=====
def use_male_voice_1():
    speech_engine.setProperty('voice', male_voice_1)