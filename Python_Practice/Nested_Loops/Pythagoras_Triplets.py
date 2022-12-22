# Pythagorus Triplets
N = int(input("Enter The Number : "))
count = 0
for a in range(1, N+1):
    for b in range(1, N+1):
        for c in range(1, N+1):
            if a < b < c:
                if a*a + b*b == c*c:
                    count += 1
print(count)