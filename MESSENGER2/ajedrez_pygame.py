import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900

screen =  pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Ajedrez')
fuente = pygame.font.SysFont('georgia', 20)
mediana = pygame.font.Font('freesansbold.ttf', 32)
Titulos = pygame.font.SysFont('georgia', 30, bold=True)
timer = pygame.time.Clock()
fps = 60

#Juego
piezas_blancas = ['torre','caballo','alfil', 'rey', 'reina','alfil', 'caballo', 'torre',
                  'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
ubicacion_blancas= [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), 
                    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
piezas_negras = ['torre','caballo','alfil', 'rey', 'reina','alfil', 'caballo', 'torre',
                  'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
ubicacion_negras= [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), 
                    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6) ]
piezas_capturadas_blancas = []
piezas_capturadas_negras = []

#0 turno blancas sin seleccionar - 1 blancas selecciono una pieza - 2 turno negras sin seleccionar - 3 negras selecciono una pieza - 
turn_step = 0
seleccion = 100
movimientos_validos = []

#cargar imagenes de la carpeta
torre_blanca = pygame.image.load('imagenes/TB.png')
torre_blanca = pygame.transform.scale(torre_blanca, (80, 80))
torre_blanca_pequeña = pygame.transform.scale(torre_blanca, (45, 45))
caballo_blanco = pygame.image.load('imagenes/CB.png')
caballo_blanco = pygame.transform.scale(caballo_blanco, (80, 80))
caballo_blanco_pequeño = pygame.transform.scale(caballo_blanco, (45, 45))
alfil_blanco = pygame.image.load('imagenes/AB.png')
alfil_blanco = pygame.transform.scale(alfil_blanco, (80,80))
alfil_blanco_pequeño = pygame.transform.scale(alfil_blanco, (45, 45))
reina_blanca = pygame.image.load('imagenes/RB.png')
reina_blanca = pygame.transform.scale(reina_blanca, (90, 90))
reina_blanca_pequeña = pygame.transform.scale(reina_blanca, (45, 45))
rey_blanco = pygame.image.load('imagenes/ReB.png')
rey_blanco = pygame.transform.scale(rey_blanco, (90, 90))
rey_blanco_pequeño = pygame.transform.scale(rey_blanco, (45, 45))
peon_blanco = pygame.image.load('imagenes/PB.png')
peon_blanco = pygame.transform.scale(peon_blanco, (65, 65))
peon_blanco_pequeño = pygame.transform.scale(peon_blanco, (45, 45))
torre_negra = pygame.image.load('imagenes/TN.png')
torre_negra = pygame.transform.scale(torre_negra, (80, 80))
torre_negra_pequeña = pygame.transform.scale(torre_negra, (45, 45))
caballo_negro = pygame.image.load('imagenes/CN.png')
caballo_negro = pygame.transform.scale(caballo_negro, (80, 80))
caballo_negro_pequeño = pygame.transform.scale(caballo_negro, (45, 45))
alfil_negro = pygame.image.load('imagenes/AN.png')
alfil_negro = pygame.transform.scale(alfil_negro, (80, 80))
alfil_negro_pequeño = pygame.transform.scale(alfil_negro, (45, 45))
reina_negra = pygame.image.load('imagenes/RN.png')
reina_negra = pygame.transform.scale(reina_negra, (90, 90))
reina_negra_pequeña = pygame.transform.scale(reina_negra, (45, 45))
rey_negro = pygame.image.load('imagenes/ReN.png')
rey_negro = pygame.transform.scale(rey_negro, (90, 90))
rey_negro_pequeño = pygame.transform.scale(rey_negro, (45, 45))
peon_negro = pygame.image.load('imagenes/PN.png')
peon_negro = pygame.transform.scale(peon_negro, (65, 65))
peon_negro_pequeño = pygame.transform.scale(peon_negro, (45, 45))

