def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)


def partition(the_list, p, r, compare_func):
    i = p
    for j in range(p, r+1):
        if compare_func(the_list[j], the_list[r]):
            the_list[j], the_list[i] = the_list[i], the_list[j]
            i += 1
    return i - 1


def quicksort(the_list, p, r, compare_func):
    if r - p < 1:
        return

    pivot = partition(the_list, p, r, compare_func)
    quicksort(the_list, p, pivot-1, compare_func)
    quicksort(the_list, pivot+1, r, compare_func)
