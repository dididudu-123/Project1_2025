from gpiozero import LED, Button
from time import sleep
from random import uniform

left_name = input('left player name is ')
right_name = input('right player name is ')
led = LED(4)

right_button = Button(15)
left_button = Button(14)

left_score = 0
right_score = 0

def pressed(button):
    global left_score, right_score
    if button.pin.number == 14:
        print(left_name + ' won the game')
        left_score += 1
    else:
        print(right_name + ' won the game')
        right_score += 1
    print(f"{left_name}'s score: {left_score}, {right_name}'s score: {right_score}")

right_button.when_pressed = pressed
left_button.when_pressed = pressed
while True:
    sleep(uniform(5, 10))
    led.on()
    sleep(10)
    led.off()
    
