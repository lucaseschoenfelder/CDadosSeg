# Parte1

# Descrição
Este script recebe como entrada o caminho para um diretório contendo arquivos 'AndroidManifest.xml' e retorna a lista de permissões por APK, as listas de permissões únicas por APK e a list de permissões comuns a todos os APKs analisados. 
Opcionalmente, o script aceita um argumento '--plot' e retorna um gráfico de barras do número de ocorrências de cada permissão no conjunto de APKs analisados.

O diretório manifests/ contém um conjunto de 10 arquivos Manifest.xml obtidos da análise por meio da ferramenta [apktool](https://ibotpeaches.github.io/Apktool/) de APKs encontrados no site https://www.apkmirror.com/categories/

## Utilização
```
python3 script.py <caminho_para_diretorio> [--plot]
```
