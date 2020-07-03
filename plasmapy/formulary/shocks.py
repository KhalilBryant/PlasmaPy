""" This module gathers functions relating to shocks and the properties thereof.
"""
__all__ = ["entropy_across_shock_polytropic"]


from astropy import units as u
from plasmapy.utils.decorators import (
    angular_freq_to_hz,
    check_relativistic,
    validate_quantities,
)
from astropy.constants import c, a0, k_B
from numpy import pi, exp, sqrt, log


validate_quantities(
    rho_1={"can_be_negative": False}, rho_2={"can_be_negative": False})
def entropy_across_shock_polytropic(c_v: u.J / u.K, p_1: u.Bar, p_2: u.Bar, rho_1: u.kg / u.m ** 3, rho_2: u.kg / u.m ** 3, gamma) -> u.J / u.K:
    r"""
    Entropy is not conserved across a shock, since a shock is
    an irreversible, non-adiabatic process. This equation is based on the specific entropy
    of a polytropic gas before and after the shock has passed.

     .. math::

        s_2 - s_1 =
        c_v ln\left[ \frac{p_2}{p_1} \left( \frac{\rho_1}{\rho_2} \right)^{\gamma} \right]
    Here variables indexed by 1 and 2 are upstream (pre shock)
    and downstream (post shock) respectively.

    Parameters
    ----------
    c_v : `~astropy.units.Quantity`
        Heat capacity a constant volume for the gas.

    p_1 : `~astropy.units.Quantity`
        Upstream pressure of the gas.

    p_2 : `~astropy.units.Quantity`
        Downstream pressure of the gas.

    rho_1 : `~astropy.units.Quantity`
        Upstream mass density of the gas.

    rho_2 : `~astropy.units.Quantity`
        Downstream mass density of the gas.

    gamma : `float`
        Polytropic index of the gas.

    Returns
    -------
    ds: `~astropy.units.Quantity`
        The change of entropy due to the shock on the gas.

    """
    pressure_ratio = p_2 / p_1
    density_ratio = (rho_1 / rho_2)

    ds = c_v * log(pressure_ratio * density_ratio ** gamma)
    return ds