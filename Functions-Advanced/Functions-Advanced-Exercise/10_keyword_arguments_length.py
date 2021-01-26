def kwargs_length(**kwargs):
    result = len(kwargs)
    return result


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
