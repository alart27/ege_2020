def match(string, mask : str) -> bool:
    """ Определить совпадение строки <string> с win-like маской <mask> со спецсимволами:
    ? - любая одна буква
    * - 0 или больше любых букв
    остальные символы воспринимаются  буквально
    """
    def _match(si, mi : int) -> bool:
        """Внутренняя рекурсивная функция
        si : string index
        mi : mask index
        """
        if si < len(string):
            s = string[si]
        elif si == len(string):
            s = None  # признак конца строки
        else:
            return False  # guard

        if mi < len(mask):
            m = mask[mi]
        elif mi == len(mask):
            m = None
        else:
            return False

        if m == None:
            return s == None
        elif m == '?':
            return _match(si + 1, mi + 1)
        elif m == '*':
            return (
                _match(si, mi + 1) or  # пустой символ
                _match(si + 1, mi) or  # съели символ маской
                _match(si + 1, mi + 1) # захватили один символ
            )
        else: # любой не-спецсимвол
            if s != m:
                return False
            else:
                return _match(si + 1, mi + 1)
    return _match(0, 0)


def test():
    data = [
        (('abc' , 'abc')  , True) ,
        (('abc' , 'ab?')  , True) ,
        (('abc' , '???')  , True) ,
        (('abc' , '*')    , True) ,
        (('abc' , 'abc*') , True) ,
        (('abc' , 'ab*?') , True) ,

        (('abc' , 'ab')    , False) ,
        (('ab'  , 'abc')   , False) ,
        (('abc' , 'abc*d') , False) ,
        (('abc' , '*b')    , False) ,
        (('abc' , 'abc*?') , False) ,

    ]

    for (string, mask), expected_answer in data:
        ans = match(string, mask)
        print(
            string, mask, ans,
            'OK' if ans == expected_answer else 'FAIL',
            sep='\t',
        )

if __name__ == '__main__':
    test()
