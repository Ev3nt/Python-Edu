morze = {'А': '•—','Б': '—•••','В': '•——', 'Г': '——•', 'Д': '—••', 'Е': '•', 'Ж': '•••—', 'З': '——••', 'И': '••', 'Й': '•———' ,'К': '—•—' ,'Л': '•—••', 'М': '——', 'Н': '—•', 'О': '———', 'П': '•——•', 'Р': '•—•', 'С': '•••', 'Т': '—', 'У': '••—', 'Ф': '••—•' ,'Х': '••••' ,'Ц': '—•—•', 'Ч': '———•', 'Ш': '————', 'Щ': '——•—', 'Ъ': '•——•—•', 'Ы': '—•——', 'Ь': '—••—', 'Э': '••—••', 'Ю': '••——', 'Я': '•—•—', '0': '—————', '1': '•————', '2': '••———', '3': '•••——', '4': '••••—', '5': '•••••', '6': '—••••', '7': '——•••', '8': '———••', '9': '————•', ',': '•—•—•—', '.': '••••••', ';': '—•—•—', ':': '———•••', '?': '••——••', '!': '——••——', '-': '—••••—', ' ': '\t'}

def Crypt(str):
    str = str.upper()

    data = ''

    # Тут просто, пробегаясь по строке, сопоставляем её с символом в таблице.
    for l in str:
        data += morze[l] + ' '

    return data

def Decrypt(str):
    str = str.upper()

    data = ''

    # Здесь по-интереснее, разбивает строку на куски, используя пробел как сепаратор, далее идёт от обратного, ищем ключ в таблице по известному значению.
    str = str.split(' ')
    for l in str:
        for k, v in morze.items():
            if l == v:
                data += k

    return data