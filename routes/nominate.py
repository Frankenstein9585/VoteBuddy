from flask_login import login_required, current_user
from config import app, db
from flask import render_template, request, redirect, url_for, jsonify
from models import Positions, User


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    results = User.query.filter(User.name.ilike(f'%{search}%')).all()
    suggestions = [{'id': user.id, 'label': user.name.title()} for user in results]
    print(suggestions)
    return jsonify(suggestions)


@app.route('/nominate')
def nominate():
    positions = Positions.query.all()
    return render_template('nominate.html', positions=positions)
