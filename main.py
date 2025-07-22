# run --> pip install -r requirements.txt

# IMPORTS
import pyautogui as autogui
import pytesseract as tess
import time
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# VARIABLES
pendente_img = "imgs/pendente.png"
desconto_img = "imgs/desconto.png" # !
kit_item = "imgs/kit_item.png"
ncm_item = "imgs/ncm.png"
valor_item = "imgs/valor.png"
max_scrolls = 10

# SCRIPT
time.sleep(2)

# Lista todos os pendentes encontrados
pendente_occurrences = list(autogui.locateAllOnScreen(pendente_img, confidence=0.9))
for pendente_pos in pendente_occurrences:
    # Clica no icone (pendente)
    centro = autogui.center(pendente_pos)
    autogui.moveTo(centro)
    autogui.click()

    time.sleep(1)
    autogui.scroll(-500)
    time.sleep(1)

    # Lista todos os kits encontrados
    kit_occurrences = list(autogui.locateAllOnScreen(kit_item, confidence=0.9))
    for kit_pos in kit_occurrences:
        # Clica no kit
        centro = autogui.center(kit_pos)
        autogui.moveTo(centro)
        autogui.click()
        
        time.sleep(1)

        # Clica no NCM
        ncm_pos = autogui.locateCenterOnScreen(ncm_item, confidence=0.9)
        autogui.moveTo(ncm_pos)
        autogui.click()

        # Pressiona Ctrl + A
        autogui.hotkey('ctrl', 'a')

        # Pressiona Backspace
        autogui.press('backspace')

        # Digita o NCM
        autogui.write('3926.40.00', interval=0.05)

        # Clica no valor
        valor_pos = autogui.locateCenterOnScreen(valor_item, confidence=0.9)
        autogui.moveTo(valor_pos)
        autogui.click()

        exit()











# Scrolla até encontrar
# for _ in range(max_scrolls):
#     encontrou = autogui.locateCenterOnScreen(img, confidence=0.8)
#     if encontrou:
#         autogui.moveTo(encontrou)
#         break
#     else:
#         autogui.scroll(-300)
#         time.sleep(0.5)
