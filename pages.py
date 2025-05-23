import streamlit as st

# 🎀 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🐰", layout="centered")

# 🎨 스타일 (연분홍 테마 적용)
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .stApp {
        font-family: "Helvetica", sans-serif;
        color: #333333;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #d63384;
    }
    .subtitle {
        font-size: 22px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# 🐰 타이틀
st.markdown('<p class="title">🐰 MBTI로 알아보는 나의 진로 🎓</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">MBTI를 선택하면, 나에게 딱 맞는 직업을 알려줄게요!</p>', unsafe_allow_html=True)
st.markdown("---")

# 🌸 MBTI 선택
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
selected_mbti = st.selectbox("🌟 내 MBTI를 골라보세요!", mbti_list)

# 🎯 추천 직업 데이터 (예시)
job_recommendations = {
    "INTJ": ["전략 컨설턴트", "데이터 사이언티스트", "연구원"],
    "ENFP": ["광고기획자", "콘텐츠 크리에이터", "교사"],
    "ISFJ": ["간호사", "사회복지사", "도서관 사서"],
    "ESTP": ["기업가", "세일즈 매니저", "이벤트 플래너"],
    # 나머지도 필요하면 추가 가능
}

# 🧠 결과 출력
if selected_mbti:
    st.subheader(f"📌 {selected_mbti} 유형에게 어울리는 직업은?")
    jobs = job_recommendations.get(selected_mbti, ["아직 준비 중이에요! 💡"])
    for job in jobs:
        st.markdown(f"- 💼 {job}")
else:
    st.info("MBTI를 선택하면 추천 직업이 나와요! 😊")

# 🐰 귀여운 푸터
st.markdown("---")
st.markdown("🐇 _이 웹앱은 당신의 진로 고민을 귀엽게 해결해드려요!_ 🎀")
