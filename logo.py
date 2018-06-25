#!/usr/bin/env python3

import sys

# Read command line arguments
if len(sys.argv) == 7:
    r, t, m, c_r, c_g, c_b = sys.argv[1:]
else:
    print('Usage:', sys.argv[0],
         'RADIUS THICKNESS MARGIN RED GREEN BLUE', file=sys.stderr)
    sys.exit(1)

r, t, m = int(r), int(t), int(m)

# Validate radius and width
if r % 3 != 0:
    print('Error: RADIUS must be a multiple of 3', file=sys.stderr)
    sys.exit(1)

if t % 2 != 0:
    print('Error: WIDTH must be a multiple of 2', file=sys.stderr)
    sys.exit(1)

r_max = int(r + t/2 + m)
size = int(2 * r_max)
r_b = int(r / 3)
r_g = int(2 * r_b)
r_r = int(r)

print('size: {size}x{size}'.format(size=size), file=sys.stderr)
print('r:', int(r_r - t/2), r_r, int(r_r + t/2), file=sys.stderr)
print('g:', int(r_g - t/2), r_g, int(r_g + t/2), file=sys.stderr)
print('b:', int(r_b - t/2), r_b, int(r_b + t/2), file=sys.stderr)

logo = """<?xml version="1.0" encoding="UTF-8" ?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-{r_max} -{r_max} {size} {size}" width="{size}" height="{size}">
<circle r="{r_r}" stroke="{c_r}" stroke-width="{t}" fill-opacity="0.0"/>
<circle r="{r_g}" stroke="{c_g}" stroke-width="{t}" fill-opacity="0.0"/>
<circle r="{r_b}" stroke="{c_b}" stroke-width="{t}" fill-opacity="0.0"/>
</svg>
"""
logo = logo.format(r_max=r_max, size=size,
                   r_r=r_r, r_g=r_g, r_b=r_b, t=t,
                   c_r=c_r, c_g=c_g, c_b=c_b)
print(logo)
