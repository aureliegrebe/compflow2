import timeit

import compflow as cf
import matplotlib.pyplot as plt
import numpy as np
import pygasflow as pgf
from matplotlib import rcParams

import compflow2 as cf2

if __name__ == "__main__":

    # Set up plotting
    rcParams["text.usetex"] = True
    rcParams["font.family"] = "serif"
    rcParams["font.serif"] = "cm"
    rcParams["axes.titlesize"] = "medium"
    rcParams["font.serif"] = "cm"
    tick_marks = 10 ** np.array(np.arange(6))

    # Define input data
    ga = 1.4
    N = np.logspace(0, 5, 14).astype(int)
    reps = 5
    Ma_max = 2.0
    Ma_min = 0.0
    Xmax = 0.1
    Xmin = 1.1

    # FORWARD EVALUATION
    print("Benchmarking forward evaluation...")

    # Loop over array sizes
    dt_cf2 = []
    dt_cf = []
    dt_pgf = []
    dt_min_cf2 = []
    dt_min_cf = []
    dt_min_pgf = []
    for Ni in N:

        # Randomise input data
        Ma = np.random.rand(Ni) * (Ma_max - Ma_min) + Ma_min

        # Timers
        T_cf = timeit.Timer("cf.Po_P_from_Ma(Ma,ga)", "from __main__ import Ma,ga,cf")
        T_cf2 = timeit.Timer(
            "cf2.Po_P_from_Ma(Ma,ga)", "from __main__ import Ma,ga,cf2"
        )
        T_pgf = timeit.Timer(
            "pgf.isentropic.pressure_ratio(Ma,ga)", "from __main__ import Ma,ga,pgf"
        )

        # Repeat a number of runs, calculate time per call
        time_per_call = np.empty((3, reps))
        for i in range(reps):
            res_cf = T_cf.autorange()
            res_cf2 = T_cf2.autorange()
            res_pgf = T_pgf.autorange()
            time_per_call[0, i] = res_cf[1] / res_cf[0]
            time_per_call[1, i] = res_cf2[1] / res_cf2[0]
            time_per_call[2, i] = res_pgf[1] / res_pgf[0]

        # Add fastest time to list
        dt_cf.append(time_per_call[0, :].mean())
        dt_cf2.append(time_per_call[1, :].mean())
        dt_pgf.append(time_per_call[2, :].mean())
        dt_min_cf.append(time_per_call[0, :].min())
        dt_min_cf2.append(time_per_call[1, :].min())
        dt_min_pgf.append(time_per_call[2, :].min())

    # Plot
    f, a = plt.subplots()
    f.set_size_inches((4.0, 3.0))
    a.loglog(N, dt_pgf, "r-", label="pgf")
    a.loglog(N, dt_cf, "b-", label="compflow")
    a.loglog(N, dt_cf2, "g-", label="compflow2")
    a.loglog(N, dt_min_pgf, "r:", label="pgf min")
    a.loglog(N, dt_min_cf, "b:", label="compflow min")
    a.loglog(N, dt_min_cf2, "g:", label="compflow2 min")
    a.set_xlabel(r"Array Length, $n$")
    a.set_ylabel(r"Time per call, $\Delta t$/s")
    a.grid(True)
    a.set_title("Benchmark evaluation of $\dot{m}\sqrt{c_pT_0}/Ap_0$")
    a.legend()
    a.set_xlim((1, 1e5))
    a.set_ylim((1e-7, 1e-2))
    a.set_xticks(tick_marks)
    f.tight_layout(pad=0.1)
    plt.savefig("bench_forward.png", dpi=250)

    speedup = np.array(dt_cf) / np.array(dt_cf2)
    print("Fortran speedup: ", 1.0 / speedup[(0, -1),])

    plt.show()

    # FORWARD EVALUATION
    print("Benchmarking inversion...")

    # Initialise lookup table
    cf.to_Ma("mcpTo_APo", 0.4, ga, use_lookup=True)

    # Loop over array sizes
    dt_cf2 = []
    dt_cf = []
    dt_lookup = []
    for Ni in N:

        X = np.random.rand(Ni) * (Xmax - Xmin) + Xmin

        # Set up timers
        T_cf = timeit.Timer("cf.Ma_from_Po_P(X,ga)", "from __main__ import X,ga,cf")
        T_cf2 = timeit.Timer("cf2.Ma_from_Po_P(X,ga)", "from __main__ import X,ga,cf2")
        # T_lookup = timeit.Timer(
        #     'cf.to_Ma("mcpTo_APo",X,ga,use_lookup=True)', "from __main__ import X,ga,cf"
        # )

        # Repeat a number of runs, calculate time per call
        time_per_call = np.empty((3, reps))
        for i in range(reps):
            res_cf = T_cf.autorange()
            res_cf2 = T_cf2.autorange()
            # res_lookup = T_lookup.autorange()
            time_per_call[0, i] = res_cf[1] / res_cf[0]
            time_per_call[1, i] = res_cf2[1] / res_cf2[0]
            # time_per_call[2, i] = res_lookup[1] / res_lookup[0]

        dt_cf.append(time_per_call[0, :].min())
        dt_cf2.append(time_per_call[1, :].min())
        # dt_lookup.append(time_per_call[2, :].min())

    # Make plot
    f, a = plt.subplots()
    f.set_size_inches((4.0, 3.0))
    a.loglog(N, dt_cf2, label="Native")
    a.loglog(N, dt_cf, label="Fortran")
    # a.loglog(N, dt_lookup, label="Lookup")
    a.set_xlabel(r"Array Length, $n$")
    a.set_ylabel(r"Time per call, $\Delta t$/s")
    a.set_title("Benchmark inversion of $\dot{m}\sqrt{c_pT_0}/Ap_0$")
    a.grid(True)
    a.legend()
    a.set_xlim((1, 1e5))
    a.set_xticks(tick_marks)
    a.set_ylim((1e-7, 1e-1))
    f.tight_layout(pad=0.1)
    plt.savefig("bench_inverse.png", dpi=250)

    speedup = np.array(dt_cf) / np.array(dt_cf2)
    print("Fortran speedup: ", 1.0 / speedup[(0, -1),])
    # speedup = np.array(dt_lookup) / np.array(dt_cf2)
    # print("Lookup speedup: ", 1.0 / speedup[(0, -1),])

    plt.show()
