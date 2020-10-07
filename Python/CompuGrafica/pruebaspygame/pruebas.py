import pygame as pyg

if __name__ == "__main__":
    pyg.init()
    pantalla = pyg.display.set_mode([1000,600])

    position = [200,250]

    fin = False
    while(not fin):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                fin = True

            if event.type == pyg.MOUSEBUTTONDOWN:
                print (event.pos, event.button)
                position = event.pos

            if event.type == pyg.MOUSEMOTION:
                #print (event.pos, event.rel, event.buttons) 
                posmouse = event.pos

        pantalla.fill([0,0,0])
        pyg.draw.line(pantalla, [0,250,0], [100,100], position)
        pyg.draw.circle(pantalla, [250,0,0], posmouse, 20, 1)
        pyg.display.flip()        
                

    print("Fin del programa")        

 