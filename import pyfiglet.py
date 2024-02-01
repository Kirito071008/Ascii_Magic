import pyfiglet,platform,os,time
#from PrivateCoder import var
from ascii_magic import AsciiArt
val = "off"
val1 = "none"
if platform.system() == "Windows":
    def clear(): os.system("cls")
else:
    def clear(): os.system("clear")
def menu(val,val1):
    clear()
    ascii_banner = pyfiglet.figlet_format("Kirito's art")
    print(ascii_banner)
    print("Welcome! What do you want to do?")
    x = input("1)Ascii art from a path 2)Ascii art from a link 3)From a text input 4)Options: ")
    if x == "1":
        path()
    elif x == "2":
        link()
    elif x == "3":
        ai()
    elif x == "4":
        while True:
            x = input(f"Monochrome: {val}\nChar: {val1}\n").lower()
            if x == "set monochrome on":
                val = "on"
            elif x == "set char":
                x = input("Chose an ASCII glyphs: ")
                val1 = x
            elif x == "set monochrome off":
                val = "off"
            elif x == "set char none":
                val1 = "none"
            elif x == "e":
                menu(val,val1)
    else:
        menu(val,val1)
def path():
    x = input("Path: ")
    my_art = AsciiArt.from_image(r""+x.strip('"'))
    my_art.to_terminal()
    z = input("Do you want to save this?(Y/n)").lower()
    if z == "y":
        my_art.to_file('save.txt', monochrome=True)
        print("Image saved! You can find it at users\yourname as save.txt")
    y = input("Continue?(Y/n)\t").lower()
    if y == "y":
        menu(val,val1)
    else:
        exit()
def link():
    x = input("Link: ")
    try:
        my_art = AsciiArt.from_url(x)
    except OSError as e:
        print(f'Could not load the image, server said: {e.code} {e.msg}')
    my_art.to_terminal(char="#")
    z = input("Do you want to save this?(Y/n)").lower()
    if z == "y":
        my_art.to_file('save.txt', monochrome=True)
        print("Image saved! You can find it at users\yourname as save.txt")
    y = input("Continue?(Y/n)\t").lower()
    if y == "y":
        menu(val,val1)
    else:
        exit()
def ai():
    print("Working on...")
    time.sleep(4)
    menu(val,val1)
    x = input("Input: ")
    api_key = var
    my_art = AsciiArt.from_dalle(x, api_key)
    my_art.to_html_file('cow_dalle.html', columns=200)
    y = input("Continue?(Y/n)\t").lower()
    if y == "y":
        menu(val,val1)
    else:
        exit()
menu(val,val1)