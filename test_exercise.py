from excercise import Exercise

BINARY_1_IDX = 0
BINARY_2_IDX = 1
SOLUTION_IDX = 2

def main():
    print("Testing start!")
    test_binary_sum()

def test_binary_sum():
    print_start_test_msg('sum_binary')
    arrays = binaries_to_sum()
    success = True
    for array in arrays:
        result = Exercise.sum_binary(array[BINARY_1_IDX], array[BINARY_2_IDX])
        print('WTF: ', array[BINARY_1_IDX], array[BINARY_2_IDX])
        success = result == array[SOLUTION_IDX]
        print_solution(array[BINARY_1_IDX], array[BINARY_2_IDX], result, array[SOLUTION_IDX])

    print_result(success)

def binaries_to_sum():
    arrays = []
    # tuple (binary1, binary2, solution)
    arrays.append(([1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 0]))
    arrays.append(([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]))
    arrays.append(([0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1]))
    arrays.append(([0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0]))
    arrays.append(([0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 1]))
    arrays.append(([0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0]))
    return arrays

def print_start_test_msg(method_name):
    print("Testing ", method_name)

def print_result(is_correct=True):
    result = 'SUCCEDED' if is_correct else 'FAILED'
    print('\nTests ', result, '!')

def print_solution(b1=[], b2=[], result=[], solution=[]):
    print("")
    test_result = 'CORRECT' if result == solution else 'ERROR'
    print(test_result)
    print('b1: {}, b2: {} -> result: {} ----> correct solution: {}'.format(b1, b2, result, solution))
    print('Decimal >> b1: {}, b2: {} -> result: {} ----> correct solution: {}'.format(to_integer(b1), to_integer(b2), to_integer(result), to_integer(solution)))

def to_integer(binary):
    res = 0
    for digit in binary:
        res = (res << 1) | digit
    return res


if __name__ == "__main__":
    main()