import logging
from repository.data_repository import DataRepository
import pandas as pd

class FeatureEngineeringCommand:
    def __init__(self) -> None:
        self.commands = []
        self.data_repository = DataRepository()

    def add_command(self, command):
        self.commands.append(command)
        return self

    def execute(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        ratings, movies = self.__load_data__()
        for command in self.commands:
            logging.info(f"Executing command {command.__name__}")
            ratings, movies = command(ratings, movies).execute()
        self.__save_data__(ratings, movies)
        logging.info("Feature engineering finished")
        return ratings, movies

    def __load_data__(self):
        ratings = self.data_repository.get_original_ratings()
        movies = self.data_repository.get_original_movies()
        return ratings, movies

    def __save_data__(self, ratings: pd.DataFrame, movies: pd.DataFrame):
        self.data_repository.save_ratings(ratings)
        self.data_repository.save_movies(movies)