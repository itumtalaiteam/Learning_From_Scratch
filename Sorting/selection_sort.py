from temp import generate_random_data

def selectionSort(liste):
    length = len(liste)
    for ind in range(length):
        min_index = ind
        for j in range(ind + 1, length):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[ind], liste[min_index] = liste[min_index], liste[ind] # Swap
    return liste
 
veri = generate_random_data()
sortlanmis_hali = selectionSort(veri)
print('The liste after sorting in Ascending Order by selection sort is:')
print(sortlanmis_hali)