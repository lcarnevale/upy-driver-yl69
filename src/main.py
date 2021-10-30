from time import sleep
from machine import Pin
from machine import ADC

pin = Pin(32)
adc = ADC(pin)
adc.atten(ADC.ATTN_11DB)

while True:
    adc_reading = adc.read()
    print('{soil_moisture: %d}' % (adc_reading))
    sleep(2)