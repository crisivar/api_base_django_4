class UsersRouter(object):
    """
    users/models.py => users, others => default
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'users' and obj2._meta.app_label == 'users':
            return True
        elif 'users' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'users' or model._meta.app_label == "users":
            return False
