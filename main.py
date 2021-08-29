from collections import Counter

string = "uosulmkgu fumucfjb bcm euul jrlpxjsup kl rfpuf sr kdwfrgu sbu mujxfkst clp uzzkjkuljt rz uaujsfrlkj " \
         "cxjskrlm. briuguf, lrs dxjb cssulskrl bcm euul wckp sr sbu pumkhl kmmxum. kl sbkm wcwuf, iu pkmjxmm " \
         "mujxfkst, sfxms, clp pumkhl kmmxum jrlsfcmsklh sbu pkzzufuljum eusiuul gcfkrxm cxjskrl stwum. iu ikaa mbri " \
         "sbcs wrrf pumkhl zrf cl uaujsfrlkj cxjskrl efucjbum sbu mujxfkst rz sbu mtmsud clp puhfcpum ksm " \
         "wfcjskjcakst --lr dcssuf bri mujxfu uzzkjkuls cfu sbu exkapklh earjvm rz cl uaujsfrlkj cxjskrl. " \
         "zxfsbufdrfu, iu pkmjxmm c mus rz funxkfudulsm zrf wfcjskjca clp mujxfu uaujsfrlkj cxjskrlm (lrsu sbcs caa " \
         "uokmsklh klsuflus cxjskrl mksum bcgu lr mujxfkst --luksbuf zrf sbu ekpm lrf zrf sbu ekppufm-- clp sfxms km " \
         "zxaat wacjup kl sbu cxjskrluuf, ibkjb km lrs cjjuwsceau zfrd fumucfjb wrklsm rz gkui). "

print(string)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
letters = {}
for i in range(len(alphabet)):
    # print(alphabet[i])
    # print("{} letter count: {} ".format(alphabet[i], string.count(alphabet[i])))
    letters[alphabet[i]] = string.count(alphabet[i])

# print(letters)
sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
# print(sorted_letters)
for x in range(len(sorted_letters)):
    print(sorted_letters[x])

replaced_string = string.replace('u', 'e')
replaced_string = replaced_string.replace('s', 't')
replaced_string = replaced_string.replace('l', 's')
print(replaced_string)

word_string = string.split(' ')
a = dict(Counter(word_string))
# print(word_string)
# print(a)
sorted_words = sorted(a.items(), key=lambda item: item[1], reverse=True)
print(sorted_words)
