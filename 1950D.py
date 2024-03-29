def gen(length):
    def gen_helper(prefix, length):
        if length == 0:
            if prefix[0] != "0":
                binary_strings.append(prefix)
        else:
            gen_helper(prefix + "0", length - 1)
            gen_helper(prefix + "1", length - 1)

    binary_strings = []
    gen_helper("", length)
    return binary_strings


for _ in range(int(input())):
    n = int(input())
    if n == 1 or all(i in "01" for i in str(n)):
        print("YES")
        continue
    all_factors = [100_000] + gen(5) + gen(4) + gen(3) + gen(2)
    all_factors = [int(i) for i in all_factors]
    while n > 1:
        good = False
        for factor in all_factors:
            if not n % factor:
                good = True
            while not n % factor:
                n //= factor
        if not good:
            print("NO")
            break
    else:
        print("YES")
