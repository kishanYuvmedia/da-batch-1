# a=1
# while a<=10:
#     if a==5:
#         break
#     print(a)
#     a+=1

for i in range(1,11):
    if i==5:
        print("5 is skipped")
        continue
    print(i)