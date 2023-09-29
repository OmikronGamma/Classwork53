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
    ...

# copy the other methods from CatalogueRouter and change 'catalogue' to 'vetclinic'
