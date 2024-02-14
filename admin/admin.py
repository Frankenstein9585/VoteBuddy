from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user


class UserView(ModelView):
    can_edit = True
    column_exclude_list = ['created_at', 'updated_at', 'password']

    def is_accessible(self):
        from models import Admin
        if current_user.is_authenticated:
            return isinstance(current_user, Admin)

    def inaccessible_callback(self, name, **kwargs):
        return 'You should not be here!'


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        from models import Admin
        if current_user.is_authenticated:
            return isinstance(current_user, Admin)

    def inaccessible_callback(self, name, **kwargs):
        return 'You should not be here!'


class VoteView(ModelView):
    can_delete = False

    column_list = ['user', 'candidate', 'position']

    def is_accessible(self):
        from models import Admin
        if current_user.is_authenticated:
            return isinstance(current_user, Admin)

    def inaccessible_callback(self, name, **kwargs):
        return 'You should not be here!'


class CandidateView(ModelView):
    form_columns = ['matric_number', 'first_name', 'last_name', 'image', 'faculty', 'department', 'programme',
                    'positions']
    column_list = form_columns
    form_excluded_columns = ['created_at', 'updated_at']

    def is_accessible(self):
        from models import Admin
        if current_user.is_authenticated:
            return isinstance(current_user, Admin)

    def inaccessible_callback(self, name, **kwargs):
        return 'You should not be here!'


class PositionsView(ModelView):
    column_list = ['title', 'candidates']
    column_exclude_list = ['created_at', 'updated_at']
    form_excluded_columns = ['created_at', 'updated_at']

    def is_accessible(self):
        from models import Admin
        if current_user.is_authenticated:
            return isinstance(current_user, Admin)

    def inaccessible_callback(self, name, **kwargs):
        return 'You should not be here!'


class CandidateVotesView(ModelView):
    column_list = ['candidate_id', 'position_id', 'vote_count']
    form_excluded_columns = ['created_at', 'updated_at']
    can_create = False
    can_edit = False
    can_delete = False

    def is_accessible(self):
        from models import Admin
        if current_user.is_authenticated:
            return isinstance(current_user, Admin)

    def inaccessible_callback(self, name, **kwargs):
        return 'You should not be here!'
