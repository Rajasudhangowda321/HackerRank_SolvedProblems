#Given an integer,n , and n space-separated integers as input, create a tuple,t , of those n integers. Then compute and print the result of hash(t).
n=int(input())
lst=[]
for i in range(1,n+1):
    lst.append(i)
tup=tuple(lst)
print(hash(tup))
