def validate_email(arg):
    if not isinstance(arg, str):
        raise TypeError

    return arg.find("@") >= 0
