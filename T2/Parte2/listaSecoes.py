import sys
import pefile
import os

if (len(sys.argv) < 2):
    print('forneca um diretorio com arquivos .exe e execute este script com python3 script.py <caminho_para_diretorio')
    exit(0)

pathname = sys.argv[1]
files = {}
for filename in os.listdir(pathname):
    if filename.endswith('.exe'):
        pe = pefile.PE(pathname + filename)
        sections = []
        for section in pe.sections:
            sections.append(section.Name.decode('utf-8'))
        files[filename] = sections


#print(files)
print('################################\n')
print('Seções executáveis por arquivo\n')
print('################################\n')
for file in files:
    print(file,':', ', '.join(files[file]),'\n')
