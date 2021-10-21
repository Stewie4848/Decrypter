from collections import Counter
import csv


cipher = "omqisespiakgwfvoangvkuvqdiqimfsrtklowuiakgwfvzprpzljmekzbnbusyqmprgkjoljweagvqhymeuhgkxggnbruucahtwxzrggwtlvbxbubusjmiwaryqmprgkjoliwtsxmlolkzqbbjixmccgcriewekxgchfoxicvplamgckpkqegzuvtrqfuvcgokquvnzimwcvfvukvggditgfqymsmfvrdkjrsexxwccjmjnbftwtlhqkqtofstcxmiwtsxmlolkzqbbjitmaucqypnitbowawjilqegkxxqpsfxkvowuiakgwfvzprpzlgubiebyiesbvueahfirtcoibomfoelhqqrvzyighvuvbgcfczjvrviipbhymxbusyqmprgkjolqsinuznuzdkvgwdmucgdvzowqkzvyiardcybcopitizclvzmdirtzwgvveovaweohqqoemtoywjpgcphzwtqfhymswfhnmrtxbfetbldvwlihqkquvnbuqyevrvtecfsunuzesrtkagokmnwjsmmxqgzvayiqogbgjyskwuvywemyqgirbowagtwsxnfvlzwfsrtklowuiakgwfvylhskwobffvtoiaqvwtzrocbourdiqimhduizmfseorqfvrvjdvqbzkgnitbowagrzkkbbjqjmesuiyifqvvjqauuckbbhymhqqrvzyjvruqtohdkpkarhktkurbkxxqps"








# Finding patterns within the cipher text

hexe = ""
hexes = {}
index = 0
for l in cipher:
    if index < len(cipher) - 6:
        hexe = l + cipher[index + 1] + cipher[index + 2] + cipher[index + 3] + cipher[index + 4] + cipher[index + 5]
        if hexe in hexes:
            hexes[hexe] += 1
        else:
            hexes[hexe] = 1
    index += 1


# Sorting the patterns

sorted_hexes = sorted(hexes.items(), key=lambda item: item[1], reverse=True)
print(sorted_hexes)


# Counting the number of letters within the keyword length. Index 6 = first letter patterns

index = 6
shift = {}
for l in cipher:
    if index == 6:
        if l in shift:
            shift[l] += 1
        else:
            shift[l] = 1
        index = 0
    index += 1


print(shift)

sorted_shift = sorted(shift.items(), key=lambda item: item[1], reverse=True)

print("Sorted shifts: ")
print(sorted_shift)

# Place cipher text into 6 letter words

COUNT = 5
count = 0
cipherText = ""
for l in cipher:
    if count == COUNT:
        cipherText += l + ' '
        count = 0
    else:
        cipherText += l
        count += 1

print("6 letter ciphertext")
print(cipherText)

# Decipher the cipher text into plaintext using the keyword 'ORIGIN'

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
KEYWORD = [14, 17, 8, 6, 8, 13]
plaintext = ''

index = 0
for l in cipher:
    letter_place = alphabet.index(l) - KEYWORD[index]
    if letter_place < 0:
        letter_place = 26 + letter_place
    plaintext += alphabet[letter_place]
    if index == 5:
        index = 0
    else:
        index += 1

print("Plaintext: ")
print(plaintext)

