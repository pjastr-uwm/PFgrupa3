from unittest.mock import Mock

m2 = Mock(autospec=True)

m2.get_data.side_effect = [89, True, "mmm"]

print(m2.get_data(44))
print(m2.get_data(False, 33))
print(m2.get_data())


def modify(*args):
    return [elem * 2 for elem in args]


m2.get_data.side_effect = modify

print(m2.get_data(-9,0,3,-5))

m2.get_data.side_effect = TypeError("Wrong type")

try:
    print(m2.get_data())
except TypeError as err:
    print("Error", err)