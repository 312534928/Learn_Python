from math import floor, ceil
import copy


def Merge(a, low, mid, high):
    i = low
    j = mid + 1
    k = 0
    tmp = []
    while (i <= mid and j <= high):
        if (a[i] <= a[j]):
            tmp.append(a[i])
            i = i + 1
            k = k + 1
        else:
            tmp.append(a[j])
            j = j + 1
            k = k + 1
    while (i <= mid):
        tmp.append(a[i])
        i = i + 1
        k = k + 1
    while (j <= high):
        tmp.append(a[j])
        j = j + 1
        k = k + 1
    a[low:high + 1] = copy.copy(tmp[:k])
    tmp.clear()


def MergeSort(a, low, high):
    if low < high:
        mid = floor((low + high) / 2)
        MergeSort(a, low, mid)
        MergeSort(a, mid + 1, high)
        Merge(a, low, mid, high)


if __name__ == "__main__":
    a = [3, 2, 8, 5, 6, 1, 9, 7, 4]
    MergeSort(a, 0, len(a) - 1)
    print(a)
