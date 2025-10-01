def rse(s):
    words = s.split()  
    words.reverse() 
    print(' '.join(words))

sen = input()
rse(sen)