#lista imagenes
imagenes_blancas = [torre_blanca, caballo_blanco, alfil_blanco, reina_blanca, rey_blanco, peon_blanco]
imagenes_blancas_pequeñas = [torre_blanca_pequeña, caballo_blanco_pequeño, alfil_blanco_pequeño, reina_blanca_pequeña, rey_blanco_pequeño, peon_blanco_pequeño]
imagenes_negras = [torre_negra, caballo_negro, alfil_negro, reina_negra, rey_negro, peon_negro]
imagenes_negras_pequeñas = [torre_negra_pequeña, caballo_negro_pequeño, alfil_negro_pequeño, reina_negra_pequeña, rey_negro_pequeño, peon_negro_pequeño]  

#lista de piezas
lista_piezas = ['torre', 'caballo', 'alfil', 'reina', 'rey', 'peon']


#contador
contador = 0
ganador = ''

#Tablero
def dibujar_tablero():
    casilla_size = 100
    for fila in range(8):
        for columna in range(8):
            x = columna * casilla_size
            y = fila * casilla_size
            if (fila + columna) % 2 == 0:
                color = 'light gray'
            else:
                color = 'black'
            pygame.draw.rect(screen, color, [x, y, casilla_size, casilla_size]) 
            pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5 )
            pygame.draw.rect(screen, 'gold', [800, 0, 200,  HEIGHT], 5 )
            texto_turno = ['Turno de blancas: seleccione una pieza', 'Turno de blancas: escoje el destino',
            'Turno de negras: seleccione una pieza', 'Turno de negras: escoje el destino']
            screen.blit(Titulos.render(texto_turno[turn_step], True, 'black'),(20, 820))
    screen.blit(mediana.render('¿Rendirse?', True, 'black'), (810, 830))
       

#piezas del tablero
def piezas():
    for i in range (len(piezas_blancas)):
        index = lista_piezas.index(piezas_blancas[i])
        if piezas_blancas[i] == 'peon':
            screen.blit(peon_blanco, (ubicacion_blancas[i][0] * 100 + 15, ubicacion_blancas[i][1] * 100 + 30))   
        elif piezas_blancas[i] == 'reina':
            screen.blit(reina_blanca, (ubicacion_blancas[i][0] * 100 + 15, ubicacion_blancas[i][1] * 100 + 2))
        elif piezas_blancas[i] == 'rey':
            screen.blit(rey_blanco, (ubicacion_blancas[i][0] * 100 + 15, ubicacion_blancas[i][1] * 100 + 2))       
        else:
            screen.blit(imagenes_blancas[index], (ubicacion_blancas[i][0] * 100 + 5, ubicacion_blancas[i][1] * 100 + 12))
        if turn_step < 2:
            if seleccion == i:
                pygame.draw.rect(screen, 'red', [ubicacion_blancas[i][0] * 100 + 1, ubicacion_blancas[i][1] * 100 + 1,
                                                 100, 100], 2)
    for i in range (len(piezas_negras)):
        index = lista_piezas.index(piezas_negras[i])
        if piezas_negras[i] == 'peon':
            screen.blit(peon_negro, (ubicacion_negras[i][0] * 100 + 15, ubicacion_negras[i][1] * 100 + 30))   
        elif piezas_negras[i] == 'reina':
            screen.blit(reina_negra, (ubicacion_negras[i][0] * 100 + 15, ubicacion_negras[i][1] * 100 + 2))
        elif piezas_negras[i] == 'rey':
            screen.blit(rey_negro, (ubicacion_negras[i][0] * 100 + 15, ubicacion_negras[i][1] * 100 + 2))       
        else:
            screen.blit(imagenes_negras[index], (ubicacion_negras[i][0] * 100 + 5, ubicacion_negras[i][1] * 100 + 12))
        if turn_step >= 2:
            if seleccion == i:
                pygame.draw.rect(screen, 'blue', [ubicacion_negras[i][0] * 100 + 1, ubicacion_negras[i][1] * 100 + 1,
                                                 100, 100], 2)
                
# opciones validas dentro del tablero
def opciones(piezas, ubicaciones, turno):
    lista_movimientos = []
    todos_los_movimientos = []
    for i in range ((len(piezas))):
        ubicacion = ubicaciones[i]
        pieza = piezas[i]
        if pieza == 'peon':
            lista_movimientos = ver_peon(ubicacion, turno) 
        elif pieza == 'torre':
            lista_movimientos =ver_torre(ubicacion, turno) 
        elif pieza == 'caballo':
            lista_movimientos =ver_caballo(ubicacion, turno)
        elif pieza == 'alfil':
            lista_movimientos =ver_alfil(ubicacion, turno)
        elif pieza == 'rey':
            lista_movimientos =ver_rey(ubicacion, turno)
        elif pieza == 'reina':
            lista_movimientos =ver_reina(ubicacion, turno)
        todos_los_movimientos.append(lista_movimientos)
    return todos_los_movimientos

