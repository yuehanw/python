# Working with Lists
# In this exercise list items are strings. Dictionary objects is the preferred choice
# e.g., lead_vocals = {'lead_vocals': 'mick jagger'}
# but since the latter object has yet to be described we will stick with strings.

# The Rolling Stones (1969 lineup)
lead_vocals = 'Mick Jagger'
lead_guitar = 'Keith Richards' # also played rhythm guitar
rhythm_guitar = 'Brian Jones' # also played lead guitar and other instruments
bass = 'Bill Wyman'
drums = 'Charlie Watts'

# List creation: initialize list with band member role
band = [lead_vocals, lead_guitar, rhythm_guitar, bass, drums]

# String formatting options
# print("Band personnel\n %s\n" % band) # old school
# print("Band personnel\n {0}\n".format(band)) # str.format
print(f"List creation: Band personnel\n {band}\n") # f-string (formatted string literal)

# List indexing: return band members individually by position
mick = band[0]
keith = band[1]
brian = band[2]
# bill = band[3]
bill = band[-2] # reverse indexing (cool)
# charlie = band[4]
charlie = band[-1] # reverse indexing (cool)

print(f"List indexing: the Rolling Stones lineup (mid-1969): {mick}, {keith}, {brian}, {bill}, and {charlie}\n")

title = 'Gimme Shelter session recordings (1969)'
wikipedia_entry = 'https://en.wikipedia.org/wiki/Gimme_Shelter'
gimme_shelter_orig = 'https://www.youtube.com/watch?v=RbmS3tQJ7Os'
gimme_shelter_live = 'https://www.youtube.com/watch?v=8kl6q_9qZOs'

print(f"{title}\n {wikipedia_entry}\n {gimme_shelter_orig}\n {gimme_shelter_live}\n")

# List slicing (negative index): return Brian, Bill, and Charlie
# brian_bill_charlie = band[2:] # inclusive of reversed index position 2
brian_bill_charlie = band[-3:]
print(f"List slicing (negative index): Brian, Bill, and Charlie returned from band list\n {brian_bill_charlie}\n")

# List slicing (negative index): return Brian, Bill
# brian_bill = band[2:4] # works
brian_bill = band[-3:-1]

print(f"List slicing (negative index): Brian and Bill returned from band list\n {brian_bill}\n")

# List slicing: Gimme Shelter composers (Jagger and Richards)
gimme_shelter_composers = band[:2]

print(f"List slicing: Gimme Shelter composers\n {gimme_shelter_composers}\n")

# List creation: initialize list with Gimme Shelter recording session roles
band_roles = ['lead_vocals', 'lead_guitar', 'rhythm_guitar', 'bass', 'drums']
gimme_shelter_roles = []
for role in band_roles:
    if role == 'rhythm_guitar':
        continue
    else:
        gimme_shelter_roles.append(role)

# print(f"Roles: ", gimme_shelter_roles)

# Add piano and percussion with .append()
gimme_shelter_roles.append('piano')
gimme_shelter_roles.append('percussion')

print(f"List creation: Gimme Shelter studio roles\n {gimme_shelter_roles}\n")

# List slicing: Drop Brian from recording session without deleting him from the band
gimme_shelter = band[:2] + band[3:]

print(f"List slicing: Gimme Shelter band personnel\n {gimme_shelter}\n")

# Studio musicians (piano and percussion)
piano = 'Nicky Hopkins'
percussion = 'Jimmy Miller'

# Add session musicians with .append()
session_musicians = []
session_musicians.append(piano)
session_musicians.append(percussion)

print(f"list.append(): Gimme Shelter studio musicians\n {session_musicians}\n")

# Add session players to gimme_shelter lineup with .extend()
gimme_shelter.extend(session_musicians)

print(f"list.extend(): Gimme Shelter band and studio musicians using .extend()\n {gimme_shelter}\n")

# Use for loop, filter on additional personnel and add to session_musicians (Accumulator pattern)
session_musicians.clear()

print(f"list.clear(): remove all session_musician elements\n {session_musicians}\n")

# Accumulator pattern with conditional membership check
for person in gimme_shelter:
    if person not in band:
        session_musicians.append(person)

print(f"Control flow: repopulate session_musicians list from gimme_shelter list\n {session_musicians}\n")

