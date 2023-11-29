from flask_login import login_required, current_user

from config import app, db
from flask import render_template, request, redirect, url_for
from models import Positions, Candidate, Vote


@app.route('/votes')
@login_required
def votes():
    positions = Positions.query.all()
    return render_template('vote.html', positions=positions, Candidate=Candidate)


@app.route('/cast-vote', methods=['GET', 'POST'])
@login_required
def cast_vote():
    if request.method == 'POST':
        request_dict = request.form.to_dict()
        request_dict.pop('csrf_token')
        for position, candidate_id in request_dict.items():
            candidate = Candidate.find_obj_by(id=candidate_id)
            position = Positions.find_obj_by(title=position)
            vote = Vote(user=current_user, candidate=candidate, position=position)
            vote.save()
    return redirect(url_for('votes'))
