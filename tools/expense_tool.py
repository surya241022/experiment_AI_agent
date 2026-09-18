import pandas as pd
import os

file_path ="data/expenses.xlsx"

if not os.path.exists(file_path):
    df=pd.DataFrame(
    columns=["id",
         "amount",
         "category",
         "description"]
    )

    df.to_excel(file_path,index=False)

def add_expense(amount, category, description):

    df = pd.read_excel(file_path)

    if df.empty:
        new_id=1
    else:
        new_id=int(df["id"].max()) + 1

    new_expense=pd.DataFrame([
        {"id":new_id,
         "amount":amount,
         "category":category,
         "description":description
        }
    ])
    df=pd.concat([df,new_expense],ignore_index=True)

    df.to_excel(file_path,index=False)

    return "expense added"

