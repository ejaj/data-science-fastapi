import pandas as pd

museums = pd.read_csv("museums.csv", index_col=0)
museums["total"] = museums["paid"] + museums["free"]
museums.to_csv("museums_with_total.csv")
