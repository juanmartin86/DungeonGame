# DungeonGame v1.1
# Copyright (c) 2014 Juan Martin
# Licensed under the MIT license
# http://www.opensource.org/licenses/mit-license.php

# -------------------------------- IMPORT BLOCK -------------------------------- # 

import random  # used for the random method to work
import os  # used in order to implement clrscr() function

def clrscr():  # function to clear the console, something similar to clrscr() we know from C++
  if os.name == "posix":  # compatible with Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):  # compatible with DOS/Windows
    os.system('CLS')
  
# -------------------------------- END OF IMPORT BLOCK -------------------------------- # 

# -------------------------------- VALIDATION FUNCTIONS  -------------------------------- # 

def validate_dungeon_idx(dungeon_idx):  # function to validate if the dungeon's index is an int and greater than 1, if it is, returns dungeon's index, otherwise, exits the program
  try:
    dungeon_idx = int(dungeon_idx) 
  except:
    print("That's not an int :( please try again")
    input("Press ENTER to continue and please LOAD the program again...")
    clrscr()
    exit()
  if dungeon_idx < 2: 
      print("That's less than 2 :( please try again")
      input("Press ENTER to continue and please LOAD the program again...")
      clrscr()
      exit()
  else:
    return dungeon_idx
    
def validate_dungeon_difficulty(dungeon_difficulty):  # function to validate if the dungeon's difficulty is EASY, MEDIUM or HARD, if it is, returns dungeon's index, otherwise, exits the program
  dungeon_difficulty = dungeon_difficulty.upper()
  if dungeon_difficulty != 'EASY' and dungeon_difficulty != 'MEDIUM' and dungeon_difficulty != 'HARD':  
    input("Sorry, You've entered an invalid difficulty, please load the program and try again. Press ENTER to continue...")
    #clrscr()
    exit()
  else:
    return dungeon_difficulty
  
# -------------------------------- END OF VALIDATION FUNCTIONS -------------------------------- #   

# -------------------------------- DUNGEON_SIZE FUNCTION -------------------------------- #   

def dungeon_size(dungeon_idx):  # function to set the dungeon's size
  dungeon_cells = []  # to save dungeon cells
  dungeon_limits = []  # to establish the walls located at the right

  for x_value in range(dungeon_idx):  # given the dungeon's index, it'll create the entire dungeon as tuples and will set the limits
    for y_value in range(dungeon_idx):
      dungeon_cells.append((x_value, y_value))  # here is where the tuples are created
    dungeon_limits.append(dungeon_idx*(x_value+1)-1)  # here is where the "walls" are created

  return dungeon_cells, dungeon_limits

# -------------------------------- END OF DUNGEON_SIZE FUNCTION -------------------------------- #   

# -------------------------------- WELCOME FUNCTION -------------------------------- #   

def welcome():  # function for the beginning of the program :)
  clrscr()
  print("Welcome to the dungeon game!")
  dungeon_idx = input("In order to get started, please select the size of the dungeon (e.g: 3 for a 3x3 dungeon; 4 for a 4x4 and so on...)"
             "\nNote: It has to be 2 or bigger..."
            "\nSize:")
  dungeon_idx = validate_dungeon_idx(dungeon_idx)
  clrscr()
  dungeon_difficulty = input("Alright! Now we have another thing to before we start the game! And that's the difficulty :)"
                             "\n These are the options:"
                             "\n EASY:"
                             "\n - The monster is visible as 'M' and moves around."
                             "\n - The door is visible as 'D'."
                             "\n - The player is visible as 'X'."
                             "\n MEDIUM:"
                             "\n - The monster is visible as 'M' and moves around."
                             "\n - The door is invisible."
                             "\n - The player is visible as 'X'."
                             "\n HARD:"
                             "\n - The monster is invisible, but appears as 'M' at random steps (from 1 to dungeon's size), moves around, follows the player's track and can sense if the player is next to him."
                             "\n - Bricks appear at random locations on the map in order to make it more difficult."
                             "\n - The door is invisible."
                             "\n - The player is visible as 'X'."
                             "\n Select Difficulty:")
  
  dungeon_difficulty = validate_dungeon_difficulty(dungeon_difficulty)
  
  return dungeon_idx, dungeon_difficulty

