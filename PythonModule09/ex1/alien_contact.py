#!/usr/bin/env python3

from pydantic import (BaseModel,
                      Field,
                      ValidationError,
                      model_validator)
from enum import Enum
from datetime import datetime


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: None | str = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate(self):
        if self.contact_id[0] != 'A' or self.contact_id[1] != 'C':
            raise ValueError("Telepathic contact must start with \"AC\"")

        if (self.contact_type == ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError("Physical Contact reports must be verified")

        if (self.contact_type == ContactType.TELEPATHIC
                and not self.witness_count > 2):
            raise ValueError("Telepathic contact requeried"
                             "at least 3 witnesses")

        if (self.signal_strength > 7.0
                and self.message_received is None):
            raise ValueError("Strong signals (> 7.0) "
                             "should include received messages")

        return self


def print_contact(contact: AlienContact) -> None:
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received is not None:
        print(f"Message: '{contact.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")

    contact_valido = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 7, 9),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True
    )
    print("Valid contact report:")
    print_contact(contact_valido)

    print()
    print("========================================")

    try:
        contact_invalido = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2024, 7, 9),
            location="Roswell, New Mexico",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=4.5,
            duration_minutes=15,
            witness_count=2,
            is_verified=False
        )
        print_contact(contact_invalido)
    except ValidationError as e:
        print("Expected validation error:")
        print(e)

    print()
    print("========================================")


if __name__ == "__main__":
    main()
