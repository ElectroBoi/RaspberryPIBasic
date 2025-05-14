import gpiozero  # We are using GPIO pins
 
button = gpiozero.Button(17) # GPIO17 connects to button 
 
while True:
  if .is_pressed:
    print("Button is pressed!")
  else:
    print("Button is not pressed!")
    