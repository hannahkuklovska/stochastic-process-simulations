import numpy as np
import matplotlib.pyplot as plt


# Kapilára na priamke rotujucej okolo bodu (0,0)
# Simulujeme náhodný proces Y(t) = W(t) * sin(uhlova_rychlost  t)

# PARAMETRE
uhlova_rychlost = 0.2

T = 100 # celkový čas
N = 1000# počet časových krokov
M = 300 # počet trajektórií (realizácií procesu)

dt = T / N # dĺžka jedného časového kroku
t = np.linspace(0, T, N+1) # časová mriežka

plt.figure(figsize=(10,6))

# PRE KAZDU TRAJEKTORIU
for m in range(M):  
    # 1) Wienerov proces, W(0) = 0, začiatok
    W = np.zeros(N+1) 
    
    # Inkrementy, N rozdelenie
    for n in range(N): 
        dW = np.sqrt(dt) * np.random.randn() 
        W[n+1] = W[n] + dW
    
    # 2) Môj proces, Y(t) = sin(UR t) * W(t)
    Y = W * np.sin(uhlova_rychlost * t)

    # 3) Kreslim jednu realizáciu
    plt.plot(t, Y, alpha=0.1)

plt.xlabel("t")
plt.ylabel("Y(t)")
plt.title("300 trajektórií: Y(t) = W(t) sin(URt)")
plt.show()






