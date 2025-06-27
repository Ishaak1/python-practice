from math import pi, sqrt

def shapes_calculator(dimensions):

	result = 0

	if shape == "triangle":

		if parameter == "perimeter":

			side1 = dimensions["side1"]
			side2 = dimensions["side2"]
			side3 = dimensions["side3"]
			result = side1 + side2 + side3

		elif parameter == "area":
			
			base = dimensions["base"]
			height = dimensions["height"]
			result = 0.5 * base * height

	elif shape == "circle":

		if parameter == "perimeter":

			radius = dimensions["radius"]
			result = 2 * (pi * radius)

		elif parameter == "area":
			
			radius = dimensions["radius"]
			result = pi * (radius**2)

	elif shape == "rectangle":

		if parameter == "perimeter":

			lenght = dimensions["length"]
			width = dimensions["width"]
			result = 2 * (length + width)

		elif parameter == "area":

			lenght = dimensions["length"]
			width = dimensions["width"]			
			result = length * width

	elif shape == "square":

		if parameter == "perimeter":

			side = dimensions["side"]
			result = 4 * side

		elif parameter == "area":

			side = dimensions["side"]
			result = side**2

	elif shape == "pyramid":

		if parameter == "surface area":

			base = dimensions["base"]
			height = dimensions["height"]
			result = (base**2) + (2 * base) * sqrt((base/2))**2 + (height**2)

		elif parameter == "volume":

			base = dimensions["base"]
			height = dimensions["height"]
			result = (1/3) * (base**2) * height

	elif shape == "cone":

		if parameter == "surface area":

			radius = dimensions["radius"]
			length = dimensions["length"]
			result = pi * radius * (radius + length)

		elif parameter == "volume":

			radius = dimensions["radius"]
			height = dimensions["height"]
			result = (1/3) * pi * (radius**2) * height

	elif shape == "sphere":

		if parameter == "surface area":

			radius = dimensions["radius"]
			result = 4 * (pi) * (radius**2)

		elif parameter == "volume":

			radius = dimensions["radius"]
			result = (4/3) * pi * (radius**3)

	elif shape == "rectangular prism":

		if parameter == "surface area":

			length = dimensions["length"]
			width = dimensions["width"]
			height = dimensions["height"]
			result = 2 * ((length * width) + (length * height) + (width * height))

		elif parameter == "volume":
			
			length = dimensions["length"]
			width = dimensions["width"]
			height = dimensions["height"]
			result = lenght * width * height

	elif shape == "cube":

		if parameter == "surface area":

			side = dimensions["side"]
			result = 6 * (side**2)

		elif parameter == "volume":

			side = dimensions["side"]
			result = side**3

	elif shape == "cylinder":

		if parameter == "surface area":

			radius = dimensions["radius"]
			height = dimensions["height"]
			result = 2 * pi * radius * (height + radius)

		elif parameter == "volume":

			radius = dimensions["radius"]
			height = dimensions["height"]
			result = pi * (radius**2) * height

	return result

shape = "cylinder"
parameter = "volume"
dimensions = { "radius": 3, "height": 2 }
calculate_shape = shapes_calculator(dimensions)
print(f"{parameter} = {calculate_shape}")
