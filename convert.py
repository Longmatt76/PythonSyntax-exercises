def convert_temp(unit_in, unit_out, temp):
    if unit_in == "f":
        return (temp - 32) * .5556 
    elif unit_in == "c":
        return temp * 1.8 + 32
    else:
        return "invalid input"