# -------------------------------- END OF WELCOME FUNCTION -------------------------------- # 

# -------------------------------- GET_LOCATIONS FUNCTION -------------------------------- #   

def get_locations():  # function to get the starting locations 
  monster = random.choice(cells)  # location for monster
  door = random.choice(cells)  # location for door
  start = random.choice(cells)  # locations for player
  brick_list = []  # brick list will always be empty if dungeon_difficulty is different from HARD
  flag_repeat_brick = 0  # flag to check if there's a repeated brick
  flag_blocking_brick = 0  # flag to check if there's a blocking brick
  
  if dungeon_difficulty == 'HARD' and dungeon_idx > 3:
    brick_limit_number = range(dungeon_idx)  # the number of bricks are limited by the dungeon's index.
    for bricks in brick_limit_number:  # here we create the bricks_list
      brick_list.append(random.choice(cells))
    # here we check is there's a value repeated in the list
    for bricks_1 in brick_limit_number:  # here we compare if there are repeated values inside the list.
      brick_count_repeat = 0
      brick_compare_repeat = brick_list[bricks_1]
      for bricks_2 in brick_limit_number:
        if brick_compare_repeat == brick_list[bricks_2]:  # if the compare value has a match, count it, the first count doesn't mean that the value is repeated, it could be comparing to itself.
          brick_count_repeat += 1
          if brick_count_repeat > 1:  # when there's more than 1 count, it means that the list has a value repeated.
            flag_repeat_brick = 1
    # here we check if there are bricks located diagonal to other bricks, or on top or below other bricks. 
    # usually when this happens could be that they will be blocking the player, monster or door, so we won't let that happen.
    for bricks_3 in brick_limit_number:
      x_axis, y_axis = brick_list[bricks_3]
      # diagonal comparisson variables
      brick_compare_diagonal_up_right = x_axis - 1, y_axis + 1
      brick_compare_diagonal_up_left = x_axis - 1, y_axis - 1
      brick_compare_diagonal_down_left = x_axis + 1, y_axis - 1
      brick_compare_diagonal_down_right = x_axis + 1, y_axis + 1
      # up, down, left and right comparisson variables
      brick_compare_up = x_axis - 1, y_axis
      brick_compare_down = x_axis + 1, y_axis
      brick_compare_left = x_axis, y_axis - 1
      brick_compare_right = x_axis, y_axis + 1
      for bricks_4 in brick_limit_number:
        if brick_compare_diagonal_up_right == brick_list[bricks_4] or brick_compare_diagonal_up_left == brick_list[bricks_4] or brick_compare_diagonal_down_right == brick_list[bricks_4] or brick_compare_diagonal_down_left == brick_list[bricks_4] or brick_compare_up == brick_list[bricks_4] or brick_compare_down == brick_list[bricks_4] or brick_compare_left == brick_list[bricks_4] or brick_compare_right == brick_list[bricks_4]:  # if there's a possible blocking brick, a flag will let us know
          flag_blocking_brick = 1
    
  if dungeon_difficulty != 'HARD' and (monster == door or monster == start or door == start):
    return get_locations()
  elif dungeon_difficulty == 'HARD' and (monster == door or monster == start or door == start or monster in brick_list or door in brick_list or start in brick_list or flag_repeat_brick == 1 or flag_blocking_brick == 1):
    return get_locations()
  
  return monster, door, brick_list, start

# -------------------------------- END OF GET_LOCATIONS FUNCTION -------------------------------- #   

# -------------------------------- MOVE_PLAYER AND MOVE_MONSTER FUNCTIONS -------------------------------- #   

def move_player(player, current_move): # function to move player and monster
  prev_position_player = player['current'] # to save the previous position of player and monster
  x, y = player['current']

  #player
  if current_move == 'LEFT':
    y -= 1
  elif current_move == 'RIGHT':
    y += 1
  elif current_move == 'UP':
    x -= 1
  elif current_move == 'DOWN':
    x += 1
    
  player = x, y

  return player, prev_position_player

