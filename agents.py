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
    estimatedScore = state.get_score(old_state.get_on_move_chr()) - state.get_score(state.get_on_move_chr())
    return estimatedScore if depth % 2 == 1 else -estimatedScore

def minimax(state, depth, max_depth, old_state):
    if depth == max_depth or state.is_goal_state():
        return state_evaluation(state, old_state, depth)

    best_action = None
    if depth % 2 == 0:
        # MAX player
        score = float('-inf')
        best_score = None
        for action in state.get_legal_actions():
            new_state = state.generate_successor_state(action)
            score = max(score, minimax(new_state, depth + 1, max_depth, state))
            if (best_score is None and best_action is None) or score > best_score:
                best_action = action
                best_score = score
        return best_action if depth == 0 else score
    else:
        # MIN player
        score = float('inf')
        best_score = None
        for action in state.get_legal_actions():
            new_state = state.generate_successor_state(action)
            score = min(score, minimax(new_state, depth + 1, max_depth, state))
            if (best_score is None and best_action is None) or score < best_score:
                best_action = action
                best_score = score
        return best_action if depth == 0 else score

class MinimaxAgent(Agent):

    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        return minimax(state, 0, max_depth, None)

def minimaxAB(state, depth, max_depth, old_state, a, b):
    if depth == max_depth or state.is_goal_state():
        return state_evaluation(state, old_state, depth)

    best_action = None
    if depth % 2 == 0:
        # MAX player
        score = float('-inf')
        best_score = None
        for action in state.get_legal_actions():
            new_state = state.generate_successor_state(action)
            score = max(score, minimaxAB(new_state, depth + 1, max_depth, state, a, b))
            if (best_score is None and best_action is None) or score > best_score:
                best_action = action
                best_score = score
            # alpha update
            a = max(a, score)
            if a >= b: break

        return best_action if depth == 0 else score
    else:
        # MIN player
        score = float('inf')
        best_score = None
        for action in state.get_legal_actions():
            new_state = state.generate_successor_state(action)
            score = min(score, minimaxAB(new_state, depth + 1, max_depth, state, a, b))
            if (best_score is None and best_action is None) or score < best_score:
                best_action = action
                best_score = score
            # beta update
            b = min(b, score)
            if a >= b: break

        return best_action if depth == 0 else score

class MinimaxABAgent(Agent):

    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        return minimaxAB(state, 0, max_depth, state, float('-inf'), float('inf'))



