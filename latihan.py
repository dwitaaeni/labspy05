print('---------- Latihan Dictionary ----------')
print()
a={'Ari': '081267888', 'Dina': '087677776'}
print('Daftar Kontak :\n', a)

# Menampilkan kontak 
print('Menampilkan Kontak Ari : ', a['Ari'])
print('-----------------------------------------------------------')

# Menambahkan kontak 
print('Menambahkan Kontak Riko\n')
print('Daftar kontak sebelum ditambah :\n', a)
a['Riko']='087654544'
print('Daftar Kontak sesudah ditambah :\n', a)
print('-----------------------------------------------------------')

# Mengubah kontak
print('Mengubah Daftar Kontak Dina\n')
print('Daftar kontak sebelum diubah :\n', a)
a['Dina']='088999776'
print('Daftar kontak sesudah diubah :\n', a)
print('-----------------------------------------------------------')

# Menampilkan semua nama kontak
print('Menampilkan semua nama kontak\n')
print(a.keys())
print('-----------------------------------------------------------')

# Menampilkan semua nomor kontak
print('Menampilkan semua nomor kontak\n')
print(a.values())
print('-----------------------------------------------------------')

# Menampilkan daftar nama dan nomor kontak
print('Menampilkan daftar nama dan nomor kontaknya\n')
print(a.items())
print('-----------------------------------------------------------')

# Menghapus Kontak
print('Menghapus kontak Dina\n')
print('Daftar kontak sebelum dihapus :\n', a)
del a['Dina']
print('Daftar kontak sesudah dihapus :\n', a)
print('-----------------------------------------------------------')