# 2D axisymmetric Fishbone Moncrief Torus (SANE)

This test is described in [Porth et al. (2019)](https://comp-astrophys-cosmol.springeropen.com/articles/10.1186/s40668-017-0020-2), Section 4.  Its an axisymmetric setup of SANE accretion onto a a=0.9375 spinning Kerr black hole.

The parameters are:
```
    eqpar(gamma_)     = 5.0d0/3.0d0     ! Adiabatic index
    
    eqpar(a_)         = 0.9375d0        ! Spin parameter   
    eqpar(kappa_)     = 1.0d-3          ! Initial entropy (will be re-normalised)

    eqpar(rin_)       = 6.0d0           ! Inner torus radius
    eqpar(rtmax_)     = 12.0d0          ! Position of density maximum

    eqpar(beta_)      = 1.0d+2          ! Measure for Plasma-beta
    eqpar(rhomin_)    = 1.0d-5          ! Minimum density scale

    eqpar(Nloops_)    = 1.0d0           ! Number of magnetic loops
    eqpar(fliploops_) = 0.0d0           ! If nonzero, will create opposing-polarity loops
    eqpar(lambdar_)   = 0.0d0           ! If nonzero, radial loops wavelength

    eqpar(pmin_)     = third*1.0d-7     ! Minimum pressure parameter
```

Note that this setup employs staggered grid though as opposed to the FCT and GLM variant shown in the paper.

A parameter-file for Toth FCT is found in *amrvacFCT.par*.  To use it, also disable staggered mesh in definitions.h:
```
#undefine STAGGERED
```