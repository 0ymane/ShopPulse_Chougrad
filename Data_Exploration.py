import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv("01_Donnees/train.csv", delimiter=",")
    return (df,)


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df):
    df.columns = df.columns.str.strip()
    df['Purchased'].value_counts()
    return


@app.cell
def _(df):
    df.describe()
    return


if __name__ == "__main__":
    app.run()
