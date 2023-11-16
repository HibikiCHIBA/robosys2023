#!/usr/bin/python3
# SPDX-FileCopyrightaText: 2023 Hibiki Chiba
# SPDX-License-Identifier: BSD-3-Clause

import sys

ans = 0
for line in sys.stdin :
	try :
		ans += int(line)
	except :
		ans += float(line)

print(ans)
