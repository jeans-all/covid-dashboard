# src/app.py
import streamlit as st
from data_loader import get_global_stats

def main():
    # 페이지 기본 설정
    st.set_page_config(
        page_title="COVID-19 Dashboard",
        page_icon="🦠",
        layout="wide"
    )
    
    # 제목
    st.title("🦠 COVID-19 Dashboard")
    
    # 전역 데이터 가져오기
    global_stats = get_global_stats()
    
    if global_stats:
        # 세 개의 칼럼으로 나눔
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="전세계 확진자", 
                value=f"{global_stats['total_cases']:,}명"
            )
        
        with col2:
            st.metric(
                label="전세계 사망자", 
                value=f"{global_stats['total_deaths']:,}명"
            )
        
        with col3:
            st.metric(
                label="치명률", 
                value=f"{global_stats['fatality_rate']}%"
            )
        
        st.caption(f"마지막 업데이트: {global_stats['date']}")
    
    else:
        st.error("데이터를 불러오는데 실패했습니다.")

if __name__ == "__main__":
    main()
