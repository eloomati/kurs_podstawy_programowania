def get_data(first, last):
    full = first + " " + last
    return full.title()
def get_data_2(first, last, occupation):
    full = first + " " + last + ", " + occupation
    return full.title()

def get_data_3(first, last, occupation=""):
    if occupation:
        full = first + " " + last + ", " + occupation
    else:
        full = first + " " + last
    return full.title()