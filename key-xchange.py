class DH_Endpoint(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None
        
    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key%self.public_key2
        return partial_key
    
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key%self.public_key2
        self.full_key = full_key
        return full_key
    
    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c)+key)
        return encrypted_message
    
    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c)-key)
        return decrypted_message

message="This is a very secret message!!!"
i_public=197
i_private=199

j_public=151
j_private=157

Ishan = DH_Endpoint(i_public, j_public, i_private)
Joshua = DH_Endpoint(i_public, j_public, j_private)

i_partial=Ishan.generate_partial_key()
print(i_partial) #147

j_partial=Joshua.generate_partial_key()
print(j_partial)

i_full=Ishan.generate_full_key(j_partial)
print(i_full) #75

j_full=Joshua.generate_full_key(i_partial)
print(j_full)


j_encrypted=Joshua.encrypt_message(message)
print(j_encrypted) #'\x9f³´¾k´¾k¬kÁ°½Äk¾°®½°¿k¸°¾¾¬²°lll'

i_decrypted = Ishan.decrypt_message(j_encrypted)
print(i_decrypted) #'This is a very secret message!!!'