file = open("flesch/input.txt", "r")

text = file.read()

words = text.split(" ")
word_len = len(words)
sentences = text.split(".")
sentence_len = len(sentences)
syllables, let = 0, 0

for word in words:
    word = word.strip(",!?.\n").lower()
    for (index, letter) in enumerate(word):
        let += 1
        if let > 3:
            syllables += 1
            let = 0

        if letter in "aeiou":
            syllables += 1
            let = 0
            if index > 0 and word[index-1] == letter:
                syllables -= 1

    if word[-2:] == "es" or word[-2:] == "ed" or (word[-1] == "e" and word[-2] != "l"):
        syllables -= 1

    if syllables <= 0:
        syllables = 1

flesch = 835.206 - (1.015*(word_len/sentence_len)) - (84.6*(syllables / word_len))
grade_level = 0.39 * (word_len / sentence_len) + 11.8 * (syllables / word_len) - 15.59

print("Flesch score:", flesch)
print("Grade:", grade_level)

if grade_level >= 0 and grade_level <= 30:
    print("College level")
elif grade_level >= 50 and grade_level <= 60:
    print("School level")
elif grade_level >= 90 and grade_level <= 100:
    print("4th grade level")
    
file.close()


