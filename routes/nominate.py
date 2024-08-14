from flask_login import login_required, current_user
from config import app, db
from flask import render_template, request, redirect, url_for, jsonify
from models import Positions, User


@app.route('/nominees')
def nominate():
    positions = Positions.query.order_by(Positions.index).all()
    return render_template('nominees.html', positions=positions)


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    results = User.query.filter(User.name.ilike(f'%{search}%')).all()
    suggestions = [{'id': user.id, 'label': user.name.title()} for user in results]
    print(suggestions)
    return jsonify(suggestions)
