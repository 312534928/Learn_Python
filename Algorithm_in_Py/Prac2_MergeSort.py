from math import floor


def merge(left, right):
    i, j = 0, 0
    tmp = []
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            global count
            count = count + (len(left) - i)
            j += 1
    tmp += left[i:]
    tmp += right[j:]
    return tmp


def mergeSort(lists):
    if len(lists) <= 1:
        return lists
    mid = floor(len(lists) / 2)
    left = mergeSort(lists[:mid])
    right = mergeSort(lists[mid:])
    return merge(left, right)


if __name__ == "__main__":
    a = [6, 3, 2, 7, 8, 9, 1, 4, 5, 5]
    # a = [6, 3, 2, 7]
    count = 0
    print("排序前:", a)
    print("排序后:", mergeSort(a))
    print("逆序数:%d" % count)
