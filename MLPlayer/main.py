import pyautogui as pt
from time import sleep
import os

image_list = []

cow_directory = os.listdir('images/mob/cow')

for file in cow_directory:
    if file.endswith('.png') or file.endswith('.jpg'):
        image_list.append(file)


# fazer função que ve o mob e digita oq ele está vendo
def see_cow():
    for image in image_list:
        position = pt.locateOnScreen(os.path.join('images/mob/cow', image), confidence=0.5)
        if position is not None:
            return image
    return None

sleep(3)
duration = 1000
while duration != 0:
    detected_image = see_cow()
    if detected_image is not None:
        print(f'Im seeing a cow: {detected_image}')
    else:
        print('Im not seeing any cows')

    duration -= 1
    print("Time remaining =", duration)
