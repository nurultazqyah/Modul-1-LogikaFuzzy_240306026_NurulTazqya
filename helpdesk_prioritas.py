import numpy as np
import matplotlib.pyplot as plt

# ==============================================
# 1. Fungsi Logika Crisp
# ==============================================
def kritis_crisp(x):
    """Batas tegas: >=8 jam = kritis"""
    if x < 8:
        return 0.0
    else:
        return 1.0

# ==============================================
# 2. Fungsi Logika Fuzzy
# ==============================================
def kritis_fuzzy(x):
    """Interval transisi: 4 s.d. 12 jam"""
    if x < 4:
        return 0.0
    elif 4 <= x <= 12:
        return (x - 4) / 8   # rumus linier
    else:  # x > 12
        return 1.0

# ==============================================
# 3. Data Uji sesuai soal
# ==============================================
data_uji = [2, 4, 6, 7.9, 8.0, 8.1, 10, 12, 16, 24]

print("="*60)
print("TABEL PERBANDINGAN: CRISP vs FUZZY")
print("="*60)
print(f"{'Waktu (jam)':<12} {'Crisp':<10} {'Fuzzy':<10}")
print("-"*60)

hasil_crisp = []
hasil_fuzzy = []
for jam in data_uji:
    c = kritis_crisp(jam)
    f = kritis_fuzzy(jam)
    hasil_crisp.append(c)
    hasil_fuzzy.append(f)
    print(f"{jam:<12} {c:<10.1f} {f:<10.4f}")

print("="*60)

# ==============================================
# 4. Visualisasi & Simpan sebagai PNG
# ==============================================
x_rentang = np.linspace(0, 24, 200)
y_crisp = np.array([kritis_crisp(xi) for xi in x_rentang])
y_fuzzy = np.array([kritis_fuzzy(xi) for xi in x_rentang])

plt.figure(figsize=(10, 6))
plt.plot(x_rentang, y_fuzzy, label='Fuzzy (Linier)', color='blue', linewidth=2)
plt.plot(x_rentang, y_crisp, label='Crisp (Batas Tegas)', color='red', linestyle='--', linewidth=2)

# Tandai titik data uji
plt.scatter(data_uji, hasil_crisp, color='red', marker='o', zorder=5)
plt.scatter(data_uji, hasil_fuzzy, color='blue', marker='s', zorder=5)

plt.xlabel('Waktu Tunggu (jam)')
plt.ylabel('Derajat Keanggotaan μ(x)')
plt.title('Sistem Prioritas Tiket Helpdesk TI — Crisp vs Fuzzy')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 24)
plt.ylim(-0.1, 1.1)

# Simpan ke file PNG
nama_file = 'perbandingan_crisp_fuzzy.png'
plt.savefig(nama_file, dpi=300, bbox_inches='tight')
print(f"\n Grafik disimpan sebagai: {nama_file}")

plt.show()