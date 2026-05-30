def ft_harvest_total() -> None:
    days = 1
    total_harvest = 0
    while (days <= 3):
        total_harvest += int(input(f"Day {days} harvest: "))
        days += 1
    print(f"Total harvest: {total_harvest}")
