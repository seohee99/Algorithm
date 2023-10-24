#6003
print("Hello\nWorld")

#6004
print("'Hello'")

#6005
print('"Hello World"')

#6006
print("\"!@#$%^&*()'")

#6007
print("\"C:\\Download\\'hello'.py\"")

#6008
print("print(\"Hello\\nWorld\")")

#6009
c = input("input : ")
print(c)

#6010
c = int(input("input : "))
print(c)

#6011
c = float(input("input : "))
print(c)

#6012
a = input() 
b = input()
print(a)
print(b)

#6013
a = input() 
b = input()
print(b)
print(a)

#6014
c = input()
print(c)
print(c)
print(c)

#6015
a, b = input().split()
print(a)
print(b)

#6016
a, b = input().split()
print(b,a)

#6017
s = input()
print(s, s, s) 

#6018
a, b = input().split(':')
print(a, b, sep=':')

#6019
y, m, d = input().split('.')
print(d, m, y, sep='-')

#6020
a, b = input().split('-')
print(a+b)

#6021
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#6022
s = input()
print(s[:2],s[2:4],s[4:])

#6023
h, m, s = input().split(':')
print(m)

#6024
w1, w2 = input().split()
s = w1 + w2
print(s)

#6025
a, b = input().split()
c = int(a) + int(b)
print(c)

#6026
a = input()
b = input()
c = float(a) + float(b)
print(c)

#6027
a = input()
n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%x'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력

#6028
a = input()
n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%X'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 대문자 형태 문자열로 출력

#6029
a = input()
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)  #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

#6030
n = ord(input())  #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
print(n)

#6031
c = int(input())
print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 

#6032
s = int(input())
print(-s)

#6033
n1=input()
n2=ord(n1)+1
s=chr(n2)
print(s)

#6034
a, b = input().split()
c = int(a) - int(b)
print(c)

#6035
f1, f2 = input().split()
m = float(f1) * float(f2)
print(m)

#6036
w, n = input().split()
print(w*int(n))

#6037
n = input()
s = input()
print(int(n)*s)

#6038
w, n = input().split()
print(int(w)**int(n))

#6039
w, n = input().split()
print(float(w)**float(n))

#6040
a, b = input().split()
c = int(a) // int(b)
print(c)

#6041
a, b = input().split()
c = int(a) % int(b)
print(c)

#6042
a = float(input())
print(format(a,".2f"))

#6043
a,b=input().split()
a=float(a)
b=float(b)
c=a/b
print(format(c,".3f"))

#6044
a, b = input().split()
sum_num = int(a) + int(b)
sub_num = int(a) - int(b)
mul_num = int(a) * int(b)
share_num = int(a) // int(b)
remain_num = int(a) % int(b)
div_num = int(a) / int(b)
print(sum_num)
print(sub_num)
print(mul_num)
print(share_num)
print(remain_num)
print(format(div_num,".2f"))

#6045 정수 3개 입력받아 합과 평균 출력하기
a, b, c = input().split()
sum_num = int(a) + int(b) + int(c)
avg_num = sum_num / 3
print(sum_num, format(avg_num,".2f"))

#6046 정수 1개 입력받아 2배 곱해 출력하기
s = int(input())
print(s<<1)

#6047 2의 거듭제곱 배로 곱해 출력하기
a,b = map(int,input().split())
print(a<<b)

#6048 정수 2개 입력받아 비교하기
a,b = map(int,input().split())
print(a<b)
