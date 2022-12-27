a = [1, 2, 4, 4, 5, 6, 7, 7, 9, 9]

def reformed(a):
  return list(dict.fromkeys(a))
 
print(a)
FinalList = reformed(a)
print(FinalList)

    
    

     
