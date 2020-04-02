from models import db, Item
import os

if os.path.exists('items.db'):
    os.remove('items.db')


db.create_all()

starting_items = [
    {'name': 'Computer', 'amount': 1},
    {'name': 'Apple', 'amount': 2},
    {'name': 'Tin Can', 'amount': 2}
]

for item in starting_items:
    db.session.add(Item(name=item['name'], amount=item['amount']))

db.session.commit()