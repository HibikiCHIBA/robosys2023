#!/bin/bash -xv
# SPDX-FileCopyrightText: 2023 Hibiki Chiba
# SPDX-License-Identifier: BSD-3-Clause

### I/O TEST ###
out=$(seq 5 | python3 plus.py)
[ "${out}" = 15 ]
