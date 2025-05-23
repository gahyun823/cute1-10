import streamlit as st

# 페이지 설정
st.set_page_config(page_title="나의 소개", page_icon=":wave:", layout="centered")

# ⬇️ 여기에 너의 정보를 직접 입력해줘!
name = "정가현"
school = "고려대학교"
hobby = "야구보기, 밴드 영상 보기, 유튜브 시청하기"
email = "emilyseoul@naver.com"
profile_image_path = "profile.jpg"  # 같은 폴더에 있는 이미지 파일 경로

# 제목 및 인사말
st.title("안녕하세요! :wave:")
st.subheader(f"{name}입니다. 반가워요!")

# 프로필 이미지
try:
    st.image(profile_image_path, width=200, caption="프로필 사진")
except:
    st.warning("⚠️ 프로필 사진을 불러올 수 없습니다. 파일 경로를 확인해주세요.")

# 정보 출력
st.markdown("---")
st.write("## ✨ 나의 정보 ✨")
st.write(f"**이름:** {name}")
st.write(f"**학교:** {school}")
st.write(f"**취미:** {hobby}")
st.write(f"**이메일:** {email}")

# 푸터
st.markdown("---")
st.caption("Made with ❤️ by Streamlit")
