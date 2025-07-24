# run --> pip install -r requirements.txt

# IMPORTS
import pyautogui as autogui
import pyperclip as clip
import time

# VARIABLES
pendente_img = "imgs/pendente.png"
kit_img = "imgs/kit.png"
ncm_img = "imgs/ncm.png"
valor_img = "imgs/valor.png"
icms_img = "imgs/icms.png"
origem_img = "imgs/origem.png"
nacional_img = "imgs/nacional.png"
nacional_2_img = "imgs/nacional_2.png"
salvar_1_img = "imgs/salvar_1.png"
desconto_img = "imgs/desconto.png"
valor_frete_img = "imgs/valor_frete.png"

# SCRIPT
time.sleep(2)

# Lista todos os pendentes encontrados
pendente_occurrences = list(autogui.locateAllOnScreen(pendente_img, confidence=0.9))
for pendente_pos in pendente_occurrences:
    # Clica no icone (pendente)
    centro = autogui.center(pendente_pos)
    autogui.moveTo(centro)
    autogui.click()

    # Scroll
    time.sleep(2)
    autogui.scroll(-500)
    time.sleep(0.5)

    # Lista todos os kits encontrados
    kit_occurrences = list(autogui.locateAllOnScreen(kit_img, confidence=0.9))
    for kit_pos in kit_occurrences:
        # Clica no kit
        centro = autogui.center(kit_pos)
        autogui.moveTo(centro)
        autogui.click()
        
        time.sleep(1)

        # Clica no NCM
        ncm_pos = autogui.locateCenterOnScreen(ncm_img, confidence=0.9)
        autogui.moveTo(ncm_pos)
        autogui.click()

        # Digita o NCM
        autogui.hotkey('ctrl', 'a')
        autogui.press('backspace')
        autogui.write('3926.40.00', interval=0.05)

        # Clica no valor
        valor_pos = autogui.locateCenterOnScreen(valor_img, confidence=0.9)
        autogui.moveTo(valor_pos)
        autogui.click()

        # Copia o valor
        autogui.hotkey('ctrl', 'a')
        autogui.hotkey('ctrl', 'c')
        time.sleep(0.1)

        # Digita valor / 10
        valor_str = clip.paste()
        valor_float = float(valor_str.replace(",", "."))
        valor_div = valor_float / 10
        valor_final = f'{valor_div:.2f}'.replace(".", ",")
        autogui.write(valor_final, interval=0.05)

        # Clica no na aba ICMS
        icms_pos = autogui.locateCenterOnScreen(icms_img, confidence=0.9)
        autogui.moveTo(icms_pos)
        autogui.click()

        time.sleep(0.5)

        # Clica na origem
        origem_pos = autogui.locateCenterOnScreen(origem_img, confidence=0.9)
        autogui.moveTo(origem_pos)
        autogui.click()

        # Abre o menu-dropdown
        autogui.hotkey('enter')
        time.sleep(0.1)

        # Clica em envio nacional
        nacional_pos = autogui.locateCenterOnScreen(nacional_img, confidence=0.9)
        autogui.moveTo(nacional_pos)
        autogui.click()

        # Clica em salvar_1
        salvar_1_pos = autogui.locateCenterOnScreen(salvar_1_img, confidence=0.9)
        autogui.moveTo(salvar_1_pos)
        autogui.click()

        time.sleep(1)

        # Clica em desconto
        desconto_pos = autogui.locateCenterOnScreen(desconto_img, confidence=0.9)
        autogui.moveTo(desconto_pos)
        autogui.click()
        time.sleep(0.1)

        # Digita 0
        autogui.hotkey('ctrl', 'a')
        autogui.press('backspace')
        autogui.write('0', interval=0.05)

        # Clica em valor do frete
        valor_frete_pos = autogui.locateCenterOnScreen(valor_frete_img, confidence=0.9)
        autogui.moveTo(valor_frete_pos)
        autogui.click()
        time.sleep(0.5)
        autogui.click()

        # Digita 0
        autogui.hotkey('ctrl', 'a')
        autogui.press('backspace')
        autogui.write('0', interval=0.05)

        exit()
