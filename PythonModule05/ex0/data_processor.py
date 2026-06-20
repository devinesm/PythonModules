#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   data_processor.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 13:34:36 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/19 17:39:30 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise IndexError("Error: No data left "
                             "to output in this processor.")

        oldest_data = self._queue.pop(0)
        return oldest_data


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            for d in data:
                if not isinstance(d, (int, float)):
                    return False
            return True

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Got exception: Improper numeric data")

        if isinstance(data, list):
            for d in data:
                self._queue.append((self._rank, str(d)))
                self._rank += 1
        else:
            self._queue.append((self._rank, str(data)))
            self._rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            for d in data:
                if not isinstance(d, str):
                    return False
            return True

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Got exception: Improper text data")

        if isinstance(data, list):
            for d in data:
                self._queue.append((self._rank, str(d)))
                self._rank += 1
        else:
            self._queue.append((self._rank, str(data)))
            self._rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True

        if isinstance(data, list):
            for d in data:
                if not isinstance(d, dict):
                    return False
                for key, value in d.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True

        return False

    def ingest(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            raise ValueError("Got exception: Improper dict data")

        if isinstance(data, list):
            for d in data:
                log_str = f"{d['log_level']}: {d['log_message']}"
                self._queue.append((self._rank, log_str))
                self._rank += 1
        else:
            log_str = f"{['log_level']}: {['log_message']}"
            self._queue.append((self._rank, log_str))
            self._rank += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    num_processor = NumericProcessor()

    print(f"Trying to validate input '42': {num_processor.validate(42)}")
    print("Trying to validate input 'Hello':"
          f"{num_processor.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_processor.ingest("foo")
    except Exception as e:
        print(e)

    num_list: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_list}")
    num_processor.ingest(num_list)

    print("Extracting 3 values...")
    i = 0
    while i < 3:
        rank, val = num_processor.output()
        print(f"Numeric value {rank}: {val}")
        i += 1

    print()
    print("Testing Text Processor...")
    text_processor = TextProcessor()

    print(f"Trying to validate input '42': {text_processor.validate(42)}")

    text_list = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {text_list}")
    text_processor.ingest(text_list)

    print("Extracting 1 value...")
    rank, val = text_processor.output()
    print(f"Text value {rank}: {val}")

    print()
    print("Testing Log Processor...")
    log_processor = LogProcessor()

    print("Trying to validate input 'Hello':"
          f"{log_processor.validate('Hello')}")
    dict_list = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    log_processor.ingest(dict_list)

    print(f"Processing data: {dict_list}")
    print("Extracting 2 value...")
    i = 0
    while i < 2:
        rank, val = log_processor.output()
        print(f"Log entry {rank}: {val}")
        i += 1


if __name__ == "__main__":
    main()
