import nltk
from nltk.parse.generate import generate

# Define the CFG
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> V | V NP | V PP | Adv V NP
    NP -> PN | Det N | Det Adj N
    PP -> P NP
    Det -> 'the' | 'a'
    Adj -> 'green' | 'tall' | 'happy'
    PN -> 'John' | 'Mary' | 'Bob'
    N -> 'dog' | 'tree' | 'car'
    V -> 'runs' | 'jumps' | 'eats' | 'drives' | 'sleeps'
    P -> 'to' | 'over' | 'under' | 'through'
    Adv -> 'quickly' | 'silently'
""")

# Generate and print 15 random sentences
for i, sentence in enumerate(generate(grammar, depth=5)):
    if i == 15:
        break
    print(f"{i+1}. {' '.join(sentence)}")
