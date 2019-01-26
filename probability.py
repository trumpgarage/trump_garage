wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

wordfreq2=list(zip(wordlist,wordfreq))
zipped_list = wordfreq2[:]
zipped_list_2=list(wordfreq2)

# print("String\n" + wordstring +"\n")
# print("List\n" + str(wordlist) + "\n")
# print("Frequencies\n" + str(wordfreq) + "\n")
# print("Pairs\n" + str(zipped_list_2))


totalfreq = sum(wordfreq) #total number of frequencies
size=len(wordfreq) #size of the array
totalfreq1=[totalfreq]*size #creates array with value total freq with the same size as number of frequencies
prob=[]
for i in range(size):
	prob.append(wordfreq[i]/totalfreq1[i])
prob

print("Probability\n"+str(prob)+"\n")