#movimientos validos del peon
def ver_peon(ubicacion, color):
    lista_movimientos = []
    if color == 'white':
        if (ubicacion[0], ubicacion[1] + 1) not in ubicacion_blancas and \
                (ubicacion[0], ubicacion[1] + 1) not in ubicacion_negras and ubicacion[1] < 7:
            lista_movimientos.append((ubicacion[0], ubicacion[1] + 1))
        if (ubicacion[0], ubicacion[1] + 2) not in ubicacion_blancas and \
                (ubicacion[0], ubicacion[1] + 2) not in ubicacion_negras and ubicacion[1] == 1:
            lista_movimientos.append((ubicacion[0], ubicacion[1] + 2))
        if (ubicacion[0] + 1, ubicacion[1] + 1) in ubicacion_negras:
            lista_movimientos.append((ubicacion[0] + 1, ubicacion[1] + 1))
        if (ubicacion[0] - 1, ubicacion[1] + 1) in ubicacion_negras:
            lista_movimientos.append((ubicacion[0] - 1, ubicacion[1] + 1))
    else:
        if (ubicacion[0], ubicacion[1] - 1) not in ubicacion_blancas and \
                (ubicacion[0], ubicacion[1] - 1) not in ubicacion_negras and ubicacion[1] > 0:
            lista_movimientos.append((ubicacion[0], ubicacion[1] - 1))
        if (ubicacion[0], ubicacion[1] - 2) not in ubicacion_blancas and \
                (ubicacion[0], ubicacion[1] - 2) not in ubicacion_negras and ubicacion[1] == 6:
            lista_movimientos.append((ubicacion[0], ubicacion[1] - 2))
        if (ubicacion[0] + 1, ubicacion[1] - 1) in ubicacion_blancas:
            lista_movimientos.append((ubicacion[0] + 1, ubicacion[1] - 1))
        if (ubicacion[0] - 1, ubicacion[1] - 1) in ubicacion_blancas:
            lista_movimientos.append((ubicacion[0] - 1, ubicacion[1] - 1))
    return lista_movimientos

#moviminetos validos torre
def ver_torre(ubicacion, color):
    lista_movimientos = []
    if color == 'white':
        enemigos = ubicacion_negras
        amigos = ubicacion_blancas
    else:
        enemigos = ubicacion_blancas
        amigos = ubicacion_negras 
    for i in range (4): #direciones lineales
        camino = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0   
        while camino:
            if (ubicacion[0] + (chain * x), ubicacion[1] + (chain * y)) not in amigos and \
             0 <= ubicacion [0] + (chain * x) <= 7 and 0 <= ubicacion[1] + (chain * y) <= 7:
                lista_movimientos.append((ubicacion[0] + (chain * x), ubicacion[1] + (chain * y)))
                if (ubicacion[0] + (chain * x), ubicacion[1] + (chain * y)) in enemigos:
                    camino = False
                chain += 1
            else:
                camino = False
    return lista_movimientos

#moviminetos caballo
def ver_caballo(ubicacion, color):
    lista_movimientos = []
    if color == 'white':
        enemigos = ubicacion_negras
        amigos = ubicacion_blancas
    else:
        enemigos = ubicacion_blancas
        amigos = ubicacion_negras 
    destinos = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]    
    for i in range (8):
        destino = (ubicacion[0] + destinos [i][0], ubicacion[1] + destinos[i][1])
        if destino not in amigos and 0 <= destino [0] <=7 and 0 <= destino[1] <=7:
            lista_movimientos.append(destino)
    return lista_movimientos

