#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_data_alchemist.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 11:50:18 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/19 13:19:01 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = ["Alice", "bob", "Charlie",
               "dylan", "Emma", "Gregory",
               "john", "kevin", "Liam"]

    players_all_capitalized = [player.capitalize() for player in players]

    players_capitalized = [player for player in players
                           if player == player.capitalize()]

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {players_all_capitalized}")
    print(f"New list of capitalized names only: {players_capitalized}")

    scores = {player: random.randint(0, 1000)
              for player in players_all_capitalized}

    print(f"Score dict: {scores}")

    average = round(sum(scores[p] for p in scores) / len(scores), 2)

    print(f"Score average is {average:.2f}")

    more_average_score = {player: scores[player]
                          for player in scores if scores[player] > average}

    print(f"High scores: {more_average_score}")


if __name__ == "__main__":
    main()
