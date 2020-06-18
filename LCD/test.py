import lcddriver
from time import *
 
lcd = lcddriver.lcd()
lcd.lcd_clear()
 
lcd.lcd_display_string("123", 1)
lcd.lcd_display_string("      RaspberryPi.de", 2)
lcd.lcd_display_string("", 3)
lcd.lcd_display_string("HD44780 I2C Tutorial", 4)