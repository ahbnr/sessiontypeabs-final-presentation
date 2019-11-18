#!/usr/bin/env python3

import pickle
import os
import re
import pandas as pd
from statistics import mean
from nltk import edit_distance
from typing import Sequence, NewType, Tuple
import matplotlib.pyplot as plt
import matplotlib as mpl

from common_consecutive_calls import *

user_times_frame = pd.read_csv('./consecutive_calls/Method2DirectNoShuffle_UserTimes.csv')
user_times_frame = pd.DataFrame(
            data = user_times_frame.apply(
                lambda row: [
                    row['plain'],
                    row['enforcement']
                ],
                axis='columns',
            ).array,
            columns=['plain', 'enforcement'],
            index=user_times_frame['repetitions']
        )
user_times_fig = {
        'name': 'UserTimes',
        'frame': user_times_frame,
        'ylabel': 'user mode execution time [s]',
        'xlabel': 'repetitions'
    }

user_times_frame_await = pd.read_csv('./consecutive_calls/Method2DirectNoShuffleAwait_UserTimes.csv')
user_times_frame_await = pd.DataFrame(
            data = user_times_frame_await.apply(
                lambda row: [
                    row['plain'],
                    row['enforcement']
                ],
                axis='columns',
            ).array,
            columns=['plain', 'enforcement'],
            index=user_times_frame_await['repetitions']
        )
user_times_fig_await = {
        'name': 'UserTimesAwait',
        'frame': user_times_frame_await,
        'ylabel': 'user mode execution time [s]',
        'xlabel': 'repetitions'
    }

levenshtein_comparison_frame = pd.read_csv('consecutive_calls/Method2DirectNoShuffle_Levenshtein.csv')
def levenshtein_adjustment(frame):
    adjusted_frame = pd.DataFrame(
            data = frame.apply(
                lambda row: [
                        row['plain alternating'],
                        row['sequence length']
                    ],
                axis='columns'
            ).array,
            columns=['edits', 'sequence length'],
            index=frame['repetitions']
        )
    adjusted_frame.index.name = 'repetitions'
    return adjusted_frame

levenshtein_comparison_fig = {
        'name': 'Levenshtein',
        'frame': levenshtein_comparison_frame,
        'ylabel': 'edits',
        'xlabel': 'repetitions',
        'adjustment': levenshtein_adjustment,
        'customplot': lambda frame: frame.plot.bar()
    }

to_files = True
figures = [user_times_fig, user_times_fig_await, levenshtein_comparison_fig]
for fig in figures:
    print('Viewing figure {}'.format(fig['name']))

    if 'adjustment' in fig:
        fig['frame'] = fig['adjustment'](fig['frame'])

    ax = None
    if 'customplot' in fig:
        ax = fig['customplot'](fig['frame'])
    else:
        ax = fig['frame'].plot.bar()

    ax.set_ylabel(fig['ylabel'])
    ax.set_xlabel(fig['xlabel'])
    ax.autoscale()
    if fig['name'] == 'UserTimes' or fig['name'] == 'UserTimesAwait':
        ax.set_ylim(top=2.1)

    if to_files:
        plt.savefig(os.path.join('newcache', '{}.pdf'.format(fig['name'])))
    else:
        plt.show()
        input()

    plt.close()

