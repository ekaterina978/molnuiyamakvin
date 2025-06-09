import heapq
def dijkstra(graf, spisok_vershin, start):
    rasstoyaniya = {v: float('inf') for v in spisok_vershin}
    rasstoyaniya[start] = 0
    ochered = [(0, spisok_vershin.index(start))]
    
    while ochered:
        tekush_rasst, tekush_ind = heapq.heappop(ochered)
        tekush_versh = spisok_vershin[tekush_ind]
        if tekush_rasst > rasstoyaniya[tekush_versh]:
            continue
        for sosed, ves_rebra in graf[tekush_ind]:
            novoe_rasst = tekush_rasst + ves_rebra
            if novoe_rasst < rasstoyaniya[sosed]:
                rasstoyaniya[sosed] = novoe_rasst
                heapq.heappush(ochered, (novoe_rasst, spisok_vershin.index(sosed)))
    
    return rasstoyaniya
graf = [
    [('X', 4), ('Y', 1)],  #S
    [('Y', 1), ('Z', 2)],   #X
    [('X', 1), ('Z', 5)],   #Y
    [('K', 3)],             #Z
    []                      #K
]

vershiny = ['S', 'X', 'Y', 'Z', 'K']

startovaya = 'S'
itog = dijkstra(graf, vershiny, startovaya)

print("Кратчайшие расстояния от S:")
for vershina, rast in itog.items():
    print(f"{vershina}: {rast if rast != float('inf') else '∞'}")
