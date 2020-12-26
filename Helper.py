class utility():
    def __init__(self):
        pass
    @staticmethod
    dotProduct(a, b):
        sum = 0
        lengthA = len(a)
        lengthB = len(b)
        if lengthA != lengthB:
            raise ValueError(f'{lengthA} is different from {lengthB}')
        for i in range(lengthA):
            sum += a[i]*b[i]