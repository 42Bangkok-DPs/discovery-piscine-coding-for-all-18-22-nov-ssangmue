#!/usr/bin/env python3


original_array = [2, 8, 9, 48, 8, 22, -12, 2]


new_array = [original_array[i] + 2 for i in range(1, len(original_array), 2)]


print(f"{original_array}$")
print(f"{new_array}$")
