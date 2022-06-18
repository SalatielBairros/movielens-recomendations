from os import environ as env
from environment.constants import EnvironmentVariables, DataRepositoryType
from repository.local_storage_repository import LocalStorageRepository

class DataRepository:
    def __init__(self):
        pass

    def __get_repository__(self):
        if(env[EnvironmentVariables.data_repository_type] == DataRepositoryType.local_storage):
            return LocalStorageRepository()
        raise Exception(f'Unknown data repository type: {env[EnvironmentVariables.data_repository_type]}')

    def get_ratings(self):
        return self.__get_repository__().get_ratings()
    