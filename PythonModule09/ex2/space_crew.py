#!/usr/bin/env python3


from pydantic import (BaseModel,
                      Field,
                      ValidationError,
                      model_validator)
from enum import Enum
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)

    crew: list[CrewMember] = Field(min_length=1, max_length=12)

    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self):
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = False

        for crew_member in self.crew:
            if not crew_member.is_active:
                raise ValueError(f"Crew member {crew_member.name}"
                                 " is not active!")

            if crew_member.rank in (Rank.COMMANDER, Rank.CAPTAIN):
                has_leader = True

        if not has_leader:
            raise ValueError("Crew must have at least"
                             " one captain or commander")

        if self.duration_days > 365:
            veterans_count = sum(1 for c in self.crew
                                 if c.years_experience >= 5)
            if veterans_count / len(self.crew) < 0.5:
                raise ValueError("Missions over 365 days need"
                                 " 50% experienced crew (5+ years)")

        return self


def print_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"  - {member.name} ({member.rank.value})"
              f" - {member.specialization}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("========================================")

    sarah = CrewMember(
        member_id="C001", name="Sarah Connor", rank=Rank.COMMANDER,
        age=45, specialization="Mission Command", years_experience=15
    )
    john = CrewMember(
        member_id="C002", name="John Smith", rank=Rank.LIEUTENANT,
        age=35, specialization="Navigation", years_experience=8
    )
    alice = CrewMember(
        member_id="C003", name="Alice Johnson", rank=Rank.OFFICER,
        age=28, specialization="Engineering", years_experience=3
    )

    missao_valida = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 7, 9),
        duration_days=900,
        crew=[sarah, john, alice],
        budget_millions=2500.0
    )

    print("Valid mission created:")
    print_mission(missao_valida)

    print("\n========================================")
    print("Attempting to create an invalid mission...")
    print("========================================\n")

    try:
        bob = CrewMember(
            member_id="C004", name="Bob", rank=Rank.CADET,
            age=22, specialization="Maintenance", years_experience=1
        )

        missao_invalida = SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Asteroid Mining",
            destination="Asteroid Belt",
            launch_date=datetime(2024, 7, 9),
            duration_days=100,
            crew=[john, alice, bob],
            budget_millions=500.0
        )
        print_mission(missao_invalida)
    except ValidationError as e:
        print("Expected validation error:")
        print(e)

    print("\n========================================")


if __name__ == "__main__":
    main()
