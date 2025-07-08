import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    schema = ["student_id", "age"]

    df = pd.DataFrame(data=student_data, columns = schema)

    return df
    