def move_monster(monster, moves_monster):  # function to make the monster move
  prev_position_monster = monster
  u, v = monster
  
  #monster
  if dungeon_difficulty != 'HARD':
    monster_movement = random.choice(moves_monster) # monster makes a random choice based on his available movements
  
    if monster_movement == 'LEFT':
      v -= 1
    elif monster_movement =='RIGHT':
      v += 1
    elif monster_movement == 'UP':
      u -= 1
    elif monster_movement == 'DOWN':
      u += 1
  else:
    flag_up, flag_down, flag_left, flag_right = 0, 0, 0, 0  # a flag that tells us if there's a track
    count_flag_up, count_flag_down, count_flag_left, count_flag_right = 0, 0, 0, 0 # a flag that tells us if there's more than one track on the position
    aux_monster_trace_list = []  # auxiliar variable for monster's trace list that hast last fresh position 
    monster_trace_list = []  # monster's trace list
    # checking the surroundings for players' trace
    monster_up = u - 1, v
    monster_down = u + 1, v
    monster_left = u, v - 1
    monster_right = u, v + 1
    
    # here we check if there's an up trace
    if monster_up in player['trace_history']:
      flag_up = 1
      for idx, value in enumerate(player['trace_history']):
        if value == monster_up:
          aux_monster_trace_list = []  # resets aux_monster_trace_list
          count_flag_up += 1
          if count_flag_up > 1:
            aux_monster_trace_list = []  # resets aux_monster_trace_list
            aux_monster_trace_list.append((idx, monster_up)) #takes the last fresh position '.' of player
          else:
            aux_monster_trace_list.append((idx, monster_up)) #takes the first position if there's only one
      monster_trace_list.extend(aux_monster_trace_list)
    
    # here we check if there's a down trace
    if monster_down in player['trace_history']:
      flag_down = 1
      for idx, value in enumerate(player['trace_history']):
        if value == monster_down:
          aux_monster_trace_list = []  # resets aux_monster_trace_list
          count_flag_down += 1
          if count_flag_down > 1:
            aux_monster_trace_list = []  # resets aux_monster_trace_list
            aux_monster_trace_list.append((idx, monster_down)) #takes the last fresh position '.' of player
          else:
            aux_monster_trace_list.append((idx, monster_down)) #takes the first position of player if there's only one
      monster_trace_list.extend(aux_monster_trace_list)
    
    # here we check if there's a left trace
    if monster_left in player['trace_history']:
      flag_left = 1
      for idx, value in enumerate(player['trace_history']):
        if value == monster_left:
          aux_monster_trace_list = []  # resets aux_monster_trace_list
          count_flag_left += 1
          if count_flag_left > 1:
            aux_monster_trace_list = []  # resets aux_monster_trace_list
            aux_monster_trace_list.append((idx, monster_left)) #takes the last fresh position '.' of player
          else:
            aux_monster_trace_list.append((idx, monster_left)) #takes the first position if there's only one
      monster_trace_list.extend(aux_monster_trace_list)
    
    # here we check if there's a right trace
    if monster_right in player['trace_history']:
      flag_right = 1
      for idx, value in enumerate(player['trace_history']):
        if value == monster_right:
          aux_monster_trace_list = []  # resets aux_monster_trace_list
          count_flag_right += 1
          if count_flag_right > 1:
            aux_monster_trace_list = []  # resets aux_monster_trace_list
            aux_monster_trace_list.append((idx, monster_right)) #takes the last fresh position '.' of player
          else:
            aux_monster_trace_list.append((idx, monster_right)) #takes the first position if there's only one
      monster_trace_list.extend(aux_monster_trace_list)
    
    # if there aren't any traces, the monster makes a random movement
    if flag_up == 0 and flag_down == 0 and flag_left == 0 and flag_right == 0:
      monster_movement = random.choice(moves_monster)
      if monster_movement == 'LEFT':
        v -= 1
      elif monster_movement == 'RIGHT':
        v += 1
      elif monster_movement == 'UP':
        u -= 1
      elif monster_movement == 'DOWN':
        u += 1
    
    # if there are any traces, the monster moves to the latest trace
    if flag_up == 1 or flag_down == 1 or flag_left == 1 or flag_right == 1:
      flag_traces = 0  # this flag variable is used to let the most_recent_idx and most_recent_position 
                       # be saved for the first time in order to have something to compare with later (if there's more than 1 thing to compare)
      # here we compare all the traces in monster_trace_list and select the latest one based on its idx
      for traces in range(len(monster_trace_list)):
        if flag_traces == 0:
          most_recent_idx = monster_trace_list[traces][0]
          most_recent_position = monster_trace_list[traces][1]
          flag_traces = 1
        elif most_recent_idx < monster_trace_list[traces][0]:
          most_recent_idx = monster_trace_list[traces][0]
          most_recent_position = monster_trace_list[traces][1]
      u,v = most_recent_position
    
    # checking if new position of player is near monster in order for him to move towards player
    if monster_up == player['current']:
      u,v = monster_up
    elif monster_down == player['current']:
      u,v = monster_down
    elif monster_left == player['current']:
      u,v = monster_left
    elif monster_right == player['current']:
      u,v = monster_right
    
  monster = u,v
  
  return monster, prev_position_monster

