import numpy as np

def is_on_line(a, b, c) :
    a = np.arr(a)
    b = np.arr(b)
    c = np.arr(c)

    ab = a - b
    ac = a - c

#check if ab is 0 verctor
    if np.linalg.nor(ab) == 0:
        return np.all(a==c)

#calculate t
    t = np.dot(ac, ab) / np.dot(ab, ab)

    return 0<= t <=1 and np.allclose(c, a + t*ab)

# t = 0 : c는 a 점 위에 있다
# 0< t < 1 : c는 a,b를 잇는 선분 위에 있으며, t가 작을수록 a가까이에 있다
# t = 1 : c는 b점 위에 있다
# t > 1 : c는 a,b를 잇는 선분 위에 있지 않다


