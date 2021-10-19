from collections import Counter
import csv

# cipher = "uosulmkgu fumucfjb bcm euul jrlpxjsup kl rfpuf sr kdwfrgu sbu mujxfkst clp uzzkjkuljt rz uaujsfrlkj " \
#          "cxjskrlm. briuguf, lrs dxjb cssulskrl bcm euul wckp sr sbu pumkhl kmmxum. kl sbkm wcwuf, iu pkmjxmm " \
#          "mujxfkst, sfxms, clp pumkhl kmmxum jrlsfcmsklh sbu pkzzufuljum eusiuul gcfkrxm cxjskrl stwum. iu ikaa mbri " \
#          "sbcs wrrf pumkhl zrf cl uaujsfrlkj cxjskrl efucjbum sbu mujxfkst rz sbu mtmsud clp puhfcpum ksm " \
#          "wfcjskjcakst --lr dcssuf bri mujxfu uzzkjkuls cfu sbu exkapklh earjvm rz cl uaujsfrlkj cxjskrl. " \
#          "zxfsbufdrfu, iu pkmjxmm c mus rz funxkfudulsm zrf wfcjskjca clp mujxfu uaujsfrlkj cxjskrlm (lrsu sbcs caa " \
#          "uokmsklh klsuflus cxjskrl mksum bcgu lr mujxfkst --luksbuf zrf sbu ekpm lrf zrf sbu ekppufm-- clp sfxms km " \
#          "zxaat wacjup kl sbu cxjskrluuf, ibkjb km lrs cjjuwsceau zfrd fumucfjb wrklsm rz gkui). "

cipher = "omqisespiakgwfvoangvkuvqdiqimfsrtklowuiakgwfvzprpzljmekzbnbusyqmprgkjoljweagvqhymeuhgkxggnbruucahtwxzrggwtlvbxbubusjmiwaryqmprgkjoliwtsxmlolkzqbbjixmccgcriewekxgchfoxicvplamgckpkqegzuvtrqfuvcgokquvnzimwcvfvukvggditgfqymsmfvrdkjrsexxwccjmjnbftwtlhqkqtofstcxmiwtsxmlolkzqbbjitmaucqypnitbowawjilqegkxxqpsfxkvowuiakgwfvzprpzlgubiebyiesbvueahfirtcoibomfoelhqqrvzyighvuvbgcfczjvrviipbhymxbusyqmprgkjolqsinuznuzdkvgwdmucgdvzowqkzvyiardcybcopitizclvzmdirtzwgvveovaweohqqoemtoywjpgcphzwtqfhymswfhnmrtxbfetbldvwlihqkquvnbuqyevrvtecfsunuzesrtkagokmnwjsmmxqgzvayiqogbgjyskwuvywemyqgirbowagtwsxnfvlzwfsrtklowuiakgwfvylhskwobffvtoiaqvwtzrocbourdiqimhduizmfseorqfvrvjdvqbzkgnitbowagrzkkbbjqjmesuiyifqvvjqauuckbbhymhqqrvzyjvruqtohdkpkarhktkurbkxxqps"


# print(cipher)

# Functions
def count_words():
    # Remove punctuation
    word_string = cipher.replace(',', '').replace('.', '').replace('--', '')
    # Split words into a list
    word_string = word_string.split(' ')
    # Count the list and put it into a dictionary
    a = dict(Counter(word_string))
    print("Number of words: ")
    sorted_words = sorted(a.items(), key=lambda item: item[1], reverse=True)
    for y in range(len(sorted_words)):
        print(sorted_words[y])


def write_plaintext():
    global i
    plaintext = ''
    i = 0
    for c in cipher:
        if c in correct_letters:
            c = correct_letters.get(c)

        plaintext = plaintext + c
    print(plaintext)


COUNT = 7

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
letters = {}
correct_letters = {}

# Counts the number of letters
for i in range(len(alphabet)):
    letters[alphabet[i]] = cipher.count(alphabet[i])

# Sorts the key from descending
sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)

print("Number of letters: ")
for x in range(len(sorted_letters)):
    print(sorted_letters[x])

trigram = ""
index = 0
trigrams = {}
for l in cipher:
    if index < len(cipher) - 3:
        trigram = l + cipher[index + 1] + cipher[index + 2]
        if trigram in trigrams:
            trigrams[trigram] += 1
        else:
            trigrams[trigram] = 1
    index += 1

    # try:
    #     trigram = l + l[index + 1] + l[index + 2]
    #
    # except IndexError:
    #     pass
    # else:
    #     trigram = l + l[index + 1] + l[index + 2]
    #     if trigram in trigrams:
    #         trigrams[trigram] += 1
    #     else:
    #         trigrams[trigram] = 0

    # if len(trigram) == 3:
    #     if trigram in trigrams:
    #         trigrams[trigram] += 1
    #         trigram = l + l[index + 1] + l[index + 2]
    #
    #     else:
    #         trigrams[trigram] = l + l[index + 1] + l[index + 2]
    #     trigram = l + l[index + 1] + l[index + 2]
    # else:
    #     trigram += l
    # index += 1


# sorted_trigrams = {}


digram = ""
digrams = {}
for l in cipher:
    if len(digram) == 2:
        if digram in digrams:
            digrams[digram] += 1
            digram = l

        else:
            digrams[digram] = 1
        digram = l
    else:
        digram += l


sorted_trigrams = sorted(trigrams.items(), key=lambda item: item[1], reverse=True)
print(sorted_trigrams)
sorted_digrams = sorted(digrams.items(), key=lambda item: item[1], reverse=True)
print(sorted_digrams)


count = 0
cipherText = ""
for l in cipher:
    if count == COUNT:
        cipherText += l + ' '
        count = 0
    else:
        cipherText += l
        count += 1

print(cipherText)

with open('letters.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in letters.items():
        writer.writerow([key, value])
    csv_file.close()


# Dictionary for the correct letters derived from the testing
# correct_letters = {
#     'a': 'l',
#     'b': 'h',
#     'c': 'a',
#     'd': 'm',
#     'e': 'b',
#     'f': 'r',
#     'g': 'v',
#     'h': 'g',
#     'i': 'w',
#     'j': 'c',
#     'k': 'i',
#     'l': 'n',
#     'm': 's',
#     'n': 'q',
#     'o': 'x',
#     'p': 'd',
#     'q': 'j',
#     'r': 'o',
#     's': 't',
#     't': 'y',
#     'u': 'e',
#     'v': 'k',
#     'w': 'p',
#     'x': 'u',
#     'y': 'z',
#     'z': 'f'
# }

# correct_letters = {
#     'a': 'l',
#     'b': 'h',
#     'c': 'a',
#     'd': 'X',
#     'e': 'b',
#     'f': 'r',
#     'g': 'X',
#     'h': 'X',
#     'i': 'X',
#     'j': 'X',
#     'k': 'i',
#     'l': 'n',
#     'm': 's',
#     'n': 'X',
#     'o': 'X',
#     'p': 'd',
#     'q': 'X',
#     'r': 'o',
#     's': 't',
#     't': 'X',
#     'u': 'e',
#     'v': 'X',
#     'w': 'X',
#     'x': 'u',
#     'y': 'X',
#     'z': 'f'
# }


# Rewrite the correct sentence
