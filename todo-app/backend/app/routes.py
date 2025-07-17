@api_bp.route('/tasks/<int:task_id>/favorite', methods=['PATCH'])
def update_task_favorite(task_id):
    data = request.json
    task = Task.query.get_or_404(task_id)
    is_favorite = data.get('isFavorite')
    if is_favorite is not None:
        task.isFavorite = is_favorite
        db.session.commit()
        return jsonify(task.to_dict())
    return jsonify({'error': 'No isFavorite provided'}), 400
from datetime import datetime
from flask import Blueprint, request, jsonify
from app.models import db, Task

api_bp = Blueprint('api', __name__)

@api_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@api_bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if 'dueDate' in data and data['dueDate']:
        data['dueDate'] = datetime.strptime(data['dueDate'], '%Y-%m-%d').date()
        task = Task(**data)
        db.session.add(task)
        db.session.commit()
    return jsonify(task.to_dict()), 201

@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = Task.query.get_or_404(task_id)
    if 'dueDate' in data and data['dueDate']:
        if isinstance(data['dueDate'], str):
            data['dueDate'] = datetime.strptime(data['dueDate'], '%Y-%m-%d').date()
    for key, value in data.items():
        setattr(task, key, value)
    db.session.commit()
    return jsonify(task.to_dict())

@api_bp.route('/tasks/<int:task_id>/status', methods=['PATCH'])
def update_task_status(task_id):
    data = request.json
    task = Task.query.get_or_404(task_id)
    new_status = data.get('status')
    if new_status:
        task.status = new_status
        db.session.commit()
        return jsonify(task.to_dict())
    return jsonify({'error': 'No status provided'}), 400

@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})