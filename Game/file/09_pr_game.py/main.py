def game():
    return 873

score = game()
with open('Game/file/09_pr_game.py/hiscore.txt') as f:
    new_score = int(f.read())
    if new_score < score:
        with open('Game/file/09_pr_game.py/hiscore.txt' , 'w') as f:
           a=  f.write(str(score))
           
    else:
        pass
    



