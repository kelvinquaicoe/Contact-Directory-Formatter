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
    

