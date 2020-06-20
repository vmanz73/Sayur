import lcddriver
from time import *
 
lcd = lcddriver.lcd()
lcd.lcd_clear()
 
lcd.lcd_display_string("Berat : 7 g", 1)
lcd.lcd_display_string("Jenis Sayur : Tomat", 2)
lcd.lcd_display_string("Harga/kg : Rp.6000 ", 3)
lcd.lcd_display_string("Total harga : Rp.42000", 4)