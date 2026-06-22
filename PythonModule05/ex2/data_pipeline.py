#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   data_pipeline.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 13:34:36 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/22 18:40:13 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


from abc import ABC, abstractmethod
from typing import Any
from typing import Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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
            
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for p in self._processors:
            transport = []
            i = 0
            while i < nb:
                try:
                    data = p.output()
                    transport.append(data)
                except IndexError:
                    break
                i += 1

            if transport:
                plugin.process_output(transport)


class CsvExport():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = []
        for d in data:
            values.append(d[1])

        print("CSV Output:")
        print(", ".join(values))


class JsonExport():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_pairs = []
        for d in data:
            pair_string = f'"item_{d[0]}": "{d[1]}"'
            json_pairs.append(pair_string)

        print("JSON Output:")
        json_final = "{" + ", ".join(json_pairs) + "}"
        print(json_final)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    print()
    stream = DataStream()
    stream.print_processors_stats()
    print()
    print("Registering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    print()
    stream.register_processor(num_proc)
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    batch1 = [
        'Hello world', 
        [3.14, -1, 2.71], 
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 
        42, 
        ['Hi', 'five']
    ]
    
    print(f"Send first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    print()
    stream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CsvExport()
    stream.output_pipeline(3, csv_plugin)
    print()
    stream.print_processors_stats()
    print()
    batch2 = [
        21, 
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'], 
        [{'log_level': 'ERROR', 'log_message': '500 server crash'}, 
         {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}], 
        [32, 42, 64, 84, 128, 168], 
        'World hello'
    ]
    
    print(f"Send another batch of data:\n{batch2}")
    stream.process_stream(batch2)
    print()
    stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JsonExport()
    stream.output_pipeline(5, json_plugin)
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