# -------------------------------- END OF MOVE_PLAYER AND MOVE_MONSTER FUNCTIONS -------------------------------- #   

# -------------------------------- GET_MOVES FUNCTION -------------------------------- #   

def get_moves(player, monster, door, brick_list, dungeon_idx): # function to get the list of available movements of player and monster
  available_moves_player = ['LEFT', 'RIGHT', 'UP', 'DOWN'] # player's list of moves
  available_moves_monster = ['LEFT', 'RIGHT', 'UP', 'DOWN']# monster's list of moves
  
  #player's wall and brick limits
  if player['current'][1] == 0: # wall
    available_moves_player.remove('LEFT')
  elif (player['current'][0], player['current'][1]-1) in brick_list: # brick
    available_moves_player.remove('LEFT')
  if player['current'][1] == dungeon_idx-1: #wall
    available_moves_player.remove('RIGHT')
  elif (player['current'][0], player['current'][1]+1) in brick_list: # brick
    available_moves_player.remove('RIGHT')
  if player['current'][0] == 0: # wall
    available_moves_player.remove('UP')
  elif (player['current'][0]-1, player['current'][1]) in brick_list: # brick
    available_moves_player.remove('UP')
  if player['current'][0] == dungeon_idx-1:  # wall
    available_moves_player.remove('DOWN')
  elif (player['current'][0]+1, player['current'][1]) in brick_list: # brick
    available_moves_player.remove('DOWN')

  # monster's walls, door and brick limits (the monster can't enter the door, it's considered a wall)
  if monster[1] == 0: # wall
    available_moves_monster.remove('LEFT')
  elif (monster[0], monster[1]-1) == door: # door
    available_moves_monster.remove('LEFT')
  elif (monster[0], monster[1]-1) in brick_list:  # brick
    available_moves_monster.remove('LEFT')
  if monster[1] == dungeon_idx-1: # wall
    available_moves_monster.remove('RIGHT')
  elif (monster[0], monster[1]+1) == door: # door
    available_moves_monster.remove('RIGHT')
  elif (monster[0], monster[1]+1) in brick_list:  # brick
    available_moves_monster.remove('RIGHT')
  if monster[0] == 0: # wall
    available_moves_monster.remove('UP')
  elif (monster[0]-1, monster[1]) == door: # door
    available_moves_monster.remove('UP')
  elif (monster[0]-1, monster[1]) in brick_list:  # brick
    available_moves_monster.remove('UP')
  if monster[0] == dungeon_idx-1: # wall
    available_moves_monster.remove('DOWN')
  elif (monster[0]+1, monster[1]) == door: # door
    available_moves_monster.remove('DOWN')
  elif (monster[0]+1, monster[1]) in brick_list:  # brick
    available_moves_monster.remove('DOWN')
  return available_moves_player, available_moves_monster

# -------------------------------- END OF GET_MOVES FUNCTION -------------------------------- #   

# -------------------------------- DRAW_MAP FUNCTION -------------------------------- #   

