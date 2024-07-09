import streamlit as st
# 文字列をファイルに書き出す

def write_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)
    file.close()
    
def output_file(code):
    file_name = st.text_input("ファイル名（拡張子無）", "templete")
    st.write(f"出力するファイル名：{file_name}0000.rad")

    if st.button("ファイル出力",type="primary"):
        # Streamlitアプリケーション
        write_to_file(code, f"{file_name}000.rad")
        st.write("ファイルを出力しました")
    else:
        st.write("ファイルの出力がまたです")