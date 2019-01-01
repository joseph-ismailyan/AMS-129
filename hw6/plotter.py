import numpy as np
import matplotlib.pyplot as plt


file_path = './words.txt'

# takes file path as input and returns a dicitonary
# of how many times each letter appears in the file

def word_count(path):

    # initialize empty dictionary
    letters_dictionary = dict()

    # open the file containing the words
    file_object = open(path, 'r')

    # iterates thru all words in the file
    for word in file_object:
        for character in word:
            if character not in letters_dictionary:
                # if character is not yet in the dictionary
                # then initialize its value to one.
                letters_dictionary[character] = 1
            else:
                # if character is already in the dictionary
                # increment its value by 1
                letters_dictionary[character] += 1

    # now go back and remove non-alpha characters
    for char in letters_dictionary:
        if not char.isalpha():
            del letters_dictionary[char]
            break
    # now sort the keys by alphabetical order
    # note this creates a list of only the keys
    letters_dictionary_keys = sorted(letters_dictionary)

    # need to go thru the sorted keys list and create a new dictionary
    # thats sorted
    sorted_letters_dictionary = dict()
    # goes thru sorted keys list and creates new dict thats sorted
    for letter in letters_dictionary_keys:
        sorted_letters_dictionary[letter] = letters_dictionary.get(letter)

    return sorted_letters_dictionary
    
def plot(dictionary):
    # matplotlib cant process ndarrays so we use the list() method
    plt.bar(range(len(dictionary)), list(dictionary.values()), align='center')
    plt.xticks(range(len(dictionary)), list(dictionary.keys()))
    plt.plot(range(len(dictionary)), list(dictionary.values()), color='r', marker='o', markersize='4', linewidth='1')
    plt.grid(color='white', alpha=0.4)
    plt.xlabel('Character')
    plt.ylabel('Frequency')
    plt.savefig('result.png',dpi=300, bbox_inches='tight')

    # comment out before submitting
    #plt.show()

def main():
    plot(word_count(file_path))

if __name__ == "__main__":
    main()








