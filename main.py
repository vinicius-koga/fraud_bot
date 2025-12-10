# run --> python -m venv venv
# run --> venv\Scripts\activate
# run --> pip install -r requirements.txt
# run --> pyinstaller --onefile --add-data "imgs;imgs" --name "sonegator" main.py

import sys, os

def resource_path(relative_path):
    """Permite acessar arquivos no PyInstaller (tanto no .exe quanto no .py normal)."""
    if hasattr(sys, '_MEIPASS'):  # Quando está rodando no .exe
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(relative_path)  # Quando rodando no .py normal

# IMPORTS
import pyautogui as autogui
import pyperclip as clip
import time
from pyscreeze import ImageNotFoundException
import keyboard

# VARIABLES
pendente_img = resource_path("imgs/pendente.png")
kit_img = resource_path("imgs/kit.png")
ncm_img = resource_path("imgs/ncm.png")
valor_img = resource_path("imgs/valor.png")
icms_img = resource_path("imgs/icms.png")
origem_img = resource_path("imgs/origem.png")
nacional_img = resource_path("imgs/nacional.png")
nacional_2_img = resource_path("imgs/nacional_2.png")
salvar_1_img = resource_path("imgs/salvar_1.png")
desconto_img = resource_path("imgs/desconto.png")
valor_frete_img = resource_path("imgs/valor_frete.png")
salvar_2_img = resource_path("imgs/salvar_2.png")
checkbox_img = resource_path("imgs/checkbox.png")
enviar_nf_img = resource_path("imgs/enviar_nf.png")
enviar_selec_img = resource_path("imgs/enviar_selec.png")
ok_img = resource_path("imgs/ok.png")
nota_img = resource_path("imgs/nota.png")

# Funçao que procura até encontrar todas as ocorrencias do parametro e retorna uma lista contendo todas.
def find_occurrences(img):
    while True:
        if keyboard.is_pressed('esc'):
            print("Execução interrompida pelo usuário.")
            break
        try:
            ocorrencias = list(autogui.locateAllOnScreen(img, confidence=0.9))
            if ocorrencias:
                centros = [autogui.center(ocorrencia) for ocorrencia in ocorrencias]
                return centros
        except ImageNotFoundException:
            print("procurando...")
        time.sleep(0.5)

# Funçao que procura até encontrar a primeira ocorrencia do parametro e retorna ele.
def find_occurrence(img):
    while True:
        if keyboard.is_pressed('esc'):
            print("Execução interrompida pelo usuário.")
            break
        try:
            ocorrencia = autogui.locateCenterOnScreen(img, confidence=0.9)
            return ocorrencia
        except autogui.ImageNotFoundException:
            print("procurando...")
        time.sleep(0.5)

# Lista todos os pendentes encontrados.
while True:
    if keyboard.is_pressed('esc'):
        print("Execução interrompida pelo usuário.")
        break
    pendente_occurrences = find_occurrences(pendente_img)
    for pendente_pos in pendente_occurrences:
        time.sleep(4)

        # Clica no pendente
        autogui.moveTo(pendente_pos)
        autogui.click()

        # Scroll down
        find_occurrence(nota_img)
        autogui.scroll(-150)
        time.sleep(1)

        # Lista todos os kits encontrados
        kit_occurrences = find_occurrences(kit_img)
        for kit_pos in kit_occurrences:
            # Clica no kit
            find_occurrence(kit_img)
            autogui.moveTo(kit_pos)
            autogui.click()
            time.sleep(1)

            # Clica no NCM
            ncm_pos = find_occurrence(ncm_img)
            autogui.moveTo(ncm_pos)
            autogui.click()

            # Digita o NCM
            autogui.hotkey('ctrl', 'a')
            autogui.press('backspace')
            autogui.write('3926.40.00')

            # Clica no valor
            valor_pos = find_occurrence(valor_img)
            autogui.moveTo(valor_pos)
            autogui.click()
            time.sleep(1)
            autogui.click()

            # Copia o valor
            autogui.hotkey('ctrl', 'a')
            autogui.hotkey('ctrl', 'c')

            # Digita valor / 10
            valor_str = clip.paste()
            valor_float = float(valor_str.replace(",", "."))
            valor_div = valor_float / 10
            valor_final = f'{valor_div:.2f}'.replace(".", ",")
            autogui.write(valor_final)

            # Clica no na aba ICMS
            icms_pos = find_occurrence(icms_img)
            autogui.moveTo(icms_pos)
            autogui.click()

            # Clica na origem
            origem_pos = find_occurrence(origem_img)
            autogui.moveTo(origem_pos)
            autogui.click()

            # Abre o menu-dropdown
            autogui.hotkey('enter')

            # Clica em envio nacional
            nacional_pos = find_occurrence(nacional_img)
            autogui.moveTo(nacional_pos)
            autogui.click()

            # Clica em salvar_1
            salvar_1_pos = find_occurrence(salvar_1_img)
            autogui.moveTo(salvar_1_pos)
            autogui.click()
            time.sleep(3)

        # Clica em desconto
        desconto_pos = find_occurrence(desconto_img)
        autogui.moveTo(desconto_pos)
        autogui.click()

        # Digita 0
        autogui.hotkey('ctrl', 'a')
        autogui.press('backspace')
        autogui.write('0', interval=0.05)

        # Clica em valor do frete
        valor_frete_pos = find_occurrence(valor_frete_img)
        autogui.moveTo(valor_frete_pos)
        autogui.click()
        time.sleep(1)
        autogui.click()

        # Digita 0
        autogui.hotkey('ctrl', 'a')
        autogui.press('backspace')
        autogui.write('0', interval=0.05)

        # Scroll up
        autogui.scroll(300)
        time.sleep(1)

        # Clica em salvar_2
        salvar_2_pos = find_occurrence(salvar_2_img)
        autogui.moveTo(salvar_2_pos)
        autogui.click()
        time.sleep(1)
        autogui.click()

    # Marca as checkboxes
    time.sleep(4)
    checkbox_ocurrences = find_occurrences(checkbox_img)
    for checkbox_pos in checkbox_ocurrences[1:]:
        autogui.moveTo(checkbox_pos)
        autogui.click()
        time.sleep(0.5)

    # Clica em enviar notas
    enviar_nf_pos = find_occurrence(enviar_nf_img)
    autogui.moveTo(enviar_nf_pos)
    autogui.click()

    # Clica no botão Enviar
    enviar_selec_pos = find_occurrence(enviar_selec_img)
    autogui.moveTo(enviar_selec_pos)
    autogui.click()

    # Clica em Ok
    ok_pos = find_occurrence(ok_img)
    autogui.moveTo(ok_pos)
    autogui.click()