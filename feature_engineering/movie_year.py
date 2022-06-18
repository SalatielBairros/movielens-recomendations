import pandas as pd
import re

class MovieYear:
    __name__ = "MovieYear"

    def __init__(self, ratings: pd.DataFrame, movies: pd.DataFrame):
        self.ratings = ratings
        self.movies = movies

    def execute(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        self.movies['year'] = self.movies['title'].apply(self.__get_year_from_title__)
        self.movies['title'] = self.movies['title'].apply(self.__remove_year_from_title__)
        return self.ratings, self.movies

    def __get_year_from_title__(self, title: str) -> int:
        year_match = re.search(r'\((\d{4})\)', title)
        if year_match:
            return int(year_match.group(1))
        else:
            return 0

    def __remove_year_from_title__(self, title: str) -> str:
        year_match = re.search(r'\(\d{4}\)', title)
        if year_match:
            return title.replace(year_match.group(0), '')
        else:
            return title
    