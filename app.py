import streamlit as st
import analytics, intro_end
import pandas as pd


# 文字列をファイルに書き出す
def write_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)
    file.close()

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
    file_name = st.text_input("ファイル名（拡張子無）", "templete")
    st.write(f"出力するファイル名：{file_name}0000.rad")

    if st.button("ファイル出力",type="primary"):
        # Streamlitアプリケーション
        write_to_file(code, f"{file_name}000.rad")
        st.write("ファイルを出力しました")
    else:
        st.write("ファイルの出力がまたです")
    

if __name__=="__main__":
    main()