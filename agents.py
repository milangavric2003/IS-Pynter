import random
import time

# pip install pygame screeninfo
# python -m pip install pygame screeninfo

class Agent:
    ident = 0

    def __init__(self):
        self.id = Agent.ident
        Agent.ident += 1

    def get_chosen_action(self, state, max_depth):
        pass


class RandomAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        actions = state.get_legal_actions()
        return actions[random.randint(0, len(actions) - 1)]


class GreedyAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        actions = state.get_legal_actions()
        best_score, best_action = None, None
        for action in actions:
            new_state = state.generate_successor_state(action)
            score = new_state.get_score(state.get_on_move_chr())
            if (best_score is None and best_action is None) or score > best_score:
                best_action = action
                best_score = score
        return best_action


def state_evaluation(state, old_state, depth):
    if depth % 2 == 1:
        return state.get_score(old_state.get_on_move_chr())
    else:
        return -state.get_score(old_state.get_on_move_chr())

def id_minimax(state, depth, max_depth, old_state):

    if depth == max_depth:
        return state_evaluation(state, old_state, depth)

    best_action = None

    if depth % 2 == 0:
        # MAX player
        score = float('-inf')
        best_score = None
        for action in state.get_legal_actions():
            new_state = state.generate_successor_state(action)
            score = max(score, id_minimax(new_state, depth + 1, max_depth, state))
            if (best_score is None and best_action is None) or score > best_score:
                best_action = action
                best_score = score
        if depth == 0 : return best_action
        return score
    else:
        # MIN player
        score = float('inf')
        best_score = None
        for action in state.get_legal_actions():
            new_state = state.generate_successor_state(action)
            score = min(score, id_minimax(new_state, depth + 1, max_depth, state))
            if (best_score is None and best_action is None) or score < best_score:
                best_action = action
                best_score = score
        if depth == 0 : return best_action
        return score

class MinimaxAgent(Agent):

    def get_chosen_action(self, state, max_depth):
        print(type(self))
        time.sleep(0.5)
        return id_minimax(state, 0, max_depth, state)



