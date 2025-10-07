import pandas as pd
import os
from sqlalchemy import create_engine
import psycopg2

df = pd.read_csv("/app/src/financial_transactions.csv",delimiter=',')
#print(df.head(10))

df['date'] = pd.to_datetime(df['date'],format='%Y-%m-%d')
#print(df.dtypes)
dff = df.loc[df['date'] >= '2019-01-01'].reset_index()

dffsql = dff.rename(columns={'transaction_id':'ts_id','date':'dt','customer_id':'cust_id','amount':'amt','type':'typ','description':'descrip'})
#print(dffsql.dtypes)
#print(dffsql.head(3))

#create_engine => username, password, hostname:port, database
def get_db_engine():
    return create_engine('postgresql://{}:{}@{}/{}'.format('root', 'root', 'pgcontainer.proyecto_itsrv:5432', 'analysis'))

#retry mechanism for connect to database
db_engine = get_db_engine().connect()

dffsql.to_sql(name='business.financial',con=db_engine, if_exists='replace', index=False)
#dff.to_csv('financial.csv', index=False)
db_engine.commit()
db_engine.close()