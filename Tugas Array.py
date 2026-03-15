print("=" * 55)
print("         PROGRAM NILAI & PREDIKAT MAHASISWA")
print("=" * 55)

mahasiswa_list = []

for i in range(1, 11):
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
