# Contact Directory Formatter

A command-line Python program that cleans, validates, and formats contact details.

## Features

- Accepts contacts in `name|phone|email|address` format.
- Normalizes name capitalization and email case.
- Formats 10-digit phone numbers.
- Checks that each entry has four fields and that required fields are present.
- Reports invalid entries without stopping the program.
- Prints a contact directory and a print-friendly summary.

## Requirements

- Python 3.8 or newer
- No third-party packages

## Run

```bash
python contact_directory.py
```

Example input:

```text
john doe|5551234567|JOHN@EMAIL.COM|123 main street, raleigh nc 27601
jane smith|919-555-1234|jane.smith@gmail.com|456 oak ave, durham nc 27705
DONE
```

## Concepts practiced

String methods, splitting and joining, list and dictionary data structures, validation, exceptions, functions, and formatted output.

## Development note

This project began as COMP 163 coursework and has been cleaned up as a learning project. Contact information entered is handled in memory only and is not saved to a file.
