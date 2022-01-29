# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for _ in range(n):
    str = input()
    print(str[::2], end=" ")
    print(str[1::2])
