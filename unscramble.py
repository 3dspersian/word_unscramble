import itertools

#input scrambled words here
scrambled = [
    "ssonic",
    "oelivr",
    "rdanas",
    "labrte",
    "raptie",
    "natkrhy",
    "baulsot",
    "ordgna",
    "ahsetlt",
    "ayhazrc",
]

def read_wordlist():
    #make sure wordlist.txt is in the same directory as where you're executing this script.
    with open('wordlist.txt', 'r') as file:
        return [line.strip().lower() for line in file]

def unscramble_word(scrambled_word, wordlist):
    permutations = set(itertools.permutations(scrambled_word))
    
    for permutation in permutations:
        unscrambled = ''.join(permutation)
        if unscrambled in wordlist:
            return unscrambled
    
    return None

def main():
    wordlist = read_wordlist()
    new_word_list = []
    
    for word in scrambled:
        unscrambled_word = unscramble_word(word, wordlist)
        if unscrambled_word:
            new_word_list.append(unscrambled_word)
        else:
            print(f"No valid word found for the scrambled word: {word}")

    new_word_str = ", ".join(new_word_list)
    return new_word_str

if __name__ == "__main__":
    new_word_list = main()
    print(new_word_list)
