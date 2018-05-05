from microbit import *

div_1_x = 0
div_1_y = 0

div_2_x = 0
div_2_y = 3

div_3_x = 3
div_3_y = 0

div_4_x = 3
div_4_y = 3

while True:
  base_x = 0
  base_y = 0

  #-------------------
  # I want to detect under operation.
  # Which check is best?
  # 1) Click
  # 2) Press
  # 3) Hit button repeatedly
  # 4) Press A + B 
  #-------------------

  #-------------------
  # "is_pressed"
  #-------------------
  base_x = div_1_x
  base_y = div_1_y

  if button_a.is_pressed() == True:
    display.set_pixel(base_x, base_y, 7)
    display.set_pixel(base_x, base_y+1, 0)
  else:
    display.set_pixel(base_x, base_y, 0)
    display.set_pixel(base_x, base_y+1, 7)

  #-------------------
  # "was_pressed"
  #-------------------
  base_x = div_2_x
  base_y = div_2_y

  if button_a.was_pressed() == True:
    display.set_pixel(base_x, base_y, 7)
    display.set_pixel(base_x, base_y+1, 0)
  else:
    display.set_pixel(base_x, base_y, 0)
    display.set_pixel(base_x, base_y+1, 7)

  #-------------------
  # "get_presses"
  #-------------------
  base_x = div_3_x
  base_y = div_3_y

  if button_a.get_presses() > 0:
    display.set_pixel(base_x, base_y, 7)
    display.set_pixel(base_x, base_y+1, 0)
  else:
    display.set_pixel(base_x, base_y, 0)
    display.set_pixel(base_x, base_y+1, 7)

  #-------------------
  # "is_pressed" (A + B)
  #-------------------
  base_x = div_4_x
  base_y = div_4_y

  if button_a.is_pressed() == True and button_b.is_pressed() == True:
    display.set_pixel(base_x, base_y, 7)
    display.set_pixel(base_x, base_y+1, 0)
  else:
    display.set_pixel(base_x, base_y, 0)
    display.set_pixel(base_x, base_y+1, 7)

  sleep(500)