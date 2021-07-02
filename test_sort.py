from sort import Sort

TO_SORT_IDX = 0
SOLUTION_IDX = 1

def main():
    print("Testing start!")
    test_insertion_sort()

def test_insertion_sort():
    print_start_test_msg('insertion_sort')
    arrays = values_to_sort()
    success = True
    for array in arrays:
        sorted = Sort.insertion_sort(array[TO_SORT_IDX].copy())
        success = sorted == array[SOLUTION_IDX]
        print_solution(array[TO_SORT_IDX], sorted, array[SOLUTION_IDX])

    print_result(success)


def values_to_sort():
    arrays = []
    # tuple (array, solution)
    arrays.append(([10, 5, 1, 20, 17, 2, 1, 12], [1, 1, 2, 5, 10, 12, 17, 20]))
    arrays.append(([0, -1, 50, 22, 100, 101, 3, 20, 20, 20, 55, 0], [-1, 0, 0, 3, 20, 20, 20, 22, 50, 55, 100, 101]))
    return arrays

def print_start_test_msg(method_name):
    print("Testing ", method_name)

def print_result(is_correct=True, to_sort=[], sorted=[]):
    result = 'SUCCEDED' if is_correct else 'FAILED'
    print('\nTests ', result, '!')

def print_solution(to_sort=[], sorted=[], solution=[1]):
    result = 'CORRECT' if sorted == solution else 'ERROR'
    print('[{}]'.format(result), '-> To sort:', to_sort, '->', sorted)


if __name__ == "__main__":
    main()

