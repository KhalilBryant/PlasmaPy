import _pytest
import astropy.units as u
import numpy as np
import pytest
from astropy.constants import c

from plasmapy.formulary import entropy_across_shock_polytropic
from plasmapy.utils import PhysicsWarning


def test_entropy_across_shock_polytropic():
    c_v = 15 * u.J / u.K
    gamma = 5 / 3  # ideal gas approx
    p_1 = 101325 * u.Pa
    p_2 = 2 * p_1
    rho_1 = 2 * u.kg / u.m ** 3
    rho_2 = 3 * u.kg / u.m ** 3
    val = entropy_across_shock_polytropic(c_v, p_1, p_2, rho_1, rho_2, gamma)

    assert val.unit == u.J / u.K
    assert np.isclose(val.value, 0.26058001)

    with _pytest.warnings.warn(PhysicsWarning):
        entropy_across_shock_polytropic(c_v, p_1, 0.5 * p_1, rho_1, rho_2, gamma)

