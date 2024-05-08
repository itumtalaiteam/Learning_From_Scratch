from temp import generate_random_data

# Bubble Sort Algoritması
# En basit sıralama algoritmalarından biridir.
# Her bir elemanı bir sonraki elemanla karşılaştırır.
# Eğer bir önceki eleman bir sonraki
# elemandan büyükse yer değiştirir.
# Bu işlemi listenin sonuna kadar yapar.
# Bu işlem bir kere yapıldığında en büyük eleman
# listenin sonuna yerleşir.
# Bu işlemi listenin uzunluğu kadar yapar.


def bubble_sort(liste):
    length = len(liste)
    for i in range(length):
        swapped = False
        for j in range(0, length-i-1):
            if liste[j] > liste[j+1]:
                swapped = True
                liste[j], liste[j+1] = liste[j+1], liste[j] # Swap
        if not swapped:
            break
    return liste


# Big O Notasyonu (O(n^2))
# Bubble Sort algoritmasının karmaşıklığı O(n^2) dir.
# Bu algoritma çok büyük veri setlerinde kullanılmaz.
# Çünkü çok fazla işlem yapar.
# Bubble Sort algoritmasının en kötü durumu O(n^2) dir.
# En iyi durumu ise O(n) dir.
# Ortalama durumu ise O(n^2) dir.


if __name__ == '__main__':
    data = generate_random_data()
    print('Data:', data)
    print('Sorted Data:', bubble_sort(data))