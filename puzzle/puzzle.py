# Done as part of Cs50ai

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    #A is either a Knight or a Knave but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    #A is a knight if A is both a Knight and a Knave
    Implication(AKnight,And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    #A is either a Knight or a Knave but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    #B is either a Knight or a Knave but not both
    Or(BKnight,BKnave),
    Not(And(BKnight,BKnave)),

    #A is a Knight if both A and B are Knaves
    Implication(AKnight, And(AKnave, BKnave)),
    #B is a Knave is A is a Knight
    Implication(BKnave, AKnight),
    Implication(BKnave, Or(AKnight,AKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    #A is either a Knight or a Knave but not both
    Or(AKnight, AKnave),
    Not(And(AKnight,AKnave)),

    #B is either a Knight or a Knave but not both
    Or(BKnight,BKnave),
    Not(And(BKnight,BKnave)),

    #A is a Knight if both A and B are of the same kind
    Implication(AKnight, And(BKnave,AKnave)),
    Implication(AKnight, And(AKnight,BKnight)),
    #B is a Knave is A is a Knight 
    Implication(BKnave, AKnight)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    #A is either a Knight or a Knave but not both
    Or(AKnight, AKnave),
    Not(And(AKnight,AKnave)),

    #B is either a Knight or a Knave but not both
    Or(BKnight,BKnave),
    Not(And(BKnight,BKnave)),

    #C is either a Knight or a Knave but not both
    Or(CKnight,CKnave),
    Not(And(CKnight,CKnave)),

    #B is a Knight if A is not a Knight or a Knave
    Implication(BKnight, Not(Or(AKnight,AKnave))),
    #B is a Knight if A is a Knight and C is a Knave
    Implication(BKnight, And(AKnave,CKnave)),
    #C is a Knave if B is a Knight
    Implication(CKnave, BKnight),
    #A is a Knave if B is a Knight
    Implication(AKnave, BKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()