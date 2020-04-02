from config import db
from flask import abort, make_response
from models import Item, ItemSchema


def read_by_name():
    items = Item.query.order_by(Item.name).all()
    item_schema = ItemSchema(many=True)
    return item_schema.dump(items)


def read_by_number():
    items = Item.query.order_by(Item.amount).all()
    item_schema = ItemSchema(many=True)
    return item_schema.dump(items)


def read_by_id(id):
    item = Item.query.filter(Item.id == id).one_or_none()

    if item:
        item_schema = ItemSchema()
        return item_schema.dump(item)

    else:
        abort(404, f'Person not found for id: {id}')


def create(item):
    name = item.get("name")
    amount = item.get("amount")
    existing_item = Item.query.filter(Item.name == name).one_or_none()

    # if item already exists, adds the amount created to the amount of that item
    if existing_item is not None:
        schema = ItemSchema()
        update = schema.load(item, session=db.session)
        
        update.id = existing_item.id
        update.amount = existing_item.amount + amount
        
        db.session.merge(update)
        db.session.commit()
        
        return schema.dump(update), 200

    # creates new item with the parameters given
    else:
        schema = ItemSchema()
        new_item = schema.load(item, session=db.session)

        db.session.add(new_item)
        db.session.commit()

        return schema.dump(new_item), 201


def delete(id):
    item = Item.query.filter(Item.id == id).one_or_none()

    if item is not None:
        db.session.delete(item)
        db.session.commit()
        return make_response(f"Item {id} deleted", 200)

    else:
        abort(404, f"Item not found for id: {id}")
