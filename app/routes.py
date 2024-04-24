# app/routes.py
from flask import jsonify, request
from datetime import datetime
from app import app, db
from app.models import Event

@app.route('/events', methods=['GET'])
def get_events():
    try:
        starts_at = request.args.get('starts_at')
        ends_at = request.args.get('ends_at')

        starts_at = datetime.fromisoformat(starts_at)
        ends_at = datetime.fromisoformat(ends_at)

        events = Event.query.filter(
            Event.start_time >= starts_at,
            Event.end_time <= ends_at,
            Event.sell_mode == 'online'
        ).all()

        event_data = [{
            'id': event.id,
            'name': event.name,
            'start_time': event.start_time.isoformat(),
            'end_time': event.end_time.isoformat(),
            'sell_mode': event.sell_mode
        } for event in events]

        return jsonify(event_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
