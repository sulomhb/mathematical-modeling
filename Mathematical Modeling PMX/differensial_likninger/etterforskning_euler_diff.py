import matplotlib.pyplot as plt
def euler(T, dt, k, T_env):
    return T + dt*(-k*(T-T_env))
    
k = 0.29
T_env = float(input("Tast inn omgivelsestemperatur: "))
T_start = 37
T = [T_start]
T_body = float(input("Tast inn kroppstemperatur: "))
t = [0]
dt = 1E-3
while T[-1] >= T_body:
    T.append(euler(T[-1], dt, k, T_env))
    t.append(t[-1] + dt)
plt.plot(t, T)
plt.show()