import random


def quick_sort(A):

    def qsort(A, lo, hi):
        if lo >= hi: return
        # A[:lt] < pivot, A[lt:gt] = pivot, A[gt:] > pivot
        lt, gt, pivot, i = lo, hi+1, A[lo], lo
        while i < gt:
            if A[i] < pivot:
                if i != lt: A[i], A[lt] = A[lt], A[i]
                lt += 1
                i += 1
            elif A[i] == pivot:
                i += 1
            else:
                gt -= 1
                A[i], A[gt] = A[gt], A[i]
        qsort(A, lo, lt-1)
        qsort(A, i, hi)

    random.shuffle(A)
    qsort(A, 0, len(A)-1)


def is_sorted(A):
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            return False
        return True


if __name__ == "__main__":
    random.seed(1)
    L = [random.randint(0, 9) for _ in range(10)]
    print(L)
    quick_sort(L)
    print(L)
    assert is_sorted(L)
