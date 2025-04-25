try:
    d=5
    print(d)
    print(a)
except ZeroDivisionError:
    print('error by zero')
except TypeError:
    print('error by type')
except ValueError:
    print('error by value')
except IndexError:
    print('error by index')
except KeyError:
    print('error by key')
except NameError:
    print('error by name')
    