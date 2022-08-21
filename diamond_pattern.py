'''
Write a code to print the diamond shape:
input =4 
output =
   * 
  * * 
 * * * 
* * * * 
* * * * 
 * * * 
  * * 
   * 

'''

n=int(input("enter the num of rows"))
c=n-1
for i in range(1,n+1):
    print(" "*c,end="")
    c-=1
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(0,n):
    print(" "*i,end="")
    for j in range(i,n):
        print("*",end=" ")
    print()
