import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (11, 5)  # set default figure size

λ = 0.9
α = 0
ρ1 = 0.9
ρ2 = 0.05

A = np.array([[1, 0, 0],
              [α, ρ1, ρ2],
              [0, 1, 0]])
G = np.array([[0, 1, 0]])

eigvals = np.linalg.eigvals(A)
print(eigvals)
print((abs(eigvals) <= 1).all())

# compute the solution, i.e., formula (3)
F = (1 - λ) * G @ np.linalg.inv(np.eye(A.shape[0]) - λ * A)
print("F =", F)

# set the initial state
x0 = np.array([1, 1, 0])
T = 100  # length of simulation
m_seq = np.empty(T + 1)
p_seq = np.empty(T + 1)
m_seq[0] = G @ x0
p_seq[0] = F @ x0

# simulate for T periods
x_old = x0
for t in range(T):
    x = A @ x_old
    m_seq[t + 1] = G @ x
    p_seq[t + 1] = F @ x
    x_old = x

plt.figure()
plt.plot(range(T + 1), m_seq, label='$m_t$')
plt.plot(range(T + 1), p_seq, label='$p_t$')
plt.xlabel('t')
plt.title(f'λ={λ}, α={α}, $ρ_1$={ρ1}, $ρ_2$={ρ2}')
plt.legend()
plt.show()
