
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_

:date: 2017, march

"""

from game_2048 import *

commands = { "U" : "up", "L" : "left", "R" : "right", "D" : "down" }
options=['c','s','a']
choix=['s','n']
thème=['chimie','classique']


def choix_jeu():
    """
    """

    g=input('Voulez-vous charger une partie sauvegardée(s), ou commencer un nouveau jeu(n)')
    while g not in choix:
        g=input('Choisissez s ou n')
        g=g.lower()
    if g=='n':
        play()
    elif g=='s':
        play_sauvegarde()


def read_next_move():
    """
    read a new move

    :UC: none
    """
    m=input ('Your Move ? ((U)p, (D)own, (L)eft, (R)ight) ')
    m=m.upper()

    while m not in commands :
        m=input ('Your Move ? ((U)p, (D)own, (L)eft, (R)ight) ')
        m=m.upper()

    return(m)


def play():
    """
    main game procedure

    """
    m=input('choisissez votre thème(chimie,classique)')
    while m not in thème:
        m=input('Choisissez votre thème(chimie,classique)')
    grid = grid_init()
    grid_print(grid,m)
    i=0
    while  (is_grid_over(grid)== False) and (grid_get_max_value(grid) < 2048):
        score=grid_score(grid)
        print('Votre score  actuel est de ',score)
        move = read_next_move()

        if grid!=grid_move(grid,commands[move]):
            grid=grid_move(grid, commands[move])
            grid_add_new_tile(grid)
        grid_print(grid,m)

        i+=1
        if  i % 10 == 0:
            z=input('continuer(c), arreter(a) ou sauvegarder(s) après 15 tours').lower()
            while z not in options:
                z=input("Souhaitez-vous continuer(c), arreter(a) ou sauvegarder(s) ?").lower()

            if z=='a':
                break
            elif z =='s':
                n=input('Choisissez le nom du fichier pour enregistrer la partie : ')
                save(grid,n)
                break

    if grid_get_max_value(grid) == 2048:
            print("You Won !!")
            score=grid_score(grid)
            print('Votre score pour cette partie est de ',score)

    elif is_grid_over(grid)==True:
            print("You Lose ;-(")
            score=grid_score(grid)
            print('Votre score pour cette partie est de ',score)


def play_sauvegarde():
    """
    main game procedure

    """
    s=input('Choisissez le nom du fichier jeu sauvegardé à charger')
    grid = load(s)
    grid_print(grid)
    i=0
    while not is_grid_over(grid) and grid_get_max_value(grid) < 2048:
        score=grid_score(grid)
        print('Votre score  actuel est de',score)
        move = read_next_move()
        if grid!=grid_move(grid,commands[move]):
            grid=grid_move(grid, commands[move])
            grid_add_new_tile(grid[move])
        grid_print(grid)


        i+=1
        if  i % 10 == 0:
            g=input('Continuer(c),arreter(a) ou sauvegarder(s) après 10 tours')
            while g not in options:
                g=input("Souhaitez vous continuer(c),arreter(a) ou sauvegarder(s) ?")

            if g=='a':
                break
            elif g =='s':
                n=input('Choisissez le nom du fichier où sauvegarder la partie : ')
                save(grid,n)
                break

    if grid_get_max_value(grid) == 2048:
            print("You Won !!")
            score=grid_score(grid)
            print('Votre score dans ce jeu est de',score)

    elif is_grid_over(grid)==True:
            print("You Lose ;-(")
            score=grid_score(grid)
            print('Votre score dans ce jeu est de',score)




def usage():
    print('Usage : {:s}'.format(sys.argv[0]))
    exit(1)

if __name__ == '__main__':
    import sys
    choix_jeu()
    exit(0)

