import patch_antenna as pa
import pytest

# resonant frequency in Hz
freq = 2.4 * 10 ** 9

# dielectric constant
er = 4.4

# thickness of the cavity in meter
h = 1.6 * 10 ** -3

# Quick print result
print(pa.design_string(freq, er, h))


# Using result object
result = pa.design_result(freq, er, h)
print(result.patch_width)


# Quick write gerber file

# normal feed
pa.write_gerber(freq, er, h, 'patch_normal_design.gbr', 'normal')


# inset feed
pa.write_gerber(freq, er, h, 'patch_inset_design.gbr', 'inset')


# Custom change design parameters

# Using design object

design = pa.design(freq, er, h)

# Changing feeder length and feeder width

design.feeder_length *= 1.25

design.feeder_width *= 1.10


# To write as gerber file for both types

# normal feed

pa.write_gerber_design(design, 'patch_normal_design.gbr', 'normal')

# inset feed

pa.write_gerber_design(design, 'patch_inset_design.gbr', 'inset')


# testing Exception cases

with pytest.raises(ValueError) as execinfo:
    pa.design(0, 0, 0)

assert execinfo.value.args[0] == 'Frequency value should be in between 1MHz to 100 GHz'

with pytest.raises(ValueError) as execinfo:
    pa.design(10 ** 9, 0, 0)

assert execinfo.value.args[0] == 'Dielectric constant value should be in greater than 0 and smaller or equals 100,000'


with pytest.raises(ValueError) as execinfo:
    pa.design(10 ** 9, 1, 0)

assert execinfo.value.args[0] == 'Thickness value should be in greater than 0 and smaller or equals 1 meter'
