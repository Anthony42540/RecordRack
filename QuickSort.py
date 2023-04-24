def quickSort(arr, low, high, type):  # just sorting by album title for now!
    if low < high:
        if type == "Album Name":  # sort by album name
            left, right = partalbname(arr, low, high)
        elif type == "Artist Name":
            left, right = partartist(arr, low, high)
        elif type == "Release Date":
            left, right = partrelease(arr, low, high)
        else:
            left, right = parttracks(arr, low, high)
        quickSort(arr, low, left - 1, type)
        quickSort(arr, right, high, type)


def partalbname(arr, low, high):
    pivot = arr[low].albumName
    up = low
    down = high

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
    arr[low], arr[down] = arr[down], arr[low]

    left = low
    right = low
    track = high

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


def partartist(arr, low, high):
    pivot = arr[low].artistName
    up = low
    down = high

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
    arr[low], arr[down] = arr[down], arr[low]

    left = low
    right = low
    track = high

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


def partrelease(arr, low, high):
    pivot = arr[low].albumReleaseDate
    up = low
    down = high

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
    arr[low], arr[down] = arr[down], arr[low]

    left = low
    right = low
    track = high

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


def parttracks(arr, low, high):
    pivot = arr[low].albumNumTracks
    up = low
    down = high

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
    arr[low], arr[down] = arr[down], arr[low]

    left = low
    right = low
    track = high

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
