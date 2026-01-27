import numpy as np
import matplotlib.pyplot as plt

# Model: X(t) = X0 + a*t + c*W(t)

a = 0.2      # priemerná rýchlosť sneženia (drift)
c = 0.8      # sila náhodných výkyvov (volatilita)
X0 = 5.0       # počiatočné množstvo snehu


T = 100.0 # celkový čas simulácie
N = 500 # počet časových krokov
dt = T / N
t = np.linspace(0, T, N+1)

M = 300   # počet trajektórií

for i in range(M):
    X = np.zeros(N+1)
    X[0] = X0
    
    for n in range(N):
        # náhodný prírastok Wienerovho procesu
        dW = np.sqrt(dt) * np.random.randn()
        X[n+1] = X[n] + a * dt + c * dW
        
        # fyzikálna podmienka: sneh nemôže byť záporný
        if X[n+1] < 0:
            X[n+1] = 0
    
    plt.plot(t, X, alpha=0.3)

plt.xlabel("t")
plt.ylabel("X(t) = Množstvo snehu na streche")
plt.title("Sneh na streche – 300 simulovaných trajektórií")
plt.show()
