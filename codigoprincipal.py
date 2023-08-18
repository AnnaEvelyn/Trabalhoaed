from biblioteca import Escrever, Redimensionar, Converter

coord_nome = (113, 193)
coord_data = (114, 293)
coord_tel = (470, 296)
coord_genero = (834, 295)
nome = input("Informe seu nome: ")
data = input("Informe sua data de nascimento: ")
tel = input("Informe seu telefone: ")
genero = input ("Informe seu gênero: ")
caminho_imagem = r'cadastro.jpg'
caminho_fonte = r'C:\Windows\Fonts\ARIAL.TTF'
cor_texto = (0, 0, 0)

Escrever(coord_nome, nome,coord_data, data, coord_tel, tel,coord_genero, genero, caminho_imagem, caminho_fonte, cor_texto)

tm1 = (500, 1000)
im = 'Imagem_Grande.jpg'  
im_menor = 'Imagem_Pequena.jpg' 

Redimensionar(tm1, im, im_menor)

Converter()