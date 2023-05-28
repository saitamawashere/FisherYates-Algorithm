#Program mengacak urutan elemen-elemen dari sebuah list
import random

def fisher_yates_shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# Main program
input_data = input("Masukkan elemen-elemen yang akan diacak, pisahkan dengan spasi: ")
elements = input_data.split()
result = fisher_yates_shuffle(elements)
print("Hasil acak:", result)