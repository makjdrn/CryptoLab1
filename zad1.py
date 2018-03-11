def next_lcg(a, c, m, x):
    x = (x * a + c) % m
    return x


x = []


def predict(x_n):
    x.append(x_n)
    Max = max(x)
    check = False
    for m in range(Max + 1, 2 * Max + 10):
        for c in range(0, m):
            for a in range(0, m):
                for i in range(0, len(x) - 1):
                    if (x[i] * a + c) % m == x[i + 1]:
                        check = True
                    else:
                        check = False
                        break

                if check:
                    return (x[-1] * a + c) % m
    return x[-1]


def main():
    a = 101
    c = 13
    m = 2
    x = 1
    while True:
        x = next_lcg(a, c, m, x)
        print('x = ', x, ' Predicted: ', predict(x))


main()
