import pygame, login_page
import map_array
pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("maths pursuit")
bg = pygame.Surface((1280,720))
pygame.draw.rect(bg,(255,255,255),(0,0,1280,720),2)
for i in range(0,64):
	pygame.draw.line(bg,(255,255,255),(i*20,0),(i*20,720))
for i in range(0,36):
	pygame.draw.line(bg,(255,255,255),(0,i*20),(1280,i*20))
for a,i in enumerate(map_array.map_array):
	for b,j in enumerate(i):
		if j==1:
			pygame.draw.rect(bg,(255,255,255),(b*20,a*20,20,20))
scale = 6
bg = pygame.transform.scale(bg,(1280*scale,720*scale))
x,y=0,0
run = True
while run:
	win.fill((0,0,0))
	win.blit(bg,(x-640*scale,y-360*scale))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	pygame.draw.rect(win,(255,0,0),(335,300,20*scale,20*scale))
	if keys[pygame.K_d]:
		# handle right arrow key press
		if x+3*scale < (640-295)*scale: # Modify the boundary for right arrow
			x+=3*scale
	if keys[pygame.K_a]:
		# handle left arrow key press
		if x-3*scale > -295*scale: # Modify the boundary for left arrow
			x-=3*scale
	if keys[pygame.K_s]:
		# handle down arrow key press
		if y+3*scale < (260-175)*scale: # Modify the boundary for down arrow
			y+=3*scale
	if keys[pygame.K_w]:
		# handle up arrow key press
		if y-3*scale > -175*scale: # Modify the boundary for up arrow
			y-=3*scale
	pygame.display.update()
	print(x)
pygame.quit()