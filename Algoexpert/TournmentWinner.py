# -------   solution 1 

def tournamentWinner(competitions, results):
    # Write your code here.
    scores = {} # Dictionary to store the scores of each team
    max_score = 0  # Variable to keep track of the maximum score
    winner = ''   # Variable to store name of winner 

    for i in range(len(competitions)):
        home_team,away_team = competitions[i]

        winning_team = home_team if results[i] == 1 else away_team

        if winning_team not in scores:
            scores[winning_team] = 3
        else:
            scores[winning_team] += 3

        if scores[winning_team] > max_score:
            max_score = scores[winning_team]
            winner = winning_team
    return winner
    
    
    
    
# -------   solution 2

HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx,competition in enumerate(competitions):
        result = results[idx]

        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3 , scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam

def updateScores(team, points, scores):

    if team not in scores:
        scores[team] = 0

    scores[team] += points
    
    
