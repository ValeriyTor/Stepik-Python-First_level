s = input()
counter = 1
for i in range(len(s)):
    if s[i] == " ":
        counter += 1
print(counter)