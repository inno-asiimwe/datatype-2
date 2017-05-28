def data_type(given):
    """Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function
    Implemented by Asiimwe Innocent
    Assignment from Andela labs for bootcamp """
    if type(given) is str:
        return len(given)
    elif given == None:
        return 'no value'
    elif type(given) is bool:
        return given
    elif type(given) is int:
        return compare_to_100(given)
    elif type(given) is list:
        return return_third_item(given)
    else:
        return 'type not catered for!'

def compare_to_100(value):
    """Method handles how intergers compare to 100"""
    if value < 100:
        return 'less than 100'
    elif value == 100:
        return 'equal to 100'
    else:
        return 'more than 100'

def return_third_item(alist):
    """method returns the third item in a list or None if none exists"""
    if len(alist) >= 3:
        return alist[2]
    else:
        return None
