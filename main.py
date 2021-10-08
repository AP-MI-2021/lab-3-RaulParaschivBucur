# 9)
def has_only_odd_nr(lst):
    """
    Verifica daca o lista are doar numere impare
    """
    for elem in lst:
        if elem % 2 == 0:
            return False
    return True


def get_longest_product_is_odd(lst: list[int]) -> list[int]:
    """
    Input: O lista
    Output: Cea mai lunga secventa in care produsul tuturor numerelor este impar
            (Aceasta lista poate contine doar nr impare pt. ca doar produsul de nr
             impare este un nr impar)
    """
    result_lst = []
    maxim = 0
    for pos1 in range(0, len(lst)):
        for pos2 in range(pos1, len(lst)):
            if has_only_odd_nr(lst[pos1: pos2 + 1]):
                if len(lst[pos1: pos2 + 1]) >= maxim:
                    maxim = len(lst[pos1: pos2 + 1])
                    result_lst = lst[pos1: pos2 + 1]
    return result_lst


def test_get_longest_product_is_odd():
    assert get_longest_product_is_odd([1, 2, 3, 5, 9, 2, 4, 7, 9, 2, 9, 7, 3, 6, 6, 2, 1]) == [9, 7, 3]
    assert get_longest_product_is_odd([1, 2, 5]) == [5]
    assert get_longest_product_is_odd([]) == []
    assert get_longest_product_is_odd([1]) == [1]


# 19)
def concat_is_ascending(lst):
    """
    Verifica daca o lista are concatenarea elementelor cu cifrele in ordine crescatoare
    """
    concat = ''
    for idx in lst:
        concat += str(idx)

    for idx in range(0, len(concat) - 1):
        if concat[idx] > concat[idx + 1]:
            return False
    return True


def get_longest_concat_digits_asc(lst: list[int]) -> list[int]:
    """
    Input: O lista
    Output: Cea mai lunga secventa in care concatenarea elementelor are cifrele crescatoare
    """
    result_lst = []
    maxim = 0
    for pos1 in range(0, len(lst)):
        for pos2 in range(pos1, len(lst)):
            if concat_is_ascending(lst[pos1:pos2 + 1]):
                if len(lst[pos1:pos2 + 1]) >= maxim:
                    maxim = len(lst[pos1:pos2 + 1])
                    result_lst = lst[pos1:pos2 + 1]
    return result_lst


def test_get_longest_concat_digits_asc():
    assert get_longest_concat_digits_asc([1, 2, 3, 4, 2, 1, 3, 7]) == [1, 2, 3, 4]
    assert get_longest_concat_digits_asc([]) == []
    assert get_longest_concat_digits_asc([1]) == [1]
    assert get_longest_concat_digits_asc([12, 3, 2, 1, 1, 23, 4, 9, 1, 2, 1]) == [1, 1, 23, 4, 9]


def read_list() -> list[int]:
    size = int(input('Alege dimensiunea listei: '))
    lst = []
    while size:
        elem = int(input('Adauga element: '))
        lst.append(elem)
        size -= 1
    return lst


def main():
    lst = []
    while True:
        print(" ")
        print("1. Citire lista")
        print("2. Det. cea mai lunga subsecv. in care produsul numerelor este impar")
        print("3. Det. cea mai lunga subsecv. in care concat. elementelor are cifrele în ordine cresc")
        print("4. Iesire")
        optiune = int(input('Alege o optiune: '))
        if optiune == 1:
            lst = read_list()
            print('Lista introdusa: ', lst)
        elif optiune == 2:
            if lst == []:
                print('Nu ai introdus inca lista')
            else:
                print('Cea mai lunga subsecv cu produsul elementelor impar este:', get_longest_product_is_odd(lst))
        elif optiune == 3:
            if lst == []:
                print('Nu ai introdus inca lista')
            else:
                print('Cea mai lunga subsecv in care concat elementelor are cif în ord cresc este:', get_longest_concat_digits_asc(lst))
        elif optiune == 4:
            break


test_get_longest_product_is_odd()
test_get_longest_concat_digits_asc()
main()
