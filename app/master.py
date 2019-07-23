from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.auth import login_required

bp = Blueprint('master', __name__)

@bp.route('/')
@login_required
def index():
    return f"HELLO THERE {g.user}"
