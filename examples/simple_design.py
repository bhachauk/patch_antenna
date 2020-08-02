import json
import patch_antenna as pa

# resonant frequency in Hz
freq = 2.4 * 10 ** 9

# dielectric constant
er = 4.4

# thickness of the cavity in meter
h = 1.6 * 10 ** -3


result = pa.design(freq, er, h)

# pretty printing
print(json.dumps(result, indent=4))


# To write as gerber file for both types

# normal feed
pa.write_gerber(freq, er, h, '/tmp/patch_normal_design.gbr', 'normal')

# inset feed
pa.write_gerber(freq, er, h, '/tmp/patch_inset_design.gbr', 'inset')

