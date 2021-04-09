usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

asssistiram = usuarios_data_science.copy()
asssistiram.extend(usuarios_machine_learning)

print(set(asssistiram))
for usuario in set(asssistiram):
    print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
print(usuarios_data_science | usuarios_machine_learning) # Juntar os usuarios indepedente do curso
print(usuarios_data_science & usuarios_machine_learning) # intersecção dos cursos
print(usuarios_data_science - usuarios_machine_learning) # Os que não estão no conjuntos pos
print(usuarios_data_science ^ usuarios_machine_learning) # Ou exclusivo

usuarios_machine_learning.add(99) # adição no conjunto
print(usuarios_machine_learning)
usuarios = frozenset(usuarios_machine_learning)
print(usuarios)