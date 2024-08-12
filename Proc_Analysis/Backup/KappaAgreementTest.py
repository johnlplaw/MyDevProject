import itertools

from sklearn.metrics import cohen_kappa_score
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

def calculate_Cohen_Kappa_Score(raters):

    data = np.zeros((len(raters), len(raters)))
    # Calculate cohen_kappa_score for every combination of raters
    # Combinations are only calculated j -> k, but not k -> j, which are equal
    # So not all places in the matrix are filled.
    for j, k in list(itertools.combinations(range(len(raters)), r=2)):
        data[j, k] = cohen_kappa_score(raters[j], raters[k])

    print(data)
    return data

def platHeatMapKappaScore(data):
    sns.heatmap(
        data,
        mask=np.tri(len(raters)),
        annot=True, linewidths=5,
        vmin=0, vmax=1,
        xticklabels=[f"Rater {k + 1}" for k in range(len(raters))],
        yticklabels=[f"Rater {k + 1}" for k in range(len(raters))],
    )
    plt.show()

# Note that I updated the numbers so all Cohen kappa scores are different.
rater1 = [-8, -7, 8, 6, 2, -5]
rater2 = [-3, -5, 3, 3, 2, -2]
rater3 = [-4, -2, 1, 3, 0, -2]

raters = [rater1, rater2, rater3]

kappaScores = calculate_Cohen_Kappa_Score(raters)

platHeatMapKappaScore(kappaScores)
