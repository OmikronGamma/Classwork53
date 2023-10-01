# routers/vetclinic.py

class VetClinicRouter:
    """
    A router to control all database operations on models in the
    vetclinic application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read vetclinic models go to vetclinic db.
        """
        if model._meta.app_label == 'vetclinic':
            return 'vetclinic'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write vetclinic models go to vetclinic db.
        """
        if model._meta.app_label == 'vetclinic':
            return 'vetclinic'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the vetclinic app is involved.
        """
        if obj1._meta.app_label == 'vetclinic' or \
           obj2._meta.app_label == 'vetclinic':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the catalogue app only appears in the 'catalogue'
        database.
        """
        if app_label == 'vetclinic':
            return db == 'vetclinic'
        return None
