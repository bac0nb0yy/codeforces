for _ in range(int(input())):
    s = input()
    i = 0
    part = 0
    mixed_found = False
    while i < len(s):
        if s[i] == "0":
            one_found = False
            while i < len(s):
                if s[i] == "1" and mixed_found:
                    break
                if s[i] == "1":
                    one_found = True
                elif s[i] == "0" and one_found:
                    break
                i += 1
            if one_found:
                mixed_found = True
        elif s[i] == "1":
            while i < len(s):
                if s[i] == "0":
                    break
                i += 1
        part += 1
    print(part)
