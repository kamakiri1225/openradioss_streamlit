import streamlit as st
import parttemp, mattemp, proptemp
import pandas as pd


st.header('OpenRadioss Setting GUI', divider='rainbow')


st.title("❶解析の種類")

options1 = ["線形解析", "熱解析", "流体解析", "衝撃解析", "エアバッグ解析"]
# options2 = {
#     1: "線形解析",
#     2: "熱解析",
#     3: "流体解析"
# }
# sel2 = st.selectbox( label="性別（値で取得）",
#     options = (1, 2, 3), 
#     index=2,
#     format_func=lambda x: options2.get(x),
# )
# st.write(f'選択されたのは、{options2.get(sel2)} --> {sel2}です。')
# st.markdown('---')

sel1 = st.selectbox('分野', options1, index=0)
st.write(f'解析を行う分野は{sel1}です。')

def test_func():
    tab1, tab2, tab3 = st.tabs(["part1", "part2", "part3"])
    with tab1:
        st.subheader("プロパティ")
        propid = st.number_input("PROP ID number", step=1, min_value = 1)
        prop1 = ["prop1", "prop2", "prop3"]
        prop_sel1 = st.selectbox('プロパティ', prop1, index=0)
        st.write(prop_sel1)
        # st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        pd.options.display.precision = 10
        df_prop= pd.DataFrame(
            {
                "setting": ["Ishell", "Thick"],
                "value": [4, 0.33333],
                "explanation": [
                    "説明あり",
                    "説明あり",
                    ]
            }
        )
        # pd.options.display.precision = 2
        # st.dataframe(
        #     df_prop,
        #     column_config={
        #         "setting": "setting",
        #         # "url": st.column_config.LinkColumn("App URL")
        #     },
        #     # hide_index=True,
        # )
        df_prop = st.data_editor(df_prop)
        if prop_sel1 == "prop1": code_prop = proptemp.prpo_test(propid, df_prop)
        st.subheader("材料定義")
        # st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
        matid = st.number_input("MAT ID number", step=1, min_value = 1)
        mat1 = ["LAW1", "LAW2", "LAW3"]
        mat_sel1 = st.selectbox('材料', mat1, index=0)

        pd.options.display.precision = 10
        df_mat = pd.DataFrame(
            {
                "setting": ["rho", "E11", "E22", "NU11"],
                "value": [8.5e-5, 500, 500, 500],
                "explanation": [
                    "説明あり",
                    "説明あり",
                    "説明あり",
                    "説明あり",
                    ]
            }
        )
        # pd.options.display.precision = 2
        # st.dataframe(
        #     df_mat,
        #     column_config={
        #         "setting": "setting",
        #         # "url": st.column_config.LinkColumn("App URL")
        #     },
        #     # hide_index=True,
        # )
        df_mat = st.data_editor(df_mat)
        if mat_sel1 == "LAW1": code_mat = mattemp.Mat_test(matid, df_mat)

        st.subheader("パートの定義")
        # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        parttitle = st.text_input("パート名", "template")
        pid = st.number_input("PID number", step=1, min_value = 1)
                
        code_part = parttemp.Part_test(parttitle, pid, propid, matid)

    with tab2:
        pass
    with tab3:
        pass

    return code_part, code_prop, code_mat

st.markdown('---')
st.title("❷解析の設定")

if sel1 == "線形解析":
    code_part, code_prop, code_mat = test_func()


if sel1 == "熱解析":
    pass


if sel1 == "流体解析":
    pass

if sel1 == "衝撃解析":
    pass

if sel1 == "エアバッグ解析":
    pass


st.markdown('---')

st.title("❸設定ファイルの出力")

# 文字列をファイルに書き出す
def write_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)
    file.close()

title = st.text_input("解析タイトル", "templete")

intro = \
    f"""
#RADIOSS STARTER
#--------------------------------------------------------------------------------------------------|
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/BEGIN
{title}
      2020         0
                  Mg                  mm                   s
                  Mg                  mm                   s
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
#-  1. CONTROL CARDS:
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/TITLE
{title}
"""
end = \
    f"""
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/END
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
"""
try:
    code = intro + code_part + code_prop + code_mat + end
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
