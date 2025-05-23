import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="나의 소개", page_icon="👋", layout="centered")

# 사이드바
st.sidebar.title("👤 간단 소개")
st.sidebar.markdown("안녕하세요! 이 앱은 나를 소개하는 Streamlit 페이지입니다.")

# 제목
st.title("안녕하세요, 반가워요! 👋")

# 사진
uploaded_file = st.file_uploader("📸 나의 사진을 업로드 해보세요!", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="나의 사진", use_column_width=True)
else:
    st.image("https://via.placeholder.com/300x400.png?text=사진+업로드", caption="사진이 여기에 표시됩니다", use_column_width=True)

# 나의 정보 입력
st.header("📌 나에 대해 소개할게요")

name = st.text_input("이름", placeholder="예: 김학생")
school = st.text_input("학교", placeholder="예: 서울대학교")
hobbies = st.text_area("취미", placeholder="예: 독서, 음악 듣기, 여행하기")
email = st.text_input("이메일", placeholder="예: example@email.com")

# 정보 출력
if name or school or hobbies or email:
    st.subheader("📝 입력된 정보")
    st.markdown(f"**이름:** {name}")
    st.markdown(f"**학교:** {school}")
    st.markdown(f"**취미:** {hobbies}")
    st.markdown(f"**이메일:** {email}")
else:
    st.info("왼쪽에 정보를 입력하면 여기에 표시돼요!")

# 푸터
st.markdown("---")
st.markdown("ⓒ 2025 나의 소개 페이지 with Streamlit")
