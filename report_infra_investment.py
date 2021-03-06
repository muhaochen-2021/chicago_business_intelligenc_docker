import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
import pandas as pd
import numpy as np
from tqdm import tqdm

def rp_infra(db_connection):
        pd.set_option('display.max_columns', None)

        # connect to the postgresql
        cursor = db_connection.cursor()
        # get data
        select_data = (
            """
                SELECT * FROM "neighborhood_community_zip";
            """)
        # create the table
        cursor.execute(select_data)
        result_1 = cursor.fetchall();
        # set dataframe
        df_1 = pd.DataFrame(result_1)
        df_1.columns = ["id","geo_id","zipcode","community","neighborhood"]
        df_1 = df_1[["zipcode","community","neighborhood"]]
        df_1.zipcode = df_1.zipcode.astype("int")
        # get data
        select_data = (
            """
                SELECT * FROM "building_permits";
            """)
        # create the table
        cursor.execute(select_data)
        result_1 = cursor.fetchall();
        # set dataframe
        df_2 = pd.DataFrame(result_1)
        df_2.columns = ["id","permit_id","permit_type","total_fee","latitude","longitude","zipcode"]
        df_2 = df_2[["permit_id","total_fee","zipcode"]]
        df_2.zipcode = df_2.zipcode.astype("int")
        # get data
        select_data = (
            """
                SELECT * FROM "public_health_statistics";
            """)
        # create the table
        cursor.execute(select_data)
        result_1 = cursor.fetchall();
        # set dataframe
        df_3 = pd.DataFrame(result_1)
        df_3.columns = ["id","community_area_name","below_poverty_level","per_capita_income","unemployment"]
        df_3 = df_3[["community_area_name","below_poverty_level","unemployment"]]
        df_3.columns = ["community","below_poverty_level","unemployment"]
        pro_df_1 = df_3.merge(df_1,how='inner', on='community')
        pro_df_2 = pro_df_1.merge(df_2,how='inner', on='zipcode')
        pro_df_2["poverty+unemployment"] = pro_df_2["below_poverty_level"]+pro_df_2["unemployment"]
        pro_df_2 = pro_df_2[["neighborhood","total_fee","poverty+unemployment"]]
        pro_df_2 = pro_df_2.reset_index(drop=True)
        pro_df_3 = pro_df_2.groupby(by=["neighborhood","poverty+unemployment"],dropna=False)["total_fee"].sum().reset_index()
        rp_top5 = pro_df_3.sort_values(by="poverty+unemployment" , ascending=False)[:5]
        rp_top5 = rp_top5.reset_index(drop=True)

        return rp_top5