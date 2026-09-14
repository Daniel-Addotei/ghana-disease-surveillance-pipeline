# Multiple surveillance reports stored as a list of dictionaries
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



print("Disease Surveillance Reports")
print("----------------------------")

for surveillance_report in surveillance_reports:
    print ("\n----------------------------")
    print ("Report Week:", surveillance_report["report_week"])
    print ("Region:", surveillance_report["region"])
    print ("District:", surveillance_report["district"])
    print ("Disease:", surveillance_report["disease"])
    print ("Suspected Cases:", surveillance_report["suspected_cases"])
    print ("Confirmed Cases:", surveillance_report["confirmed_cases"])
    print ("Deaths:", surveillance_report["deaths"])