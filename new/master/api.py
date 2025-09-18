from flask import Flask
import console
import gpio
import time

app = Flask(__name__)

@app.route("/test")
def test():
    console.send_command("test")
    time.sleep(1)
    gpio.set_pin_high(31)
    time.sleep(1)
    gpio.set_pin_low(31)
    return 200

@app.route("/year/<year>/on")
def handle_year_on(year):
    if not gpio.check_if_year_valid(year=year):
        return "Invalid year", 400
    if gpio.check_if_year_local(year=year):
        pin = gpio.get_pin_from_master_year_dict(year=year)
        gpio.set_pin_high(pin=pin)
        return "OK", 200
    else:
        pin = gpio.get_pin_from_slave_year_dict(year=year)
        console.send_command(f"{pin}-HIGH")
        return "OK", 200

@app.route("/year/<year>/off")
def handle_year_off(year):
    if not gpio.check_if_year_valid(year=year):
        return "Invalid year", 400
    if gpio.check_if_year_local(year=year):
        pin = gpio.get_pin_from_master_year_dict(year=year)
        return "OK", 200
    else:
        pin = gpio.get_pin_from_slave_year_dict(year=year)
        console.send_command(f"{pin}-LOW")
        return "OK", 200

app.run(host="0.0.0.0", port=5000)