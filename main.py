import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = pd.read_excel("/content/data_hambatan.xlsx")
df = pd.DataFrame(url)

# Kolom 0 adalah Arus (I), Kolom 1 adalah Tegangan (V)
I = df.iloc[:, 0]  # Sumbu X
V = df.iloc[:, 1]  # Sumbu Y

# Persamaan: V = m*I + c
# Derajat polinomial = 1 (garis lurus)
m, c = np.polyfit(I, V, 1)

# Berdasarkan Hukum Ohm: V = R*I, Maka gradien (m) adalah nilai Hambatan (R)
R_estimasi = m

print("-" * 30)
print("HASIL ANALISIS HUKUM OHM")
print("-" * 30)
print(f"Gradien kemiringan (m) : {m:.4f}")
print(f"Konstanta (c)          : {c:.4f}")
print(f"Estimasi Hambatan (R)  : {R_estimasi:.2f} Ohm")
print("-" * 30)

# Plotting Grafik V vs I 
plt.figure(figsize=(8, 6))

# Plot data asli (titik scatter)
plt.scatter(I, V, color='blue', label='Data Pengukuran')

# Plot garis regresi linear
V_prediksi = m * I + c
plt.plot(I, V_prediksi, color='red', linestyle='--', label=rf'Regresi Linear (R = {R_estimasi:.2f} $\Omega$)')

# Label dan Judul
plt.title('Grafik Hubungan Tegangan (V) vs Arus Listrik (I)')
plt.xlabel('Arus Listrik $I$ (Ampere)')
plt.ylabel('Tegangan Listrik $V$ (Volt)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Menampilkan plot
plt.show()