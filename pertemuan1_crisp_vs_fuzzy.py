import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# 1. DEFINISI FUNGSI KARAKTERISTIK CRISP
# ==========================================================
def crisp_memuaskan(rating, threshold=4.0):
    """
    Fungsi karakteristik crisp.
    Mengembalikan 1 jika rating >= threshold, selain itu 0.
    """
    return np.where(rating >= threshold, 1.0, 0.0)


# ==========================================================
# 2. DEFINISI FUNGSI KEANGGOTAAN FUZZY
# ==========================================================
def fuzzy_memuaskan(rating, a=2.5, b=4.5):
    """
    Fungsi keanggotaan fuzzy linear naik.
    - x <= a       : derajat 0
    - a <= x <= b  : derajat (x - a) / (b - a)
    - x >= b       : derajat 1
    """
    derajat = (rating - a) / (b - a)
    return np.clip(derajat, 0.0, 1.0)

# ==========================================================
# 3. GENERASI DATA SEMESTA PEMBICARAAN
# ==========================================================
# Domain rating layanan dari 1.0 sampai 5.0
ratings = np.linspace(1.0, 5.0, 500)

y_crisp = crisp_memuaskan(ratings, threshold=4.0)
y_fuzzy = fuzzy_memuaskan(ratings, a=2.5, b=4.5)

# ==========================================================
# 4. VISUALISASI PERBANDINGAN
# ==========================================================
plt.figure(figsize=(10, 5))

# Plot Logika Crisp
plt.step(ratings, y_crisp, label='Crisp (Threshold = 4.0)', 
         color='#d9534f', linewidth=2.5, where='post')

# Plot Logika Fuzzy
plt.plot(ratings, y_fuzzy, label='Fuzzy (Linear Naik [2.5, 4.5])', 
         color='#0275d8', linewidth=2.5)

# Penanda titik batas kritis
plt.axvline(x=3.9, color='gray', linestyle='--', alpha=0.7)
plt.axvline(x=4.0, color='gray', linestyle='--', alpha=0.7)
plt.scatter([3.9, 4.0], [crisp_memuaskan(3.9), crisp_memuaskan(4.0)], 
            color='#d9534f', zorder=5, s=60)
plt.scatter([3.9, 4.0], [fuzzy_memuaskan(3.9), fuzzy_memuaskan(4.0)], 
            color='#0275d8', zorder=5, s=60)

plt.title('Perbandingan Logika Crisp vs Logika Fuzzy: Kategori "Layanan Memuaskan"', fontsize=13, fontweight='bold')
plt.xlabel('Rating Pengguna (Skala 1 - 5)', fontsize=11)
plt.ylabel('Derajat Keanggotaan / Nilai Kebenaran', fontsize=11)
plt.ylim(-0.05, 1.1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()

# Simpan dan tampilkan grafik
plt.savefig('visualisasi_crisp_vs_fuzzy.png', dpi=300)
plt.show()

test_values = [3.8, 3.9, 3.99, 4.0, 4.01, 4.2]

print(f"{'Rating':<8} | {'Crisp':<8} | {'Fuzzy mu(x)':<12} | {'Interpretasi Fuzzy'}")
print("-" * 55)
for val in test_values:
    c_val = float(crisp_memuaskan(val))
    f_val = float(fuzzy_memuaskan(val))
    interpretasi = f"Tingkat pemenuhan {f_val*100:.1f}%"
    print(f"{val:<8.2f} | {c_val:<8.1f} | {f_val:<12.3f} | {interpretasi}")