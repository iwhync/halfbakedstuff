import random
consonant = "bcdfghjklmnprstvwxz"
vowel = "aeiou"
word = []
for _ in range(random.randint(3,8)):
    word.append(consonant[random.randint(0,len(consonant)-1)])
    word.append(vowel[random.randint(0,len(vowel)-1)])
word = "".join(word)
print(word)
