import sys
import pefile
import os

def extract_sections (filename):
    pe = pefile.PE(filename)
    sections = []
    for section in pe.sections:
        sections.append(section.Name.decode('utf-8'))
    return sections

if (len(sys.argv) < 3):
    print('Execute com: python3 script.py <arquivo_1> <arquivo_2>')
    exit(0)

file1_sections = extract_sections(sys.argv[1])
file2_sections = extract_sections(sys.argv[2])

set1 = set(file1_sections)
set2 = set(file2_sections)

print('################################\n')
print('Seções comuns aos dois arquivo\n')
print('################################\n')
print(', '.join(list(set.intersection(set1, set2))),'\n\n')

print('################################\n')
print('Seções únicas do arquivo 1\n')
print('################################\n')
print(', '.join(list(set1.difference(set2))),'\n\n')

print('################################\n')
print('Seções únicas do arquivo 2\n')
print('################################\n')
print(', '.join(list(set2.difference(set1))),'\n\n')
