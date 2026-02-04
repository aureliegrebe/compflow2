import compflow as cf
import matplotlib.pyplot as plt
import numpy as np
import pygasflow as pgf
from matplotlib import rcParams

import compflow2 as cf2

GAMMA = 1.4


def main():
    machs = np.linspace(0.0, 4, 50)
    machs_sub = np.linspace(0.1, 0.9, 50)

    plt.plot(machs, cf2.To_T_from_Ma(machs, GAMMA), "b", label="T0/T cf2")
    plt.plot(machs, cf.To_T_from_Ma(machs, GAMMA), "b:", label="T0/T cf")
    plt.plot(
        machs,
        cf2.Po_P_from_Ma(machs, GAMMA),
        color="orange",
        linestyle="-",
        label="P0/P cf2",
    )
    plt.plot(
        machs,
        cf.Po_P_from_Ma(machs, GAMMA),
        color="orange",
        linestyle=":",
        label="P0/P cf",
    )
    plt.plot(machs, cf2.rhoo_rho_from_Ma(machs, GAMMA), "g", label="rho0/rho cf2")
    plt.plot(machs, cf.rhoo_rho_from_Ma(machs, GAMMA), "g:", label="rho0/rho cf")
    plt.plot(machs, cf2.V_cpTo_from_Ma(machs, GAMMA), "r", label="V/cpT0 cf2")
    plt.plot(machs, cf.V_cpTo_from_Ma(machs, GAMMA), "r:", label="V/cpT0 cf")
    plt.plot(machs, cf2.mcpTo_APo_from_Ma(machs, GAMMA), "m", label="mcpTo_APo cf2")
    plt.plot(machs, cf.mcpTo_APo_from_Ma(machs, GAMMA), "m:", label="mcpTo_APo cf")
    plt.plot(
        machs,
        cf2.mcpTo_AP_from_Ma(machs, GAMMA),
        color="brown",
        linestyle="-",
        label="mcpTo_AP cf2",
    )
    plt.plot(
        machs,
        cf.mcpTo_AP_from_Ma(machs, GAMMA),
        color="brown",
        linestyle=":",
        label="mcpTo_AP cf",
    )
    plt.plot(
        machs,
        cf2.A_Acrit_from_Ma(machs, GAMMA),
        color="pink",
        linestyle="-",
        label="P0/P cf2",
    )
    plt.plot(
        machs,
        cf.A_Acrit_from_Ma(machs, GAMMA),
        color="pink",
        linestyle=":",
        label="P0/P cf",
    )
    plt.plot(
        machs,
        cf2.Mash_from_Ma(machs, GAMMA),
        color="grey",
        linestyle="-",
        label="Mash cf2",
    )
    plt.plot(
        machs,
        cf.Mash_from_Ma(machs, GAMMA),
        color="grey",
        linestyle=":",
        label="Mash cf",
    )
    plt.plot(
        machs,
        cf2.Posh_Po_from_Ma(machs, GAMMA),
        color="olive",
        linestyle="-",
        label="posh_po cf2",
    )
    plt.plot(
        machs,
        cf.Posh_Po_from_Ma(machs, GAMMA),
        color="olive",
        linestyle=":",
        label="posh_po cf",
    )

    plt.xlabel("M")
    plt.xlim([0, 4])
    plt.ylim([0, 3])

    plt.legend()
    plt.grid()

    t0_t = cf.To_T_from_Ma(machs, GAMMA)
    p0_p = cf.Po_P_from_Ma(machs, GAMMA)
    rho0_rho = cf.rhoo_rho_from_Ma(machs, GAMMA)
    v_cpt0 = cf.V_cpTo_from_Ma(machs, GAMMA)
    mcpt0_ap0_sub = cf.mcpTo_APo_from_Ma(machs_sub, GAMMA)
    mcpt0_ap = cf.mcpTo_AP_from_Ma(machs, GAMMA)

    plt.figure()
    plt.plot(t0_t, cf2.Ma_from_To_T(t0_t, GAMMA), "b", label="T0/T cf2")
    plt.plot(t0_t, cf.Ma_from_To_T(t0_t, GAMMA), "b:", label="T0/T cf")
    plt.plot(
        p0_p,
        cf2.Ma_from_Po_P(p0_p, GAMMA),
        color="orange",
        linestyle="-",
        label="P0/P cf2",
    )
    plt.plot(
        p0_p,
        cf.Ma_from_Po_P(p0_p, GAMMA),
        color="orange",
        linestyle=":",
        label="P0/P cf",
    )
    plt.plot(rho0_rho, cf2.Ma_from_rhoo_rho(rho0_rho, GAMMA), "g", label="rho0/rho cf2")
    plt.plot(rho0_rho, cf.Ma_from_rhoo_rho(rho0_rho, GAMMA), "g:", label="rho0/rho cf")
    plt.plot(v_cpt0, cf2.Ma_from_V_cpTo(v_cpt0, GAMMA), "r", label="V/cpT0 cf2")
    plt.plot(v_cpt0, cf.Ma_from_V_cpTo(v_cpt0, GAMMA), "r:", label="V/cpT0 cf")
    # plt.plot(
    #     mcpt0_ap0_sub,
    #     cf2.Ma_from_mcpTo_APo(mcpt0_ap0_sub, GAMMA),
    #     "m",
    #     label="mcpTo_APo cf2",
    # )
    plt.plot(
        mcpt0_ap0_sub,
        cf.Ma_from_mcpTo_APo(mcpt0_ap0_sub, GAMMA),
        "m:",
        label="mcpTo_APo cf",
    )
    # plt.plot(
    #     mcpt0_ap,
    #     cf2.Ma_from_mcpTo_AP(mcpt0_ap, GAMMA),
    #     color="brown",
    #     linestyle="-",
    #     label="mcpTo_AP cf2",
    # )
    plt.plot(
        mcpt0_ap,
        cf.Ma_from_mcpTo_AP(mcpt0_ap, GAMMA),
        color="brown",
        linestyle=":",
        label="mcpTo_AP cf",
    )

    plt.xlabel("Y")
    plt.xlim([0, 3])
    plt.ylim([0, 4])
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
