# Recommendation Systems

This material is based on this [Alura course](https://cursos.alura.com.br/course/introducao-a-sistemas-de-recomendacao-com-python).

The material from course is implemented using Jupyter Notebooks, but here I implement a variation using only python and a different project structure. The goal is to implement my own version of KNN to recommend movies to a user.

The data-source can be obtained [here](https://grouplens.org/datasets/movielens/latest/). The small dataset is included on this repository, but the full dataset must be downloaded separately.

## Dependencies

    - [pandas](https://pandas.pydata.org/)
    - [numpy](https://numpy.org/)
    - [fastAPI](https://fastapi.tiangolo.com/)

    ```bash
    pip install pandas 
    pip install numpy 
    pip install fastapi
    pip install "uvicorn[standard]"
    ```

## Running de Code

There is two ways to run the code: (1) running the recommendations on the console and (2) using a FastAPI server.

(1)
```bash
python main.py
```

(2)
```bash
uvicorn main:app --reload
```

> The `reload` option is used to reload the code when it changes and should be used only when developing.

For te API, the Documentation can be found at [http://localhost:8000/docs](http://localhost:8000/docs).

## Improvements

* Start using mongodb to store the data and not in a csv file.
* Create workers to preprocess de data.