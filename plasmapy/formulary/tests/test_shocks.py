import astropy.units as u
import numpy as np
import pytest
from astropy.constants import c

from plasmapy.formulary import entropy_across_shock_polytropic


def test_entropy_across_shock_polytropic():
    c_v = 15 * u.J / u.K
    gamma = 5 / 3  # ideal gas approx
    p_1 = 101325 * u.Pa
    p_2 = 2 * p_1
    rho_1 = 2 * u.kg / u.m ** 3
    rho_2 = 3 * u.kg / u.m ** 3
    entropy_across_shock_polytropic(c_v, p_1, p_2, rho_1, rho_2, gamma)

    assert (
        entropy_across_shock_polytropic(c_v, p_1, p_2, rho_1, rho_2, gamma)
    ).unit == u.J / u.K

    with pytest.raises(ValueError):
        entropy_across_shock_polytropic(c_v, p_1, 0.25 * p_1, rho_1, rho_2, gamma)
