# used Quick Sort code from lecture 6 (Sorting) slide 122
# used explanation for handling duplicates in quicksort from https://mathcenter.oxford.emory.edu/site/cs171/quickSort3Way/
def quickSort(arr, low, high, type): # recursive call to use quick sort and partition functions on array
    if low < high:
        if type == "Album Name":  # sort by album name
            left, right = partalbname(arr, low, high)
        elif type == "Artist Name":  # sort by album name
            left, right = partartist(arr, low, high)
        elif type == "Release Date":  # sort by release date
            left, right = partrelease(arr, low, high)
        else: # sort by track total
            left, right = parttracks(arr, low, high)
        #  recursively called on left and right halves of list (excluding duplicate pivot values)
        quickSort(arr, low, left - 1, type)
        quickSort(arr, right, high, type)


#  partition for album name
def partalbname(arr, low, high):
    #  assigns pivot to first index in partition
    pivot = arr[low].albumName
    up = low
    down = high

    #  swaps values higher and lower than pivot until the up index passes the down index
    while up < down:
        for j in range(up, high):
            if arr[up].albumName > pivot:
                break
            up += 1
        for j in range(high, low, -1):
            if arr[down].albumName < pivot:
                break
            down -= 1
        if up < down:
            arr[up], arr[down] = arr[down], arr[up]
    #  swaps pivot value with low index value (pivot is at down index)
    #  pivot value is now in the correct place, but without regard to duplicate pivot values
    arr[low], arr[down] = arr[down], arr[low]

    left = low
    right = low
    track = high

    #  puts duplicate pivots in proper place and returns index of the first pivot value (left)
    #  and index of the first non pivot value after the pivots (right)
    while right <= track:
        if arr[right].albumName < arr[down].albumName:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right += 1
        elif arr[right].albumName > arr[down].albumName:
            if arr[track].albumName == arr[down].albumName:
                arr[track], arr[right] = arr[right], arr[track]
            track -= 1
        else:
            right += 1
    return left, right


#  partition for artist name
def partartist(arr, low, high):
    #  assigns pivot to first index in partition
    pivot = arr[low].artistName
    up = low
    down = high

    #  swaps values higher and lower than pivot until the up index passes the down index
    while up < down:
        for j in range(up, high):
            if arr[up].artistName > pivot:
                break
            up += 1
        for j in range(high, low, -1):
            if arr[down].artistName < pivot:
                break
            down -= 1
        if up < down:
            arr[up], arr[down] = arr[down], arr[up]
    #  swaps pivot value with low index value (pivot is at down index)
    #  pivot value is now in the correct place, but without regard to duplicate pivot values
    arr[low], arr[down] = arr[down], arr[low]

    left = low
    right = low
    track = high

    #  puts duplicate pivots in proper place and returns index of the first pivot value (left)
    #  and index of the first non pivot value after the pivots (right)
    while right <= track:
        if arr[right].artistName < arr[down].artistName:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right += 1
        elif arr[right].artistName > arr[down].artistName:
            if arr[track].artistName == arr[down].artistName:
                arr[track], arr[right] = arr[right], arr[track]
            track -= 1
        else:
            right += 1
    return left, right


#  partition for release date
def partrelease(arr, low, high):
    #  assigns pivot to first index in partition
    pivot = arr[low].albumReleaseDate
    up = low
    down = high

    #  swaps values higher and lower than pivot until the up index passes the down index
    while up < down:
        for j in range(up, high):
            if arr[up].albumReleaseDate > pivot:
                break
            up += 1
        for j in range(high, low, -1):
            if arr[down].albumReleaseDate < pivot:
                break
            down -= 1
        if up < down:
            arr[up], arr[down] = arr[down], arr[up]
    #  swaps pivot value with low index value (pivot is at down index)
    #  pivot value is now in the correct place, but without regard to duplicate pivot values
    arr[low], arr[down] = arr[down], arr[low]

    left = low
    right = low
    track = high

    #  puts duplicate pivots in proper place and returns index of the first pivot value (left)
    #  and index of the first non pivot value after the pivots (right)
    while right <= track:
        if arr[right].albumReleaseDate < arr[down].albumReleaseDate:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right += 1
        elif arr[right].albumReleaseDate > arr[down].albumReleaseDate:
            if arr[track].albumReleaseDate == arr[down].albumReleaseDate:
                arr[track], arr[right] = arr[right], arr[track]
            track -= 1
        else:
            right += 1
    return left, right


#  partition for number of tracks
def parttracks(arr, low, high):
    #  assigns pivot to first index in partition
    pivot = arr[low].albumNumTracks
    up = low
    down = high

    #  swaps values higher and lower than pivot until the up index passes the down index
    while up < down:
        for j in range(up, high):
            if arr[up].albumNumTracks > pivot:
                break
            up += 1
        for j in range(high, low, -1):
            if arr[down].albumNumTracks < pivot:
                break
            down -= 1
        if up < down:
            arr[up], arr[down] = arr[down], arr[up]
    #  swaps pivot value with low index value (pivot is at down index)
    #  pivot value is now in the correct place, but without regard to duplicate pivot values
    arr[low], arr[down] = arr[down], arr[low]

    left = low
    right = low
    track = high

    #  puts duplicate pivots in proper place and returns index of the first pivot value (left)
    #  and index of the first non pivot value after the pivots (right)
    while right <= track:
        if arr[right].albumNumTracks < arr[down].albumNumTracks:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right += 1
        elif arr[right].albumNumTracks > arr[down].albumNumTracks:
            if arr[track].albumNumTracks == arr[down].albumNumTracks:
                arr[track], arr[right] = arr[right], arr[track]
            track -= 1
        else:
            right += 1
    return left, right