#-------------------------------------------------------------------------------
# Name:        forms
# Purpose:     Provides Patron Blueprint forms for applications using the
#              Catalog Pull Platform.
#
#
# Author:      Jeremy Nelson
#
# Created:     2014-02-12
# Copyright:   (c) Jeremy Nelson, Colorado College 2014
# Licence:     MIT
#-------------------------------------------------------------------------------

from flask_wtf import Form
from wtforms import TextField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(Form):
    email = TextField('Email', validators=[Email,])
    password = PasswordField('Password')

class RegisterForm(Form):
    givenName = TextField('First Name')
    familyName = TextField('Last Name', validators=[DataRequired,])
    email = TextField('Email address', validators=[Email,])