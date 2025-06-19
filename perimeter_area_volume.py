from math import pi
from math import sqrt

def perimeter_area_volume(parameter, shape, dimensions):

	if parameter == "perimeter":

		if shape == "triangle":

			side1 = dimensions["side1"]
			side2 = dimensions["side2"]
			side3 = dimensions["side3"]
			result = side1 + side2 + side3

		elif shape == "circle":

			radius = dimensions["radius"]
			result = 2 * (pi * radius)

		elif shape == "rectangle":

			length = dimensions["length"]
			width = dimensions["width"]
			result = 2 * (length + width)

		elif shape == "square":

			length = dimensions["length"]
			result = 4 * length

	elif parameter == "area" or parameter == "surface area":

		if shape == "triangle":

			base = dimensions["base"]
			height = dimensions["height"]
			result = 0.5 * base * height

		elif shape == "circle":

			radius = dimensions["radius"]
			result = pi * (radius**2)

		elif shape == "rectangle":

			length = dimensions["length"]
			width = dimensions["width"]
			result = length * width

		elif shape == "square":

			length = dimensions["length"]
			result = length**2

		elif shape == "pyramid":

			base = dimensions["base"]
			height = dimensions["height"]
			result = (base**2) + (2 * base) * (sqrt((base / 2)**2 + height**2))

		elif shape == "cone":

			radius = dimensions["radius"]
			length = dimensions["length"]
			result = pi * radius * (radius + length)

		elif shape == "sphere":

			radius = dimensions["radius"]
			result = 4 * pi * (radius)**2

		elif shape == "rectangular prism":

			length = dimensions["length"]
			width = dimensions["width"]
			height = dimensions["height"]
			result = 2 * ((length * width) + (length * height) + (width * height))

		elif shape == "cube":

			length = dimensions["length"]
			result = 6 * (length**2)

		elif shape == "cylinder":

			radius = dimensions["radius"]
			height = dimensions["height"]
			result = 2 * pi * radius * (height + radius)

	elif parameter == "volume":

		if shape == "pyramid":

			base = dimensions["base"]
			height = dimensions["height"]
			result = (1/3) * (base**2) * (height)

		elif shape == "cone":

			radius = dimensions["radius"]
			height = dimensions["height"]
			result = (1/3) * pi * (radius**2) * height

		elif shape == "sphere":

			radius = dimensions["radius"]
			result = (4/3) * pi * (radius**3)

		elif shape == "rectangular prism":

			length = dimensions["length"]
			width = dimensions["width"]
			height = dimensions["height"]
			result = length * width * height

		elif shape == "cube":

			length = dimensions["length"]
			result = length**3

		elif shape == "cylinder":

			radius = dimensions["radius"]
			height = dimensions["height"]
			result = pi * (radius**2) * height

	return result

shape = "cone"
parameter = "volume"
dimensions = { "height": 5, "radius": 6 }
answer = perimeter_area_volume(parameter, shape, dimensions)
print(f"{parameter} = {answer}")