def first_unique_char(s):
    for i in range(len(s)):
        if s.count(s[i])==1:
            print(i)
            break

s="leetcode"
first_unique_char(s)