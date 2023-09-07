alpha = {'AEIOULNSTRАВЕИНОРСТ': 1,
'DGДКЛМПУ': 2,
'BCMPБГЁЬЯ': 3,
'FHVWYЙЫ': 4,
'KЖЗХЦЧ': 5,
'JXШЭЮ': 8,
'QZФЩЪ': 10}

word = input('Введите слово: ')
total = 0
new_alpha = {}
for letters, score in alpha.items():
    new_alpha.update(dict.fromkeys(letters, score))

for char in word.upper():
    total += new_alpha.get(char)

# for char in word.upper():
# for letters, score in alpha.items():
# if char in letters:
# total += score

print(f'Слово {word} весит {total} очков')