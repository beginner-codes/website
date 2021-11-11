# Beginner.Codes Website

The [beginner.codes](https://beginner.codes) website. Built collaboratively by the members of the Beginner.Codes discord server!

## Setup & Run

We're using Poetry to manage our dependencies. It also helpfully creates a virtual environment for us. You'll Python 3.9, start by installing Poetry.
```shell
python -m pip install poetry
```
Once it completes installing go to the root of the project and run
```shell
poetry install
```
This will install all the necessary modules inside of a virtual environment.

**Launching**

From the terminal you can launch the site by running
```shell
poetry run python -m bc_website
```
This assumes that you're in the repo folder where you can see the `bc_website` folder along with the `LICENSE`, `poetry.lock`, `pyproject.toml`, and `README.md` files.

## Code

Code should go inside the `bc_website` folder.
