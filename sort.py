class Sort(object):

    @staticmethod
    def insertion_sort(elements):
        count = len(elements)
        for j in range(1, count):
            key = elements[j]
            i = j - 1
            while i >= 0 and key < elements[i]:
                elements[i + 1] = elements[i]
                i-=1
            elements[i + 1] = key
        return elements
