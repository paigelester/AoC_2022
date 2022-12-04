from enum import Enum
from abc import ABC, abstractmethod

class ABCHandShapes(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

class XYZHandShapes(Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'

class HandShapes:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class RoundOutcomes:
    WIN = 6
    DRAW = 3
    LOSE = 0

class XYZRoundOutcomes:
    WIN = 'Z'
    DRAW = 'Y'
    LOSE = 'X'


def load_text_file(filepath):
    with open(filepath) as input_file:
        return input_file.read().splitlines()


class RockPaperScissorsRoundPlayer(ABC):
    @abstractmethod
    def play(self, player_input: str, opponent_input: str) -> int:
        raise NotImplementedError
    
    def _convert_input_to_hand_shape(self, input: str, input_type: Enum) -> HandShapes:
        if input == input_type['ROCK'].value:
            return HandShapes.ROCK

        if input == input_type['PAPER'].value:
            return HandShapes.PAPER

        return HandShapes.SCISSORS


class RockPaperScissorsClassicRoundPlayer(RockPaperScissorsRoundPlayer):
    def play(self, player_input: str, opponent_input: str) -> int:
        player_hand_shape: HandShapes = self._convert_input_to_hand_shape(player_input, XYZHandShapes)
        opponent_hand_shape: HandShapes = self._convert_input_to_hand_shape(opponent_input, ABCHandShapes)

        outcome_score = RoundOutcomes.WIN

        if player_hand_shape == opponent_hand_shape:
            outcome_score = RoundOutcomes.DRAW

        elif player_hand_shape == HandShapes.ROCK and opponent_hand_shape == HandShapes.PAPER:
            outcome_score = RoundOutcomes.LOSE
        
        elif player_hand_shape == HandShapes.PAPER and opponent_hand_shape == HandShapes.SCISSORS:
            outcome_score = RoundOutcomes.LOSE
        
        elif player_hand_shape == HandShapes.SCISSORS and opponent_hand_shape == HandShapes.ROCK:
            outcome_score = RoundOutcomes.LOSE

        return outcome_score + player_hand_shape

class RockPaperScissorsOutcomeRoundPlayer(RockPaperScissorsRoundPlayer):
    def play(self, player_input: str, opponent_input: str) -> int:
        opponent_hand_shape: HandShapes = self._convert_input_to_hand_shape(opponent_input, ABCHandShapes)

        if player_input == XYZRoundOutcomes.DRAW:
            return opponent_hand_shape + RoundOutcomes.DRAW
        
        outcome_score = RoundOutcomes.WIN if player_input == XYZRoundOutcomes.WIN else RoundOutcomes.LOSE
        
        player_hand_shape: HandShapes = HandShapes.SCISSORS

        if player_input == XYZRoundOutcomes.LOSE:
            if opponent_hand_shape == HandShapes.PAPER:
                player_hand_shape = HandShapes.ROCK
            if opponent_hand_shape == HandShapes.SCISSORS:
                player_hand_shape = HandShapes.PAPER

        if player_input == XYZRoundOutcomes.WIN:
            if opponent_hand_shape == HandShapes.SCISSORS:
                player_hand_shape = HandShapes.ROCK
            if opponent_hand_shape == HandShapes.ROCK:
                player_hand_shape = HandShapes.PAPER

        return outcome_score + player_hand_shape

def main():
    input_filepath = "input.txt"
    strategy_guide = load_text_file(input_filepath)

    part_1_total_score = 0
    part_2_total_score = 0

    for round_guide in strategy_guide:
        round_hand_shapes = round_guide.strip().split(" ")
        opponent_input = round_hand_shapes[0]
        player_input = round_hand_shapes[1]

        part_1_player = RockPaperScissorsClassicRoundPlayer()
        part_1_round_score = part_1_player.play(player_input, opponent_input)
        part_1_total_score += part_1_round_score

        part_2_player = RockPaperScissorsOutcomeRoundPlayer()
        part_2_round_score = part_2_player.play(player_input, opponent_input)
        part_2_total_score += part_2_round_score

    print("PART 1 TOTAL SCORE:", part_1_total_score)
    print("PART 2 TOTAL SCORE:", part_2_total_score)


if __name__ == "__main__":
    main()