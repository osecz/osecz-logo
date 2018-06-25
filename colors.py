#!/usr/bin/env python3

"""Analyze luminance and contrast ratios of colors."""

# Reference: https://www.w3.org/TR/WCAG20-TECHS/G17.html#G17-tests


from math import sqrt


def srgb_to_linear(c):
    """Convert SRGB value of a color channel to linear value."""
    assert 0 <= c <= 1
    if c <= 0.03928:
        return c /12.92
    else:
        return ((c + 0.055) / 1.055)**2.4


def luminance(color_code):
    """Compute luminance of specified color."""
    # Scale the hex value of each channel to a value between 0 and 1.
    r = int(color_code[1:3], 16) / 255
    g = int(color_code[3:5], 16) / 255
    b = int(color_code[5:7], 16) / 255

    # Convert SRGB values to linear values.
    r = srgb_to_linear(r)
    g = srgb_to_linear(g)
    b = srgb_to_linear(b)

    # Luminance.
    return (0.2126 * r + 0.7152 * g + 0.0722 * b)


def contrast(L1, L2):
    """Compute contrast between two colors and/or luminance values."""
    if isinstance(L1, str):
        L1 = luminance(L1)

    if isinstance(L2, str):
        L2 = luminance(L2)

    if L1 < L2:
        L1, L2 = L2, L1

    a = 0.05
    return (L1 + a) / (L2 + a)


def analyze_colors(fg_colors, bg_colors):
    """Print luminance and contrast details of specified colors."""
    # Print header.
    print('{:7}  {:>6}'.format('', 'Lum'), end='')
    for bg in bg_colors:
        print('  {:7}'.format(bg), end='')
    print()

    # Print computation.
    for fg in fg_colors:
        print('{:7}  {:6.4f}'.format(fg, luminance(fg)), end='')
        for bg in bg_colors:
            print('  {:7.2f}'.format(contrast(fg, bg)), end='')
        print()


def html_preview(fg_colors, bg_colors):
    """Generate an HTML to preview the specified colors."""
    html = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '<meta charset="UTF-8">',
        '<title>HTML Preview of Colors</title>',
        '<style>',
        'body { background: #c0c0c0; font-family: monospace; line-height: 1.5em }',
        'body > div { margin: 1em; padding: 1em; max-width: 15em }',
        'div > div { margin: 1em; text-align: center }',
        '</style>',
        '</head>',
        '<body>'
    ]

    for bg in bg_colors:
        html.append('')
        html.append('<div style="background: {}">'.format(bg))
        for fg in fg_colors:
            html.append('  <div style="background: {}">{}</div>'.format(fg, fg))
        html.append('</div>')

    html.append('')
    html.append('</body>')
    html.append('</html>')

    preview_filename = 'color-preview.html'
    with open(preview_filename, 'w') as f:
        f.write('\n'.join(html))
    print()
    print('Preview written to:', preview_filename)


def neutral_luminance(c1, c2):
    """Compute luminance with equal contrast with c1 and c2 (color codes)."""
    a = 0.05
    Lc1 = luminance(c1)
    Lc2 = luminance(c2)
    Ld, Lb = (Lc1, Lc2) if Lc1 <= Lc2 else (Lc2, Lc1)
    Lc = sqrt(a*a + Lb*a + Ld*a + Lb*Ld) - a
    return Lc


def desired_luminance(desired_contrast_ratio, color):
    """Luminance required to obtain desired contrast with color."""
    a = 0.05
    Lo = luminance(color)
    Lc = desired_contrast_ratio * (Lo + a) - a
    return Lc


def main():
    """Print ideal luminance and analyze details of chosen colors."""
    # Luminance of background colors we will work with.
    L_black = luminance('#000000')
    L_gray3 = luminance('#303030')
    L_white = luminance('#ffffff')
    print('Luminance: black: {:6.4f}'.format(L_black))
    print('Luminance: gray3: {:6.4f}'.format(L_gray3))
    print('Luminance: white: {:6.4f}'.format(L_white))
    print()

    # Contrast between background colors.
    print('Contrast: white/black: {:7.4f}'
          .format(contrast('#ffffff', '#000000')))
    print('Contrast: white/gray8: {:7.4f}'
          .format(contrast('#ffffff', '#808080')))
    print('Contrast: white/gray3: {:7.4f}'
          .format(contrast('#ffffff', '#303030')))
    print()

    # Luminance for neutral colors that have equal contrast with two
    # background colors.
    L_black_white_neutral = neutral_luminance('#000000', '#ffffff')
    L_gray3_white_neutral = neutral_luminance('#303030', '#ffffff')
    print('Neutral luminance: black/white: {:6.4f}'
          .format(L_black_white_neutral))
    print('Contrast with black: {:7.4f}'
          .format(contrast(L_black_white_neutral, L_black)))
    print('Contrast with white: {:7.4f}'
          .format(contrast(L_black_white_neutral, L_white)))
    print()
    print('Neutral luminance: gray3/white: {:6.4f}'
          .format(L_gray3_white_neutral))
    print('Contrast with gray3: {:7.4f}'
          .format(contrast(L_gray3_white_neutral, L_gray3)))
    print('Contrast with white: {:7.4f}'
          .format(contrast(L_gray3_white_neutral, L_white)))
    print()

    # Luminance of a bright color that has good contrast with gray3
    # background.
    L_desired = desired_luminance(4.5826, '#303030')
    print('Desired luminance: gray3: {:6.4f}'.format(L_desired))
    print('Contrast with gray3: {:7.4f}'.format(contrast(L_desired, L_gray3)))
    print()

    # Analyze the contrast of chosen foreground colors against chosen
    # background colors.
    fg_colors=['#ec0304', '#028902', '#166bff',
               '#ff6657', '#02b102', '#129dff']
    bg_colors=['#000000', '#303030', '#ffffff']
    analyze_colors(fg_colors, bg_colors)
    html_preview(fg_colors, bg_colors)


if __name__ == '__main__':
    main()
