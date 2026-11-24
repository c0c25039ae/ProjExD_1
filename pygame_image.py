import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0

    rebg_img=pg.transform.flip(bg_img,True,False)
    
    tori_img=pg.image.load("fig/3.png")
    tori_img=pg.transform.flip(tori_img,True,False)

    tori_rct=tori_img.get_rect()
    tori_rct.center=300,200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%3200#練習５

        screen.blit(bg_img, [-x, 0])
        screen.blit(rebg_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])

        screen.blit(tori_img,tori_rct)
        key_lst=pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            tori_rct.move_ip((0,-1))
        elif key_lst[pg.K_DOWN]:
            tori_rct.move_ip((0,1))
        elif key_lst[pg.K_LEFT]:
            tori_rct.move_ip((-1,0))
        elif key_lst[pg.K_RIGHT]:
                tori_rct.move_ip((1,0))
        pg.display.update()
        tmr += 1        
        clock.tick(200)

        

        



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()