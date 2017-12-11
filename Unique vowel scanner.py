print "---------------------Find your Unique vowel finder---------------------"
line = raw_input("Enter any sentence : ")
vowels = ['a','A','e','E','i','I','o','O','u','U']
Bigkey= None
Bigval = 0
dic = {}

def Vow():
    for words in line:
        words.split()
        if words in vowels:
            dic[words] = dic.get(words,0)+1
    print "Total  vowels are ",sum(dic.values())
    print "There have", len(dic.keys()), "unique vowels in the sentence.Those are ",dic.keys()
    for key , val in dic.items():
        if Bigkey is None or Bigval < val:
            Bigkey = key
            Bigval = val
    print " The most used Vowel is", Bigkey, '.It seems ',Bigval , 'times.'

print Vow()
