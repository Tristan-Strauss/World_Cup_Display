from pynput import keyboard


year = ""
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
valid_year_list = ["1930","1934","1938","1942","1946","1950","1954","1958","1962","1966","1970","1974","1978","1982","1986","1990","1994","1998","2002","2006","2010","2014","2018","2022","2026","2030","2034","2038","2042","2046","2050","2054","2058","2062","2066","2070","2074","2078","2082","2086","2090","2094","2098","2102","2106","2110","2114","2118","2122","2126","2130","2134",]


def on_press(key):
    global year
    try:
        add_number_to_year(key=key)
    except:
        pass


def on_release(key):
    if key == keyboard.Key.esc:
        return False


# This makes sure that the year is only ever 4 digits long
def add_number_to_year(key):
    if key.char not in numbers_list:
        return
    global year
    if len(year) == 4:
        year = f"{year[1:]}{key.char}"
    else:
        year = f"{year}{key.char}"
    # print(f"Year: {year}")
    handle_year_check()


def handle_year_check():
    global year
    if len(year) > 4:
        return
    if year in valid_year_list:
        print(f"Valid year input: {year}")


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
