# %% Import of packages:

import matplotlib.pyplot as plt
import numpy as np

# %% Model parameters:

H = 0.079  # [m]  Water height
D = 0.090  # [m]  Inner diameter
c = 4180  # [J/(kg*K)] Specific heat capacity of water
rho = 1000  # [kg/m3] Density of water
    # Area-specific thermal conductivity of plastic:
k_tc = 0.2  # [(W*m/(m2*K)) = W/(m*K)]
L = 3e-3  # [m]

# %% Derived parameters:

V = H*np.pi*(D/2)**2  # [m3] Water volume 
C = c*rho*V  # [J/K] Heat capacity of water in kettle
A = np.pi*D*H + 2*np.pi*(D/2)**2  # [m2]
G = (k_tc/L)*A  # [W/K]  Thermal conductivity

# %% Simulation time settings:

dt = 0.1  # [s]
t_start = 0  # [s]
t_stop = 500  # [s]
N_sim = int((t_stop - t_start)/dt) + 1  # Num time-steps

# %%  Params of input signals:

T_room = 20  # [oC]
P_on = 700  # [W]
P_off = 0  # [W]

# %% Preallocation of arrays for plotting:

t_array = np.linspace(t_start, t_stop, N_sim)
k_array = np.arange(0, N_sim)
T_array = np.zeros(N_sim)
T_room_array = np.zeros(N_sim) + T_room
P_array = np.zeros(N_sim)

# %% State limits:

T_min = 0  # [oC]
T_max = 100  # [oC]

# %% Initialization:

T_init = 20.0  # [oC]
T_k = T_init

# %% Simulation loop:

for k in k_array:


    t_k = t_array[k]

    # Setting input:
    if (t_k >= t_start):
        P_k = P_on
 
    # Time-derivative:
    dT_dt_k = (1/C)*(P_k + G*(T_room - T_k))

    # Euler forward integration:
    T_kp1 = T_k + dt*dT_dt_k
    
    # Limitation of state:
    T_kp1 = np.clip(T_kp1, T_min, T_max) 

    # Updating arrays for plotting:
    T_array[k] = T_k
    P_array[k] = P_k

    # Time shift:
    T_k = T_kp1

# %% Plotting:

plt.close('all')
plt.figure(num=1, figsize=(12, 9))

plt.subplot(2, 1, 1)
plt.plot(t_array, T_array,'b')
plt.plot(t_array, T_room_array,'g')
plt.ylabel('[deg C]')
plt.grid()
plt.legend(labels=('T', 'T_room'))

plt.subplot(2, 1, 2)
plt.plot(t_array, P_array, 'r')
plt.grid()
plt.xlabel('t [s]')
plt.ylabel('[W]')
plt.legend(labels=('P',))

plt.show()

# plt.savefig('prog_sim_kettle.pdf')