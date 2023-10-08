def hanoi(nDisk, from_rod, to_rod, aux_rod):
    if nDisk == 1:
        return
    hanoi(nDisk-1, from_rod, aux_rod, to_rod)
    hanoi(nDisk, from_rod, to_rod, aux_rod)
    hanoi(nDisk-1, aux_rod, to_rod, from_rod)