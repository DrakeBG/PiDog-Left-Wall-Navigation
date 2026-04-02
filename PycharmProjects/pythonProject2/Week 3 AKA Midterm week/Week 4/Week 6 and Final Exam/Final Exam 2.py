word = "This is American University in Washington DC. TT"

letter_count ={}
# for char in word:
#     letter_count[char] = letter_count.get(char, 0)+1

for char in word:
    if char in letter_count.keys():
        letter_count[char] += 1
    else:
        letter_count[char] = 1

print (letter_count['n']) #Answer is 5

# for key in sorted(letter_count.keys()):
#     if letter_count[key] >1:
#         print (key, letter_count[key])
#
print (letter_count)


word2 = "Embourgeoisement almost always refers to a shift by the working class, not the upper class. The word was coined during the first half of the 20th century, when scholars noticed workers adopting the outlook and behavior of the middle class. For example, the new bourgeois might have a declining interest in class consciousness and an increased interest in seeing gradual, not revolutionary, changes in society."


sting1 = word2.split()
biggest_word = {}
for x in sting1:
    if x in biggest_word():
        print(x)

print(biggest_word)
