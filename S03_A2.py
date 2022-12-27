col = int(input("Please enter the columns: "))
row = int(input("Please enter the rows: "))
array = []
array = [["*#"  for p in range(col)] for a in range(row)]
for a in range (col):
    print(array[a])