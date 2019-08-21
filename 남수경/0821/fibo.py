# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# def fibo(n):
#     if n ==1 :
#         return 1
#     if n ==0:
#         return 0
#     else:
#         return fibo(n-1)+fibo(n-2)

def fibo1(n):
    global memo
    if n >=2 and len(memo) <=n : #계산되었는지 안 되었는지 list의 크기로 하겠습니다.
        memo.append(fibo1(n-1)+fibo1(n-2))
    return memo[n]
memo = [0 , 1]


# print(factorial(4))
print(fibo1(7))