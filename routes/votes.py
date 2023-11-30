from flask_login import login_required, current_user

from config import app, db
from flask import render_template, request, redirect, url_for
from models import Positions, Candidate, CandidatePositionAssociation, Vote


@app.route('/votes')
@login_required
def votes():
    candidate_position = []
    positions = Positions.query.all()
    return render_template('vote.html', positions=positions, Candidate=Candidate,
                           CandidatePositionAssociation=CandidatePositionAssociation)


@app.route('/cast-vote', methods=['GET', 'POST'])
@login_required
def cast_vote():
    if request.method == 'POST':
        votes = request.form.to_dict()
        votes.pop('csrf_token')
        for vote in votes.values():
            candidate_position = CandidatePositionAssociation.find_obj_by(id=vote)
            candidate_position.vote_count += 1
            candidate = Candidate.find_obj_by(id=candidate_position.candidate_id)
            position = Positions.find_obj_by(id=candidate_position.position_id)
            vote_object = Vote(user=current_user, candidate=candidate, position=position)
            db.session.add(vote_object)
            db.session.commit()
    return redirect(url_for('votes'))
