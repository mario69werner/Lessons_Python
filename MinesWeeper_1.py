import pygame as pg
from dataclasses import dataclass

auflösung = 1000
raster = 10
abstand = auflösung // raster

pg.init()
screen = pg.display.set_mode([auflösung, auflösung])
cell_normal = pg.transform.scale(pg.image.load('C:\Sprachen\Python\Lessons\Teil_10_ms_cell_normal.gif'), (abstand, abstand))
cell_marked = pg.transform.scale(pg.image.load('C:\Sprachen\Python\Lessons\Teil_10_ms_cell_marked.gif'), (abstand, abstand))
cell_mine = pg.transform.scale(pg.image.load('C:\Sprachen\Python\Lessons\Teil_10_ms_cell_mine.gif'), (abstand, abstand))
cell_selected = []
for n in range(9):
    cell_selected.append(pg.transform.scale(pg.image.load(f'C:\Sprachen\Python\Lessons\Teil_10_ms_cell_{n}.gif'), (abstand, abstand)))


anzMinen = 10
matrix = []

@dataclass
class Cell():
    spalte : int
    zeile : int
    mine : bool = False
    selected : bool = False
    flagged : bool = False
    anzMinenDrumrum : int = 0

    def show(self):
        pos = (self.spalte * abstand, self.zeile * abstand)
        if self.selected:
            if self.mine:
                screen.blit(cell_mine, pos)
            else:
                screen.blit(cell_selected[self.anzMinenDrumrum], pos)
        else: 
            if self.flagged:
                screen.blit(cell_marked, pos)
            else:
                screen.blit(cell_normal, pos)



pg.quit()

