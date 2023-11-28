from flask_login import login_required

from config import app
from flask import render_template
from models import Positions, Candidate


@app.route('/votes')
@login_required
def votes():
    positions = Positions.query.all()
    return render_template('vote.html', positions=positions, Candidate=Candidate)
