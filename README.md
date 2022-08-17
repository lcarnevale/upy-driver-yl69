# Resistive Soil Moisture Driver in MicroPython
This project contains a MicroPython driver for the resistive soil moisture sensor (YL-69 or HL-69), which measures the volumetric water content in soil, providing in output the voltage value.

The picture below shows the proper operation of the sensor. A lower output voltage is the result of sensing a wet soil, whereas a higher output voltage is the result of sensing a dry soil.

![Image of Yaktocat](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2016/07/soil-moisture-sensor-e1467578282801.png?resize=895%2C487&quality=100&strip=all&ssl=1)

 
## Before to start
Resolve the project dependecies by using the collected requirements.
```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements
```

Install *picocom*, a minimal dumb-terminal emulation program that is great for accessing a serial port based Linux console.
```bash
$ sudo apt-get install picocom
```

Plug the device to your PC and flash a clean micropython firmware. I am using an ESP-WROOM-32. After plugging the device, it typically appears on /dev/ttyUSB0. Try another enumeration otherwise, but be sure the USB cable you are using is a data cable (not energy only).
```bash
$ esptool.py --port /dev/ttyUSB0 erase_flash
$ esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 /PATH/OF/FIRMWARE
```

For more information about how flashing MicroPython on ESP32-based device, see the MicroPython official documentation [here](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html).

## Upload the MicroPython script
Put all files in the board by using the *ampy* tool as follow.
```bash
$ ampy --port /dev/ttyUSB0 put examples/boot.py
$ ampy --port /dev/ttyUSB0 put examples/main.py
$ ampy --port /dev/ttyUSB0 put drivers
```

For more information about how using the *ampy* tool, see the official documentation [here](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/overview).

## Monitor your application
Monitor the application's output by using the *picocom* tool.
```bash
$ picocom -b 115200 -r -l /dev/ttyUSB0
```

To quit *picocom* use CTRL+A CTRL+X.

## Troubleshooting
```bash
sudo chmod 666 /dev/ttyUSB0
```

## Credits
1. [Guide for Soil Moisture Sensor YL-69 or HL-69 with Arduino](https://randomnerdtutorials.com/guide-for-soil-moisture-sensor-yl-69-or-hl-69-with-the-arduino/), Random Nerd Tutorials