def data_type(given):
    if type(given) is str:
        return len(given)
    elif given == None:
        return 'no value'
    elif type(given) is bool:
        return given
    elif type(given) is int:
        compare_to_100(given)
    elif type(given) is list:
        return_third_item(given)
    else:
        return 'type not catered for!'
