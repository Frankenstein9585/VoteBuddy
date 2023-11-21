from flask_admin.contrib.sqla import ModelView


class ModelView(ModelView):
    def is_accessible(self):
        return False
