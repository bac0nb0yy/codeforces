from string import ascii_lowercase

# a = input()[1:-1].split(", ")
# print(len(set(a)) if a != [""] else 0)
print(len(set(input()) & set(ascii_lowercase)))
