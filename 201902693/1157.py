from collections import Counter
word = str(input())
count_word = Counter(word.upper())

if len(count_word) == 1:
    print(count_word.most_common(1)[0][0])
else :
    a1, a2 = count_word.most_common(2)
    if a1[1] == a2[1] :
        print('?')
    else :
        print(a1[0])