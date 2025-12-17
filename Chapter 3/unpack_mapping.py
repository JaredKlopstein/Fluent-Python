def dump(**kwargs):
    return kwargs

print(dump(**{'x': 1}, y=2, **{'z': 3}))