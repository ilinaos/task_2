## Я не знаю, успею ли я довести задачу до конца, поэтому пока промежуточный этап.
## Если добью, то обновлю
## Я старалась =(

def check(line, match_open, match_close):
    matches=[]
    for i in range(len(line)):
        if line[i] in match_open:
            matches.append(line[i])
        elif line[i] in match_close:
            if matches[-1]!=match_open[match_close.index(line[i])]:
                return False
            else:
                matches.pop()
    if len(matches)==0:
        return True
    else:
        return False


check_string = input('Введите строку для проверки:\n')
input_string=input('Какие скобки будем искать? Введите только открывающие:\n')
#сформировать списки для проверки скобок
input_string=list(set(input_string))
open_list=[]
close_list=[]
for i in input_string:
    if i=='(':
        open_list.append('(')
        close_list.append(')')
    if i=='[':
        open_list.append('[')
        close_list.append(']')
    if i=='{':
        open_list.append('{')
        close_list.append('}')
    if i=='<':
        open_list.append('<')
        close_list.append('>')

print(check(check_string, open_list,close_list))