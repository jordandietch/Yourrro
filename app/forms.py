from flask.ext.wtf import Form, TextField, BooleanField
from flask.ext.wtf import Required

class Submit(Form):
    property_address = TextField('property_address', validators = [Required()])
    email_address = TextField('email_address', validators = [Required()])
    phone_number = TextField('phone_number')
    name = TextField('name')