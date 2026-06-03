import pandas as pd  # Import pandas library

try:
    # Read CSV file
    df = pd.read_csv("students.csv")

    # Display complete dataset
    print("Student Dataset")
    print(df)

    # Calculate average marks
    print("\nAverage Marks:")
    print(df["Marks"].mean())

    # Filter CSE students
    print("\nCSE Students:")
    print(df[df["Department"] == "CSE"])

    # Department-wise average marks
    print("\nDepartment Wise Average Marks:")
    print(df.groupby("Department")["Marks"].mean())

except Exception as e:
    print("Error:", e)