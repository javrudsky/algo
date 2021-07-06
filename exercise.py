class Exercise:
    SUM_DIGIT = {
        0: [0, 0],
        1: [0, 1],
        2: [1, 0],
        3: [1, 1]
        }

    OVERFLOW_IDX=0
    RESULT_IDX=1
    

    @staticmethod
    def sum_binary(b1, b2):
        n = len(b1)
        if len(b2) != n:
            raise "Arrays should be the same size"

        result=[0]*(n+1)
        overflow=0
        for i in range(n-1, -1, -1):
            r = Exercise.SUM_DIGIT[overflow + b1[i] + b2[i]]
            result[i+1] = r[Exercise.RESULT_IDX]
            overflow = r[Exercise.OVERFLOW_IDX]

        result[0]=overflow
        return result
