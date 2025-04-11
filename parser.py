answer1 = "авто водитель ООО"
answer2 = "водитель авто"
answer3 = "авто водитель"
answer4 = "ООО"
answer5 = "авто водитель ИП"
answer6 = "ИП ООО"
answer7 = "водитель"
answer8 = "   "
answer9 = ""

allowed = ["авто", "водитель"]

# for word in words:
# if word in allowed:
# result.append(word)

def parse(text: str):
    words = text.split(" ") 
    result = []
    for word in words:
        if word in allowed:
            result.append(word) 
     
    
    return result 

# ["ИП"]
print(parse('америка франция ИП'))
print(parse('америка франция зеландия ИП водитель'))
print(parse('америка россия франция зеландия ООО водитель'))

#проверить что ИП и ООО нельзя и вернуть пустой список
