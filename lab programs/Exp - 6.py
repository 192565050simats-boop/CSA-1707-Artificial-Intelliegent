# Vacuum Cleaner Problem

room = {
    'A': 'Dirty',
    'B': 'Dirty'
}

position = 'A'

while 'Dirty' in room.values():

    print("Vacuum is in room", position)

    if room[position] == 'Dirty':
        print("Cleaning room", position)
        room[position] = 'Clean'

    if position == 'A':
        position = 'B'
    else:
        position = 'A'

print("All rooms are clean!")
