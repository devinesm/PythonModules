#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_raise_exception.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/10 20:37:26 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/10 20:37:43 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    inputs = ["25", "abc", "100", "-50"]

    for i in inputs:
        print(f"Input data is '{i}'")
        try:
            print(f"Temperature is now {input_temperature(i)}°C")
        except ValueError as value_error:
            print(f"Caught input_temperature error: {value_error}")
        print()


def main() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    test_temperature()

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