def draw_map(): # function to draw the entire dungeon :) dungeon difficulty is more important than flag
  for roof in range(dungeon_idx):
    print(" _", end='') # to show the roof
  print("") #to give a space 

  tile = '|{}'

  for idx, cell in enumerate(cells):
    if idx not in dungeon_limits:
      if cell == player['current']:
        print(tile.format('X'), end='')  # show player
      elif cell == door and dungeon_difficulty == 'EASY':
        print(tile.format('D'), end='') # show door
      elif cell == monster and appearance_monster_flag == 1 or cell == monster and dungeon_difficulty != 'HARD':
          print(tile.format('M'), end='') # show monster
      elif cell in player['trace_history']: 
        print(tile.format('.'), end='') # show previous location of player
      elif dungeon_difficulty == 'HARD' and cell in brick_list:
        print(tile.format('O'), end='') # show's a brick if there's any
      else:
        print(tile.format('_'), end='')
    else:
      if cell == player['current']:
        print(tile.format('X|')) # show player
      elif cell == door and dungeon_difficulty == 'EASY':
        print(tile.format('D|')) # show door 
      elif cell == monster and appearance_monster_flag == 1 or cell == monster and dungeon_difficulty != 'HARD':
        print(tile.format('M|'))  # show monster
      elif cell in player['trace_history']:
        print(tile.format('.|')) # show previous location of player 
      elif dungeon_difficulty == 'HARD' and cell in brick_list:
        print(tile.format('O|')) # show's a brick if there's any
      else:
        print(tile.format('_|'))

# -------------------------------- END OF GET DRAW_MAP FUNCTION -------------------------------- #   

# -------------------------------- BEGINNING OF PROGRAM :) -------------------------------- #   

dungeon_idx, dungeon_difficulty = welcome() # gets the dungeon's size and difficulty

cells, dungeon_limits = dungeon_size(dungeon_idx) # create a dungeon based on the size given
player = {'current':'', 'trace_history':[]} # player dictionary with current position = 'current' with 1 value , and the complete trace history = 'trace_history' for the monster to track
brick_list = []  # list of bricks (only works on HARD difficulty)
appearance_monster_flag = 0  # variable that tells if the monster will appear or not (only works on HARD difficulty)
move_count = 0  # variable used to count the players movements in order to compare it to random_appearance, if they are equal, the monster will appear (only works on HARD difficulty)
random_appearance = random.randint(1,dungeon_idx)  # variable used to set in how many turns the monster will appear (only works on HARD difficulty)

monster, door, brick_list, player['current'] = get_locations()  # sets the locations for monster, door, brick_list and player

while True:
    clrscr()
    available_moves_player, moves_monster = get_moves(player, monster, door, brick_list, dungeon_idx)
    print("You're currently in room {}".format(player['current']))
    print("You can move {}".format(available_moves_player))
    print ("Enter QUIT to quit")

    draw_map()
    current_move = input("> ")
    current_move = current_move.upper()
    
    if current_move == 'QUIT':
      break

    if current_move in available_moves_player:
      if dungeon_difficulty == 'HARD':
        move_count += 1  # counts moves to compare to random_appearance, if there's a match between move_count and random appear, the monster will show up
        if move_count == random_appearance:
          appearance_monster_flag = 1  # this tells that there's a match
          random_appearance = random.randint(1,dungeon_idx)  # new random number to next turn after monster's appearance
          move_count = 0  # resets move_count
        else:
          appearance_monster_flag = 0  # no match
      player['current'], prev_position_player = move_player(player, current_move)  # moves player
      player['trace_history'].append(prev_position_player)  # updates player's positions
      monster, prev_position_monster = move_monster(monster, moves_monster)  # moves monster
    else:
      input("++ Oops! That can't be done! Try again :P ++"
            "\nPlease press ENTER to continue...")
      continue
    if player['current'] == door:
      print("You escaped!")
      break
    elif player['current'] == monster or (player['current'] == prev_position_monster and monster == prev_position_player): # 1st conditional: if the player and monster are at the same position # 2nd conditional(or): if monster and player encounter 
      print("You were eaten by the grue!")
      break

# -------------------------------- END OF PROGRAM -------------------------------- #   

