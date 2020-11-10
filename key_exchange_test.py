from key_exchange import diffie_hellman as dh


message="This is a very secret message!!!"
i_public=197
i_private=199

j_public=151
j_private=157

Ishan = dh.DH_Endpoint(i_public, j_public, i_private)
Joshua = dh.DH_Endpoint(i_public, j_public, j_private)

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