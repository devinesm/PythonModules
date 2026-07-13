#!/usr/bin/env python3

from functools import wraps
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__} ...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power', args[-1] if args else 0)
            if not isinstance(power, int) or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying ..."
                              f" (attempt {attempt}/{max_attempts})")
                    else:
                        message = "Spell casting failed after"
                        message += f" {max_attempts} attempts"
                        return message
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer ...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print()
    print("Testing retrying spell ...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise ValueError("Magic fizzled!")

    @retry_spell(max_attempts=3)
    def waaaaagh_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(unstable_spell())
    print(waaaaagh_spell())

    print()
    print("Testing MageGuild ...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("A"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
