import string
from random import randint

class BoggleBoard:

  alphabet = string.ascii_uppercase
  board = []
  underscore = "__ __ __ __\n__ __ __ __\n__ __ __ __\n__ __ __ __"
  die = {
    1: ['A', 'A', 'E', 'E', 'G', 'N'],
    2: ['E', 'L', 'R', 'T', 'T', 'Y'],
    3: ['A', 'O', 'O', 'T', 'T', 'W'],
    4: ['A', 'B', 'B', 'J', 'O', 'O'],
    5: ['E', 'H', 'R', 'T', 'V', 'W'],
    6: ['C', 'I', 'M', 'O', 'T', 'U'],
    7: ['D', 'I', 'S', 'T', 'T', 'Y'],
    8: ['D', 'E', 'I', 'L', 'R', 'X'],
    9: ['E', 'I', 'O', 'S', 'S', 'T'],
    10:['D', 'E', 'L', 'R', 'V', 'Y'],
    11:['A', 'C', 'H', 'O', 'P', 'S'],
    12:['H', 'I', 'M', 'N', 'Qu', 'U'],
    13:['E', 'E', 'I', 'N', 'S', 'U'],
    14:['E', 'E', 'G', 'H', 'N', 'W'],
    15:['A', 'F', 'F', 'K', 'P', 'S'],
    16:['H', 'L', 'N', 'N', 'R', 'Z'],
  }
  
  def randomize_die(self):
    die_order = []
    while len(die_order) < 16:
      for i in self.die:
        random_index = randint(1,16)
        if self.die[random_index] not in die_order:
          die_order.append(self.die[random_index])
    return die_order

  def __init__(self, alphabet=alphabet, board=board, initialized=True):
    self.alphabet = alphabet
    self.board = board
    if initialized:
      print(self.underscore)

  def shake(self):
    self.board = []
    self.initialized = False
    
    randomized = self.randomize_die()

   

    for i in randomized:
     
      self.board.append(i[randint(0,5)])


   

    scrambled_board = ""
    temp = ""

    for i in range(16):
      if self.board[i] == "Qu":
        temp += f"{self.board[i]} "
      else: 
        temp += f"{self.board[i]}  "
      if i % 4 == 3:
        scrambled_board += f"\n{temp}"
        temp = ""

    return scrambled_board
