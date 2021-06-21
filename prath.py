def countWords():
    rat=input("enter the file name")
    no=0
    dog=open(rat)
    for cat in dog:
        words=cat.split()
        no =no+len(words)
    print("number of words")    
    print(no)    


countWords()    
   