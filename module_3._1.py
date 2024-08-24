calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


print(calls)


def string_info(string):
    tuple_ = [len(string), string.upper(), string.lower()]
    return tuple_


print(string_info('пылесос'))
print(count_calls())


def is_contains(string, list_to_search):
    string = str(string.upper())
    print(string)
    for i in range(len(list_to_search)):
        list_to_search[i] = str(list_to_search[i].upper())
        print(list_to_search)
    if string in list_to_search:
        return True
    else:
        return  False


print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(count_calls())
print(is_contains('cycle', ['recycling', 'cyclic']))
print(count_calls())
