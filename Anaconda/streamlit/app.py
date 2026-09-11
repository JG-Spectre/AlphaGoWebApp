import streamlit as st # type: ignore
import time

def type_text(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(f"{typed}")
        time.sleep(0.1)

def type_header(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(f"# {typed}")
        time.sleep(0.1)

def type_subheader(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(f"### {typed}")
        time.sleep(0.1)

with st.sidebar:
    st.title("GitHub Copilot 소개")
    menu = st.radio(
        "섹션 선택",
        ["Github", "Copilot", "요금제 비교", "FAQ"]
    )


st.set_page_config(page_title="GitHub Copilot")

st.logo("source/copilot.png")

st.image("source/copilot.png", width=400)
type_header("GitHub Copilot")
type_subheader("Imagination to Life.")
type_text("프로그래밍에 새로운 **역사**를 쓰는 *AI 에이젼트*\n")

st.write("GitHub")
time.sleep(1)

git_tab1, git_tab2, git_tab3 = st.tabs(["GitHub", "Copilot", "요금제 비교"])

with git_tab1:
    st.header("애초에 GitHub가 뭔데?")
    st.write("GitHub는 소프트웨어 개발자들의 필수 플랫폼이라고 불리는 웹사이트로, 소스 코드 관리와 버전 관리를 위한 Git 저장소를 호스팅하는 서비스입니다.")
    st.write("GitHub에선 개발자들이 협업하여 프로젝트를 진행할 수 있으며, 오픈 소스 프로젝트를 공유하고 기여할 수 있는 환경을 제공합니다.")
    st.write("또한, GitHub는 이슈 추적, 코드 리뷰, 프로젝트 관리 도구 등 다양한 기능을 제공하여 개발자들이 효율적으로 작업할 수 있도록 지원합니다.")

with git_tab2:
    st.header("GitHub에서 만들어진 에이젼트, Copilot")
    st.write("GitHub Copilot은 AI 기반 코드 자동완성 도구입니다.")

with git_tab3:
    st.header("요금제 비교") 
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Free")
        st.markdown("##### 무료")
        st.write("매월 2000회 코드 작성")
        st.write("Claude Haiku 4.5, GPT-5 mini 등에 액세스")
        st.write("Copilot CLI")
        st.write("커뮤니티 지원")

    with col2:
        st.subheader("Pro")
        st.markdown("##### 월 $10")
        st.write("클라우드 에이젼트 및 코드 검토에 액세스")
        st.write("무제한 코드 완성과 다음 수정 제안")
        st.write("타사 에이젼트에 액세스")
        st.write("모델 선택")
        st.write("Pro 월간 크레딧 총 $15")
    with col3:
        st.subheader("Pro+")
        st.markdown("##### 월 $39")
        st.write("프리미엄 모델 액세스")
        st.write("감사 로그")
        st.write("Pro 대비 4배 더 많은 사용량")
        st.write("Pro+ 월간 크레딧 총 $70")
    with col4:
        st.subheader("Max")
        st.markdown("##### 월 $100")
        st.write("새로운 모델 및 기능 우선 이용")
        st.write("Pro+ 대비 2.9배 더 많은 사용량")
        st.write("Max 월간 크레딧 총 $200")

st.header("GitHub Copilot의 기능")
feat_tab1, feat_tab2, feat_tab3 = st.tabs(["코드 자동완성", "Copilot Chat", "Copilot CLI"])

with feat_tab1:
    st.write("코드를 작성하면 자동으로 다음 줄을 제안해줍니다.")

with feat_tab2:
    st.write("채팅으로 코드에 대해 질문하고 답변을 받을 수 있습니다.")

with feat_tab3:
    st.write("터미널에서 명령어를 물어보고 바로 실행할 수 있습니다.")