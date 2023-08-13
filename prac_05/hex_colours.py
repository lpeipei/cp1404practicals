COLORS_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Azure1": "#f0ffff",
    "BabyPink": "#f4c2c2",
    "Beige": "#f5f5dc",
    "BlueBell": "#a2a2d0",
    "Bone": "#e3dac9",
    "BubbleGum": "#ffc1cc",
    "CadetBlue2": "#8ee5ee",
    "CameoPink": "#efbbcc"
}

COLOR_CODES_LOWER = {color.lower(): code for color, code in COLORS_CODES.items()}

color_name = input("Enter a color name: ")
while color_name != "":

    print(f"The code for \"{color_name}\" is {COLOR_CODES_LOWER.get(color_name.lower())}")

    color_name = input("Enter a color name: ")
