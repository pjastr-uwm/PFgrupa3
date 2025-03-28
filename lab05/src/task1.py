from unittest.mock import Mock

m1 = Mock(name="First mock")
m1.get_data.return_value = 42

print(m1.get_data(89))
print(m1.get_data("XYZ"))
print(m1.get_data("user"))

m1.get_data.assert_called_with("user")
print(m1.get_data.call_args)
print(m1.get_data.call_args_list)
