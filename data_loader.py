import os
import pandas as pd

CSV_PATH = os.path.join("data", "db_temperature.csv")

def load_db_temperature():

    use_cols = [
        "Timestamp", "CPU Temperature (°C)"]
    df = pd.read_csv(CSV_PATH, usecols=use_cols, parse_dates=["Timestamp"])

    df["ts"] = pd.to_datetime(df["Timestamp"])

    df = df.drop(columns=["Timestamp"])

    df = df.rename(columns={"CPU Temperature (°C)": "temp"})

    df = df.set_index("ts").sort_index()

    return df

if __name__ == "__main__":
    ts = load_db_temperature()
    print(ts.head())