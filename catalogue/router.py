# class CatalogueRouter:
#     """
#     A router to control all database operations on models in the
#     catalogue application.
#     """
#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read catalogue models go to catalogue db.
#         """
#         if model._meta.app_label == 'catalogue':
#             return 'catalogue'
#         return None
#
#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write catalogue models go to catalogue db.
#         """
#         if model._meta.app_label == 'catalogue':
#             return 'catalogue'
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Allow relations if a model in the catalogue app is involved.
#         """
#         if obj1._meta.app_label == 'catalogue' or \
#            obj2._meta.app_label == 'catalogue':
#            return True
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Make sure the catalogue app only appears in the 'catalogue'
#         database.
#         """
#         if app_label == 'catalogue':
#             return db == 'catalogue'
#         return None

class CatalogueRouter:
    def db_for_read(self, model, **hints):
        return 'catalogue'  # always read from 'catalogue' database

    def db_for_write(self, model, **hints):
        return 'catalogue'  # always write to 'catalogue' database

    def allow_relation(self, obj1, obj2, **hints):
        return True  # always allow relationships

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'catalogue'  # only allow migrations on 'catalogue' database
