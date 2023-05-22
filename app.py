# streamlit_app.py

import streamlit as st
from google.cloud import bigquery # 클라우드 기반의 데이터 웨어하우징 및 분석 서비스
import seaborn as sns
import pandas as pd
import pandas_gbq

from utils import credentials, SERVICE_KEY
client = bigquery.Client(credentials=credentials) # 구글 클라우드 빅쿼리 서비스와 상호 작용하기 위한 클라이언트 객체를 생성하는 코드
# bigquery.Client() 빅쿼리 서비스와 통신하여 데이터베이스 작업을 수행하는 데 사용, 데이터베이스에 연결하고 쿼리를 실행하거나 테이블을 생성, 수정, 삭제하는 등 작업 수행
# credentials 매개변수 : 인증 정보를 지정하는 데 사용됩니다.

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600) # 캐시 기능 사용하는 데코레이터, ttl : 캐시된 데이터의 유효 기간 지정(Time to Live)
def run_query(cols, name):
    st.write("Load DataFrame")
    sql = f"SELECT {cols} FROM streamlit-dashboard-369600.seoul.{name}" # sql 쿼리문을 생성하는 코드
    df = client.query(sql).to_dataframe() # SQL 쿼리를 실행하고 그 결과를 데이터프레임 형식으로 반환하는 코드

    st.dataframe(df)

def main():
    tableNames = st.selectbox("테이블 선택", ("realestate", "iris")) # 드롭다운 메뉴 제공
    if tableNames == "iris":
        run_query(cols="*", name="iris")
    else:
        sql = """
        SELECT STRING_AGG(column_name) # 컬럼 이름을 문자열로 합치는 역할 수행
        FROM `streamlit-dashboard-369600.seoul.INFORMATION_SCHEMA.COLUMNS` # 내 프로젝트로 바꿔야함!!
        where table_name = 'realestate'
        group by table_name
        """

        df = client.query(sql).to_dataframe()
        all_cols = df.values[0][0].split(",")
        columns = st.multiselect("컬럼명 선택", all_cols, default=all_cols) # 사용자로부터 컬럼 선택을 위한 다중 선택 상자를 제공하는 코드
        temp_Strings = ", ".join(columns) # 사용자가 선택한 컬럼들을 문자열로 합치는 코드
        run_query(temp_Strings, tableNames) # 앞서 생성한 문자열과 선택한 테이블 이름을 인자로하여 호출

if __name__ == "__main__":
    main()