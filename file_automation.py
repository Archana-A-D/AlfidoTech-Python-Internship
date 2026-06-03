import shutil

try:
    shutil.move("students.csv", "OldFiles/students.csv")
    print("File moved successfully")

except Exception as e:
    print("Error:", e)