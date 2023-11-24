from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user


class UserView(ModelView):
    can_edit = False
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
    column_exclude_list = ['created_at', 'updated_at']
    form_excluded_columns = ['created_at', 'updated_at']

    def is_accessible(self):
        from models import Admin
        if current_user.is_authenticated:
            return isinstance(current_user, Admin)

    def inaccessible_callback(self, name, **kwargs):
        return 'You should not be here!'


class PositionsView(ModelView):
    column_exclude_list = ['created_at', 'updated_at']
    form_excluded_columns = ['created_at', 'updated_at']

    def is_accessible(self):
        from models import Admin
        if current_user.is_authenticated:
            return isinstance(current_user, Admin)

    def inaccessible_callback(self, name, **kwargs):
        return 'You should not be here!'
