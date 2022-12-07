import pandas as pd


def main():
    df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
    )
    print(df)
    print(df.describe())

    ages = pd.Series([2, 35, 58], name="Age")
    ages
    print(ages.max())


if __name__ == "__main__":
    main()
