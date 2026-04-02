str1 = 'To be, or not to be, that is the question: Whether \'tis nobler in the mind to suffer\
        The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles\
        And by opposing end them. To die—to sleep, No more; and by a sleep to say we end\
        The heart-ache and the thousand natural shocks That flesh is heir to: \'tis a consummation\
        Devoutly to be wish\'d. To die, to sleep; To sleep, perchance to dream—ay, there\'s the rub:\
        For in that sleep of death what dreams may come,When we have shuffled off this mortal coil,\
        Must give us pause—there\'s the respect That makes calamity of so long life.'
hamlet_file = open('hamlet_file.txt', 'w')
hamlet_file.write(str1)
hamlet_file.close()
hamlet_file = open('hamlet_file.txt', 'r')
hamlet_file_words = hamlet_file.read()
hamlet_file.close()
# print(hamlet_file_words)
hamlet_vowels = open('hamlet_vowels.txt', 'a')
hamlet_consonants = open('hamlet_consonants.text', 'a')
vowel_count = 0
consonant_count = 0
for var in hamlet_file_words:
    if var == 'A' or var == 'E' or var == 'I' or var == 'U' or var == 'O' or var == 'a' or \
            var == 'e' or var == 'i' or var == 'u' or var == 'o' or var =='Y' or var == 'y':
        hamlet_vowels.write(f'{var}\n')
        vowel_count +=1
    elif var == ' ' or var == '\'' or var == '—' or var == '.' or var == ';' or var == ':' or var == ',':
        pass
    else:
        hamlet_consonants.write(f'{var}\n')
        consonant_count +=1
hamlet_vowels.close()
hamlet_consonants.close()
print(f'This passage has {vowel_count} vowels.')
print(f'This passage has {consonant_count} consonants.')