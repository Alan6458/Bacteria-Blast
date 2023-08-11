import pygame, random
pygame.init()

size = width, height = 800, 500
background = pygame.image.load("data\Background.png")
backgroundOverlay = pygame.image.load("data\Background copy.png")
rbc = pygame.image.load("data/rbc.png")
vir = pygame.image.load("data/vir.png")
cursorUp = pygame.image.load("data\cursorUp.png")
cursorDown = pygame.image.load("data\cursorDown.png")
heart = pygame.image.load("data/Heart.png")
heartLost = pygame.image.load("data/HeartLost.png")
goldenHeart = pygame.image.load("data/GoldenHeart.png")
font = pygame.font.Font("data\prstart.ttf", 20)
pygame.mixer.music.load("data/vir.wav")
pygame.display.set_icon(vir)
pygame.display.set_caption("Bacteria Blast")
background = pygame.transform.scale(background, (840, 525))
backgroundOverlay = pygame.transform.scale(backgroundOverlay, (840, 525))
rbc = pygame.transform.scale(rbc, (80, 60))
vir = pygame.transform.scale(vir, (80, 80))
heart = pygame.transform.scale(heart, (21, 18))
heartLost = pygame.transform.scale(heartLost, (21, 18))
goldenHeart = pygame.transform.scale(goldenHeart, (21, 18))
types = ["rbc", "vir"]
splashes = ["Made for My First Game Jam Summer 2022", "Made by alan6458", "Big thanks to BFXR!", "Big thanks to pygame!", "Destroy the viruses!"]
currentSplash = random.choice(splashes)
realHearts = 3
spriteData = []
toRemove = []
score = 0
health = 3
game = False
startGame = False
elementY = -2
scores = []
with open("data/Scores.txt") as file:
    scores = file.readlines()
    scores = [int(s.rstrip()) for s in scores]
if len(scores) < 3:
    scores.append(0)
    scores.append(0)
    scores.append(0)
scores.sort(reverse=True)
cursorUp = pygame.transform.scale(cursorUp, (21, 21))
cursorDown = pygame.transform.scale(cursorDown, (21, 21))
mouseDownRegistered = False
screen = pygame.display.set_mode(size)
color = (255, 80, 80)
level = 1
virusesKilledThisLevel = 0
running = True
pygame.mouse.set_visible(False)
customCursor = cursorUp
dtClock = pygame.time.Clock()
dtClock.tick()
dt = dtClock.get_time() / 1000

