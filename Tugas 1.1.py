def hitung_ganjil(lower, upper):
    if bawah < 0 or atas < 0:
        return "Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol"
    
    total = 0
    for num in range(bawah, atas + 1):
        if num % 2 != 0:
            total += 1
    
    return total

bawah = int(input("batas bawah : "))
atas = int(input("batas atas : "))

print("Total: ", hitung_ganjil(bawah, atas))