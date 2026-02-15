import pandas as pd

def load_data(filepath="../data/students_data.csv"
):

    student_df = pd.read_csv(filepath)
    return student_df


if __name__ == "__main__":
    df = load_data()
    # print(df)


def clean_data():
    df = load_data()
    for col in df.columns:
        if df[col].isnull().any():
            if df[col].dtype != 'object':
                df[col] = df[col].fillna(df[col].mean())
    return df


if __name__ =="__main__":
    df = clean_data()
    print(df)