############ main.py
import report_airport
import report_alert
import report_ccvi
import report_construction
import report_infra_investment
import report_loan
import report_streetcaping

# import required lib
import time
import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 


# set db_host
db_host = "host.docker.internal"
time_each_report = 10

# set connection function

def connect_db():
    return psycopg2.connect(host=db_host,dbname="chicago_business_intelligence", user="postgres" , password="12345")


def main_report():
    # set report function

    def generate_report_airport_s():
        db_connection = connect_db()
        return report_airport.rp_airport(db_connection)

    def generate_report_alert_s():
        db_connection = connect_db()
        return report_alert.rp_alert(db_connection)


    def generate_report_ccvi_s():
        db_connection = connect_db()
        return report_ccvi.rp_ccvi(db_connection)

    def generate_report_construction_s():
        db_connection = connect_db()
        return report_construction.rp_construction(db_connection)

    def generate_report_infra_investment_s():
        db_connection = connect_db()
        return report_infra_investment.rp_infra(db_connection)

    def generate_report_loan_s():
        db_connection = connect_db()
        return report_loan.rp_loan(db_connection)

    def generate_report_streetcaping_s():
        db_connection = connect_db()
        return report_streetcaping.rp_street(db_connection)

    print("*************************")
    print("-----report_airport-----")
    print("*************************")
    print(generate_report_airport_s())
    time.sleep(time_each_report)


    print("*************************")
    print("-----report_alert-----")
    print("*************************")
    print(generate_report_alert_s())
    time.sleep(time_each_report)


    print("*************************")
    print("-----report_ccvi-----")
    print("*************************")
    print(generate_report_ccvi_s())
    time.sleep(time_each_report)


    print("*************************")
    print("-----report_construction-----")
    print("*************************")
    print(generate_report_construction_s())
    time.sleep(time_each_report)


    print("*************************")
    print("-----report_infra_investment-----")
    print("*************************")
    print(generate_report_infra_investment_s())
    time.sleep(time_each_report)


    print("*************************")
    print("-----report_loan-----")
    print("*************************")
    print(generate_report_loan_s())

    time.sleep(time_each_report)


    print("*************************")
    print("-----report_streetcaping-----")
    print("*************************")
    print(generate_report_streetcaping_s())

    time.sleep(time_each_report)


# dudge whether there are any data in db 
try_time = 0

while(True):
    try:
        db_connection = connect_db()
        # connect to the postgresql
        cursor = db_connection.cursor()
        # get data
        select_data = (
            """
                SELECT * FROM "neighborhood_community_zip";
            """)
        # create the table
        cursor.execute(select_data)
        result_1 = cursor.fetchall()
        # set dataframe
        df_1 = pd.DataFrame(result_1)
        df_1.columns = ["id","geo_id","zipcode","community","neighborhood"]
        df_1 = df_1[["zipcode","community","neighborhood"]]
        main_report()
        break
    except:
        if (try_time > 10):
            print("fall this time")
            break
        try_time += 1
        time.sleep(60)








