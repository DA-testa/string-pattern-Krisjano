def read_input():
    ievade = input()
    if 'F' in ievade:
        try:
            with open("./tests/06") as fails:
                f = fails.readlines()
                pattern = f[0].rstrip()
                text = f[1].rstrip()
        except FileNotFoundError:
            print("Fails nav atrasts")
            return

    elif 'I' in ievade:
        pattern = input().rstrip()
        text = input().rstrip()

    else:
        print("Nepareiza komanda")
        return
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    d = 256
    q = 101
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    pp = 0
    tt = 0
    h = 1

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        pp = (d * pp + ord(pattern[i])) % q
        tt = (d * tt + ord(text[i])) % q

    occurances = []
    for i in range(N - M + 1):
        if pp == tt:
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
            j = j + 1
            if j == M:
                occurances.append(i)
        if i < N - M:
            tt = (d * (tt - ord(text[i]) * h) + ord(text[i + M])) % q
            if tt < 0:
                tt = tt + q
    return occurances

if __name__ == '__main__':
    pattern, text = read_input()
    if pattern and text:
        print_occurrences(get_occurrences(pattern, text))
