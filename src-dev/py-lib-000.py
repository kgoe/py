modulename = __name__
modulefilename = __file__


def fn_test_function():
    return true


def fn_test_basic_types():
    var1 = "this is a string"              # <type 'str'>
    var2 = 1024                            # <type 'int'>
    var3 = 2.56                            # <type 'float'>
    var4 = 3.14j                           # <type 'complex'>
    var10 = [1,2,3]                        # <type 'list'>
    var11 = {1,2,3}                        # <type 'set'>
    var12 = (1,2,3)                        # <type 'tuple'>
    var20 = {'a': 'a', 'b': 'b', 'c': 'c'} # <type 'dict'>
    var30 = fn_test_function  # <type 'function'>

    output = [var1,var2,var3,var4,var10,var11,var12,var20, var30]

    output.append(int('1000',16))          # <type 'int'>
    # output.append(long('1000',100))
    output.append(float(1000))             # <type 'float'>
    output.append(complex(1000,100))       # <type 'complex'>
    output.append(str(100))                # <type 'str'>
    output.append(repr(100))               # <type 'str'>
    output.append(eval('var1'))            # <type 'str'>
    output.append(tuple('123'))            # <type 'tuple'>
    output.append(list('123'))             # <type 'list'>
    output.append(set('123'))              # <type 'set'>
    # output.append(dict(('a','a')))
    # frozenset()
    # ord()
    # hex()
    # oct()
    return output
    pass


def fn_start():
    inputs = fn_test_basic_types()
    for input in inputs:
        print([input, type(input)])
    pass


if modulename == '__main__':
    fn_start()