import streamlit as st

# 기본 설정
st.set_page_config(page_title="KBO 2025 상대전적", page_icon="⚾", layout="centered")

# 팀 데이터
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
    "한화 이글스": {"color": "#FA5B1F", "emoji": "🦅"},
}

# 상대전적 (예시 데이터, 원하는 값으로 수정 가능)
matchups = {}
team_names = list(teams.keys())
for i in range(len(team_names)):
    for j in range(i + 1, len(team_names)):
        team1, team2 = team_names[i], team_names[j]
        win1 = 8 + (i + j) % 3  # 예시 로직: 다양한 값으로 자동 생성
        win2 = 16 - win1
        matchups[(team1, team2)] = f"{team1} {win1}승 {win2}패"

# 스타일 함수
def style_team(name):
    color = teams[name]["color"]
    emoji = teams[name]["emoji"]
    return f"<span style='color:{color}; font-weight:bold'>{emoji} {name}</span>"

# 타이틀
st.markdown("<h1 style='text-align: center;'>⚾️ 2025 KBO 리그 상대전적</h1>", unsafe_allow_html=True)
st.markdown("### 두 팀을 선택하면 올해의 맞대결 전적을 보여줄게요!")

# 팀 선택 UI
col1, col2 = st.columns(2)
with col1:
    team1 = st.selectbox("🏏 팀 A", team_names)
with col2:
    team2 = st.selectbox("🏟️ 팀 B", team_names, index=1)

# 결과 표시
st.markdown("---")
if team1 == team2:
    st.warning("⚠️ 같은 팀은 비교할 수 없어요!")
else:
    matchup = matchups.get((team1, team2)) or matchups.get((team2, team1))
    st.markdown(f"### 📊 {style_team(team1)} vs {style_team(team2)}", unsafe_allow_html=True)
    st.success(f"📈 결과: {matchup}")

# 푸터
st.markdown("---")
st.caption("🐰 2025 KBO 리그 통계 서비스 · Made with ❤️ and ⚾️")
