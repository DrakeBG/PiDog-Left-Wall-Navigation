#Seeing if both words are in both sentences
string1 = "I am a student in American University"
string2 = "American University is where I am studying"

duplicates = {}

string1_words = string1.split()
string2_words = string2.split()

for word1 in string1_words:
    for word2 in string2_words:
        if word1 == word2:
            duplicates[word1] = 1
print (duplicates)