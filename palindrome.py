a = "naman"
rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev +a[i]

if rev == a:
    print("Palindrome number")
else:
    print("Not a palindrome")