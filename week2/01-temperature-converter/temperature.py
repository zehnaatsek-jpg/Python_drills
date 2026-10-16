def celsius_to_fahrenheit(celsius):
  fahren = round((celsius * 9/5) + 32, 2)
  return fahren


def fahrenheit_to_celsius(fahrenheit):
  cels = round((fahrenheit - 32) * 5/9, 2)
  return cels


def celsius_to_kelvin(celsius):
  kelv = round(celsius + 273.15, 2)
  return kelv


def convert_temperature(value, from_unit, to_unit):
  lowest = {"celsius": -273.15, "fahrenheit": celsius_to_fahrenheit(-273.15), "kelvin": celsius_to_kelvin(-273.15)}
  
  if from_unit == None or to_unit == None:
    raise ValueError("unsupported unit")
  
  from_unit = from_unit.lower()
  to_unit = to_unit.lower()

  if not isinstance(value, (int, float)) or isinstance(value, bool):
    raise ValueError("text is not a number")

  if from_unit in lowest.keys() and value < lowest[from_unit]:
      raise ValueError("below absolute zero")
  elif from_unit not in lowest or to_unit not in lowest:
    raise ValueError("unsupported unit")
  

  if from_unit == "celsius" and to_unit == "fahrenheit":
    return celsius_to_fahrenheit(value)
  elif from_unit == "celsius" and to_unit == "kelvin":
    return celsius_to_kelvin(value)
  elif from_unit == "fahrenheit" and to_unit == "kelvin":
    cels = fahrenheit_to_celsius(value)
    return celsius_to_kelvin(cels)
  elif from_unit == "fahrenheit" and to_unit == "celsius":
    return fahrenheit_to_celsius(value)
  elif from_unit == "kelvin" and to_unit == "celsius":
    return value - 273.15
  elif from_unit == "kelvin" and to_unit == "fahrenheit":
    cel = value - 273.15
    return celsius_to_fahrenheit(cel)
  return value
print(convert_temperature(-40, "kelvin", "fahrenheit"))