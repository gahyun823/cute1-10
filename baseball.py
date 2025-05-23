import streamlit as st

# ⚾️ 기본 설정
st.set_page_config(page_title="KBO 2025 상대전적", page_icon="⚾", layout="centered")

# 팀 정보 정의
teams = {
    "LG 트윈스": {"color": "#C60C30", "emoji": "🦁"},
    "KT 위즈": {"color": "#000000", "emoji": "🧙‍♂️"},
    "NC 다이노스": {"color": "#005BAC", "emoji": "🦕"},
    "두산 베어스": {"color": "#1F1F1F", "emoji": "🐻"},
    "SSG 랜더스": {"color": "#E60012", "emoji": "🚀"},
    "KIA 타이거즈": {"color": "#D6001C", "emoji": "🐯"},
    "삼성 라이온즈": {"color": "#1B4080", "emoji": "🦁"},
    "롯데 자이언츠": {"color": "#E6002D", "emoji": "⚓️"},
    "키움 히어로즈": {"color": "#722F37", "emoji": "🦸"},
    "한화 이글스": {"color": "#FA5B1F", "emoji": "🦅"}
}

# 🎯 타이틀
st.markdown("<h1 style='text-align: center;'>⚾️ 2025 KBO 리그 팀별 상대전적</h1>", unsafe_allow_html=True)
st.markdown("### 팀을 선택하면 올 시즌 상대전적을 보여드려요!")

# 🧩 팀 선택
col1, col2 = st.columns(2)
with col1:
    team1 = st.selectbox("🏏 내 팀을 선택하세요", list(teams.keys()), index=0)
with col2:
    team2 = st.selectbox("🏟️ 상대 팀을 선택하세요", list(teams.keys()), index=1)

# 🎨 팀별 색상 적용
def style_team_name(name):
    color = teams[name]["color"]
    emoji = teams[name]["emoji"]
    return f"<span style='color:{color}; font-weight:bold'>{emoji} {name}</span>"

# 예시 상대전적 데이터 (임의 값)
matchups = {
    ("LG 트윈스", "KT 위즈"): "LG 9승 7패",
    ("두산 베어스", "한화 이글스"): "한화 10승 6패",
    ("삼성 라이온즈", "NC 다이노스"): "삼성 8승 8패",
    # 필요 시 나머지도 추가 가능
}

# 결과 출력
st.markdown("---")
if team1 == team2:
    st.warning("⚠️ 같은 팀을 선택할 수 없어요!")
else:
    result = matchups.get((team1, team2)) or matchups.get((team2, team1))
    if result:
        st.markdown(f"### 📊 {style_team_name(team1)} vs {style_team_name(team2)}", unsafe_allow_html=True)
        st.success(f"💥 결과: {result}")
    else:
        st.info(f"📅 {team1}와 {team2}의 전적 데이터는 아직 등록되지 않았어요!")

# ⚾ 푸터
st.markdown("---")
st.caption("Made with ❤️ by 야구 사랑 개발자")
