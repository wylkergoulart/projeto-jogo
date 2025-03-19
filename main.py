import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))

print('Loop Start')
while True:
    # Check for all events - Confira todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close Window - fecha a janela
            quit()  # End pygame - Fim do pygame
