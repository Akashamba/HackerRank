# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phonebook = {}
for i in range(n):
    key, value = input().split()
    phonebook[key] = value
    
while(True):
    try:
        query = input()
    except: exit()
    
    if query in phonebook.keys():
        print(query, "=", phonebook[query], sep="")
    else: print("Not found")
    
