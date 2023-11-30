from flask_login import login_required

from config import app
from flask import render_template, request
from models import Positions, Candidate, CandidatePositionAssociation


@app.route('/votes')
@login_required
def votes():
    candidate_position = []
    positions = Positions.query.all()
    # for position in positions:
    #     candidate_position.append()
    return render_template('vote.html', positions=positions, Candidate=Candidate,
                           CandidatePositionAssociation=CandidatePositionAssociation)


@app.route('/cast-vote', methods=['GET', 'POST'])
@login_required
def cast_vote():
    ...
