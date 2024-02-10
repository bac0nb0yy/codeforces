print(
    -sum(
        __import__("heapq").nsmallest(
            int(input().split()[1]), (int(x) for x in input().split() if x[0] == "-")
        )
    )
)
