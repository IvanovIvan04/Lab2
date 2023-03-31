        if result < 0.999:
            a = pow(-1, i) * pow(x, 2 * i + 1) / (2 * i + 1)
            if a > 0.9999:
                break
            else:
                result += a
                print(a)
                print(result)
                print(i)
        break

    return round(result, 3)

x = float(input())
n = int(input())
print(sum_series(x, n))