import pyaes
import os

class lock_or_unlock():
    def lock(name):
        file_name = str(name)
        file = open(file_name, 'rb')
        file_data = file.read()
        file.close()
        os.remove(file_name)
        key = b'qwertyuiop123456'
        aes = pyaes.AESModeOfOperationCTR(key)
        dado_criptografado = aes.encrypt(file_data)
        new_file_name = (file_name)
        new_file = open(new_file_name, 'wb')
        new_file.write(dado_criptografado)
        new_file.close()

    def unlock(name):
        file_name = str(name)
        file = open(file_name, 'rb')
        file_data = file.read()
        file.close()
        key = b'qwertyuiop123456'
        aes = pyaes.AESModeOfOperationCTR(key)
        dado_descriptografado = aes.decrypt(file_data)
        os.remove(file_name)
        new_file_name = (file_name)
        new_file = open(new_file_name,'wb')
        new_file.write(dado_descriptografado)
        new_file.close()
    
