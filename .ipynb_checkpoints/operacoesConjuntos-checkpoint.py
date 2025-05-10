#a) Dados A = {0, 1, 2, 3} e B = {2, 3, 4, 5}, determine A ∪ B.
A = {0, 1, 2, 3}
B = {2, 3, 4, 5}
C = A|B # A u B
print("A u B = ", C) 

#b) Dados A = {- 1, 0, 2, 4, 5} e B = {- 2, - 1, 1, 3, 4, 6}, determine A - B e B - A.
A = {-1, 0, 2, 4, 5}
B = {-2, -1, 1, 3, 4, 6}
C = A - B # A menos B
D = B - A # B menos A
print("A - B = ", C)
print("B - A = ", D)

#c) Considere os conjuntos A = {0, 1, 2, 3, 4, 5, 6}, B = {1, 2}, C = {2, 3, 4} e D = {4, 5}, determine
# (A − B) ∩ (C ∩ D).
A = {1, 2, 3, 4, 5, 6}
B = {1, 2}
C = {2, 3, 4}
D = {4, 5}
E = A - B
F = C & D 
G = E & F
