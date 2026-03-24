import pyautogui
from time import sleep
import os

# Define o diretório de trabalho como a pasta onde seu script está localizado
os.chdir(os.path.dirname(os.path.abspath(__file__)))

seta = pyautogui.locateCenterOnScreen('files/arrow.png')  # Adiciona 'files/' antes do nome do arquivo
sleep(2)
pyautogui.click(seta[0], seta[1])