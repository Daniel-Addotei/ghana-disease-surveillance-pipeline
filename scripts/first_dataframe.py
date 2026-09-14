import pandas as pd
surveillance_reports = [
    {   "report_week": 25,
        "region": "Greater Accra",
        "district": "Ayawaso Central",
        "disease": "Cholera",
        "suspected_cases": 27,
        "confirmed_cases": 12,
        "deaths": 1
    },
    {
        "report_week": 25,
        "region": "Volta",
        "district": "Ketu South",
        "disease": "Measles",
        "suspected_cases": 45,
        "confirmed_cases": 18,
        "deaths": 2
    },
    {   "report_week": 25,
        "region": "Northern",
        "district": "Tamale Metro",
        "disease": "Meningitis",
        "suspected_cases": 30,
        "confirmed_cases": 15,
        "deaths": 4
    },
    {   "report_week": 25,
        "region": "Ashanti",
        "district": "Kumasi Metro",
        "disease": "Yellow Fever",
        "suspected_cases": 32,
        "confirmed_cases": 9,
        "deaths": 3
    }
]
df = pd.DataFrame(surveillance_reports)
print(df)

