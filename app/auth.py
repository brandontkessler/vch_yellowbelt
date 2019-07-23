import functools
import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        pw_check = 'vchyb'
        password = request.form['password']
        error = None

        if not password:
            error = 'Password is required.'
        elif password != pw_check:
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = int(round(random.randint(1,9e15) * random.random(),0))
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = user_id


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
