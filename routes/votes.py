from flask_login import login_required, current_user

from config import app, db
from flask import render_template, request, redirect, url_for
from models import Positions, Candidate, CandidatePositionAssociation, Vote, User


@app.route('/votes')
@login_required
def votes():
    if not current_user.has_voted:
        positions = Positions.query.order_by(Positions.index).all()
        return render_template('vote.html', positions=positions, Candidate=Candidate,
                               CandidatePositionAssociation=CandidatePositionAssociation)
    else:
        return render_template('thankyou.html', text='You have already voted!')


@app.route('/cast-vote', methods=['GET', 'POST'])
@login_required
def cast_vote():
    if not current_user.has_voted:
        if request.method == 'POST':
            votes_dict = request.form.to_dict()
            votes_dict.pop('csrf_token')
            for vote in votes_dict.values():
                candidate_position = CandidatePositionAssociation.find_obj_by(id=vote)
                candidate_position.vote_count += 1
                candidate = Candidate.find_obj_by(id=candidate_position.candidate_id)
                position = Positions.find_obj_by(id=candidate_position.position_id)
                vote_object = Vote(user=current_user, candidate=candidate, position=position)
                db.session.add(vote_object)
                db.session.commit()
            current_user.has_voted = True
            db.session.commit()
        text = 'Thank you for voting!'
    else:
        text = 'You have already voted'
    return render_template('thankyou.html', text=text)
