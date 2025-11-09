s = ["h","e","l","l","o"]
# ["o","l","l","e","h"]
for i in range (0, len(s)//2):
    cur_el = s[i]
    s[i] = s[-i-1]
    s[-i-1] = cur_el
print(s)

