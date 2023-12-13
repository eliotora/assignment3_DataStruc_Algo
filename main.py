from math import floor, e
from random import shuffle, seed
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np


def selection(alpha, candidates):
    interview = candidates[:floor(alpha * len(candidates))]
    best_seen = max(interview)
    for candidate in candidates[floor(alpha * len(candidates)) + 1:]:
        if candidate > best_seen:
            return candidate
    return None


if __name__ == '__main__':
    n = 1000
    it_nbr = 10000
    successes = []
    for j in tqdm(range(n-1)):
        fraction = (j + 1) / n
        seed(j)
        candidates = [i for i in range(n)]
        success = 0
        for i in range(it_nbr):
            shuffle(candidates)
            if selection(fraction, candidates) == n - 1:
                success += 1
        successes.append(success / it_nbr)
    print('Successes: ', successes)
    plt.plot(np.arange(n-1)/(n-1), successes, "b.")
    plt.plot((1/e, 1/e),(0, 0.45), "r-")
    plt.plot((0, 1), (1 / np.e, 1 / np.e), "r-")
    plt.ylabel("Frequency of success")
    plt.xlabel("Fraction of candidate interviewed before considering hire")
    plt.title("Frequency of success in function of the fraction \nof candidate interviewed before considering hire")
    plt.show()
