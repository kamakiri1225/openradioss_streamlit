import pandas as pd
import streamlit as st
import parttemp, mattemp, proptemp, BCS

def test_func():
    tab1, tab2, tab3 = st.tabs(["part1", "part2", "part3"])
    with tab1:
        st.subheader("プロパティ")
        propid = st.number_input("PROP ID number", step=1, min_value = 1)
        prop_title = st.text_input("PROP Title", "templete")
        prop1 = ["SH_ORTH", "prop2", "prop3"]
        prop_sel1 = st.selectbox('プロパティ', prop1, index=0)

        if prop_sel1 == "SH_ORTH":
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
            df_prop = st.data_editor(df_prop)
            
            code_prop = proptemp.prpo_SH_ORTH(prop_title, propid, df_prop)
        
        st.subheader("材料定義")
        # st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
        matid = st.number_input("MAT ID number", step=1, min_value = 1)
        mat_title = st.text_input("MAT Title", "templete")
        mat1 = ["LAW1", "/MAT/ELAST", "/MAT/PLAS_TAB"]
        mat_sel1 = st.selectbox('材料', mat1, index=0)
        
        if mat_sel1 == "LAW1": 
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
            df_mat = st.data_editor(df_mat)
            code_mat = mattemp.Mat_test(mat_title, matid, df_mat)
        if mat_sel1 == "/MAT/ELAST": 
            st.markdown(
                """
                このキーワードは、フックの法則を使用して等方性の線形弾性材料を定義します。この材料則は応力とひずみの間の線形関係を表します。トラス、ビーム（タイプ3のみ）、シェルとソリッド要素に使用可能です。
                """
            )
            pd.options.display.precision = 10
            df_mat = pd.DataFrame(
                {
                    "setting": ["rho", "E", "Nu"],
                    "value": [8.5e-7, 210000, 0.3],
                    "explanation": [
                        "説明あり",
                        "説明あり",
                        "説明あり",
                        ]
                }
            ) 
            df_mat = st.data_editor(df_mat)

            HEAT_Flag = st.checkbox("Heat")

            code_mat = mattemp.Mat_ELAST(mat_title, matid, df_mat, HEAT_Flag)
            

        if mat_sel1 == "/MAT/PLAS_TAB": 
            pd.options.display.precision = 10
            df_mat = pd.DataFrame(
                {
                    "setting": ["rho", "E", "Nu"],
                    "value": [8.5e-7, 210000, 0.3],
                    "explanation": [
                        "説明あり",
                        "説明あり",
                        "説明あり",
                        ]
                }
            )            
            df_mat = st.data_editor(df_mat)
            code_mat = mattemp.Mat_PLAS_TAB(mat_title, matid, df_mat)


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


def test_func1():
    tab1, tab2, tab3 = st.tabs(["BCS1", "part2", "part3"])
    with tab1:
        st.subheader("固定境界")
        bcsid = st.number_input("BCS ID number", step=1, min_value = 1)
        bcstitle = st.text_input("BCS Title", "templete")
        bcs1 = ["BCS", "BCS2", "BCS3"]
        bcs_sel1 = st.selectbox('BCS', bcs1, index=0)

        if bcs_sel1 == "BCS":
            pd.options.display.precision = 10
            df_bcs= pd.DataFrame(
                {
                    "setting": ["Tra", "rot", "grnod_ID"],
                    "value": [111, 111, 1],
                    "explanation": [
                        "説明あり",
                        "説明あり",
                        "説明あり",
                        ]
                }
            )

            df_bcs = st.data_editor(df_bcs)
            
            code_bcs = BCS.bcs(bcstitle, bcsid, df_bcs)
 
    with tab2:
        pass
    with tab3:
        pass

    return code_bcs
