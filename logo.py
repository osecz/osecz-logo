#!/usr/bin/env python3

import sys

# Default radius, width and margin
r, w, m = 90, 10, 0

# Read command line arguments
if len(sys.argv) == 1:
    pass
elif len(sys.argv) == 2:
    r, = sys.argv[1:]
elif len(sys.argv) == 3:
    r, w = sys.argv[1:]
elif len(sys.argv) == 4:
    r, w, m = sys.argv[1:]
else:
    print('Usage: {} [RADIUS [WIDTH [MARGIN]]\n\n'
          'See https://github.com/osecz/osecz.org for more details\n',
          file=sys.stderr)
    sys.exit(1)

r, w, m = int(r), int(w), int(m)

# Validate radius and width
if r % 3 != 0:
    print('Error: RADIUS must be a multiple of 3', file=sys.stderr)
    sys.exit(1)

if w % 2 != 0:
    print('Error: WIDTH must be a multiple of 2', file=sys.stderr)
    sys.exit(1)

r_max = int(r + w/2 + m)
size = int(2 * r_max)
r_b = int(r / 3)
r_g = int(2 * r_b)
r_r = int(r)

print('size: {size}x{size}'.format(size=size), file=sys.stderr)
print('r:', int(r_r - w/2), r_r, int(r_r + w/2), file=sys.stderr)
print('g:', int(r_g - w/2), r_g, int(r_g + w/2), file=sys.stderr)
print('b:', int(r_b - w/2), r_b, int(r_b + w/2), file=sys.stderr)

logo = """<?xml version="1.0" encoding="UTF-8" ?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-{r_max} -{r_max} {size} {size}" width="{size}" height="{size}">
<circle r="{r_r}" stroke="#ec0304" stroke-width="{w}" fill-opacity="0.0"/>
<circle r="{r_g}" stroke="#028902" stroke-width="{w}" fill-opacity="0.0"/>
<circle r="{r_b}" stroke="#166bff" stroke-width="{w}" fill-opacity="0.0"/>
</svg>
"""
logo = logo.format(r_max=r_max, size=size, r_r=r_r, r_g=r_g, r_b=r_b, w=w)
print(logo)
