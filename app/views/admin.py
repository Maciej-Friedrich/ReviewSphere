from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from ..models import User
from .. import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.before_request
@login_required
def require_admin():
    if current_user.role != 'admin':
        abort(403)


@admin_bp.route('/users')
def user_list():
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template('admin/users.html', users=users)


@admin_bp.route('/users/<int:user_id>/set_role', methods=['POST'])
def set_user_role(user_id):
    user = User.query.get_or_404(user_id)
    new_role = request.form.get('role')

    if new_role not in ['recenzent', 'moderator', 'admin']:
        flash('Nieprawidłowa rola.', 'danger')
        return redirect(url_for('admin.user_list'))

    user.role = new_role
    db.session.commit()
    flash(f"Zmieniono rolę użytkownika {user.username} na {new_role}.", "success")
    return redirect(url_for('admin.user_list'))
