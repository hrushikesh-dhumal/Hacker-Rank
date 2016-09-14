# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python
## Read the first line 
no_of_board_configurations = int(raw_input())

# Create a list of board_configurations
board_configurations = [None] * no_of_board_configurations

t = []

def read_snakes_or_ladders(text_list):
    keys = [None] * len(text_list)
    values = [None] * len(text_list)
    for ind in range(len(text_list)):
        t1 = text_list[ind].split(',')
        keys[ind] = float(t1[0])
        values[ind] = float(t1[1])
    return(dict(zip(keys, values)))

for i in range(no_of_board_configurations):
    
    # Data structure to store board configuration
    board_config = {'die_probability': [], 'num_ladder': None, 'num_snakes': None, 'ladders': {}, 'snakes': {}}

    # Read the next 4 lines
    # Store first line as die probability
    board_config['die_probability'] = [float(val) for val in raw_input().split(",")]
    
    # Store next line as number of ladders & number of snakes
    t = [int(val) for val in raw_input().split(",")]
    board_config['num_ladder'] = t[0]
    board_config['num_snakes'] = t[1]
    
    # Store the next line in ladders
    board_config['ladders'] = read_snakes_or_ladders(raw_input().split())
    
    # Store the next line in snakes
    board_config['snakes'] = read_snakes_or_ladders(raw_input().split())
    
    board_configurations[i] = board_config

import random

def die_roll(die_range):
    roll = random.random()    
    val = 0
    
    if (roll > 0.0) & (roll <= die_range[0]):
        val = 1
    elif  (roll > die_range[0]) & (roll <= die_range[1]):
        val = 2
    elif  (roll > die_range[1]) & (roll <= die_range[2]):
        val = 3
    elif  (roll > die_range[2]) & (roll <= die_range[3]):
        val = 4
    elif  (roll > die_range[3]) & (roll <= die_range[4]):
        val = 5
    elif  (roll > die_range[4]) & (roll <= 1):
        val = 6
    
    return(val)

no_of_games_to_simulate = 5000
roll_threshold = 1000

def accumu(lis):
    total = 0
    for x in lis:
        total += x
        yield total       

for board in board_configurations: # Boards
    die_range = list(accumu(board['die_probability'])) 
    time = []
    for sim_no in range(no_of_games_to_simulate): # Games on each board
        current_pos = 1
        roll_count  = 0
        while (roll_count < roll_threshold): # 1 game
            # Roll a die
            possible_pos = current_pos + die_roll(die_range)
            roll_count = roll_count + 1
            
            if (possible_pos < 100):
                new_pos = possible_pos
            elif (possible_pos == 100):
                time.append(roll_count)
                break
            elif (possible_pos > 100):
                continue           
            
            # Check where if new pos is ladder or snake
            ladder_pos  = board['ladders'].get(new_pos)
            if ladder_pos:
                new_pos = ladder_pos
            else:
                snake_pos  = board['snakes'].get(new_pos)
                if snake_pos:
                    new_pos = snake_pos
                
            # Update current pos
            current_pos = new_pos
            if (current_pos == 100):
                time.append(roll_count)
                break 
                
    print str(int(sum(time) /  len(time)))