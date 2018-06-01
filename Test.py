import random

wordlist, features = [], []
while True:
    message = input(": ")
    words = message.split(" ")

    def find_index(word_list, word):
        for i in range(0, len(word_list)):
            if word_list[i] == word:
                return i

    def word_to_list(list_, feature_list, word_list):
        output = []
        for i in range(0, len(word_list)): # For every entry in
            if word_list[i] not in list_ and word_list[i] != '':
                list_.append(word_list[i])
                feature_list.append([])
                feature_list[len(feature_list)-1].append(find_index(list_, word_list[i]))
                feature_list[len(feature_list)-1].append(i)
        output.append(list_)
        output.append(feature_list)
        return output

    wordlist = word_to_list(wordlist, features, words)
    features = wordlist[1]
    wordlist = wordlist[0]
    print(wordlist)
    print(features)
    while True:
        newMsgLen = input(": ")
        if newMsgLen.isdigit():
            newMsgLen = int(newMsgLen)
            break
    randChoice = []
    finalMsg = ""
    print("Maxlength: " + str(len(features)))
    for i in range(0, newMsgLen):
        randChoice = []
        for x in features:
            if x[1] == i:
                randChoice.append(wordlist[x[0]])
        finalMsg += random.choice(randChoice) + " "
    print(finalMsg)
