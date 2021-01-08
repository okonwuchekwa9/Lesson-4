def celsius_to_fahr(temp):
    """Converts Celsius temperatures to Fahrenehit."""
    return 9/5 * temp + 32

def kelvins_to_celsius(temp_kelvins=0):
    return temp_kelvins - 273.15

def kelvins_to_fahr(temp_kelvins):
    temp_celsius = kelvins_to_celsius(temp_kelvins)
    temp_fahr = celsius_to_fahr(temp_celsius)
    return temp_fahr