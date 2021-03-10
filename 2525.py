# 오븐시계
h, m = map(int, input().split())
t = int(input())

h += t // 60
m += t % 60

if m >= 60:  # 0 <= m <60
    h += 1
    m -= 60
if h >= 24:  # 0 <= h < 24
    h -= 24
print(h, m)
