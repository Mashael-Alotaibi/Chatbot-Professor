from tkinter import *
from random import choice
from PIL import Image, ImageTk



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





user = StringVar()
bot = StringVar()

wiindow.title("Professor...")

Label(wiindow, text=" أسألني").pack()
Entry(wiindow, textvariable=user).pack(side=LEFT)

Label(wiindow, text="  ").pack()
Label(wiindow, textvariable=bot).pack()

def main():
    question = user.get()
    if question in greeting:
        bot.set(choice(response))
        im = Image.open("waving.gif")


    elif question in userinput:
        index = userinput.index(question)
        bot.set(response_userinput[index])

    else:
        bot.set(choice(error))

Button(wiindow, text="speak", command=main).pack(side=LEFT)


mainloop()