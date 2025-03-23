import pandas as pd

df = pd.read_csv("./dataset/QQQ.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

train_df = df[(df["Date"].dt.year ==2024) & (df["Date"].dt.month <= 6)]
new_df = train_df[["Date","Close/Last","Open"]].copy()

new_df["Rise/Fall"] = 0
for idx in new_df.index:
    if new_df.loc[idx, "Close/Last"] - new_df.loc[idx, "Open"]>0:
        new_df.loc[idx, "Rise/Fall"] =1
df.drop(['Close/Last', 'Open'], axis=1)
new_df.to_csv("output.csv", index=False)
