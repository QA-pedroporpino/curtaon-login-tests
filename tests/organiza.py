import os

pasta = "C:/Projects/curtaON!automacoes"  # Ajuste para o seu caminho
for filename in os.listdir(pasta):
    if filename.endswith(".py"):
        path = os.path.join(pasta, filename)
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace(
            'logging.FileHandler("logs/log_',
            'logging.FileHandler("logs/log_'
        ).replace(
            'driver.save_screenshot("screenshots/screenshots/screenshots/screenshots/',
            'driver.save_screenshot("screenshots/screenshots/screenshots/screenshots/screenshots/'
        )
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
print("✅ Todos os arquivos atualizados!")
