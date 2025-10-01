def volume(initi, n):
    v = initi
    for i in range(n):
        v = v * 0.97 + 1.2
    return v

assert volume(52,1) == 51.64
assert volume(52,5) == 50.304808308400006