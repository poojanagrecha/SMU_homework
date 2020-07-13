import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

class SQLHelper():

    def __init__(self):
        self.connection_string = "sqlite:///Resources/hawaii.sqlite"
        self.engine = create_engine(self.connection_string)

    def TotalPrecipitation(self):
        query = f"""
                    SELECT 
                        date,
                        sum(prcp) as total_precipitation
                    FROM
                        measurement
                    GROUP BY
                        date
                    ORDER BY
                        date ASC;
                """

        conn = self.engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()

        return df

    def TotalStations(self):
        query = f"""
            SELECT 
                station as station_id,
                name as station_name,                
                latitude,
                longitude,
                elevation
            FROM
                station
            ORDER BY
                station_id ASC;
            """

        conn = self.engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()

        return df

    def activeTemp(self):
        query = f"""
            SELECT 
                station,
                date,
                tobs as temperature
            FROM
                measurement
            WHERE 
                station = 'USC00519281' AND
                date > '2016-08-23'
            ORDER BY
                date ASC;
            """

        conn = self.engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()

        return df

    #date must be a string
    #date must be format like '2017-08-23'
    def getTempInfoForDate(self, date):
        query = f"""
            SELECT 
                date,
                min(tobs) as min_temp,
                max(tobs) as max_temp,
                avg(tobs) as avg_temp
            FROM
                measurement
            WHERE
                date = '{date}'
            """

        conn = self.engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()

        return df

    #date must be a string
    #date must be format like '2017-08-23'
    def getTempInfoForDateRange(self, start, end):
        query = f"""
            SELECT 
                min(tobs) as min_temp,
                max(tobs) as max_temp,
                avg(tobs) as avg_temp
            FROM
                measurement
            WHERE
                date >= '{start}'
                AND date < '{end}'
            """

        conn = self.engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()

        return df
