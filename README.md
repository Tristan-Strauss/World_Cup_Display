# World Cup Display

---

## Required Equipment

1. GPIO jumper cables
2. Raspberry Pi 4 B+ 8GB Ram (hereby refered to as RPI4)
3. Raspberry Pi Zero 2 W (hereby refered to as RPI_Zero)

## Features

1. Listens for input from keypad
2. Receives year input and loads mp4 file
3. Play mp4 file and trigger GPIO pins for relay for LED for associated ball

## Install

### RPI Setup

Take note of the following pinout on the raspberry pis
![image](./RPI_Pinout.png)

RPI4 pin 8 (GPIO 14 TXD) -> RPI_Zero pin 10 (GPIO 15 RXD)
RPI4 pin 10 (GPIO 15 RXD) -> RPI_Zero pin 8 (GPIO 14 TXD)
