from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user


class MyModelView(ModelView):
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
