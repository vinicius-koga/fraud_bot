# run --> pip install -r requirements.txt

# IMPORTS
import pyautogui as autogui
import pyperclip as clip
import time
from pyscreeze import ImageNotFoundException

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
salvar_2_img = "imgs/salvar_2.png"
checkbox_img = "imgs/checkbox.png"
enviar_nf_img = "imgs/enviar_nf.png"
enviar_selec_img = "imgs/enviar_selec.png"
ok_img = "imgs/ok.png"
nota_img = "imgs/nota.png"

# Funçao que procura até encontrar todas as ocorrencias do parametro e retorna uma lista contendo todas.
def find_occurrences(img):
    while True:
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
        try:
            ocorrencia = autogui.locateCenterOnScreen(img, confidence=0.9)
            return ocorrencia
        except autogui.ImageNotFoundException:
            print("procurando...")
        time.sleep(0.5)

# Lista todos os pendentes encontrados.
while True:
    pendente_occurrences = find_occurrences(pendente_img)
    for pendente_pos in pendente_occurrences:
        time.sleep(3)

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