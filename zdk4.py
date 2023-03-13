def jednadzba_pravca(x1, y1, x2, y2):
    if x1 == x2:
        print("podijelit ce se s nulom u formuli kasnije a to se ne moze")    
    else:
        k = (y2 - y1) / (x2 - x1)
        n = y1 - k * x1

        print("Jednadžba pravca je y = {}x + {}".format(k, n))
jednadzba_pravca(1, 2, 3, 4)