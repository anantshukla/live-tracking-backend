import flask
from Backend import db,ma

class User(db.Model):
    empID = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), unique=False, nullable=False)
    email = db.Column(db.String(45), unique=False,nullable=False)
    phoneno = db.Column(db.String(15),unique=False,nullable=False)
    password = db.Column(db.String(45),unique=False, nullable=False)
    dob = db.Column(db.String(40), unique=False, nullable=False)
    sex = db.Column(db.String(1), unique=False, nullable=False)
    Location = db.relationship('Location',backref='locationof')


class Location(db.Model):
    locationID = db.Column(db.Integer, primary_key=True, nullable=False)
    CurrentLocation = db.Column(db.String(255), unique=False, nullable=False)
    LastUpdated = db.Column(db.String(60), unique=False, nullable=False)
    BatteryStatus = db.Column(db.Integer, unique=False, nullable=False)
    empID = db.Column(db.Integer, db.ForeignKey('user.empID'))


class Locationdetails(db.Model):
    empID = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), unique=False, nullable=False)
    email = db.Column(db.String(45), unique=False,nullable=False)
    phoneno = db.Column(db.String(15),unique=False,nullable=False)
    dob = db.Column(db.String(40), unique=False, nullable=False)
    sex = db.Column(db.String(1), unique=False, nullable=False)
    CurrentLocation = db.Column(db.String(255), unique=False, nullable=False)
    LastUpdated = db.Column(db.String(60), unique=False, nullable=False)
    BatteryStatus = db.Column(db.Integer, unique=False, nullable=False)



class LocationdetailsSchema(ma.Schema):
    class Meta:
        fields = ('empID','name','CurrentLocation','phoneno')


class LocationdetailsnextSchema(ma.Schema):
    class Meta:
        fields = ('empID','name','CurrentLocation','LastUpdated','BatteryStatus')

nextLocationDetailsSchemas = LocationdetailsnextSchema(many=True)

locationDetailsSchemas = LocationdetailsSchema(many=True)
