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


def test_design_string():
    freq = 2.4 * 10 ** 9
    er = 4.4
    h = 1.6 * 10 ** -3
    result = pa.design_string(freq, er, h)
    assert isinstance(result, str)


def test_gerber():
    freq = 2.4 * 10 ** 9
    er = 4.4
    h = 1.6 * 10 ** -3
    pa.write_gerber(freq, er, h, 'test.gbr', "normal")
    assert True


def test_gerber2():
    freq = 2.4 * 10 ** 9
    er = 4.4
    h = 1.6 * 10 ** -3
    pa_design = pa.design(freq, er, h)
    pa.write_gerber_design(pa_design, "test1.gbr", feed_type="normal")
    assert True


def test_gerber_inset():
    freq = 2.4 * 10 ** 9
    er = 4.4
    h = 1.6 * 10 ** -3
    pa_design = pa.design(freq, er, h)
    pa.write_gerber_design(pa_design, "test1.gbr", feed_type="inset")
    assert True
