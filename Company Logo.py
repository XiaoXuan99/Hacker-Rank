def sortString(str) :
    str = ''.join(sorted(str))
    return str

def checkLength(str):
    if len(str) < 3 or len(str)>10000:
        return False
    else:
        return True

def checkDistinctChar(str):
    arr = []
    arr.append(str[0])
    count = 0
    
    for i in range(len(str)):
        if str[i] != arr[count]:
            arr.append(str[i])
            count = count + 1
        
        if count == 2:
            return True
    
    return False

while True:
    S = input("Enter a string: ")    
    S=sortString(S)
    
    if checkLength(S) == False:
        print("The length of string should between 3 and 10000.")
    
    
    elif checkDistinctChar(S) == False:
        print("There must at least 3 distinct characters.")
    
    else:
        break

letter = []
count = [] 
    
letter.append(S[0])
i=0
count.append(0)

for l in range(len(S)):
    if S[l] == letter[i]:
        count[i] = count[i] + 1
    
    else:
        i = i + 1
        letter.append(S[l])
        count.append(1) 

occurence = max(count)
i = 0
common = 3

while occurence>0:
    for i in range(len(count)):
        if count[i] == occurence and common>0:
            print(letter[i], ": ", count[i]) 
            common = common - 1
         
    occurence = occurence -1
