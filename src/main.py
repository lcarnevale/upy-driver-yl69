"""
This implementation does its best to follow the Robert Martin's Clean code guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

from time import sleep
from machine import Pin
from machine import ADC

pin = Pin(32)
adc = ADC(pin)
adc.atten(ADC.ATTN_11DB)

def normalize(adc_reading, adc_max=4095):
    """Normalize (percentage)

    ADC reads a value in the range [0,4095] across 
    voltage range [0.0v,1.0v].

    Args:
        adc_reading: value read from ADC pin
        adc_max: maximum value allowed by ADC

    Returns:
        A normalized (percentage) value of ADC
    """
    return (100 * adc_reading) / adc_max

while True:
    adc_reading = adc.read()
    adc_normalized = normalize(adc_reading)
    print('{soil_moisture: %d%%}' % (adc_normalized))
    sleep(2)