#movimientos alfil
def ver_alfil(ubicacion, color):
    lista_movimientos = []
    if color == 'white':
        enemigos = ubicacion_negras
        amigos = ubicacion_blancas
    else:
        enemigos = ubicacion_blancas
        amigos = ubicacion_negras 
    for i in range (4): #direciones en diagonal
        camino = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1   
        while camino:
            if (ubicacion[0] + (chain * x), ubicacion[1] + (chain * y)) not in amigos and \
             0 <= ubicacion [0] + (chain * x) <= 7 and 0 <= ubicacion[1] + (chain * y) <= 7:
                lista_movimientos.append((ubicacion[0] + (chain * x), ubicacion[1] + (chain * y)))
                if (ubicacion[0] + (chain * x), ubicacion[1] + (chain * y)) in enemigos:
                    camino = False
                chain += 1
            else:
                camino = False
    return lista_movimientos

#movimientos reyna
def ver_reina(ubicacion, color):
    lista_movimientos = ver_alfil (ubicacion, color)
    segunda_lista = ver_torre (ubicacion, color)
    for i in range(len(segunda_lista)):
        lista_movimientos.append(segunda_lista[i])
    return lista_movimientos

#movimientos rey
def ver_rey(ubicacion, color):
    lista_movimientos = []
    if color == 'white':
        enemigos = ubicacion_negras
        amigos = ubicacion_blancas
    else:
        enemigos = ubicacion_blancas
        amigos = ubicacion_negras 
    destinos = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]    
    for dx, dy in destinos:
        destino = (ubicacion[0] + dx, ubicacion[1] + dy)
        if destino not in amigos and 0 <= destino[0] <= 7 and 0 <= destino[1] <= 7:
            lista_movimientos.append(destino)
        
    return lista_movimientos
        
        
# verificar movimientos validos
def verificar_movimientos_validos():
    if seleccion == 100:
        return []
    if turn_step < 2:
        lista_opciones = opciones_blancas
    else:
        lista_opciones = opciones_negras
    if seleccion >= len(lista_opciones):
        return []
    opciones_validas = lista_opciones [seleccion]
    return opciones_validas
    
#piezas capturadas   
def piezas_capturadas():
    for i in range (len(piezas_capturadas_blancas)):
        piezas_capturadas = piezas_capturadas_blancas[i]
        index = lista_piezas.index(piezas_capturadas)
        screen.blit(imagenes_negras_pequeñas[index], (825, 5 + 50*i))
    for i in range (len(piezas_capturadas_negras)):
        piezas_capturadas = piezas_capturadas_negras[i]
        index = lista_piezas.index(piezas_capturadas)
        screen.blit(imagenes_blancas_pequeñas[index], (925, 5 + 50*i))
            
#ver moviminetos validos
def dibujar_movimientos_validos(movimientos):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range (len(movimientos)):
        pygame.draw.circle(screen, color, (movimientos[i][0] * 100 + 50, movimientos[i][1] * 100 + 50), 10)   

# jaques
def jaque():
    if turn_step < 2:
        if 'rey' in piezas_blancas:
            rey_index = piezas_blancas.index('rey')
            ubicacion_rey = ubicacion_blancas[rey_index]
            for i in range(len(opciones_negras)):
                if ubicacion_rey in opciones_negras[i]:
                    if contador < 15:
                        pygame.draw.rect(screen, 'dark red', [ubicacion_blancas[rey_index][0] * 100 + 1, 
                                                              ubicacion_blancas[rey_index][1] * 100 +1, 100, 100], 5)
    else:
        if 'rey' in piezas_negras:
            rey_index = piezas_negras.index('rey')
            ubicacion_rey = ubicacion_negras[rey_index]
            for i in range(len(opciones_negras)):
                if ubicacion_rey in opciones_blancas[i]:
                    if contador < 15:
                        pygame.draw.rect(screen, 'dark blue', [ubicacion_negras[rey_index][0] * 100 + 1, 
                                                               ubicacion_negras[rey_index][1] * 100 +1, 100, 100], 5)

#ganador
def pantalla_ganador():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(fuente.render(f'{ganador} ganaron el juego', True,'white'),(210, 210))
    screen.blit(fuente.render(f'presiona enter para reiniciar', True,'white'),(210, 240))
