def all_sum(*number):
    sum = 0
    for n in number:
        sum += n
    return sum

arr = list(map(int, input().split()))
total = all_sum(*arr)
print(total)
