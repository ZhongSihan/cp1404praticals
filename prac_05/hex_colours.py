HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

def main():
    print("Hex Colour Lookup")
    while True:
        colour_name = input("Enter colour name: ").strip().lower()
        if colour_name == "":
            break
        hex_code = HEX_COLOURS.get(colour_name)
        if hex_code:
            print(f"{colour_name.title()} is {hex_code}")
        else:
            print("Invalid colour name")

main()
