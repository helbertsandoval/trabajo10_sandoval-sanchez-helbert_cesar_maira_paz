import libreria

assert (libreria.validar_nombre("jose")==True)
assert (libreria.validar_nombre("luis")==True)
assert (libreria.validar_nombre(190)==False)
assert (libreria.validar_nombre(13)==False)
assert (libreria.validar_nombre("helbert")==True)
assert (libreria.validar_nombre(15)==False)
assert (libreria.validar_nombre("lucas")==True)
assert (libreria.validar_nombre("juan")==True)
assert (libreria.validar_nombre("judas")==True)
assert (libreria.validar_nombre(2198091)==False)
assert (libreria.validar_nombre(14)==False)
print("validar nombre ok")

assert (libreria.validar_numero(1234)==True)
assert (libreria.validar_numero(0)==True)
assert (libreria.validar_numero("hola")==False)
assert (libreria.validar_numero("ABCD")==False)
assert (libreria.validar_numero(9483393)==True)
assert (libreria.validar_numero(245)==True)
assert (libreria.validar_numero(50)==True)
assert (libreria.validar_numero(20)==True)
assert (libreria.validar_numero("jordan")==False)
assert (libreria.validar_numero("mateo")==False)
assert (libreria.validar_numero("sanson")==False)
print("validar numero ok")


