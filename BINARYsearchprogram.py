A = [10,20,30,40,50,60]
key = int(input("Enter searched elements: "))
low = 0
high = 5
found = False
while(low<=high):
    mid = (low+high)//2
    if(A[mid]==key):
        print("Element found at position",mid)
        found = True
        break
    elif(key<A[mid]):
        high = mid-1
    else:
        low = mid+1
if not found:
    print("Element not found")