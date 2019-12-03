def rgbMixer(color1, color2):
    color1 = color1.lower()
    color2 = color2.lower()
    colorProduct = ""
    
    if color1 == "red":
        if color2 == "red":
            colorProduct = "red"
        elif color2 == "blue":
            colorProduct = "purple"
        elif color2 == "yellow":
            colorProduct = "orange"
            
    elif color1 == "blue":
        if color2 == "red":
            colorProduct = "purple"
        elif color2 == "blue":
            colorProduct = "blue"
        elif color2 == "yellow":
            colorProduct = "green"
        
    elif color1 == "yellow":
        if color2 == "red":
            colorProduct = "orange"
        elif color2 == "blue":
            colorProduct = "green"
        elif color2 == "yellow":
            colorProduct = "yellow"

    return colorProduct

print()
print("Let's mix some colors!")
print("**Red, Blue, or Yellow only**")
print()

color1 = input("What first color to mix? ")
color2 = input("What's the other color? ")
product = rgbMixer(color1, color2)
print()

print(color1.upper()," and ", color2.upper(), " makes ", product.upper(), "!",sep="")
