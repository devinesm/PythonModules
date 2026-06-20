#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   data_stream.py                                      :+:      :+:    :+:   #
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


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, new_proc: DataProcessor) -> None:
        self._processors.append(new_proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            sucess: bool = False
            for p in self._processors:
                if p.validate(data) is True:
                    p.ingest(data)
                    sucess = True
                    break
            if sucess is False:
                print("DataStream error -"
                      f"Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for p in self._processors:
            name = p.__class__.__name__
            total_processed = p._rank
            left = len(p._queue)
            print(f"{name} Processor: total {total_processed} "
                  f"items processed, remaining {left} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    stream = DataStream()

    stream.print_processors_stats()

    print()
    print("Registering Numeric Processor")
    num_processor = NumericProcessor()
    stream.register_processor(num_processor)

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print()
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print()

    print("Registering other data processors")
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    stream.register_processor(text_processor)
    stream.register_processor(log_processor)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print()
    print("Consume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")
    i = 0
    while i < 3:
        num_processor.output()
        i += 1
    i = 0
    while i < 2:
        text_processor.output()
        i += 1
    log_processor.output()
    stream.print_processors_stats()

    return


if __name__ == "__main__":
    main()
