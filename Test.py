import random

wordlist, features = [], []
while True:
    message = input(": ")
    words = message.split(" ")  # Take up the message and divide it into individual words

    def find_index(word_list, word):  # Find the index of a word in a wordlist
        for i in range(0, len(word_list)):  # Loop through every index in the wordlist
            if word_list[i] == word:  # If the item is the same as the word,
                return i  # return the index

    def word_to_list(list_, feature_list, word_list):  # Return a list without duplicates and an int version.
        output = []
        for i in range(0, len(word_list)):  # For every entry in the list of words
            if word_list[i] not in list_ and word_list[i] != '':  # If the entry being looped isn't in the word list,
                list_.append(word_list[i])  # Append that to the non-duplicate list
                feature_list.append([])  # Append it to the feature list.
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
