from translate_shell.translate import translate
# import text2emotion as te

#text = "Seriously membazir celebrate awal2 ni. Lebih kepada feel good factor sahaja. Whether rakyat really celebrate it is another question mark. Or do they even bother"
text3 = "Kerajaan madani is the best! Tolak bersih BODOH PAK LEBAI X PANDAI JAGA NEGARA"
#text2 = "Apa macam kamu?"

textList = text3.split(" ")

print(textList)

textlist2 = []
for txt in textList:
    translate_en = translate(txt, source_lang="auto", target_lang="en").results[0].paraphrase
    textlist2.append(translate_en)


newTxt = ' '.join(textlist2)
print(newTxt)

# emotionDetected = te.get_emotion(newTxt)
# print(emotionDetected)

