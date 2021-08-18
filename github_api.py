import os
token = "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"
username = 'paramteraiya09'
repo_name = "Crear_MaskRCNN"
# for_terminal = 'git clone https://paramteraiya09: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@github.com/paramteraiya09/Crear_MaskRCNN.git'
for_terminal = f'git clone https://{username}:{token}@github.com/{username}/{repo_name}.git'
os.system(f"{for_terminal}")