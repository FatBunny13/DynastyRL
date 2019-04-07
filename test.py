import os
import shelve

with shelve.open('can') as db:
    db['fuck'] = 'fuck'

if os.path.isfile('spam'):
    print('yay')
else:
    print('fuck')