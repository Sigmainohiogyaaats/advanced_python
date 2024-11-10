
user_input = input("Enter a sentence or word: ").lower()

#define vowels
vowels = {"a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0}


#vowel_count = 0

#loop through every character in the input
for char in user_input:
    if char in vowels:
        vowels[char] += 1


print("Number of vowels:", vowels)
