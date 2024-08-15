from flask_login import login_required, current_user
from config import app, db
from flask import render_template, request, redirect, url_for, jsonify
from models import Positions, User, Candidate, CandidatePositionAssociation


@app.route('/nominees')
def nominees():
    positions = Positions.query.order_by(Positions.index).all()
    return render_template('nominees.html', positions=positions)


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    results = Candidate.query.filter(Candidate.name.ilike(f'%{search}%')).all()
    suggestions = [{'id': candidate.id, 'label': candidate.name.title()} for candidate in results]
    print(suggestions)
    return jsonify(suggestions)


@app.route('/nominate', methods=['GET', 'POST'])
def nominate():
    ids = []
    if request.method == 'POST':
        print('Request Received')
        nominations = request.form.to_dict()
        nominations.pop('csrf_token')
        for position_id, candidate in nominations.items():
            if candidate in ["", None]:
                continue
            candidate_obj = Candidate.find_obj_by(name=candidate)
            candidate_id = candidate_obj.id
            candidate_position = CandidatePositionAssociation.query.filter_by(
                candidate_id=candidate_id, position_id=position_id
            ).first()
            if candidate_position:
                candidate_position.vote_count += 1
            else:
                candidate_position = CandidatePositionAssociation(candidate_id=candidate_id, position_id=position_id,
                                                                  vote_count=1)
            candidate_position.save()
        db.session.commit()
        return nominations

