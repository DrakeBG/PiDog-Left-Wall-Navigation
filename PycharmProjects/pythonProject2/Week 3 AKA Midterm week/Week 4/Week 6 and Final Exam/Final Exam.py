str1 = 'Either the well was very deep, or she fell very slowly, for she had\
        plenty of time as she went down to look about her and to wonder what\
        was going to happen next. First, she tried to look down and make out\
        what she was coming to, but it was too dark to see anything; then she\
        looked at the sides of the well, and noticed that they were filled with\
        cupboards and book-shelves; here and there she saw maps and pictures\
        hung upon pegs. She took down a jar from one of the shelves as she\
        passed; it was labelled “ORANGE MARMALADE”, but to her great\
        disappointment it was empty: she did not like to drop the jar for fear\
        of killing somebody underneath, so managed to put it into one of the\
        cupboards as she fell past it.'
para_file = open('para_file.txt', 'w')
para_file.write(str1)
para_file.close()
para_file = open('para_file.txt', 'r')
para_file_words = para_file.read()
para_file.close()



def reverse(str0):
    if (len(str0) == 0):
        return str0
    else:
        return(str0[1:]) + str0[0]

str = 'Either the well was very deep, or she fell very slowly, for she had\
        plenty of time as she went down to look about her and to wonder what\
        was going to happen next. First, she tried to look down and make out\
        what she was coming to, but it was too dark to see anything; then she\
        looked at the sides of the well, and noticed that they were filled with\
        cupboards and book-shelves; here and there she saw maps and pictures\
        hung upon pegs. She took down a jar from one of the shelves as she\
        passed; it was labelled “ORANGE MARMALADE”, but to her great\
        disappointment it was empty: she did not like to drop the jar for fear\
        of killing somebody underneath, so managed to put it into one of the\
        cupboards as she fell past it.'

str2 = reverse(str)

para_file1 = open('para_file1.txt', 'w')
para_file1.write(str2)
para_file1.close()
para_file1 = open('para_file1.txt', 'r')

para_file1.close()
print(str1)
print(str2)