sentance=input("Enter a string:")
words=sentance.split()
freq={}

for word in words:
     freq[word]=freq.get(word,0)+1

print("Frequency:",freq)