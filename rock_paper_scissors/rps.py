#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    total_plays = []
    def create_rps_plays(total_plays, plays, n):
        if len(plays) == n:
            total_plays.append(plays)
        else:
            for option in ['rock', 'paper', 'scissors']:
                new_plays = plays.copy()
                new_plays.append(option)
                create_rps_plays(total_plays, new_plays, n)

    create_rps_plays(total_plays, [], n)
    return total_plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')