from tkinter import *

from random import choice
import webbrowser
from PIL import Image, ImageTk
from enum import Enum


greeting = ["اهلا", "مرحبا","اهلا و سهلا"]
response = ["أهلا أهلا", "مرحبا", "اهلا بك"]
error = ["هل يمكنك تبسيط السؤال قليلا", "لا اعلم ما الذي تقصدة", "ما الذي قلته"," اعد السؤال بطريقة مختلفة" ]

userinput=["الانفجار العظيم","الزمكان","الثقوب السوداء","الطاقة النووية","السفر عبر الزمن"]

response_userinput=[
"تمثّلُ نظريّة الإنفجار العظيم التفسير الأساسيّ لكيفيّة بدء الكون؛ إذ تعطينا هذه النظرية، في أبسط صورها، تصوّرًا عن نشأةِ الكون الذي بدأ من نقطةٍ مفردة شديدة الكثافة أخذت تتضخّمُ خلال الـ 13,8 مليار سنة التالية، لتصبحَ الكونَ الذي نعرفه اليوم",
"دمج لمفهومي الزمان والمكان، هو الفضاء بأبعادها الأربعة، الأبعاد المكانية الثلاثة التي نعرفها؛ الطول والعرض والارتفاع، مضاف إليها الزمن كبعد رابع هذه الفضاء الرباعي تشكل نسيج أو شبكة تحمل كل شيء في هذا الكون",
"منطقة موجودة في الزمكان تتميز بجاذبية قوية جداً بحيث لايمكن لأي شيء  ولا حتى الجسيمات أو موجات الإشعاع الكهرومغناطيسي مثل الضوء  الإفلات منها",
"الطاقة المنبعثة بنسب كبيرة في العمليات المؤثرة على أنوية الذرات، وبشكلٍ عام فإن الطاقة النووية  يتم توليدها بعدة طرق ومنها الانشطار النووي الذي يحدث في المفاعلات النووية العالمية",
"يمكن السفر عبر الزمن عن طريق الثقب الدودي (Wormhole) وهو  عبارة عن ممر نظري موجود في الزمكان (Space-time)، وبإمكانه خلق طرق مختصرة لرحلات طويلة عبر الكون. تم التنبؤ بالثقوب الدودية من قبل النسبية العامة"]

wiindow=Tk()

image_paths = ["img/waving.gif", "img/holding-a-pointer.gif", "img/sign-with-advice.gif", "img/idea.gif", "img/stop-sign.gif"]

img1 = Image.open(image_paths[0])
img1 = ImageTk.PhotoImage(img1)
panel = Label(wiindow, image=img1)
panel.pack()


user = StringVar()
bot = StringVar()

wiindow.title("Professor...")

class Mood(Enum):
    HI = 0
    ADVICSE = 1
    CONFUSE = 2
    IDEA = 3
    STOP = 4

Label(wiindow, text=" أسألني").pack()
Entry(wiindow, textvariable=user).pack(side=LEFT)

Label(wiindow, text="  ").pack()
Label(wiindow, textvariable=bot).pack()


def main():
    global panel
    global img1
    global window

    question = user.get()
    if question in greeting:
        bot.set(choice(response))

    elif question in userinput:
        index = userinput.index(question)
        bot.set(response_userinput[index])
        current_mood = Mood.ADVICSE
    elif "الانفجار العظيم" in question:
        bot.set(response_userinput[0])
        current_mood = Mood.ADVICSE
    elif "الزمكان" in question:
        bot.set(response_userinput[1])
        current_mood = Mood.IDEA
    elif "الثقوب السوداء" in question:
        bot.set(response_userinput[2])
        current_mood = Mood.ADVICSE
    elif "الطاقة النووية" in question:
        bot.set(response_userinput[3])
        current_mood = Mood.IDEA
    elif "السفر عبر الزمن" in question:
        bot.set(response_userinput[4])
        current_mood = Mood.ADVICSE
    else:
        bot.set(choice(error))
        current_mood = Mood.CONFUSE
    
    img1 = Image.open(image_paths[current_mood.value])
    img1 = ImageTk.PhotoImage(img1)
    panel = Label(wiindow, image=img1)
    panel.pack(side=LEFT)



Button(wiindow, text="speak", command=main).pack(side=LEFT)


mainloop()