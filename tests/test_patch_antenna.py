import patch_antenna as pa
import pytest


def test_frequency_limit():

    with pytest.raises(ValueError) as execinfo:
        pa.design(0, 0, 0)

    return execinfo.value.args[0] == 'Frequency value should be in between 1MHz to 100 GHz'


def test_dielectric_limit():

    with pytest.raises(ValueError) as execinfo:
        pa.design(10 ** 9, 0, 0)

    return execinfo.value.args[0] == 'Dielectric constant value should be in greater than 0 and smaller or equals 100,000'


def test_thickness_limit():

    with pytest.raises(ValueError) as execinfo:
        pa.design(10 ** 9, 1, 0)

    return execinfo.value.args[0] == 'Thickness value should be in greater than 0 and smaller or equals 1 meter'
