
from random import randint


# Euclid's algorithm
# gcd(a, 0) = a
# gcd(a, b) = gcd(b, a mod b)

def interactive_gdc(a, b):
    i = min(a, b)
    if i == 0:
        return max(a, b)
    while ((a % i) != 0) or ((b % i) != 0):
        i -= 1
    return i


def recursive_gdc(a, b):
    if min(a, b) == 0:
        return max(a, b)
    return recursive_gdc(b, a % b)


def main():
    cases = [
        ( 2305843009213693951,  2147483647),
        (618970019642690137449562111,  2305843009213693951),
        (162259276829213363391578010288127, 618970019642690137449562111),
        (170141183460469231731687303715884105727, 162259276829213363391578010288127)
    ]

    for case in cases:
        a, b = case

        delta_i = []
        delta_r = []
        for k in xrange(1, 1000000):
            i_t1 = time.time()
            i = 0 #interactive_gdc(a, b)
            i_t2 = time.time()
            #delta_i.append(i_t2 - i_t1)
            delta_i.append(0)

            r_t1 = time.time()
            r = recursive_gdc(a, b)
            r_t2 = time.time()
            delta_r.append(r_t2 - r_t1)

        m_i = sum(delta_i) / len(delta_i)
        m_r = sum(delta_r) / len(delta_r)

        print "GDC(" + str(a) + ", " + str(b) + ") i=" + str(i) + " i_t=" + str(m_i) + ", r=" + str(r) + " r_t=" + str(m_r)


if __name__ == "__main__":
    main()
