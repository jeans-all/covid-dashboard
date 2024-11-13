# src/data_loader.py
import pandas as pd
import requests
from datetime import datetime, timedelta
import streamlit as st

# 데이터 URL
BASE_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"

@st.cache_data(ttl=3600)  # 1시간 동안 데이터 캐시
def load_daily_data(date_str):
    """
    특정 날짜의 COVID-19 데이터를 불러옵니다.
    날짜 형식: MM-DD-YYYY.csv
    """
    try:
        url = f"{BASE_URL}{date_str}.csv"
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"데이터 로드 중 에러 발생: {e}")
        return None

def get_latest_data():
    """
    가장 최근 데이터를 가져옵니다.
    """
    # 어제 날짜부터 시작해서 가용한 최신 데이터를 찾습니다
    today = datetime.now()
    for i in range(1, 10):  # 최대 10일 전까지 확인
        check_date = today - timedelta(days=i)
        date_str = check_date.strftime('%m-%d-%Y')
        df = load_daily_data(date_str)
        if df is not None:
            return df, date_str
    return None, None

def process_data(df):
    """
    데이터를 처리하고 필요한 컬럼만 선택합니다.
    """
    if df is None:
        return None
    
    # 필요한 컬럼만 선택
    useful_columns = ['Country_Region', 'Confirmed', 'Deaths', 'Recovered', 'Active']
    
    # 국가별 합계 계산
    grouped_df = df.groupby('Country_Region')[useful_columns[1:]].sum().reset_index()
    
    # 치명률 계산
    grouped_df['Fatality_Rate'] = (grouped_df['Deaths'] / grouped_df['Confirmed'] * 100).round(2)
    
    return grouped_df

def get_global_stats():
    """
    전세계 통계를 반환합니다.
    """
    df, date_str = get_latest_data()
    if df is not None:
        global_data = {
            'total_cases': df['Confirmed'].sum(),
            'total_deaths': df['Deaths'].sum(),
            'date': date_str
        }
        global_data['fatality_rate'] = (global_data['total_deaths'] / global_data['total_cases'] * 100).round(2)
        return global_data
    return None

# 테스트 코드
if __name__ == "__main__":
    df, date = get_latest_data()
    if df is not None:
        print(f"Latest data date: {date}")
        print("\nGlobal Statistics:")
        stats = get_global_stats()
        print(stats)
