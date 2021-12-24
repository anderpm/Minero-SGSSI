import hashlib

ruta = 'C:/Users/Sleekbook/Desktop/SGSSI-21.CB.07.txt'
import hashlib as hl
import sys
from os import remove
import shutil
import string,random
NEW_FILE_SUFIX = "hash50"
TARGET_HASH_PREFIX = '00000'
STRING_LEN = 8

def find_file_hash(file_name):
    
    new_file_name = file_name[:-3]+NEW_FILE_SUFIX+".txt"
    shutil.copyfile(file_name, new_file_name)
    f = open(file_name,'r')
    file_con = f.readlines()
    con = ''
    for i in range(0,len(file_con)):
        con += file_con[i]
    random.seed(22)
    f.close()
    with open(ruta, mode='rb') as objeto_fichero:
        content = objeto_fichero.read()
        h = hashlib.sha256(content)
        hex_dig = h.hexdigest()
    while hex_dig[:len(TARGET_HASH_PREFIX)] != TARGET_HASH_PREFIX:
        f2 = open(new_file_name, "w")
        rand_string = ''.join(random.choices(string.hexdigits,k=STRING_LEN))
        rand_string = rand_string.lower()
        f2.write(con + rand_string + " G38")
        f2.close()
        with open(ruta, mode='rb') as objeto_fichero:
            content = objeto_fichero.read()
            h = hashlib.sha256(content)
            hex_dig = h.hexdigest()
        """if hex_dig[:len(TARGET_HASH_PREFIX)] == TARGET_HASH_PREFIX:
            break
        else:
            remove("C:/Users/asier/Desktop/4_maila/SGSSI/Semana7/Labo05.37AREZ/SGSSI-21.CB.06.hash50.txt")
            shutil.copyfile(file_name, new_file_name)"""
    print("VALID hash: "+hex_dig+"\n")
find_file_hash(sys.argv[1])