def age_assignment(*args, **kwargs):
    result = {name: val for key, val in kwargs.items() for name in args if key in name}
    # for name in args:
    #     for key, val in kwargs.items():
    #         if key in name:
    #             result.update({name: val})

    return result

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
