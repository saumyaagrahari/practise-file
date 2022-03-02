# x=15
# while(x==15):
# print("Hello")
# x=x-3
# [46]:
# x = "123"
# for i in x:
# print("a")
# [47]:
# i=9
# while True:
# if i%3==0:
# breakprint("A")
# [48]:
# a=5
# while(a<=10):
# print("a")
# a+=1
# [49]:
# i=0
# while i<3:
# print(i)
# i=i+1
# else:
# print(7)
# [50]:
# i=0
# while i<3:
# print(i)
# i=i+1
# print(0)
# [51]:
# i=2
# for x in range(i):
# i+=1
# print(i)
# print(i)
# [52]:
# i=2
# for x in range(i):
# x+=1
# print(x)
# print(x)
# [53]:
# i=2
# for x in range(i):
# x+=1
# print(x)
# print("x")[54]:
# i=100
# while i<57:
# print(i)
# i+=5
# [55]
# for i in range(5):
# for j in range(i):
# print("A",end=" ")
# print()
# [56]
# for i in range(5):
# for j in range(i):
# print("A",end="a")
# print()
# [57]
# for i in range(5):
# print("AS"*i,"\n")[/showhide]
# [58]
# for i in range(5):
# for j in (i):
# print("AS"*i,"\n")
# [59]
# print(10*2//3**2)
# [60]
# print(12+34-320+23**2)
# [61]
# a = 7
# for i in 7:
# print(a)
# [62]
# a = "AMIT"
# for i in range(len(a)):
# print(a)[63]
# x = "Welcome to my blog"
# j = "i"
# while j in x:
# print(j)
# [64]
# print(range (5, 0, -2))
# [65]
# for i in range(0,2,-1):
# print("Hello")
# [66]
# s1="csworld.com"
# s2=""
# s3=""
# for x in s1:
# if(x=="s" or x=="n" or x=="p"):
# s2+=x
# print(s2,end=" ")
# print(s3)
# [67]
# s1="csworld.com"
# c=0
# for x in s1:
# if(x!="l"):
# c=c+1
# print(c)
# [68]
# j=12
# c=9
# while( j):
# if( j>5):
# c=c+j-2
# j=j-1
# else:
# break
# print(j, c)
# print(c)[69]
# L = [13 , 12 , 21 , 16 , 35 , 7, 4]
# s = 5
# s1 = 3
# for i in L:
# if (i % 4 == 0):
# s = s + i
# continue
# if (i % 7 == 0):
# s1 = s1 + i
# print(s , end=" ")
# print(s1)
# [70]
# print('cs' + 'ip' if '234'.isdigit() else 'IT' + '-402')
# [71]
# def fib(n):
# p, q = 0, 1
# while(p < n):
# yield p
# p, q = q, p + q
# x = fib(10)