#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_data_alchemist.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 11:50:18 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/19 12:51:41 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = ["Alice", "bob", "Charlie",
               "dylan", "Emma", "Gregory",
               "john", "kevin", "Liam"]

    players_capitalized = []
    players_all_capitalized = []

    for player in players:
        if (player == player.capitalize()):
            players_capitalized.append(player)
            players_all_capitalized.append(player)
        else:
            players_all_capitalized.append(player.capitalize())

    print()
    print(f"Initial list of players: {players}")
    print(f"New list with all capitalized: {players_all_capitalized}")
    print(f"New list of capitalized names only: {players_capitalized}")
    print()

    scores: dict = {}
    for player in players_all_capitalized:
        scores.update({player: random.randrange(150, 1000)})

    print(f"Score dict: {scores}")
    print(f"Score average is {sum(scores.values()) / len(scores):.2f}")

    more_average_score: dict = {}
    for key, value in scores.items():
        if (value > sum(scores.values()) / len(scores)):
            more_average_score[key] = value
    print(f"High scores: {more_average_score}")


if __name__ == "__main__":
    main()
