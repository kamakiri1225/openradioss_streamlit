import streamlit as st
import analytics, intro_end, output_file

def main():
    st.header('OpenRadioss Setting GUI', divider='rainbow')
    st.title("解析の種類")

    options1 = ["線形解析", "熱解析", "流体解析", "衝撃解析", "エアバッグ解析"]
    sel1 = st.selectbox('分野', options1, index=0)
    st.write(f'解析を行う分野は{sel1}です。')

    st.markdown('---')
    st.title("解析の設定")

    if sel1 == "線形解析":
        code_part, code_prop, code_mat = analytics.test_func()
        code_bcs =  analytics.test_func1()

    if sel1 == "熱解析":
        pass

    if sel1 == "流体解析":
        pass

    if sel1 == "衝撃解析":
        pass

    if sel1 == "エアバッグ解析":
        pass

    st.markdown('---')

    st.title("設定ファイルの出力")

    title = st.text_input("解析タイトル", "templete")

    intro, end = intro_end.intro_end(title)

    try:
        code = intro + code_part + code_prop + code_mat + code_bcs + end
    except:
        pass

    # ファイル名
    output_file.output_file(code)

if __name__=="__main__":
    st.set_page_config(
            page_title="Ex-stream-ly Cool App",
            page_icon="🧊",
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"
            }
        )
    main()