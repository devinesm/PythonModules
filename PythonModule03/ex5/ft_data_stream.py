#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_data_stream.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 11:00:36 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/19 11:45:38 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


import typing
import random


def gen_event(players: list, actions: list) -> typing.Generator[
                                               tuple[str, str], None, None]:
    while (True):
        yield (random.choice(players), random.choice(actions))


def consume_event(gen: list) -> typing.Generator[tuple[str, str], None, None]:
    while (len(gen) > 0):
        event = random.choice(gen)
        gen.remove(event)
        yield (event)
    return


def main() -> None:
    print("=== Game Data Stream Processor ===")

    players = ["alice", "bob",
               "charlie", "dylan"]

    actions = ["climb", "eat", "grab",
               "move", "release", "run",
               "sleep", "swim", "use"]

    gen: typing.Generator[tuple[str, str],
                          None, None] = gen_event(players, actions)
    for i in range(1000):
        player, action = next(gen)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events: list = [next(gen) for i in range(10)]
    print()
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print()
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
