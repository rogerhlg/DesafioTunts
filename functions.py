def round_roger(n):
    x = int(n)
    y = n % x
    if y != 0:
        return x+1
    else:
        return x


def generate_naf(avg):
    naf = (((avg + avg) - 14) * -1) + avg
    return naf

