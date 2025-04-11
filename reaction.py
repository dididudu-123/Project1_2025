from gpiozero import LED, Button
from time import sleep, time
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is ')
right_name = input('right player name is ')
left_score = 0
right_score = 0

while True:
    led.on()
    sleep(uniform(5, 10))
    start_time = time()
    led.off()

    def pressed(button):
        global left_score, right_score
        end_time = time()
        elapsed_time = end_time - start_time
        if button.pin.number ==14:
            left_score += 1
            print(f"{left_name} won the game in {elapsed_time:.2f} seconds")
        else:
            right_score += 1
            print(f"{right_name} won the game in {elapsed_time:.2f} seconds")
        print(f"{left_name}'s total score: {left_score}")
        print(f"{right_name}'s total score: {right_score}")

    right_button.when_pressed = pressed
    left_button.when_pressed = pressed
