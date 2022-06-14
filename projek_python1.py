def SELAMAT_DATANG():
    """Print "SELAMAT DATANG KEPADA PELANGGAN YANG DIHORMATI" and return None."""
    print("SELAMAT DATANG KEPADA PELANGGAN YANG DIHORMATI")

SELAMAT_DATANG()

nama=str(input("Sila masukkan nama penuh anda:"))
umur=int(input("Sila masukkan umur anda:"))
hobi= str(input("Sila masukkan hobi anda:"))

if nama=="":
    nama=str(input("Sila masukkan nama penuh anda:"))
else:
    if umur<=0:
        print("Umur anda mesti lebih daripada 0.")
        umur=int(input("Sila masukkan umur anda:"))
        hobi=str(input("Sila masukkan hobi anda:"))
    else:
        print("Salam sejahtera",nama,".Anda berumur",umur, "tahun"". Hobi anda adalah",hobi,". Terima Kasih. Jumpa lagi.")

    

    