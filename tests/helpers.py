"""Small fakes and builders shared by the tests."""
from game.game import Game
from player.player import Player
from question.question import Question
from room.room import Room


class FakeQuestions:
    """Stands in for QuestionDAO: returns whatever question it was given."""

    def __init__(self, question=None):
        self.question = question
        self.calls = []

    def load_question(self, room, difficulty, character):
        self.calls.append((room, difficulty, character))
        return self.question


def make_question(answer="4", hint=None):
    return Question(1, "Start", 1, "What is 2+2?", answer, hint)


def make_player():
    return Player("Hal Jordan", "2814", "Fearless", "Reckless")


def make_rooms():
    return {
        "Start": Room("Start", "A plain room.", {"east": "Vault"},
                      ["Spare Battery", "Lens of Will"], False, None, ["lens of will"]),
        "Vault": Room("Vault", "A locked vault.", {"west": "Start"}, [], True, ["lens of will"]),
    }


def make_game(question=None):
    return Game(make_player(), 1, make_rooms(), FakeQuestions(question), "Start")
