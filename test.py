def fenetre_cible(nombres: list[int], cible: int) -> list[int]:
    debut = 0
    somme = 0
    
    for fin in range(len(nombres)):
        somme += nombres[fin]
        
        while somme > cible and debut <= fin:
            somme -= nombres[debut]
            debut += 1
    
        if somme == cible:
            return [debut,fin]
        
    return [-1,-1]
    
print(fenetre_cible([1, 3, 2, 5, 1, 1], 8)) # [2, 4]
print(fenetre_cible([4, 2, 6], 6)) # [0, 1]
print(fenetre_cible([1, 2, 3], 7)) # [-1, -1] (aucune fenêtre)
print(fenetre_cible([5], 5)) # [0, 0] (un seul élément)
print(fenetre_cible([1, 1, 1, 1], 3)) # [0, 2]
print(fenetre_cible([10, 1, 2, 3], 6)) # [1, 3] (le 10 est retiré)
print(fenetre_cible([2, 4], 1)) # [-1, -1] (cible plus petite que tout)
