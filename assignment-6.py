count = 0
directory = []


info = input('Enter contact information (format: name|phone|email|address):')
print('\n=== CONTACT DIRECTORY ===')
while info.strip().upper() != 'DONE':
    parts = info.split('|')
    name = parts[0].title().strip()
    email = parts[2].lower().strip()
    phone = ''.join([c for c in parts[1] if c.isdigit()])
    address = parts[3].strip().title()
    address = address.replace("N C", "NC").replace("S C", "SC").replace("V A", "VA")

    phone1, phone2, phone3 = phone[:3], phone[3:6], phone[6:]
    count += 1
    print(f'\nCONTACT {count}:')
    print(f'Name:     {name}')
    print(f'Phone:    ({phone1}) {phone2}-{phone3}')
    print(f'Email:    {email}')
    print(f'Address:  {address}')

    directory.append((name, f'({phone1}) {phone2}-{phone3}', email))

    
    info = input()
print('\n=== DIRECTORY SUMMARY ===')
print(f'Total contacts processed: {count}')

print('=== FORMATTED FOR PRINTING ===')
for entry in directory:
    name, phone, email = entry
    parts = name.split()
    last = parts[-1]
    first = ' '.join(parts[:-1])
    print(f'{last}, {first:<25}{phone:<20}{email}')



