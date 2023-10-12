#!/usr/bin/python3

import sys

ans = 0.0
for line in sys.stdin :
	ans += float(line)

print(ans)

# 実行：python3 plus_stdin.py < nums
