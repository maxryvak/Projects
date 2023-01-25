import json

words = []

with open('badwords.txt', encoding='utf-8') as badwords:
    for word in badwords:
        badword = word.lower().split('\n')[0]
        if badword != '':
            words.append(badword)

with open('badwords.json', 'w', encoding='utf-8') as badwords:
    json.dump(words, badwords)