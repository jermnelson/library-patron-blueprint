#-------------------------------------------------------------------------------
# Name:        models
# Purpose:     Provides Patron Blueprint models for application in the Catalog
#              Pull Platform.
#
#
# Author:      Jeremy Nelson
#
# Created:     2014-02-12
# Copyright:   (c) Jeremy Nelson, Colorado College 2014
# Licence:     MIT
#-------------------------------------------------------------------------------
import datetime

from flask.ext.login import make_secure_token, UserMixin
from flask.ext.mongokit import Document

class Patron(Document, UserMixin):
    """Patron class provides authentication, analytics, and other Patron
    functionality in the Catalog Pull Platform"""
    __collection__ = 'patrons'
    # Uses Schema.org Person properties for Patron
    structure = {
       'creation': datetime.datetime,
       'givenName': unicode,
       'email': unicode,
       'familyName': unicode,
       'name': unicode,
       'history': list,
       'saved': list
    }
    required_fields = ['familyName']
    default_values = {'creation': datetime.datetime.utcnow}

    def get_id(self):
        return self.id

    def is_active(self):
        return self.active

    def get_auth_token(self):
        return make_secure_token(self.email,
                                 key='deterministic')