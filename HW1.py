''' миллера рабина + псевдопростые + жадній алгоритм + цена за разрез '''
import random


def prepare(n):
    """
    Функція яка розкладає число n = 2**s*t, де t - непарне

    :param n: число яке необхідно представити в заданому вигляді
    :return: s: ступінь двійки у розкладі
    :return: t: непарне число
    """
    s = 0
    while not n % 2:
        n /= 2
        s += 1
    return s, n


def check(a, s, t, n):
    """
    Функція перевірки окремого свідка простоти

    :param a: випадкове число
    :param s: степень двійки у розкладі даного числа числа
    :param t: непарне число у розкладі
    :param n: число яке перевіряється на простоту
    :return:
    """
    x = pow(a, t, n)
    if x == 1:
        return True
    for i in range(s - 1):
        if x == n - 1:
            return True
        x = pow(x, 2, n)
    return x == n - 1


def millerRabin(n, k=50):
    """
    Головна функція перевірки на простоту

    :param n: число яке необхідно перевірити
    :param k: кількість тестів імовірність помилки 4**(-k)
    :return: True - імовірно просте, False - складене
    """
    if n in [2, 3]:
        return True
    if not n & 1:
        return False
    s, t = prepare(n-1)
    for i in range(k):
        a = random.randrange(2, n-1)
        if not check(a, s, int(t), n):
            return False
    return True


if __name__ == '__main__':
    # test
    for j in range(2, 200):
        t = random.randint(2, 10000)
        print(f'n = {t}, Простота: {millerRabin(t)}')
