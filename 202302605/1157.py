word = input().upper()
spell = list(set(word))
# set은 중복된 요소들을 제거, 하나만 남김.
# ex) word = 'mississipi' / spell = list(set(word)) = ['m', 'i', 's', 'p'] 
list = []

for i in spell:
    count = word.count(i)
    list.append(count)

if list.count(max(list)) >= 2:
    print('?')

else:
    print(spell[list.index(max(list))])