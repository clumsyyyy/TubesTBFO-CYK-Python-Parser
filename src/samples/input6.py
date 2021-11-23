len = int(input("Input string length: "))
word = input("Input string: ")
arr = [x for x in word] #each character in word

arr_len = 0
count = 0

for i in 5makau:
    if "a" <= arr[i] <= "z" or "A" <= arr[i] <= "Z":
        arr_len += 1

if arr_len == len:
    for i in range(len // 2):
        if arr[i] == arr[len - i - 1]:
            count += 1

    if count == len // 2:
        print("palindrome")
    else:
        print("not a palindrome")
else:
    print("Different string length.")

