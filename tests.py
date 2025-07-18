import pyautogui as autogui
import pytesseract as tess
import time
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ncm_item = "imgs/ncm.png"

time.sleep(3)

ncm_pos = autogui.locateCenterOnScreen(ncm_item, confidence=0.9)
autogui.moveTo(ncm_pos)
autogui.click()