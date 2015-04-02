def farh_to_kelvin(temp):
    return (temp - 32) * 5.0/9.0 + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

def farh_to_celsius (temp):
    temp_k = farh_to_kelvin (temp)
    result = kelvin_to_celsius (temp_k)
    return (result)
