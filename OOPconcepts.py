class Player:
    def __init__(self, name:str, score:int = 0) -> None:
        self.name = name      
        self.score = score
        
    @property
    def score(self) -> int:
            return self._score
        
    @score.setter
    def score(self, value:int) -> None:
            if value < 0:
                raise ValueError("Score can not be negative")
            self._score = value
    
    @classmethod
    def new_player(cls, name:str = "", score:int = 0) -> "Player":
        return cls(name, score)
    
    @staticmethod
    def valid_points(points:int) -> bool:
        return points in (1, 2, 3)
    
    def scoring_message(self, points:int) -> None:
        if points == 2:
            print(f'{self.name} just scored a two pointer!')
        elif points == 3:
            print(f'{self.name} just scored a three pointer!')
        else:
            print(f'{self.name} just made a free throw!')
    
    def scores(self, points:int) -> None:
        if not self.valid_points(points):
            print("Points must be 1, 2, or 3")
            return
    
        self.scoring_message(points)
            
        self.score += points
    
    def __gt__(self, other) -> bool:
        return self.score > other.score

    
    def __str__(self) -> str:
        return f"{self.name} is having {self.score} points right now"

class Star(Player):
    def __init__(self, name, score, ranking) -> None:
        super().__init__(name, score)
        self.ranking = ranking
    
    def __str__(self) -> str:
        return f"{self.name} {self.ranking}"
    
    def scoring_message(self, points:int) -> None:
        if points == 2:
            print(f'SUPERSTAR {self.name} just scored a two pointer!')
        elif points == 3:
            print(f'SUPERSTAR {self.name} just scored a three pointer!')
        else:
            print(f'SUPERSTAR {self.name} just made a free throw!')
    
    @classmethod
    def new_player(cls, name:str, ranking:int, score:int = 0) -> "Player":
        return cls(name, score, ranking)
    
class Team:
    def __init__(self, 
                 name:str, 
                 city:str,
                 coach:str | None = None,
                 players:list[Player] | None = None,
                 games_won:int = 0, 
                 games_lost:int = 0
                 ) -> None:
        self.name = name
        self.city = city
        self.coach = coach
        if players is None:
            self.players = []
        else:
            self.players = players
        self.games_won = games_won
        self.games_lost = games_lost
    
    def __str__(self) -> str:
        return f"{self.city} {self.name}"
        
    def won(self) -> None:
        self.games_won +=1
        print(f'{self.name} has won the game!')
        
    def lost(self) -> None:
        self.games_lost +=1
        print(f'{self.name} has lost the game!')
    
    def games_played(self) -> int:
        return self.games_won + self.games_lost
    
    def total_points(self) -> int:
        pts = 0
        for player in self.players:
            pts += player.score
        return pts
    
    def highest_scoring_player(self) -> Player | None:
        if not self.players:
            print("there is currently no players on the team")
            return
        
        max_score_player = self.players[0]
        for player in self.players[1:]:
            if player.score > max_score_player.score:
                max_score_player = player
        return max_score_player
    
    def add_player(self, player:Player) -> None:
        self.players.append(player)
        
class Match:
    def __init__(self, home_team:Team, away_team:Team, is_finished:bool = False, home_score:int = 0, away_score:int = 0) -> None:
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score 
        self.is_finished = is_finished
        
    @property
    def home_score(self) -> int:
        return self._home_score
    
    @property
    def away_score(self) -> int:
        return self._away_score
    
    @home_score.setter
    def home_score(self, value:int) -> None:
        if value < 0:
            raise ValueError("Score can not be negative")
        self._home_score = value
        
    @away_score.setter
    def away_score(self, value:int) -> None:
        if value < 0:
            raise ValueError("Score can not be negative")
        self._away_score = value
        
    def record_score(self, player:Player, points:int) -> None:
        if self.is_finished:
            raise RuntimeError("The game is already finished, no more score can be recorded")
        
        if points not in (1, 2, 3):
            print("Points must be 1, 2, or 3")
            return
        
        if player in self.home_team.players:
            self.home_score += points
            player.scores(points)
        elif player in self.away_team.players:
            self.away_score += points
            player.scores(points)
        else:
            print("player not in this match")
            
    def winner(self) -> Team | None:
        if self.is_finished:
            if self.home_score > self.away_score:
                print(f"Winner is {self.home_team}")
                return self.home_team
                
            elif self.home_score < self.away_score:
                print(f"Winner is {self.away_team}")
                return self.away_team
        
        else:
            print("The game hasn't finished yet")
            return
            
    def leading_team(self) -> Team | None:
        if not self.is_finished:
            if self.home_score > self.away_score:
                print(f"The leading team is {self.home_team}")
                return self.home_team
            elif self.home_score < self.away_score:
                print(f"The leading team is {self.away_team}")
                return self.away_team
            else:
                print("The game is currently tied")
                return
        
        else:
            print("The game is already finished")
            return
            
    def end_game(self) -> None:
        if self.is_finished:
            print("The game is already finished!")
            return
        
        if self.home_score == self.away_score:
            raise ValueError("The game can't be finished if it's tied")
        
        self.is_finished = True
        if self.home_score > self.away_score:
            self.home_team.won()
            self.away_team.lost()
        else:
            self.home_team.lost()
            self.away_team.won()
            
player = Player("Tatum")

try:
    player.score = -10
except ValueError as e:
    print(f"Invalid value: {e}")
    














# jayson_tatum = Player(name="Jayson Tatum")
# derrick_white = Player("Derrick White")
# paul_george = Player("Paul George")
# payton_pritchard = Player("Payton Pritchard")
# nemsis_queta = Player("Nemesis Queta")

# boston_celtics = Team(name="Celtics",
#                       city="Boston", 
#                       coach="Joe Mazulla", 
#                       players=[jayson_tatum,
#                                derrick_white, 
#                                payton_pritchard, 
#                                paul_george, 
#                                nemsis_queta
#                                ]
#                       )

# tyrese_maxey = Player("Tyrese Maxey")
# jaylen_brown = Player("Jaylen Brown")
# lebron_james = Player("LeBron James")
# joel_embiid = Player("Joel Embiid")
# v_j_edgecombe = Player("VJ Edgecombe")

# philadelphia_76ers = Team(
#     name="76ers",
#     city="Philadelphia",
#     coach="Nick Nurse",
#     players=[
#         tyrese_maxey,
#         jaylen_brown,
#         lebron_james,
#         joel_embiid,
#         v_j_edgecombe
#     ]
# )

# celtics_vs_76ers = Match(boston_celtics, philadelphia_76ers)

# celtics_vs_76ers.record_score(jayson_tatum, 3)
# celtics_vs_76ers.record_score(jayson_tatum, 3)
# celtics_vs_76ers.record_score(jayson_tatum, 2)
# celtics_vs_76ers.record_score(lebron_james, 2)

# celtics_vs_76ers.leading_team()

# celtics_vs_76ers.end_game()

# celtics_vs_76ers.leading_team()
# celtics_vs_76ers.winner()

# Star.new_player("Wemby", 2)