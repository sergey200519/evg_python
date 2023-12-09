# slice("abc", 0, 2) --> "ab"
# print("abcd"[0:1]) # 0
# print("abcd"[0:2]) # 0 1
# print("abcd"[0:3]) # 0 1 2

def slice(row, start, end):
    answer = ""
    i = start
    while i < end:
        answer += row[i]
        i += 1
    return answer

print(slice("abc", 0, 2)) # 0 1
print(slice("abc", 1, 2))