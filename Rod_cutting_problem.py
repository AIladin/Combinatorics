def to_sum(n):
    '''Розкладає число n в усі можливі суми чисел менших за n
    Працює не зовсім корректно бо іноді видає однакові послідовності декілька разів.

    :param n: число яке необхідно представити у вигляді суми
    :return: генератор списків розбиттів
    '''
    r = [n]

    while True:
        for i in range(len(r)-1,-1,-1):

            yield r

            if r[i] > 1:
                if i == len(r)-1:
                    r.append(1)
                    r[i] -= 1
                    continue
                elif len(r)-1>i>=0:
                    r[i] -=1
                    r[i+1] +=1
                    continue
            if r[0] == 1:
                yield [1]*n
                raise StopIteration


def count(p, r, cut_p = 0):
    ''' Підраховує ціну конкретнго розбиття

    :param p: Прайс-ліст
    :param r: Розрбиття
    :param cut_p: Ціна розрізу
    :return:
    '''
    s = 0
    for i in r:
        s += p[i]-cut_p
    return s


def main():
    p = [0,1,5,8,9,10,17,17,20,24,30]
    n = 8
    for i in to_sum(n):
        t = ((count(p,i),i) ) # перебираємо усі розбиття, підраховуємо їх вартість та знаходимо максимальну
        print(t)



if __name__ == '__main__':
    print(main())

