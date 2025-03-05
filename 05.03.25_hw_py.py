def vowels_count(s):
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1
    return count

def consonants_count(s):
    consonants = "бвгґджзйклмнпрстфхцчшщБВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ"
    count = 0
    for letter in s:
        if letter in consonants:
            count += 1
    return count

text = input("Введите текст: ")
vowels_result = vowels_count(text)
consonants_result = consonants_count(text)

print("Гласных букв:", vowels_result)
print("Согласных букв:", consonants_result)
