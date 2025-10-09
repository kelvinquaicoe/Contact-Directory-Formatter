# -comp163-assignment-6
assignment-6

PROJECT OVERVIEW

Inconsistent contact data is cleaned, standardized, and formatted into a refined layout in this project.
It demonstrates proper output alignment and fluent use of Python string techniques.

Users can input multiple contacts (in the format name|phone|email|address), and the program will:

Parse and clean each field

Correct capitalization and spacing

Standardize phone numbers

Correct email case

Format addresses with proper state abbreviations

Display a neatly formatted contact directory and summary


STRING METHODS USED

.split('|') - Parse contact fields 

.split() - Separate name parts and address components 

.join() - Reassemble cleaned address components 

.strip() - Remove extra whitespace 

.title() - Proper case for names and addresses 

.upper() - Standardize state abbreviations 

.lower() - Standardize email addresses 

.replace() - Clean phone number formatting and remove punctuation 

.isdigit() - Extract phone number digits 

.isalpha() - Identify state abbreviations 

F-string formatting with alignment for precise output e.g. (<25)


PROGRAM FEATURES

.title() To capiltalize the first letters and .strip() to remove extra spaces.

Extracts only digits using .isdigit()

Converts emails to lowercase with .lower()

Displays contacts in a well-aligned format using f-string width specifiers (< 25 <30)

