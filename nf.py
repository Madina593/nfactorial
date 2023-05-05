import string
 
def en_matr(key):
    # создание таблицы символов по ключу
    new_key = ''
    for lett in key:
        if lett not in new_key:
            new_key += lett
    table = []
    lett = new_key + ''.join(sorted(set(string.ascii_uppercase).difference(set(key))))
    lett = lett.replace('J','') # чтобы уменьшить обычно опускается J
    for i in range(0, coll_line*5, coll_line):
        table.append(list(lett[i:i+5]))
    return table
 
def bigram(data):
    # разделяем строку на биграммы 
    data = data.replace(' ','') #для одного слова можно убрать
    bigr = []
    n = 0
    # пока в биграмме нет одинаковых символов перезаписываем строку с добавлением Х
    while n < len(data)-1:
        if data[n] == data[n+1]:
            data = data[:n+1] + 'X' + data[n+1:]
            n = 0
        n += 2
    if len(data)%2:
        data = data +'X'
    list_bigr = [data[i:i+2] for i in range(0,len(data),2)]
    return list_bigr
            
def code_(key, data):
    # получаем индексы букв, собираем новую строку по перестановкам
    result = ''
    table = en_matr(key) 
    for big in bigram(data):
        l,r = list(big)
        for i, line in enumerate(table):
            if l in line:
                index_l = [i, line.index(l)]
            if r in line:
                index_r = [i, line.index(r)]
        result += substitute((index_l, index_r), table)
    return result
 
def substitute(site_, table):
    # переставляем символы по условиям
    left, right = site_
    if left[0] == right[0]:
        left[1] = (left[1]+1)%coll_line
        right[1] = (right[1]+1)%coll_line
        
    elif left[1] == right[1]:
        left[0] = (left[0]+1)%coll_line
        right[0] = (right[0]+1)%coll_line
 
    else:
        tmp = left[0]
        left[0] = right[0] 
        right[0] = tmp
        return table[right[0]][right[1]]+ table[left[0]][left[1]]
 
    return table[left[0]][left[1]]+table[right[0]][right[1]]
        
 
coll_line = 5    
key = 'WHEATSON'
# кодируем всю строку удалив пробелы (как потом их находить?)
data = 'IDIOCY OFTEN LOOKS LIKE INTELLIGENCE'
print(code_(key, data))
# кодируем слова ( добавил от себя)
for i in data.split():
    print(code_(key, i), end = ' ')