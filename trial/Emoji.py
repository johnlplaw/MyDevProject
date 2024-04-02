import demoji

txt = "Email: rasapopmedia@gmail.com. Inquiries for event appearances are temporarily closed 🙏🏻 Derma untuk G AZ A di sini:"

def demoji_proc(input):

    result_dic = demoji.findall(txt)
    inputList = input.split()
    newInputList = []
    for a in inputList:
        if result_dic.get(a):
            emoji_desc = result_dic.get(a)
            emoji_descList = emoji_desc.split(":")
            a = emoji_descList[0].replace(" ", "_").strip()
        newInputList.append(a)
    return " ".join(newInputList)

a = demoji_proc(txt)
print(a)

#print(result["🙏🏻"])