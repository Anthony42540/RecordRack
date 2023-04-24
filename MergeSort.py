def mergeSort(array, left, right, sortBy):
    if left < right:
        # m is the point where the array is divided into two subarrays
        mid = left + (right - left) // 2
        mergeSort(array, left, mid, sortBy)
        mergeSort(array, mid + 1, right, sortBy)
        # Merge the sorted subarrays
        merge(array, left, mid, right, sortBy)


def merge(array, left, mid, right, sortBy):
    # Create X ← arr[left..mid] & Y ← arr[mid+1..right]
    n1 = mid - left + 1
    n2 = right - mid
    X = [0] * n1
    Y = [0] * n2
    for i in range(0, n1):
        X[i] = array[left + i]
    for i in range(0, n2):
        Y[i] = array[mid + 1 + i]
    # Merge the arrays X and Y into arr
    i = 0
    j = 0
    k = left
    # If sorting by album name
    if sortBy == "Album Name":
        while i < n1 and j < n2:
            if X[i].albumName <= Y[j].albumName:
                array[k] = X[i]
                i += 1
            else:
                array[k] = Y[j]
                j += 1
            k += 1
    # If sorting by artist name
    if sortBy == "Artist Name":
        while i < n1 and j < n2:
            if X[i].artistName <= Y[j].artistName:
                array[k] = X[i]
                i += 1
            else:
                array[k] = Y[j]
                j += 1
            k += 1
    # If sorting by release date
    if sortBy == "Release Date":
        while i < n1 and j < n2:
            if X[i].albumReleaseDate <= Y[j].albumReleaseDate:
                array[k] = X[i]
                i += 1
            else:
                array[k] = Y[j]
                j += 1
            k += 1
    # If sorting by album number of tracks
    if sortBy == "Album Number of Tracks":
        while i < n1 and j < n2:
            if X[i].albumNumTracks <= Y[j].albumNumTracks:
                array[k] = X[i]
                i += 1
            else:
                array[k] = Y[j]
                j += 1
            k += 1
    # When we run out of elements in either X or Y append the remaining elements
    while i < n1:
        array[k] = X[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = Y[j]
        j += 1
        k += 1