import random
import numpy as np


mutation_rate = 0.1

population_matrix = [['10100010','10100101'],['10011000','10010110'],['10101000','10111100'],['11101000','10100100']]
for i in population_matrix:
      for j in i:
        for k in j:
            print(k)
            if random.random() < mutation_rate:
                if k == '0':
                    k = '1'
                else:
                    k = '0'
