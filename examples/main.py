"""
This implementation does its best to follow the Robert Martin's Clean code guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

import _thread
from time import sleep
from driver.yl69 import YL69Driver

def loop(driver):
    while True:
        reading = driver.read()
        print('{"yl69": %f}' % (reading))
        sleep(2)

def main():
    pin = 32
    driver = YL69Driver().build_pin(pin)
    args = (driver,)
    _thread.start_new_thread(loop, args)

main()