#Main   
opciones_blancas=opciones(piezas_blancas, ubicacion_blancas, 'white')
opciones_negras=opciones(piezas_negras, ubicacion_negras, 'black')
run = True
while run:
    timer.tick(fps)
    if contador < 30:
        contador += 1
    else:
        contador = 0
    screen.fill('light blue') 
    dibujar_tablero()
    piezas()
    piezas_capturadas()
    jaque()
    if seleccion != 100:
        if (turn_step < 2 and seleccion < len(piezas_blancas)) or (turn_step >= 2 and seleccion < len(piezas_negras)):
            movimientos_validos = verificar_movimientos_validos()
            dibujar_movimientos_validos(movimientos_validos)
    for event in pygame.event.get():#obtiene info de lo que se hace con la 
    #compu, mouse, teclado etc.
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            cordenda_x = event.pos[0] // 100
            cordenada_y= event.pos[1] // 100 
            cordenadas_clicadas = (cordenda_x, cordenada_y)
            if turn_step <=1:
                if cordenadas_clicadas == (8, 8) or cordenadas_clicadas == (9, 8):
                    ganador = 'blancas'
                if cordenadas_clicadas in ubicacion_blancas:
                    seleccion = ubicacion_blancas.index(cordenadas_clicadas)
                    if turn_step == 0:
                     turn_step = 1
                if cordenadas_clicadas in movimientos_validos and seleccion != 100:
                    ubicacion_blancas[seleccion] = cordenadas_clicadas
                    if cordenadas_clicadas in ubicacion_negras:
                        pieza_negra = ubicacion_negras.index(cordenadas_clicadas)
                        piezas_capturadas_blancas.append(piezas_negras[pieza_negra])
                        if pieza_negra[pieza_negra] == 'rey':
                            ganador = 'blancas'
                        piezas_negras.pop(pieza_negra)
                        ubicacion_negras.pop(pieza_negra)
                        
                    opciones_negras=opciones(piezas_negras, ubicacion_negras, 'black')
                    opciones_blancas=opciones(piezas_blancas, ubicacion_blancas, 'white')
                    turn_step = 2
                    seleccion = 100
                    movimientos_validos = []
                    
            if turn_step > 1:
                if cordenadas_clicadas == (8, 8) or cordenadas_clicadas == (9, 8):
                    ganador = 'negras'
                if cordenadas_clicadas in ubicacion_negras:
                    seleccion = ubicacion_negras.index(cordenadas_clicadas)
                    if turn_step == 2:
                        turn_step = 3
                if cordenadas_clicadas in movimientos_validos and seleccion != 100:
                    ubicacion_negras[seleccion] = cordenadas_clicadas
                    if cordenadas_clicadas in ubicacion_blancas:
                        pieza_blanca = ubicacion_blancas.index(cordenadas_clicadas)
                        piezas_capturadas_negras.append(piezas_blancas[pieza_blanca])
                        if piezas_blancas[pieza_blanca] == 'rey':
                            ganador = 'negras'
                        piezas_blancas.pop(pieza_blanca)
                        ubicacion_blancas.pop(pieza_blanca)
                    opciones_blancas=opciones(piezas_blancas, ubicacion_blancas, 'white')
                    opciones_negras=opciones(piezas_negras, ubicacion_negras, 'black')
                    turn_step = 0
                    seleccion = 100
                    movimientos_validos = []
        if event.type == pygame.KEYDOWN and fin_juego:
            if event.key == pygame.K_RETURN:
                fin_juego = False
                ganador = ''
                piezas_blancas = ['torre','caballo','alfil', 'rey', 'reina','alfil', 'caballo', 'torre',
                  'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
                ubicacion_blancas= [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), 
                    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
                piezas_negras = ['torre','caballo','alfil', 'rey', 'reina','alfil', 'caballo', 'torre',
                  'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
                ubicacion_negras= [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), 
                    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6) ]
                piezas_capturadas_blancas = []
                piezas_capturadas_negras = []
                turn_step = 0
                seleccion = 100
                movimientos_validos = []
                opciones_negras = opciones(piezas_negras, ubicacion_negras, 'black')
                opciones_blancas = opciones(piezas_blancas, ubicacion_blancas, 'white')    
    if ganador != '':
        fin_juego = True
        pantalla_ganador()
    pygame.display.flip()
pygame.quit()