while running:
    camOffSetX = (pygame.mouse.get_pos()[0]-400)/20
    camOffSetY = (pygame.mouse.get_pos()[1]-250)/20
    while game == False:
        camOffSetX = (pygame.mouse.get_pos()[0]-400)/20
        camOffSetY = (pygame.mouse.get_pos()[1]-250)/20
        screen.blit(background, (-20-camOffSetX*0.2, -12.5-camOffSetY*0.2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = True
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if elementY == -2:
                    startGame = True
        screen.blit(pygame.transform.rotate(rbc, 123+elementY), (123, 134+elementY, 80, 80))
        screen.blit(pygame.transform.rotate(rbc, 1564+elementY), (678, 178+elementY, 80, 80))
        screen.blit(pygame.transform.rotate(vir, 135+elementY), (157, 326+elementY, 80, 80))
        screen.blit(pygame.transform.rotate(rbc, 354+elementY), (654, 289+elementY, 80, 80))
        screen.blit(pygame.transform.rotate(rbc, 3451+elementY), (456, 235+elementY, 80, 80))
        screen.blit(pygame.transform.rotate(vir, 1154+elementY), (67, 223+elementY, 80, 80))
        screen.blit(pygame.font.Font("data\prstart.ttf", 55).render("Bacteria Blast", True, (0, 120, 0), None), pygame.font.Font("data\prstart.ttf", 55).render("Bacteria Blast", True, (0, 150, 0), None).get_rect(center = (400, elementY + 100)))
        screen.blit(font.render("Click to Start", True, (0, 0, 0), None), font.render("Click to Start", True, (0, 0, 0), None).get_rect(center = (400, elementY + 360)))
        screen.blit(font.render("High Scores:", True, (0, 150, 0), None), font.render("High Scores:", True, (0, 150, 0), None).get_rect(center = (400, elementY + 210)))
        screen.blit(font.render(currentSplash, True, (0, 120, 0), None), font.render(currentSplash, True, (0, 100, 0), None).get_rect(center = (400, elementY + 150)))
        for i in range(3):
            screen.blit(font.render(str(scores[i]).zfill(6), True, (0, 120, 0), None), font.render(str(scores[i]).zfill(6), True, (0, 120, 0), None).get_rect(center = (400, elementY + 240 + (i*30))))
        if startGame and elementY <= -2:
            elementY -= (elementY)**2 * dt
            if elementY <= -400:
                game = True
        else:
            if elementY >= 1:
                elementY -= (elementY)*2 * dt
                elementY = max(-2, elementY)
            else:
                elementY = -2
        pygame.display.flip()
        dt = dtClock.get_time() / 1000
        dtClock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            customCursor = cursorDown
            if mouseDownRegistered == False:
                mouseDownRegistered = True
                for i, v in enumerate(spriteData[::-1]):
                    if v[0] == "rbc":
                        if pygame.Rect.collidepoint(pygame.Rect(v[2]-camOffSetX*v[1], v[3]-camOffSetY*v[1], v[1]*80, v[1]*60), pygame.mouse.get_pos()):
                            toRemove.append(spriteData[-(i+1)])
                            pygame.mixer.music.load("data/rbc.wav")
                            pygame.mixer.music.set_volume(v[1]-0.3)
                            pygame.mixer.music.play()
                            score -= 1
                            break
                    if v[0] == "vir":
                        if pygame.Rect.collidepoint(pygame.Rect(v[2]-camOffSetX*v[1], v[3]-camOffSetY*v[1], v[1]*80, v[1]*80), pygame.mouse.get_pos()):
                            toRemove.append(spriteData[-(i+1)])
                            virusesKilledThisLevel += 1
                            pygame.mixer.music.load("data/vir.wav")
                            pygame.mixer.music.set_volume(v[1]-0.3)
                            pygame.mixer.music.play()
                            score += 5
                            break
        elif event.type == pygame.MOUSEBUTTONUP:
            customCursor = cursorUp
            mouseDownRegistered = False
    if virusesKilledThisLevel >= (level):
        virusesKilledThisLevel = 0
        level += 1
        health += 1
        if level % 10 == 0:
            realHearts += 1
        realHearts = min(realHearts, 10)
        health = min(10, health)
        health = max(realHearts, health)
        pygame.mixer.music.load("data/LevelUp.wav")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    if len(spriteData) < 4 + 0.5*level:
        spriteData.append([random.choice(types), random.uniform(0.5, 1.5), random.randrange(800, 1200), random.randrange(75, 350)])
        spriteData.sort(key=lambda x: x[1])
    screen.blit(background, (-20-camOffSetX*0.2, -12.5-camOffSetY*0.2))
    for j in toRemove:
        spriteData.remove(j)
    toRemove = []
    for i, v in enumerate(spriteData):
        spriteData[i][2] -= (98+2*level)*v[1]*dt
        if v[0] == "rbc":
            screen.blit(pygame.transform.scale(rbc, (80*v[1], 60*v[1])), (spriteData[i][2]-camOffSetX*v[1], v[3]-camOffSetY*v[1]))
            if spriteData[i][2] <= -(v[1]*80):
                toRemove.append(spriteData[i])
                score += 1
        elif v[0] == "vir":
            screen.blit(pygame.transform.scale(vir, (80*v[1], 80*v[1])), (spriteData[i][2]-camOffSetX*v[1], v[3]-camOffSetY*v[1]))
            if spriteData[i][2] <= -(v[1]*80):
                toRemove.append(spriteData[i])
                score -= 10
                health -= 1
                pygame.mixer.music.load("data/heartLost.wav")
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play()
    score = max(score, 0)
    if health <= 0:
        scores.append(score)
        scores.sort(reverse=True)
        currentSplash = " ".join(["Game Over!", "Score:", str(score)])
        elementY = 400
        realHearts = 3
        game = False
        startGame = False
        spriteData = []
        toRemove = []
        score = 0
        health = 3
        level = 1
        virusesKilledThisLevel = 0
        mouseDownRegistered = False
    screen.blit(backgroundOverlay, (-20-camOffSetX*0.2, -12.5-camOffSetY*0.2))
    for i in range(realHearts):
        screen.blit(heartLost, (10+(i*30), 10))
    for i in range(health):
        if i < realHearts:
            screen.blit(heart, (10+(i*30), 10))
        else:
            screen.blit(goldenHeart, (10+(i*30), 10))
    screen.blit(font.render("Score:" + str(score).zfill(6), True, (0, 0, 0), None), (550, 10, 20, 20))
    screen.blit(font.render("Level:" + str(level).zfill(3), True, (0, 0, 0), None), (550, 480, 20, 20))
    if 0 < pygame.mouse.get_pos()[1] < 499 and 0 < pygame.mouse.get_pos()[0] < 799:
        screen.blit(customCursor, (pygame.mouse.get_pos()[0]-10.5, pygame.mouse.get_pos()[1]-10.5))
    pygame.display.flip()
    dt = dtClock.get_time() / 1000
    dtClock.tick()
scores = [s for s in scores if s]
with open('data/Scores.txt', 'w') as sc:
    for item in scores:
        # write each item on a new line
        sc.write("%s\n" % item)
pygame.quit()