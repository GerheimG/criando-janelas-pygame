import os
os.system('cls')  # Limpa o terminal no Windows


import cores as cores
import pygame
import sys
import tela_entrar as entrar


# Inicializa o pygame
pygame.init()


# Define as dimensões da janela
largura = 800
altura = 500

# Cria a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Janela Pincipal")


# Fonte
fonte = pygame.font.SysFont('Unicode', 40)

# Botão 'entrar'
botao_entrar = pygame.Rect(100, 100, 100, 50) # x, y, largura, altura
botao_registrar = pygame.Rect(100, 180, 130, 50) # x, y, largura, altura
botao_sair = pygame.Rect(100, 260, 100, 50) # x, y, largura, altura



# Loop principal
def janela_principal():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_entrar.collidepoint(event.pos):
                    print('entrou')
                    return entrar.tela_entrar(tela)
                if botao_registrar.collidepoint(event.pos):
                    print('registrou')
                if botao_sair.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                    print('saiu')

        # Preenche a tela com uma cor (por exemplo, branco)
        tela.fill(cores.BRANCO)

        # Desenha o botao
        pygame.draw.rect(tela, cores.OURO , botao_entrar)
        pygame.draw.rect(tela, cores.OURO , botao_registrar)
        pygame.draw.rect(tela, cores.VERMELHO_ESCURO , botao_sair)

        # Desenha o texto no botão
        texto = fonte.render('Entrar', True, cores.PRETO)
        texto_rect = texto.get_rect(center=botao_entrar.center)
        tela.blit(texto, texto_rect)

        texto = fonte.render('Registrar', True, cores.PRETO)
        texto_rect = texto.get_rect(center=botao_registrar.center)
        tela.blit(texto, texto_rect)

        texto = fonte.render('Sair', True, cores.PRETO)
        texto_rect = texto.get_rect(center=botao_sair.center)
        tela.blit(texto, texto_rect)

        # Atualiza o display
        pygame.display.update()




if __name__ == "__main__":
    janela_principal()