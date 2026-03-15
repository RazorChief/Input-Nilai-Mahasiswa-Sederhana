import matplotlib.pyplot as plt
import numpy as np

print("=" * 55)
print("         PROGRAM NILAI & PREDIKAT MAHASISWA")
print("=" * 55)

mahasiswa_list = []

for i in range(1, 4):
    print(f"\nData Mahasiswa ke-{i}")
    print()
    nama = input("Nama Mahasiswa : ")
    nim = input("NIM            : ")

    while True:
        try:
            tugas = float(input("Nilai Tugas    : "))
            uts = float(input("Nilai UTS      : "))
            uas = float(input("Nilai UAS      : "))
            if all(0 <= n <= 100 for n in [tugas, uts, uas]):
                break
            else:
                print("Nilai harus antara 0 - 100!\n")
        except ValueError:
            print("Input harus berupa angka!\n")

    rata_rata = (tugas + uts + uas) / 3

    if rata_rata >= 85:
        grade = "A"
        predikat = "Sangat Baik"
    elif rata_rata >= 75:
        grade = "B"
        predikat = "Baik"
    elif rata_rata >= 60:
        grade = "C"
        predikat = "Cukup"
    else:
        grade = "D"
        predikat = "Kurang"

    status = "LULUS" if rata_rata >= 60 else "TIDAK LULUS"

    mahasiswa_list.append({
        "No": i,
        "Nama": nama,
        "NIM": nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Rata-rata": round(rata_rata, 2),
        "Grade": grade,
        "Predikat": predikat,
        "Status": status,
    })

# ── Rekap teks ──────────────────────────────────────────
print("\n" + "=" * 55)
print("         REKAP NILAI MAHASISWA")
print("=" * 55)

for mhs in mahasiswa_list:
    print(f"\nNo             : {mhs['No']}")
    print(f"Nama Mahasiswa : {mhs['Nama']}")
    print(f"NIM            : {mhs['NIM']}")
    print(f"Nilai Tugas    : {mhs['Tugas']}")
    print(f"Nilai UTS      : {mhs['UTS']}")
    print(f"Nilai UAS      : {mhs['UAS']}")
    print(f"Rata-rata      : {mhs['Rata-rata']}")
    print(f"Grade          : {mhs['Grade']}")
    print(f"Predikat       : {mhs['Predikat']}")
    print(f"Status         : {mhs['Status']}")
    print("-" * 55)

# ── Persiapan data untuk grafik ─────────────────────────
nama_list = [mhs["Nama"] for mhs in mahasiswa_list]
rata_list = [mhs["Rata-rata"] for mhs in mahasiswa_list]
tugas_list = [mhs["Tugas"] for mhs in mahasiswa_list]
uts_list = [mhs["UTS"] for mhs in mahasiswa_list]
uas_list = [mhs["UAS"] for mhs in mahasiswa_list]
status_list = [mhs["Status"] for mhs in mahasiswa_list]

nilai_max = max(rata_list)
nilai_min = min(rata_list)
nama_max = nama_list[rata_list.index(nilai_max)]
nama_min = nama_list[rata_list.index(nilai_min)]
jumlah_lulus = status_list.count("LULUS")
jumlah_tidak = status_list.count("TIDAK LULUS")

print(f"\nNilai Tertinggi : {nama_max} ({nilai_max})")
print(f"Nilai Terendah  : {nama_min} ({nilai_min})")
print(f"Lulus           : {jumlah_lulus} mahasiswa")
print(f"Tidak Lulus     : {jumlah_tidak} mahasiswa")

# ── Grafik ──────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("Rekap Nilai Mahasiswa", fontsize=14, fontweight="bold")

x = np.arange(len(nama_list))
width = 0.25
colors = ["#4A90D9", "#E87040", "#50B86C"]

# -- Grafik 1: Nilai per komponen (grouped bar) --
ax1 = axes[0]
ax1.bar(x - width, tugas_list, width, label="Tugas", color=colors[0])
ax1.bar(x,         uts_list,   width, label="UTS",   color=colors[1])
ax1.bar(x + width, uas_list,   width, label="UAS",   color=colors[2])
ax1.set_title("Nilai per Komponen")
ax1.set_xticks(x)
ax1.set_xticklabels(nama_list, rotation=15, ha="right")
ax1.set_ylabel("Nilai")
ax1.set_ylim(0, 110)
ax1.legend()
ax1.axhline(y=60, color="red", linestyle="--",
            linewidth=0.8, label="Batas lulus")

# -- Grafik 2: Rata-rata + highlight min & max --
ax2 = axes[1]
bar_colors = []
for n in rata_list:
    if n == nilai_max:
        bar_colors.append("#2ECC71")
    elif n == nilai_min:
        bar_colors.append("#E74C3C")
    else:
        bar_colors.append("#5B8DEF")

bars = ax2.bar(nama_list, rata_list, color=bar_colors)
ax2.set_title("Rata-rata Nilai (Hijau=Max, Merah=Min)")
ax2.set_ylabel("Rata-rata")
ax2.set_ylim(0, 110)
ax2.set_xticklabels(nama_list, rotation=15, ha="right")
ax2.axhline(y=60, color="red", linestyle="--", linewidth=0.8)

for bar, val in zip(bars, rata_list):
    ax2.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 1.5,
             str(val), ha="center", va="bottom", fontsize=9)

# -- Grafik 3: Pie chart kelulusan --
ax3 = axes[2]
labels = []
sizes = []
colors3 = []
if jumlah_lulus > 0:
    labels.append(f"Lulus ({jumlah_lulus})")
    sizes.append(jumlah_lulus)
    colors3.append("#2ECC71")
if jumlah_tidak > 0:
    labels.append(f"Tidak Lulus ({jumlah_tidak})")
    sizes.append(jumlah_tidak)
    colors3.append("#E74C3C")

ax3.pie(sizes, labels=labels, colors=colors3,
        autopct="%1.1f%%", startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5})
ax3.set_title("Data Kelulusan")

plt.tight_layout()
plt.savefig("grafik_nilai.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nGrafik disimpan sebagai 'grafik_nilai.png'")
