from PIL import Image, ImageFont, ImageDraw

def Escrever(coord_nome, nome,coord_data, data, coord_tel, tel,coord_genero, genero, caminho_imagem, caminho_fonte, cor_texto):
    imagem = Image.open(caminho_imagem)
    fonte = ImageFont.truetype(caminho_fonte, 20)
    desenho = ImageDraw.Draw(imagem)
    desenho.text(coord_nome, nome, font=fonte, fill=cor_texto)
    desenho.text(coord_data, data, font=fonte, fill=cor_texto)
    desenho.text(coord_tel,tel, font=fonte, fill=cor_texto)
    desenho.text(coord_genero,genero, font=fonte, fill=cor_texto)
    imagem.save('cadastro_preenchido.jpg')
    imagem.show()

def Redimensionar(tm1,im, im_menor):
    tm1= (500,1000)
    im = Image.open ("Imagem_Grande.jpg")
    im_menor = im.resize(tm1)
    im_menor.save("Imagem_Little.jpg")
    im_menor.show()


def Converter():
    imgRGB = Image.open("endeota.jpg")
    modo_cores = imgRGB.mode
    print(modo_cores)
    imgCMKY = imgRGB.convert('CMYK')
    imgCMKY.save('endeotaCMYK.jpg')
    imgCMKY2 = Image.open("endeotaCMYK.jpg")
    modo_coresFinal = imgCMKY2.mode
    print(modo_coresFinal)
