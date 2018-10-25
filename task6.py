import numpy as np


def getdimension(a):
    return len(a.shape)


def getdiagonal(a):
    return np.array([a[i, i] for i in range(len(a))])


def cutarray(a, minvalue, maxvalue):
    return np.clip(a, minvalue, maxvalue)


def getmoments(a):
    return (np.mean(a), np.var(a))


def getdotproduct(a, b):
    return sum(a[i]*b[i] for i in range(len(a)))


def checkequal(a, b):
    return a == b


def comparewithnumber(a, bound):
    return a < bound


def matrixproduct(a, b):
    return np.matmul(a, b)


def matrixdet(a):
    return np.linalg.det(a)


def getones(n, k):
    return np.array([1 if i % n-i//n == k else 0 for i in range(n*n)],
                    float).reshape(n, n)


if __name__ == "__main__":
    assert getdimension(np.array([1, 2, 3])) == 1
    assert getdimension(np.array([[1], [2], [3]])) == 2
    assert getdimension(np.array([[[[1]]]])) == 4
    print("getdimension - OK")

    assert np.array_equal(np.array(getdiagonal(np.array([[1, 2], [3, 4]]))),
                          np.array([1, 4]))
    print("getdiagonal - OK")

    assert np.array_equal(cutarray(np.array([1, 2, 3, 4]), 2, 3),
                          np.array([2, 2, 3, 3]))
    print("cutarray - OK")

    assert getmoments(np.array([2, 1, 9])) == (4.0, 12.666666666666666)
    print("getmoments - OK")

    assert getdotproduct(np.array([1, 2, 3]), np.array([4, 5, 6])) == 32
    print("getdotproduct - OK")

    assert np.array_equal(checkequal(np.array([1, 2, 3]), np.array([1, 5, 3])),
                          np.array([True, False, True]))
    print("checkequal - OK")

    assert np.array_equal(comparewithnumber(np.array([[1, 2], [3, 4]]), 4),
                          np.array([[True, True], [True, False]]))
    print("comparewithnumber - OK")

    assert np.array_equal(matrixproduct(np.array([[1, 2], [3, 4]]),
                                        np.array([[5, 6], [7, 8]])),
                          np.array([[19, 22], [43, 50]]))
    assert np.array_equal(matrixproduct(np.array([[1, 2]]),
                                        np.array([[3], [4]])),
                          np.array([[11]]))
    print("matrixproduct - OK")

    assert int(round(matrixdet(np.array([[5, 6], [7, 8]])))) == -2
    assert int(round(matrixdet(np.array([[123]])))) == 123
    print("matrixdet - OK")

    assert np.array_equal(getones(3, 1), np.array([[0., 1., 0.],
                                                   [0., 0., 1.],
                                                   [0., 0., 0.]]))
    assert np.array_equal(getones(3, 9), np.array([[0., 0., 0.],
                                                   [0., 0., 0.],
                                                   [0., 0., 0.]]))
    print("getones - OK")
