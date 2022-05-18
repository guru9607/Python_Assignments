def word_count(str) :
    counts=dict()
    word_gr=str.split()
    
    for word in word_gr:
        if word in counts:
            counts[word]+=1

        else:
            counts[word]=1
    return counts
print(word_count("The CSE is the best departmesnt in NCER"))
