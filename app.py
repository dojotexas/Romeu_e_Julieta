"""
Regras do Romeu e Julieta

1. Se a posição for multiplo de 3: Queijo
2. Se a posição for multiplo de 5: Goiabada
3. Se a posição for multiplo de 3 e 5: Romeu e Julieta
4. Para qualquer outra posição fale o própio nº
"""
def romeu_julieta(n):
	if n % 3 == 0 and n % 5 == 0:
		return 'Romeu e Julieta'
	if n%3 == 0:
		return 'Queijo'
	if n%5 == 0:
		return 'Goiabada'
	return n