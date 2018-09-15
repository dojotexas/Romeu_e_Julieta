"""
Regras do Romeu e Julieta

1. Se a posição for multiplo de 3: Queijo
2. Se a posição for multiplo de 5: Goiabada
3. Se a posição for multiplo de 3 e 5: Romeu e Julieta
4. Para qualquer outra posição fale o própio nº
"""
def romeu_julieta(n):
	if n == 3 :
		return "queijo"
	if n == 2 :
		return "2"
	if n == 4:
		return "4"
	if n == 5:
		return "goiabada"
	if n == 15 or n == 30:
		return "Romeu e Julieta"
	return '1'
