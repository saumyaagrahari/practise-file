# k=1
# i=1
# while i<=7:
#     b=1
#     while b<=7-i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=k:
#         print("*  ",end=" ")
#         j=j+1
#     k=k+1
#     print()
#     i=i+1
#  k=6
# i=1
# while i<=6:
#     b=1
#     while b<=i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=k:
#         print("*  ",end=" ")
#         j=j+1
#     k=k-1
#     print()
#     i=i+1
        


# for i in range(7):
#     for j in range(5):
#         if i==3 or i not in {}:
#             print("*",end=" ")
#         elif j==0 or j==4:
#             print("*",end=" ")
#         #elif j in {1,6}:
#          #   print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input("enter a number:"))
# temp=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
#     if temp==rev:
#         print("polindrome")
#     else:
#         print("not polindrome")


# n=int(input("enter a number:"))
# rev=0
# while n!=0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
#     print("reverse num is",rev)


# n=int(input("enter a number:"))
# i=1
# sum=0
# while i<n:
#     if n%i==0:
#         sum=sum+i
#     i=i+1
# if sum==n:
#     print("perfect")
# else:
#     print("not")


# n=int(input("enter a number:"))
# temp=n
# sum=0
# a=str(n)
# i=len(a)
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**i
#     temp=temp//10
#     if n==sum:
#         print("amstrong")
#     else:
#         print("not")


# n=int(input("enter a number:"))
# z=n
# sum=0
# i=1
# while i<=n:
#     num=n%10
#     sum=sum+num
#     n=n//10
# print(sum)
# if z%sum==0:
#     print("harshad")
# else:
#     print("not")


# n=int(input("enter a number:"))
# s=0
# r=0
# while n>0:
#     r=n%10
#     s=s+r**2
#     n=n//10
# n=int(input("enter a number:"))
# res=n
# while res!=1 and res!=4:
#     if res==1:
#          print("happy")
#     elif res==4:
#          print("not")


# n=int(input("enter a number:"))
# i=2
# f=0
# while n>i:
#     if n%i==0:
#         f+=1
#     i+=1
# if f==0:
#     print("prime")
# else:
#     print("not")



