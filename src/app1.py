# src/app.py
import streamlit as st

def main():
    # 페이지 기본 설정
    st.set_page_config(
        page_title="COVID-19 Dashboard",
        page_icon="🦠",
        layout="wide"
    )
    
    # 제목
    st.title("🦠 COVID-19 Dashboard")
    
    # 간단한 설명
    st.markdown("""
    이 대시보드는 COVID-19 데이터를 시각화하여 보여줍니다.
    * 데이터 출처: JHU CSSE COVID-19 Dataset
    * 최종 업데이트: 2024년
    """)
    
    # 사이드바
    st.sidebar.header("필터")
    st.sidebar.text("여기에 나중에 필터가 들어갈 예정입니다.")
    
    # 메인 페이지
    st.header("주요 통계")
    
    # 세 개의 칼럼으로 나눔
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="전세계 확진자", value="준비 중", delta="추가 예정")
    
    with col2:
        st.metric(label="전세계 사망자", value="준비 중", delta="추가 예정")
    
    with col3:
        st.metric(label="치명률", value="준비 중", delta="추가 예정")

if __name__ == "__main__":
    main()
