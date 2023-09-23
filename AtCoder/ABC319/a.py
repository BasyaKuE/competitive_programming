from typing import List

players: str = """tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481
"""
players_list: List[str] = players.split()
S: str = input()
player_index: int = players_list.index(S)
rate: str = players_list[player_index+1]
print(rate)
