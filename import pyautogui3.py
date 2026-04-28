import pyautogui
import time


# Entrada no sala do futuro

pyautogui.press("win")
pyautogui.write("Google")
pyautogui.press("enter")
time.sleep(2)

# Login no sala do futuro

pyautogui.click(x = 541, y = 35)
time.sleep(0.5)
pyautogui.click(x=1476, y=619)
pyautogui.press("tab")
pyautogui.write("110409872")
pyautogui.press("tab")
pyautogui.write("6")
pyautogui.click(x=1500, y=864)
pyautogui.write("@Rosolia2023")
pyautogui.press("enter")
time.sleep(5)

# Entrar na aba de tarefas

pyautogui.click(x=600, y=489)
pyautogui.press("tab")
time.sleep(0.3)
pyautogui.press("enter")

# Acessar tarefe pendente do usuario

time.sleep(2)
pyautogui.click(x=552, y=899)
time.sleep(2)
pyautogui.press("PgDn")
time.sleep(1)
pyautogui.click(x=621, y=953)

# Farm automática de tempo

time.sleep(2)
pyautogui.scroll(-10000000)
time.sleep(540)
pyautogui.click(x=1580, y=786)

# Caso queira mandar  a tarefa mude os números da linha de código 46 para; (x=1768, y=791)