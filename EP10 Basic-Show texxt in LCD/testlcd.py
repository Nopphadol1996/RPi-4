import lcdlib
import time

lcd=lcdlib.lcd()
while True:
	lcd.lcd_display_string("Hi there",1)
	time.sleep(2)
	lcd.lcd_clear()
	lcd.lcd_display_string("How are you ?",1)
	time.sleep(2)
	lcd.lcd_clear()
	lcd.lcd_display_string("Grate Bye",1)
	time.sleep(2)
	lcd.lcd_clear()
	lcd.backlight(0)
