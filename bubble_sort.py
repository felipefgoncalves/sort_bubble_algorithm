"""
by Felipe Fernandes - Computer Engineer
Ordenação de list numérica com o Algoritmo Bubble Sort
Sorting an array list with Bubble Sort Algorithm
"""

# Sorting Function
def bubble_sort_algorithm(list):
    LenghtOfTheArray = len(list)

    # Iterate through all array elements
    for i in range(LenghtOfTheArray):

        # Last 'i' elements are in their correct places
        for j in range(0, LenghtOfTheArray-i-1):
            
            # Iterate the array from the index 0 to 'LenghtOfTheArray'-i-1
            # Swap only if the found element is greater than the next
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)

# Array example for testing purposes
list = [3, 2, 1, 54, 10, 100, 151, 5]

# Finally, calling the function
bubble_sort_algorithm(list)