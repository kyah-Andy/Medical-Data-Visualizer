import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "medical_examination.csv")

# 1 Import the data
df = pd.read_csv(file_path)

# 2 Add overweight column
df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25).astype(int)

# 3 Normalize cholesterol and glucose (0 = good, 1 = bad)
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


def draw_cat_plot():
    # 4 Create DataFrame for categorical plot using melt
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    # 5 Group and reformat the data
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # 6 Draw the catplot
    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar"
    ).fig

    # 7 Get the figure for the output
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # Clean data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Ensure numeric only
    df_heat = df_heat.select_dtypes(include=["number"])

    # Drop NaN
    df_heat = df_heat.dropna()

    # Correlation
    corr = df_heat.corr()

    # Mask
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Plot
    fig, ax = plt.subplots(figsize=(12, 10))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax
    )

    fig.savefig("heatmap.png")
    return fig