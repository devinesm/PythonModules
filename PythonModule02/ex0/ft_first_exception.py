#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_first_exception.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/10 20:20:57 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/18 14:39:17 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    inputs = ["25", "abc"]

    for i in inputs:
        print(f"Input data is '{i}'")
        try:
            print(f"Temperature is now {input_temperature(i)}°C")
        except ValueError as value_error:
            print(f"Caught input_temperature error: {value_error}")
        print()


def main() -> None:
    print("=== Garden Temperature ===")
    print()

    test_temperature()

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
