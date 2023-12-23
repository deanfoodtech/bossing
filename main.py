import time

import keyboard
import pyautogui

def eat(target_x, target_y, original_x, original_y):
    # Move to the target position
    pyautogui.moveTo(target_x, target_y)

    # Click at the target position
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(1723, 751)
    pyautogui.click()
    # Move back to the original position
    pyautogui.moveTo(original_x, original_y)

def ranged(target_x, target_y, original_x, original_y):
    # Move to the target position
    pyautogui.moveTo(target_x, target_y)
    # Click at the target position
    pyautogui.click()
    time.sleep(0.5)
    # Move back to the original position
    pyautogui.moveTo(original_x, original_y)

def magic(target_x, target_y, original_x, original_y):
    # Move to the target position
    pyautogui.moveTo(target_x, target_y)
    # Click at the target position
    pyautogui.click()
    time.sleep(0.5)
    # Move back to the original position
    pyautogui.moveTo(original_x, original_y)

def melee(target_x, target_y, original_x, original_y):
    # Move to the target position
    pyautogui.moveTo(target_x, target_y)
    # Click at the target position
    pyautogui.click()
    time.sleep(0.5)
    # Move back to the original position
    pyautogui.moveTo(original_x, original_y)

while True:

    # Listen for the 'q' key press
    if keyboard.is_pressed('q'):
        original_position = pyautogui.position()
        target_position1 = (1726, 789)
        # Simulate pressing F1
        keyboard.press_and_release('f1')
        eat(*target_position1, original_position[0], original_position[1])
        print("EAT!")
        # Listen for the 'e' key press
    if keyboard.is_pressed('e'):
        # Simulate pressing F1
        keyboard.press_and_release('f2')
        original_position = pyautogui.position()
        target_position1 = (1748, 866)
        # Simulate pressing F1
        keyboard.press_and_release('f2')
        magic(*target_position1, original_position[0], original_position[1])

        print("protecting from magic!")
    if keyboard.is_pressed('r'):
        # Simulate pressing F1
        original_position = pyautogui.position()
        target_position1 = (1791, 864)
        # Simulate pressing F1
        keyboard.press_and_release('f2')
        ranged(*target_position1, original_position[0], original_position[1])
        # Move the mouse to the specified coordinates
        print("protecting form range!")

    if keyboard.is_pressed('t'):
        # Simulate pressing F1
        original_position = pyautogui.position()
        target_position1 = (1828, 866)
        # Simulate pressing F1
        keyboard.press_and_release('f2')
        melee(*target_position1, original_position[0], original_position[1])
        # Move the mouse to the specified coordinates
        print("protecting form range!")

