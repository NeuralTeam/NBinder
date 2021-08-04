from time import sleep
import keyboard as kbd
print("NBinder for Asyakoshka")
print("   By NeuralTeam")
sleep(3)
binds = ["4","5","6","7","8","9","0","u","i","o","p","g","h","j","k","l","m","n"]
while True:
    for bind in binds:
        kbd.press_and_release(bind)
        sleep(0.35)