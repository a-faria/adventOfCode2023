def parse_subset(subset_str):
    # Split the subset string by comma and extract cube details
    cubes = subset_str.split(', ')
    cubes_info = {}
    for cube in cubes:
        num, color = cube.split()
        cubes_info[color] = int(num)
    return cubes_info

def parse_input(input_lines):
    games_data = {}
    for line in input_lines:
        # Split each line into game ID and subsets
        game_id, subsets = line.split(': ')
        game_id = int(game_id.split()[1])  # Extract game ID number
        
        # Split subsets by semicolon and parse each subset
        subsets = subsets.split('; ')
        game_subsets = [parse_subset(subset) for subset in subsets]
        
        # Store subsets for each game ID
        games_data[game_id] = game_subsets
        
    return games_data

# read input file
file_path = 'input_day2.txt'  

with open(file_path, 'r') as file:
    input_lines = file.readlines()
    

games_info = parse_input(input_lines)

#create temp game list
valid_games = []
for i in range (1,101):
    valid_games.append(i)

#iterate trough each subset and if any of the  
for game_id, subsets in games_info.items():       
    for subset in subsets:  
        # if any sets has more cubes than the possible amount remove them from valid list              
        if subset.get("red",0) > 12 or subset.get("green",0)> 13 or subset.get("blue",0)> 14:
            if game_id in valid_games:
                valid_games.remove(game_id)

#add all valid games
print(sum(valid_games))