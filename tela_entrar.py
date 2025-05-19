import os

os.system('cls')

import cores
import pygame
import sys
from principal import janela_principal


pygame.init()

# Define as dimensões da janela
largura = 800
altura = 500

# Fonte
fonte = pygame.font.SysFont('Unicode', 40)


def tela_entrar(tela):
    botao_voltar = pygame.Rect(100, 400, 100, 50) # x, y, largura, altura
    email_input = pygame.Rect(100, 150, 400, 50)
    senha_input = pygame.Rect(100, 300, 400, 50)
    texto_email = ''
    texto_senha = ''
    email_ativo = False
    senha_ativo = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.collidepoint(event.pos):
                    return janela_principal()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if email_input.collidepoint(event.pos):
                    email_ativo = True # Ativa o campo
                else:
                    email_ativo = False # Desativa o campo
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if senha_input.collidepoint(event.pos):
                    senha_ativo = True # Ativa o campo
                else:
                    senha_ativo = False # Desativa o campo
            
            if event.type == pygame.KEYDOWN:
                if email_ativo:
                    if event.key == pygame.K_BACKSPACE:
                        # apaga o ultimo caracter
                        texto_email = texto_email[:-1]
                    elif event.key == pygame.K_RETURN:
                        # Quando pressionar enter aparece o texto
                        print('Texto digitado:', texto_email)
                    else:
                        # Adiciona o caractere pressionado ao texto
                        texto_email += event.unicode

                if senha_ativo:
                    if event.key == pygame.K_BACKSPACE:
                        # apaga o ultimo caracter
                        texto_senha = texto_senha[:-1]
                    elif event.key == pygame.K_RETURN:
                        # Quando pressionar enter aparece o texto
                        print('Texto digitado:', texto_senha)
                    else:
                        # Adiciona o caractere pressionado ao texto
                        texto_senha += event.unicode
        


        # Preenche a tela com a cor de fundo
        tela.fill(cores.BRANCO)

        # Renderiza os rótulos "Email" e "Senha" acima dos campos de entrada
        email = fonte.render('Email', True, cores.PRETO)
        senha = fonte.render('Senha', True, cores.PRETO)
        tela.blit(email, (email_input.x, email_input.y - 40))   # Exibe "Email" acima do campo
        tela.blit(senha, (senha_input.x, senha_input.y - 40))   # Exibe "Senha" acima do campo

        # Desenha os retângulos dos campos de entrada
        pygame.draw.rect(tela, cores.OURO, email_input, 2)      # Campo para digitar o email
        pygame.draw.rect(tela, cores.OURO, senha_input, 2)      # Campo para digitar a senha

        # Define a cor do texto digitado com base na ativação dos campos
        cor_email = cores.PRETO if email_ativo else cores.CINZA_CLARO
        cor_senha = cores.PRETO if senha_ativo else cores.CINZA_CLARO

        # Renderiza o texto digitado nos campos
        texto_renderizado_email = fonte.render(texto_email, True, cor_email)
        texto_renderizado_senha = fonte.render(texto_senha, True, cor_senha)

        # Exibe o texto digitado dentro dos campos
        tela.blit(texto_renderizado_email, (email_input.x + 5, email_input.y + 5))
        tela.blit(texto_renderizado_senha, (senha_input.x + 5, senha_input.y + 5))
        
        pygame.draw.rect(tela, cores.VERMELHO_ESCURO , botao_voltar)
        texto = fonte.render('Voltar', True, cores.PRETO)
        texto_rect = texto.get_rect(center=botao_voltar.center)
        tela.blit(texto, texto_rect)

        # Atualiza a tela
        pygame.display.update()