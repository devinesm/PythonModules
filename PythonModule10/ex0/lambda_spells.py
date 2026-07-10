#!/usr/bin/env python3

import data_generator


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda p: p['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m['power'], mages))
    stats: dict = {'max_power': max(powers),
                   'min_power': min(powers),
                   'avg_power': round(sum(powers) / len(powers), 2)}

    return stats


def main():
    print("🔮 Welcome to Lambda Sanctum 🔮")
    print("=" * 40)

    gerador = data_generator.FuncMageDataGenerator

    artefactos = gerador.generate_artifacts(3)
    magos = gerador.generate_mages(4)
    feiticos = gerador.generate_spells(3)

    print("\n--- Test: artifact_sorter ---")
    print("Generated artifacts:", artefactos)
    print("Ordered by powers:", artifact_sorter(artefactos))

    print("\n--- Test: power_filter (Min Power: 70) ---")
    print("Generated mages:", magos)
    print("Strong mages (>= 70):", power_filter(magos, 70))

    print("\n--- Test: spell_transformer ---")
    print("Original spells:", feiticos)
    print("Transformed:", spell_transformer(feiticos))

    print("\n--- Test: mage_stats ---")
    print("Guilda Stats:", mage_stats(magos))
    print("=" * 40)


if __name__ == "__main__":
    main()
