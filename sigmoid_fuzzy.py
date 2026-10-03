import numpy as np
import matplotlib.pyplot as plt

# === Parameter ===
x0 = 3.5   # titik tengah
k = 2.0    # kecuraman lereng
x = np.linspace(0, 7, 200)  # rentang nilai x

# === 1. Fungsi Sigmoid μ(x) ===
def sigmoid(x, x0, k):
    return 1 / (1 + np.exp(-k * (x - x0)))

mu_sigmoid = sigmoid(x, x0, k)

# === 2. Fungsi Linear Naik ===
# Dari x=2 sampai x=5 naik dari 0 ke 1
def linear_naik(x):
    y = np.zeros_like(x)
    mask = (x >= 2) & (x <= 5)
    y[mask] = (x[mask] - 2) / (5 - 2)
    y[x > 5] = 1
    return y

mu_linear = linear_naik(x)

# === 3. Fungsi Crisp ===
# Langsung 0 sebelum x0, 1 sesudah x0
def crisp(x, x0):
    return np.where(x < x0, 0, 1)

mu_crisp = crisp(x, x0)

# === Gambar Grafik ===
plt.figure(figsize=(10, 6))
plt.plot(x, mu_sigmoid, label=f'Sigmoid: $x_0$={x0}, $k$={k}', color='blue', linewidth=2)
plt.plot(x, mu_linear, label='Linear Naik', color='green', linestyle='--', linewidth=2)
plt.plot(x, mu_crisp, label=f'Crisp di $x_0$={x0}', color='red', linestyle='-.', linewidth=2)

plt.xlabel('Nilai x')
plt.ylabel('Derajat Keanggotaan μ(x)')
plt.title('Perbandingan Kurva Sigmoid, Linear Naik, dan Crisp')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(-0.1, 1.1)
plt.show()