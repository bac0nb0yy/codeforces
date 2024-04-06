a, b, c, d = map(int, input().split())
pa = a / b
pb = c / d

print(pa / (1 - ((1 - pa) * (1 - pb))))

# x = pa + x*(1-pa)*(1-pb)
# x - x*(1-pa)*(1-pb) = pa
# x * (1-((1-pa)*(1-pb))) = pa
# x = pa / (1-((1-pa)*(1-pb)))
