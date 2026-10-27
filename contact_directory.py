"""Collect, validate, and format contacts in a simple command-line directory."""

import re


def format_phone(raw_phone):
    digits = "".join(character for character in raw_phone if character.isdigit())
    if len(digits) != 10:
        raise ValueError("phone number must contain exactly 10 digits")
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


def parse_contact(raw_contact):
    fields = [field.strip() for field in raw_contact.split("|")]
    if len(fields) != 4:
        raise ValueError("enter exactly four fields: name|phone|email|address")

    name, raw_phone, email, address = fields
    if not name:
        raise ValueError("name cannot be empty")
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
        raise ValueError("email address does not look valid")
    if not address:
        raise ValueError("address cannot be empty")

    name = " ".join(part.capitalize() for part in name.split())
    email = email.lower()
    phone = format_phone(raw_phone)
    address = " ".join(address.split()).title()
    for spaced, abbreviation in (("N C", "NC"), ("S C", "SC"), ("V A", "VA")):
        address = address.replace(spaced, abbreviation)

    return {"name": name, "phone": phone, "email": email, "address": address}


def print_directory(contacts):
    print("\n=== CONTACT DIRECTORY ===")
    for index, contact in enumerate(contacts, start=1):
        print(f"\nCONTACT {index}:")
        print(f"Name:     {contact['name']}")
        print(f"Phone:    {contact['phone']}")
        print(f"Email:    {contact['email']}")
        print(f"Address:  {contact['address']}")

    print("\n=== DIRECTORY SUMMARY ===")
    print(f"Total contacts processed: {len(contacts)}")
    print("\n=== FORMATTED FOR PRINTING ===")
    for contact in contacts:
        name_parts = contact["name"].split()
        last_name = name_parts[-1]
        first_names = " ".join(name_parts[:-1])
        print(f"{last_name}, {first_names:<25}{contact['phone']:<20}{contact['email']}")


def main():
    contacts = []
    print("Enter each contact as name|phone|email|address.")
    print("Type DONE when you have finished.")

    while True:
        raw_contact = input("\nContact: ").strip()
        if raw_contact.upper() == "DONE":
            break
        if not raw_contact:
            continue

        try:
            contacts.append(parse_contact(raw_contact))
            print("Contact added.")
        except ValueError as error:
            print(f"Invalid contact: {error}")

    print_directory(contacts)


if __name__ == "__main__":
    main()
