# def dispathch_if(operator, x, y):
#     if operator=='add':
#         return x + y
#     elif operator=='sub':
#         return x - y
#     elif operator=='mul':
#         return x * y
#     elif operator=='div':
#         return x / y
#     else:
#         return None
#
#
# print(dispathch_if("add", 100, 300))


def dispath_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


print(dispath_dict('add', 20, 60))
