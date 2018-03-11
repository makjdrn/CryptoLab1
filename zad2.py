from numpy import uint32, long, uint64, uint8, uint16, int64, int32
from numpy.core import uint

r = []
x = []


def generator_glibc(seed):
    r.append(seed)

    for i in range(1, 30):
        r.append(int64((long(16807) * r[i - 1]) % 2147483647))
        if r[i] < 0:
            r[i] += 2147483647
    for i in range(31, 33):
        r.append(r[i - 31])
    for i in range(34, 343):
        r.append(r[i - 31] + r[i - 3])


def next_glibc():
    r.append(int32(r[len(r) - 31] + r[len(r) - 3]))
    return r[-1] >> 1


def predict(x_n):
    x.append(x_n)
    if len(x) >= 31:
        return int64((x[len(x) - 3] + x[len(x) - 31]) % 2147483647)
    return 0


def main():
    generator_glibc(1)
    next = 0
    i = 0
    while i < 50:
        x1 = uint32(next_glibc())
        print("x = ", x1)
        if next == 0:
            print("Dont know.")
        else:
            if abs(long(next) - long(x1)) <= 1:
                print("From generator glibc")
            else:
                print("From uniform distribution")
        next = uint32(predict((x1)))
        print("Predicted = ", next)
        i = i + 1


main()
