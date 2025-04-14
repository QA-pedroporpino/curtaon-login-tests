import base64
import os

# Lista de imagens
imagens = [
    "erro_email_formato_incorreto.png",
    "erro_email_nao_cadastrado.png",
    "erro_modal_nao_encontrado.png",
    "erro_sem_email_e_senha.png",
    "teste_email_nao_cadastrado_aprovado.png",
    "logo.png"
]

# Caminho onde estão suas imagens
caminho = r"C:\Projects\curtaON!automacoes\assets"  # ou screenshots se preferir

for nome in imagens:
    caminho_completo = os.path.join(caminho, nome)
    with open(caminho_completo, "rb") as imagem:
        base64_string = base64.b64encode(imagem.read()).decode("utf-8")
        print(f"BASE64 DE: {nome}\n")
        print(f'data:image/png;base64,{base64_string}\n')
        print("-" * 80)
