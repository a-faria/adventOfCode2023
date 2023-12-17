def parse_input(input_lines):
    games_points = []
    for line in input_lines:
        round_points = 0
        # Split each line into game ID and subsets
        game_id, subsets = line.split(': ')
                
        # Split wins and bets by bar and parse each subset
        wins, bets = subsets.split('|')
        wins = list(map(int, wins.split()))
        bets = list(map(int, bets.split()))

        # loop trough wiining numbers and check if they're in the bets numbers
        for i in wins:
            if i in bets :
                #conditionals for the points
                if round_points==0:
                    round_points += 1
                else:
                    round_points *= 2
        # store the points from each game
        games_points.append(round_points)

    
      
    return games_points

# read input file
file_path = 'input_day4.txt'  

with open(file_path, 'r') as file:
    input_lines = file.readlines()
    
#call function and print sum
games_info = parse_input(input_lines)
print(sum(games_info))
