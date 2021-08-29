from collections import Counter

cipher = "uosulmkgu fumucfjb bcm euul jrlpxjsup kl rfpuf sr kdwfrgu sbu mujxfkst clp uzzkjkuljt rz uaujsfrlkj " \
         "cxjskrlm. briuguf, lrs dxjb cssulskrl bcm euul wckp sr sbu pumkhl kmmxum. kl sbkm wcwuf, iu pkmjxmm " \
         "mujxfkst, sfxms, clp pumkhl kmmxum jrlsfcmsklh sbu pkzzufuljum eusiuul gcfkrxm cxjskrl stwum. iu ikaa mbri " \
         "sbcs wrrf pumkhl zrf cl uaujsfrlkj cxjskrl efucjbum sbu mujxfkst rz sbu mtmsud clp puhfcpum ksm " \
         "wfcjskjcakst --lr dcssuf bri mujxfu uzzkjkuls cfu sbu exkapklh earjvm rz cl uaujsfrlkj cxjskrl. " \
         "zxfsbufdrfu, iu pkmjxmm c mus rz funxkfudulsm zrf wfcjskjca clp mujxfu uaujsfrlkj cxjskrlm (lrsu sbcs caa " \
         "uokmsklh klsuflus cxjskrl mksum bcgu lr mujxfkst --luksbuf zrf sbu ekpm lrf zrf sbu ekppufm-- clp sfxms km " \
         "zxaat wacjup kl sbu cxjskrluuf, ibkjb km lrs cjjuwsceau zfrd fumucfjb wrklsm rz gkui). "

# print(cipher)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
letters = {}

# Counts the number of letters
for i in range(len(alphabet)):
    letters[alphabet[i]] = cipher.count(alphabet[i])

# Sorts the key from descending
sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)

print("Number of letters: ")
for x in range(len(sorted_letters)):
    print(sorted_letters[x])

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

correct_letters = {
    'a': 'l',
    'b': 'h',
    'c': 'a',
    'd': 'm',
    'e': 'b',
    'f': 'r',
    'g': 'v',
    'h': 'g',
    'i': 'w',
    'j': 'c',
    'k': 'i',
    'l': 'n',
    'm': 's',
    'n': 'q',
    'o': 'x',
    'p': 'd',
    'q': '',
    'r': 'o',
    's': 't',
    't': 'y',
    'u': 'e',
    'v': 'k',
    'w': 'p',
    'x': 'u',
    'y': '',
    'z': 'f'
}

# Rewrite the correct sentence
plaintext = ''
i = 0
for c in cipher:
    if c in correct_letters:
        c = correct_letters.get(c)

    plaintext = plaintext + c
print(plaintext)