# Mick's vocals are not enough. We need a female vocalist. Add Merry Clayton to gimme_shelter
# as second item in list using .insert().
co_lead_vocals = 'Merry Clayton'
gimme_shelter_roles.insert(1, 'co_lead_vocals') # add missing role
gimme_shelter.insert(1, co_lead_vocals) # works
# gimme_shelter.insert(-5, co_lead_vocals) # works

print(f"list.insert(): add Gimme Shelter co-lead vocals to gimme_shelter list (2nd position)\n {gimme_shelter[1]}\n")

print(f"Control flow: break out of loop if role is not lead or co-lead vocalist")
for role in gimme_shelter_roles:
    if 'vocals' in role:
        print(role)
    else:
        print('\n')
        break

# Use list slicing to extract Gimme Shelter vocalists (Keith also sings backup)
gimme_shelter_vocalists = gimme_shelter[:3]

# Use for loop to print out vocalists
print('range(): return number sequence, loop through sequence, and print out Gimme Shelter vocalists')
num = len(gimme_shelter_vocalists)
for i in range(num):
    if i == num - 1:
        print(gimme_shelter_vocalists[i], '\n')
    else:
        print(gimme_shelter_vocalists[i])

# Complete studio lineup
print(f"List: Gimme Shelter studio lineup\n {gimme_shelter}\n")

# For each musician in the lineup prepend their role as <role: > when printing out their name
print('range(): return number sequence, loop through sequence, and print out Gimme Shelter session lineup by role')
num = len(gimme_shelter)
for i in range(num):
    musician = ''.join([gimme_shelter_roles[i], ': ', gimme_shelter[i]]) # extract role and name dynamically
    if i == num - 1:
        print(musician, '\n')
    else:
        print(musician)

# Band personnel shakeup (summer 1969): oust Brian Jones
# return item with .pop(index) using .index() to surface index value.
# Note .pop() also removes item from list (very handy in this case)
ex_band_members = []
ex_band_members.append(band.pop(band.index('Brian Jones')))

print(f"list.pop(), list.index(): add Brian Jones to ex_band_members list)\n {ex_band_members}\n")

# Band personnel shakeup (summer 1969): add Mick Taylor (replaces Brian Jones)
# band[3] = 'Mick Taylor'# this also works instead of .pop() or .remove(), then .insert()
# band.remove('Brian Jones') # already removed
band.insert(2, 'Mick Taylor')

print(f"list.insert(): Mick Taylor replaces Brian Jones (late 1969)\n {band}\n")

# How many band members with the name Mick are now in the band?
# mick_count = band.count('mick') # surnames added so this no longer works

# List comprehension: [expression for item in list if condition] returns new list
mick_count = len([name for name in band if 'Mick' in name]) # future topic

print(f"List comprehension (future topic): return count of Stones named Mick\n {mick_count}\n")

# Add 2nd Mick to ex_band_members then Use del to remove him from band:
# ex_band_members.append(band[2]) # works
# del band[2] # works

ex_band_members.append(band[band.index('Mick Taylor')])
del band[band.index('Mick Taylor')]

print(f"del by list index: Mick Taylor quits the Stones (1974)\n {ex_band_members}\n")

# Add Ronnie Wood to band in same list index position formerly occupied by Mick Taylor
band.insert(2, 'Ronnie Wood') # ex-Faces lead guitarist

print(f"list.insert(): Ronnie Wood joins the Stones (1975)\n {band}\n")

# Bill Wyman retires (1992). Add to ex_band_members then remove from band.
ex_band_members.append(band.pop(band.index('Bill Wyman')))

print(f"list.pop(), list.index(); Bill Wyman retires (1992)\n {ex_band_members}\n")

# Print current band lineup.
print(f"The Rolling Stones (present day)\n {band}\n")

# Add a knighthood (Richards unhappy that Jagger accepts knighthood)
# Could also perform this operation using range()
for person in band:
    if person == 'Mick Jagger':
        band[band.index(person)] = ''.join(['Sir ', person])

# Print current band lineup.
print(f"Control flow: comparison operator (==): Queen's honors\n {band}\n")

# Perform in place reverse of elements in band list
band.reverse()

print(f"list.reverse(): Drummer Charlie Watts listed first (as it should be)\n {band}\n")

# Perform in place alpha sort of elements in band list (Jagger won't like this)
band.sort()

print(f"list.sort(): in place alpha sort of band personnel (Jagger won't like this order)\n {band}\n")

# Perform in place removal of all elements in list band
band.clear()

print(f"list.clear(): the band goes silent\n {band}\n")
