# "1.Using Iteration"
str = "suhail"
rev = ""
for char in str:
    rev = char + rev
print(rev)  #  "liahus"

# "2.using string function"
reve = str[::-1]
print(rev)  # "liahus"

# 3.using stack
stack = []
for char in str :
    stack.append(char)
rev = ""
while stack:
    rev += stack.pop()
print(rev)  # Output: "liahus"
# 4.List Revers

rev = ''.join(list(str)[::-1])
print(rev)  # Output: "liahus"

# 5.List comprehension

rev = ''.join([str[i] for i in range(len(str)-1, -1, -1)])
print(rev)  # Output: "liahus"
