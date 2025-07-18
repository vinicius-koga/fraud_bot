# IMPORTS
import pyautogui as autogui
import pytesseract as tess
import time

# CONFIGURAÇÕES DO TESSERACT
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# VARIÁVEIS
pendente_img = "imgs/pendente.png"
desconto_img = "imgs/desconto.png"
kit_item = "imgs/kit_item.png"
max_scrolls = 10

# FUNÇÃO PARA OBTER TODOS OS PENDENTES COM SCROLL
def coletar_todos_pendentes(max_scrolls=10):
    encontrados = set()
    for _ in range(max_scrolls):
        # Captura os pendentes visíveis na tela
        pendentes_visiveis = list(autogui.locateAllOnScreen(pendente_img, confidence=0.9))
        for pos in pendentes_visiveis:
            centro = autogui.center(pos)
            encontrados.add((centro.x, centro.y))
        autogui.scroll(-300)
        time.sleep(0.5)
    return list(encontrados)

# SCRIPT
print("Aguardando 3 segundos...")
time.sleep(3)

# Coleta todos os pendentes da tela com scroll
print("Coletando pedidos pendentes...")
pendente_centros = coletar_todos_pendentes(max_scrolls=max_scrolls)

# Remove duplicatas (em caso de sobreposição visual)
pendente_centros = list(set(pendente_centros))
print(f"{len(pendente_centros)} pedidos encontrados.")

# Executa ações em cada pedido
for centro in pendente_centros:
    autogui.moveTo(centro)
    autogui.click()

    time.sleep(2)
    autogui.scroll(-500)
    time.sleep(2)

    kit_occurrences = list(autogui.locateAllOnScreen(kit_item, confidence=0.9))
    for kit_pos in kit_occurrences:
        kit_centro = autogui.center(kit_pos)
        autogui.moveTo(kit_centro)
        autogui.click()
        time.sleep(2)

    # Voltar para a tela anterior, se necessário (dependendo do fluxo do Bling)
    # Ex: autogui.press("esc") ou clique no "voltar"
    # time.sleep(1)
