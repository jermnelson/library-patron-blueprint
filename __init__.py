#-------------------------------------------------------------------------------
# Name:        patron
# Purpose:     Controllers for the Patron Blueprint in the Catalog Pull Platform
#
# Author:      Jeremy Nelson
#
# Created:     2014-02-12
# Copyright:   (c) Jeremy Nelson, Colorado College 2014
# Licence:     MIT
#-------------------------------------------------------------------------------

from flask import Blueprint, current_app, flash, g, session
from flask import redirect, render_template, request, url_for

from flask.ext.login import LoginManager, login_user, login_required
from flask.ext.login import logout_user, current_user
from flask.ext.mongokit import MongoKit

from patron.forms import LoginForm, RegisterForm
from patron.models import Patron

login_manager = LoginManager()
patron = Blueprint('patron', __name__, template_folder='templates')

@login_manager.user_loader
def load_patron(patronid):
    return g.mongo_storage.Patron.get(patronid)

@patron.route("/history", methods=['GET', 'POST'])
@login_required
def history():
    patron_ = g.mongo_storage.Patron.get(current_user.id)
    return render_template("history.html", patron=patron_)

@patron.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        patron_ = Patron.get(form)
        login_user(patron_)
        return redirect(request.args.get('next') or url_for('home'))
    return render_template("login.html", form=form)

@patron.route('/logout',
           methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("Logged out")
    return redirect(request.args.get('next') or url_for("home"))

@patron.route('/register',
              methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        patron = g.mongo_storage.Patron()
        patron.givenName = request.form.get('givenName')
        patron.familyName = request.form.get('familyName')
        patron.email = request.form.get('email')
        patron.save()
        return redirect(request.args.get('next') or url_for("home"))
    return render_template("register.html", form=form)



