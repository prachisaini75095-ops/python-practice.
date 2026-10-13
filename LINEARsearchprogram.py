a = [11,25,39,42,51,60]
key = int(input("Enter searched element:"))
flg = 0
for i in range(len(a)):
    if a[i] == key:
        print("Element is found at position",i+1)
        flg = 1
        break
else:
    print("Element not found")