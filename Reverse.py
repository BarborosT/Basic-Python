"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

"""


g = [[1, 2], [3, 4], [5, 6, 7]]
g.reverse()
for i in range(len(g)):
    (g[i]) = (g[i]) [::-1]

print(g)