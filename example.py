#usage: pyhton3 example.py

from CYK_Paser import Grammar

sentences = [
'The cat sat on the mat',
'She ate a sandwich for lunch',
'He ran to catch the bus',
'They watched a movie last night',
'The sun is shining brightly today',
'The flowers in the garden are blooming',
'The baby is sleeping peacefully',
'The car drove down the street',
'The students are studying for their exams',
'The dog barked loudly at the mailman',
'She danced gracefully across the stage',
'He cooked dinner for his family',
'They went on a hike in the mountains',
'The airplane flew over the ocean',
'The children played in the park all afternoon'
]

g = Grammar('grammar.txt')
for sentence in sentences:
    g.parse(sentence)
    g.print_parse_table()
# g.get_trees()
# print('')
# print('')
# print('')
