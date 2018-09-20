def main():
    sum = add_three(1, 2, 3)
    div_three(sum)


def add_three(v1, v2, v3):
    p = v1 + v2 + v3
    print(int(p))
    return p


def div_three(v4):
    sol = v4 / 3
    print(int(sol))
    return sol


main()
