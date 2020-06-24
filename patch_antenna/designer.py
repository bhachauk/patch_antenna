import math
from math import cos, sin, sqrt, pi
from scipy import integrate


# names
frequency_n = 'frequency'
patch_width_n = 'patch_width'
patch_length_n = 'patch_length'
feeder_width_n = 'feeder_width'
feeder_length_n = 'feeder_length'
inset_gap_width_n = 'inset_gap_width'
inset_length_n = 'inset_length'
ground_length_n = 'ground_length'
ground_width_n = 'ground_width'
edge_impedance_n = 'input_edge_impedance'

# constants
light_velocity = 299792458
impedance = 50


def design(resonant_frequency, dielectric_constant, thickness):
    """calculates length and width of patch antenna from dielectric constant, thickness and resonant frequency"""
    return DesignPatch(resonant_frequency, dielectric_constant, thickness).get_result()


class DesignPatch:
    """All parameter calculations"""
    freq = None
    er = None
    h = None
    patch_length = None
    pl_eff = None
    patch_width = None
    feeder_length = None
    feeder_width = None
    inset_gap = None
    e_eff = None
    delta_l = None
    wavelength = None
    electrical_length = None
    ground_length = None
    ground_width = None
    inset_length = None
    input_imp = None

    def __init__(self, freq, er, h):
        """
        Designs the patch parameters
        Parameters:
            freq (float): Resonant frequency in Hz.
            er (float): Dielectric constant of the cavity material.
            h (float): Thickness of the cavity in m.
        """
        self.freq = freq
        self.er = er
        self.h = h
        self.set_wavelength()
        self.set_length_width_e_eff()
        self.set_feeder_width_length()

    def set_wavelength(self):
        self.wavelength = light_velocity / self.freq

    def set_length_width_e_eff(self):
        self.patch_width = (light_velocity / (2 * self.freq)) * sqrt(2 / (self.er + 1))
        temp = 1 + 12*(self.h / self.patch_width)
        self.e_eff = ((self.er + 1) / 2) + ((self.er - 1) / 2) * temp ** -0.5
        f1 = (self.e_eff + 0.3) * (self.patch_width / self.h + 0.264)
        f2 = (self.e_eff - 0.258) * (self.patch_width / self.h + 0.8)
        self.delta_l = self.h * 0.412 * (f1 / f2)
        self.pl_eff = (self.wavelength / sqrt(self.e_eff)) / 2
        self.patch_length = self.pl_eff - 2 * self.delta_l

    def set_feeder_width_length(self):
        self.feeder_length = (light_velocity / (4 * self.freq)) * (sqrt(1 / self.e_eff))
        self.feeder_width = (2 * self.patch_width) / 5
        self.inset_gap = self.patch_width / 5
        self.set_input_impedance()
        self.inset_length = (self.patch_length / pi) * (math.acos(sqrt(impedance / self.input_imp)))
        self.ground_length = self.patch_length + self.feeder_length + (6 * self.h)
        self.ground_width = self.patch_width + self.feeder_width + (6 * self.h)

    def get_result(self):
        result = dict()
        result[frequency_n] = self.freq
        result[patch_width_n] = self.patch_width
        result[patch_length_n] = self.patch_length
        result[feeder_width_n] = self.feeder_width
        result[feeder_length_n] = self.feeder_length
        result[inset_gap_width_n] = self.inset_gap
        result[inset_length_n] = self.inset_length
        result[ground_length_n] = self.ground_length
        result[ground_width_n] = self.ground_width
        result[edge_impedance_n] = self.input_imp
        return result

    def get_k(self):
        k0 = (2*pi)/self.wavelength
        return k0

    def S_i(self, a):
        temp = integrate.quad(lambda x: sin(x)/x, 0, a)
        return temp[0]

    def getG1 (self):
        k0 = self.get_k()
        X = k0 * self.patch_width
        I1 = -2 + cos(X) + X * self.S_i(X) + sin(X)/X
        G1 = I1 / (120 * pi**2)
        return G1

    def J0(self, s):
        temp = integrate.quad(lambda x: cos(s*sin(x)), 0, pi)
        return (1/pi) * temp[0]

    def getG12 (self):
        k0 = self.get_k()
        temp = integrate.quad(lambda x: (((sin(k0 * self.patch_width * cos(x) / 2) / cos(x)) ** 2) * self.J0(k0 * self.patch_length * sin(x)) * sin(x) ** 3), 0, pi)
        G12 = (1/(120*pi**2))*temp[0]
        return G12

    def set_input_impedance(self):
        G1, G12 = self.getG1(), self.getG12()
        self.input_imp = 1/(2*(G1+G12))
