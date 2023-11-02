#!/usr/bin/python3
# SPDX-FileCopyrightaText: 2023 Hibiki Chiba
# SPDX-License-Identifier: BSD-3-Clause

import sys

def tonum(s) :
	try :
		return int(s)
	except :
		return float(s)

ans = 0
for line in sys.stdin :
	line = line.rstrip()
	ans += tonum(line)

print(ans)
for line in sys.stdin :
	ans += tonum(line)

# 実行：python3 plus_stdin.py < nums
