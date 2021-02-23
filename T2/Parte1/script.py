import os
import xml.etree.ElementTree as ET
import sys
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print('usage: python3 script.py <path_to_apks_directory> [--plot]')
    exit(0)

path_to_apks = sys.argv[1]
dict = {}
for filename in os.listdir(path_to_apks):
    if filename.endswith('.xml'):
        tree = ET.parse(path_to_apks + '/' + filename)
        root = tree.getroot()
        dict[filename.split('_')[1].split('.xml')[0]] = {'root' : root, 'permissions' : [], 'unique_permissions' : '[]'}
#print(dict)

for key in dict:
    child_permissions = []
    for child in dict[key]['root']:
        if child.tag == "uses-permission" or child.tag == "uses-permission-sdk-23":
            permission = child.attrib['{http://schemas.android.com/apk/res/android}name'].split('.')[-1]
            child_permissions.append(permission)
        #print(child_permissions)
    dict[key]['permissions'] = child_permissions
#print(dict)

print('#############\n')
print('Permissões por APK\n')
print('#############\n')
for key, value in dict.items():
    print(key,':', value['permissions'],'\n')

sets = []
for key in dict:
    sets.append(set(dict[key]['permissions']))
intersection = set.intersection(*sets)

for (key,value), permissions_set in zip(dict.items(), sets):
    all_other = [x for x in sets if x != permissions_set]
    value['unique_permissions'] = list(permissions_set.difference(*all_other))

print('#############\n')
print('Permissões únicas por APKs\n')
print('#############\n')
for key, value in dict.items():
    print(key,':', value['unique_permissions'] if len(value['unique_permissions']) != 0 else 'Nenhuma','\n')

print('#############\n')
print('Permissões comuns das APKs\n')
print('#############\n')
print(list(intersection))

if '--plot' in sys.argv:
    count = dict.fromkeys(set([item for sublist in [dict[key]['permissions'] for key in dict] for item in sublist]), 0)
    #print(count)
    for key in dict:
        for permission in dict[key]['permissions']:
            count[permission] += 1

    #print(count)
    plt.figure(figsize=(15, 7))
    plt.bar(range(len(count)), list(count.values()), align='center', color=plt.get_cmap("viridis").colors)
    plt.title('Number of occurences of each permission')
    plt.xticks(range(len(count)), list(count.keys()))
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
