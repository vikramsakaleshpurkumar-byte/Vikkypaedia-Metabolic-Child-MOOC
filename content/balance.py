from gen import move_answer
# (unit, checkpoint index, new position of the correct option) — balances the key to 10/10/10/10
MOVES = [(4,0,0),(7,1,0),(10,1,0),(17,0,0),(20,0,0),
         (5,1,2),(9,0,2),(11,1,2),(14,1,2),(18,1,2),
         (1,1,3),(4,1,3),(6,0,3),(7,0,3),(9,1,3),(11,0,3),(14,0,3),(18,0,3),(19,0,3)]
for n, qi, t in MOVES:
    move_answer(n, qi, t)
