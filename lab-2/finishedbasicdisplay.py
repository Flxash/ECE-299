from machine import Pin, SPI, Timer # SPI is a class associated with the machine library. 
import utime

# The below specified libraries have to be included. Also, ssd1306.py must be saved on the Pico. 
from ssd1306 import SSD1306_SPI # this is the driver library and the corresponding class
import framebuf # this is another library for the display. 


# Define columns and rows of the oled display. These numbers are the standard values. 
SCREEN_WIDTH = 128 #number of columns
SCREEN_HEIGHT = 64 #number of rows


# Initialize I/O pins associated with the oled display SPI interface

spi_sck = Pin(18) # sck stands for serial clock; always be connected to SPI SCK pin of the Pico
spi_sda = Pin(19) # sda stands for serial data;  always be connected to SPI TX pin of the Pico; this is the MOSI
spi_res = Pin(21) # res stands for reset; to be connected to a free GPIO pin
spi_dc  = Pin(20) # dc stands for data/command; to be connected to a free GPIO pin
spi_cs  = Pin(17) # chip select; to be connected to the SPI chip select of the Pico 

button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

#
# SPI Device ID can be 0 or 1. It must match the wiring. 
#
SPI_DEVICE = 0 # Because the peripheral is connected to SPI 0 hardware lines of the Pico

#
# initialize the SPI interface for the OLED display
#
oled_spi = SPI( SPI_DEVICE, baudrate= 100000, sck= spi_sck, mosi= spi_sda )

#
# Initialize the display
#
oled = SSD1306_SPI( SCREEN_WIDTH, SCREEN_HEIGHT, oled_spi, spi_dc, spi_res, spi_cs, True )

Count = 0

def increment_count():
    global Count
    Count += 1

debounce_delay = 100
timer = Timer()
state = 0

def debounce_func(timer):
    global state
    if button.value() == 0 and state == 0:
        state = 1
        increment_count()
    if button.value() == 1 and state == 1:
        state = 0
        
timer.init(mode = Timer.PERIODIC, period = debounce_delay, callback = debounce_func)

# Assign a value to a variabl

#for i in range(50):
while (True):

#
# Clear the buffer
#
    oled.fill(0)
        
#
# Update the text on the screen
#
    oled.text("Welcome to ECE", 0, 0) # Print the text starting from 0th column and 0th row
    oled.text("299", 45, 10) # Print the number 299 starting at 45th column and 10th row
    oled.text("Count is: %4d" % Count, 0, 30 ) # Print the value stored in the variable Count. 

#
# Draw box below the text
#
    oled.rect( 0, 50, 128, 5, 1  )        

#
# Transfer the buffer to the screen
#
    oled.show()
    
    #if button.value() == 1:
       # Count = Count + 1
        #utime.sleep(100)
        
    #Count = Count + i
    
        