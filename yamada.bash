#!/bin/bash
# SPDX-FileCopyrightText: 2023 Hibiki Chiba
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo NG at Line
	res=1
}

ret=0

### I/O TEST ###
out=$(seq 5 | python3 plus.py)
[ "${out}" = 14 ] || ng ${LINENO}

[ "$res" = 0 ] && echo OK
exit $res
