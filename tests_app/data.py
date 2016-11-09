from tests_app.models import *

def main():
    test = Test.objects.get(pk=1)
    Option.objects.create(
        name='Marília Mendonça - Infiel',
        description='Marília Mendonça - Infiel é a música sertaneja que melhor descreve você! Gostou? Compatilhe com seus amigos.',
        image='test_imgs/infiel.jpg',
        test=test
    )
    Option.objects.create(
        name='Jorge e Mateus - Sosseguei',
        description='Jorge e Mateus - Sosseguei é a música sertaneja que melhor descreve você! Gostou? Compatilhe com seus amigos.',
        image='test_imgs/sosseguei.jpg',
        test=test
    )
    Option.objects.create(
        name='Cesar Menotti & Fabiano - To Mal',
        description='Cesar Menotti & Fabiano - To Mal é a música sertaneja da sua vida. Gostou? Compatilhe com seus amigos.',
        image='test_imgs/to_mal.jpg',
        test=test
    )
    Option.objects.create(
        name='Gusttavo Lima - To Solto Na Night',
        description='Gusttavo Lima - To Solto Na Night é a música sertaneja que melhor descreve você! Gostou? Compatilhe com seus amigos.',
        image='test_imgs/to_solto_na_night.jpg',
        test=test
    )
    Option.objects.create(
        name='Henrique & Juliano - To Valendo Nada',
        description='Assim como Henrique & Juliano você não tá valendo nada! Gostou? Compatilhe com seus amigos.',
        image='test_imgs/to_valendo_nada.jpg',
        test=test
    )
    Option.objects.create(
        name='Marília Mendonça - Saudade do Meu Ex',
        description='A música sertaneja que mais combina com você é Marília Mendonça - Saudade do Meu Ex. Gostou? Compatilhe com seus amigos.',
        image='test_imgs/saudade_do_meu_ex.jpg',
        test=test
    )
    Option.objects.create(
        name='Pedro Paulo e Alex - Esqueceu o Ex',
        description='A música sertaneja que mais combina com você é Pedro Paulo e Alex - Esqueceu o Ex. Gostou? Compatilhe com seus amigos.',
        image='test_imgs/esqueceu_o_ex.jpg',
        test=test
    )
    Option.objects.create(
        name='Antony E Gabriel - Eu Te Amo Pinga',
        description='A música sertaneja que mais combina com você é Marília Mendonça - Saudade do Meu Ex. Gostou? Compatilhe com seus amigos.',
        image='test_imgs/eu_te_amo_pinga.jpg',
        test=test
    )
    Option.objects.create(
        name='Gusttavo Lima - Homem de Família',
        description='A música sertaneja que mais combina com você é Marília Gusttavo Lima - Homem de Família. Gostou? Compatilhe com seus amigos.',
        image='test_imgs/homem_de_familia.jpg',
        test=test
    )