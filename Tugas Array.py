print("=" * 45)
print("         PROGRAM NILAI & PREDIKAT SISWA")
print("=" * 45)

nama = input("Nama Siswa : ")
nim = input("NIM        : ")

while True:
    try:
        tugas = float(input("Nilai Tugas : "))
        uts = float(input("Nilai UTS   : "))
        uas = float(input("Nilai UAS   : "))
        if all(0 <= n <= 100 for n in [tugas, uts, uas]):
            break
        else:
            print("⚠ Nilai harus antara 0 - 100!\n")
    except ValueError:
        print("⚠ Input harus berupa angka!\n")

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

print("\n" + "=" * 45)
print("          HASIL NILAI SISWA")
print("=" * 45)
print(f"  Nama      : {nama}")
print(f"  NIM       : {nim}")
print("-" * 45)
print(f"  Tugas     : {tugas:.1f}")
print(f"  UTS       : {uts:.1f}")
print(f"  UAS       : {uas:.1f}")
print("-" * 45)
print(f"  Rata-rata : {rata_rata:.2f}")
print(f"  Grade     : {grade} ({predikat})")
print(f"  Status    : {status}")
print("=" * 45)
