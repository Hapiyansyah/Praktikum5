Nama = []
NIM = []
Tugas = []
UTS = []
UAS = []
TOTAL = []

while True:
    nama = input("Nama :")
    Nama.append(nama)
    Nim = int(input("NIM :"))
    NIM.append(Nim)
    nTugas = float(input("Nilai Tugas :"))
    Tugas.append(nTugas)
    uts = float(input("Nilai UTS :"))
    UTS.append(uts)
    uas = float(input("Nilai UAS :"))
    UAS.append(uas)

    nAkhir = (int(nTugas) * .3) + (int(uts) * .35) + (int(uas) * .35)
    TOTAL.append(nAkhir) 

    Lagi = ""
    while Lagi != "y" and Lagi != "t":
        Lagi = input("Tambah data (y/t)?")
    if Lagi == "t":
        print("="*70)
        print("| No |\tNama\t   | NIM   | Tugas   | UTS     | UAS     | Akhir   |")
        print("="*70)

        for i in range(len(NIM)):
            nm = "| %d. |\t%s\t" % (i+1, Nama[i])
            im = "   | %d" % NIM[i]
            tg = "   | %.2f" % Tugas[i]
            ut = "   | %.2f" % UTS[i]
            ua = "   | %.2f" % UAS[i]
            ah = "   | %.2f" % TOTAL[i]
            In = "   |"

            join = nm + im + tg + ut + ua + ah + In
            print(join)

        break