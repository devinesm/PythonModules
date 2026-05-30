def ft_count_harvest(count, days) -> None:
    if (count > days):
        print("Harvest time!")
    else:
        print(f"Day {count}")
        ft_count_harvest(count + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    ft_count_harvest(1, days)
