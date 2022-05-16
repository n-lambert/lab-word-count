"""Count words in file."""
def word_count(data_file):

    input_file = open(data_file)
    #opens file

    word_frequency = {}

    for line in input_file:
        line = line.rstrip() 
        words = line.split(" ")
        for word in words:
            word_frequency[word] = word_frequency.get(word,0) + 1

    for word, frequency in word_frequency.items():
        print(f'{word} {frequency}')
    # print(word_frequency.items())


word_count("twain.txt")