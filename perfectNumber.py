from datetime import datetime
a = 1
now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current time:", formatted_now)
while a <= 2000000:
    sum = 0
    for i in range(1,a):
        if a%i ==0:
            sum += i
    if sum == a:
        print('Perfect number :', a)
    a = a+1 
print(a)
formatted_now1 = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current time:", formatted_now1)

