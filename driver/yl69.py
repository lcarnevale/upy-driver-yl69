"""
This implementation does its best to follow the Robert Martin's Clean code guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__author__ = "Lorenzo Carnevale <lcarnevale@unime.it>"
__license__ = "MIT License"
__description__ = "YL-69 MicroPython driver"

from machine import Pin
from machine import ADC

class YL69Driver(object):
    """Driver class to use the resistive soil moisture sensor.

    This is compatible with the YL-69 and HL-69 resistive soil
    moisture sensors.

    Args
        __instance(YL69Driver): private instance of the class
        __adc(ADC): Analog Digital Converter object
    """
    __instance = None
    
    def __new__(self) -> __instance:
        """Implement class object.
        
        Returns
            (YL69Driver) instance of the class
        """
        self.__instance = super(YL69Driver, self).__new__(self)
        return self.__instance

    def build_pin(self, pin_number) -> __instance:
        """Build the pin variable.

        Args:
            pin_number(int): custom pin number

        Returns
            (YL69Driver) instance of the class
        """
        pin = Pin(pin_number)
        self.__adc = ADC(pin)
        self.__adc.atten(ADC.ATTN_11DB)
        return self.__instance


    def read(self, normalize=True) -> float:
        """Read the ADC value of the selected pin.

        Args:
            normalize(bool): True to normalize (default), False otherwise
        
        Returns:
            (float) processed or not processed ADC reading 
        """
        adc_reading = self.__adc.read()
        if normalize:
            adc_reading = self.__normalize(adc_reading)
        return adc_reading

    def __normalize(self, adc_reading, adc_max=4095) -> float:
        """Normalize (percentage)

        ADC reads a value in the range [0,4095] across 
        voltage range [0.0v,1.0v].

        Args:
            adc_reading(float): value read from ADC pin
            adc_max(int): maximum value allowed by ADC (default is 4095)

        Returns:
            (float) a normalized value of ADC in percent
        """
        return (100 * adc_reading) / adc_max