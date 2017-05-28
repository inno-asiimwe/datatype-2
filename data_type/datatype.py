def data_type(given):
    if type(given) is str:
        return len(given)
    elif given == None:
        return 'no value'
    elif type(given) is bool:
        return given
    elif type(given) is int:
        return compare_to_100(given)
    elif type(given) is list:
        return_third_item(given)
    else:
        return 'type not catered for!'
def compare_to_100(value):
    if value < 100:
        return 'less than 100'
    elif value == 100:
        return 'equal to 100'
    else:
        return 'more than 100'
