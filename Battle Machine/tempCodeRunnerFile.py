
    wizardy = 360
    pekkax = 800
    pekkay = 350
    pekkav = -40
    score = 0
    v = 5
    m = 1
    while True:
        if game_over:
            text_screen("Game Over! Press Enter to play again.", (255,0, 0), 200, 200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            pygame.display.update()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if jump == False:
                        if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                            jump = True
                    if event.key == pygame.K_RIGHT:
                        wizardx += 50
                    if event.key == pygame.K_LEFT:
                        wizardx += -50
            if jump:
                f = (7/1)*m*(v**2)
                wizardy -= f
                v = v-1
                if v<0:
                    m = -1
                if v == -6:
                    jump = False
                    v = 5
                    m = 1 
            screen.fill((255,255,255))
            bg = pygame.image.load("bg.png")
            bg = pygame.transform.scale(bg,(1000,650)).convert_alpha()
            wizard = pygame.image.load("battle machine.png")
            wizard = pygame.transform.scale(wizard, (250,250)).convert_alpha()
            pekka = pygame.image.load("pekka.png")
            pekka = pygame.transform.scale(pekka, (200,200)).convert_alpha()
            # pekka = pygame.transform.flip(pekka, True, False)
            if abs(pekkax - wizardx) < 100 and abs(pekkay - wizardy)<100:
                game_over = True
            elif pekkax<wizardx:
                score+=0.2
                pekkav += -0.1
            screen.blit(bg, (0,0))
            screen.blit(wizard, (wizardx , wizardy))
            screen.blit(pekka, (pekkax, pekkay))
            if pekkax < -419:
                pekkax = 1000
            pekkax = pekkax + pekkav
            clock.tick(400)
            text_screen(f"Score: {int(score/3)}", (0,0,0), 70, 0)
            pygame.time.delay(10)
            pygame.display.update()
def welcome():
    pygame.mixer.music.load("Koven - Never Have I Felt This [NCS Release].mp3")
    pygame.mixer.music.play()
    bg = pygame.image.load("bg.png")
    bg = pygame.transform.scale(bg,(1000,650)).convert_alpha()