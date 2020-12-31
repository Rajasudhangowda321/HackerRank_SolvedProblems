#Consider a list (list = []). You can perform the following commands:
#insert i e: Insert integer e at position i .
#print: Print the list.
#remove e: Delete the first occurrence of integer e .
#append e: Insert integer e at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list
#Sample Input
#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print
N=int(input())
lst=[]
for i in range(N):
    g=input().split()
    if g[0]=='append':
        lst.append(int(g[1]))
    elif g[0]=='insert':
        lst.insert(int(g[1]),int(g[2]))
    elif g[0]=='sort':
        lst.sort()
    elif g[0]=='remove':
        lst.remove(int(g[1]))
    elif g[0]=='pop':
        lst.pop(int(g[1]))
    elif g[0]=='reverse':
        lst.reverse()
    elif g[0]=='print':
        print(lst)
