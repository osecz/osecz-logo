#!/usr/bin/env python3

"""Analyze luminance and contrast ratios of colors."""


# Reference: https://www.w3.org/TR/WCAG20-TECHS/G17.html#G17-tests


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


def analyze_color(color_code):
    """Print luminance and contrast details of colors."""
    lum = luminance(color_code)

    # Contrast on white background.
    cow = (luminance('#ffffff') + 0.05) / (lum + 0.05)

    # Contrast on black background.
    cob = (lum + 0.05) / (luminance('#000000') + 0.05)

    # Print the results.
    print('{}: rgb: lum: {:.4f}; cow: {:5.2f}; cob: {:5.2f}'
          .format(color_code, lum, cow, cob))


def analyze_colors(*color_codes):
    """Print luminance and contrast details of specified colors."""
    for color_code in color_codes:
        analyze_color(color_code)
    html_preview(*color_codes[1:-1])


def html_preview(*color_codes):
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

    for bg in ['#ffffff', '#000000']:
        html.append('')
        html.append('<div style="background: {}">'.format(bg))
        for fg in color_codes:
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


def main():
    """Print ideal luminance and analyze details of chosen colors."""
    # Extra term for numerator and denominator as specified in WCAG 2.0.
    x = 0.05

    # Solving (1 + x) / (L + x) = (L + x) / x, we get L = sqrt(x^2 + x) - x.
    print('Required luminance:', (x**2 + x)**0.5 - x) # 0.1791 approx.
    print()

    # Analyze the luminance and contrast of white, red, green, blue, and
    # black. The shades of red, green, and blue were chosen such that
    # their luminance values were close to 0.1791.
    analyze_colors('#ffffff', '#ec0304', '#028902', '#166bff', '#000000')


if __name__ == '__main__':
    main()
