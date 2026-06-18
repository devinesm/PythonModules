#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_score_analytics.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/18 15:57:54 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/18 16:29:12 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys


def main(args: list[str]) -> None:
    scores: list[int] = []
    i = 1

    print("=== Player Score Analytics ===")

    while (i < len(args)):
        try:
            score = int(args[i])
            scores += [score]
        except ValueError:
            print(f"Invalid parameter: '{args[i]}'")
        i += 1

    if (len(scores) == 0):
        print("No scores provided. ", end="")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores):.1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main(sys.argv)
