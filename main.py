string = "uosulmkgu fumucfjb bcm euul jrlpxjsup kl rfpuf sr kdwfrgu sbu mujxfkst clp uzzkjkuljt rz uaujsfrlkj " \
         "cxjskrlm. briuguf, lrs dxjb cssulskrl bcm euul wckp sr sbu pumkhl kmmxum. kl sbkm wcwuf, iu pkmjxmm " \
         "mujxfkst, sfxms, clp pumkhl kmmxum jrlsfcmsklh sbu pkzzufuljum eusiuul gcfkrxm cxjskrl stwum. iu ikaa mbri " \
         "sbcs wrrf pumkhl zrf cl uaujsfrlkj cxjskrl efucjbum sbu mujxfkst rz sbu mtmsud clp puhfcpum ksm " \
         "wfcjskjcakst --lr dcssuf bri mujxfu uzzkjkuls cfu sbu exkapklh earjvm rz cl uaujsfrlkj cxjskrl. " \
         "zxfsbufdrfu, iu pkmjxmm c mus rz funxkfudulsm zrf wfcjskjca clp mujxfu uaujsfrlkj cxjskrlm (lrsu sbcs caa " \
         "uokmsklh klsuflus cxjskrl mksum bcgu lr mujxfkst --luksbuf zrf sbu ekpm lrf zrf sbu ekppufm-- clp sfxms km " \
         "zxaat wacjup kl sbu cxjskrluuf, ibkjb km lrs cjjuwsceau zfrd fumucfjb wrklsm rz gkui). "

# a_number = string.count('a')
# b_number = string.count('b')
# c_number = string.count('c')
# d_number = string.count('d')
# e_number = string.count('e')
# f_number = string.count('f')
# g_number = string.count('g')
# h_number = string.count('h')
# i_number = string.count('i')
# j_number = string.count('j')
# k_number = string.count('k')
# l_number = string.count('l')
# m_number = string.count('m')
# n_number = string.count('n')
# o_number = string.count('o')
# p_number = string.count('p')
# q_number = string.count('q')
# r_number = string.count('r')
# s_number = string.count('s')
# t_number = string.count('t')
# u_number = string.count('u')
# v_number = string.count('v')
# w_number = string.count('w')
# x_number = string.count('x')
# y_number = string.count('y')
# z_number = string.count('z')

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
