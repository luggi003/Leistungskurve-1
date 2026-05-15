
def bubble_sort(data):

    n = len(data)

    #Schleife welche jedes Elemente des Arrays durchlaeuft
    for i in range(n):
        swapped = False #Variable swapped: Solange False bis die Liste sortiert ist

    #Sortieralgorithmus
        for j in range(0, n - i - 1):
            # Elemente des Arrays werden verglichen und getauscht, falls die Anordnung nicht passt
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True 

             # Wenn die Variable swapped True wird ist die Liste geordnet und die Funktion wird beendet
        if not swapped:
            break
    return data #geordnete Liste wird zurueckgegeben