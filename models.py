from config import db, ma


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    amount = db.Column(db.Integer, index=True)


class ItemSchema(ma.ModelSchema):
    class Meta:
        model = Item
        sqla_session = db.session

