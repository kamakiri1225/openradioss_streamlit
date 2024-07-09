import streamlit as st
import pandas as pd

def Mat_test(mat_title, matid, df_mat):
    matid = str(matid)
    rho = str(df_mat.iloc[0,1])
    E11 = str(df_mat.iloc[1,1])
    E22 = str(df_mat.iloc[2,1])
    NU12 = str(df_mat.iloc[3,1])
    code = \
        f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/MAT/FABRI/{matid}
{mat_title}
#              RHO_I               RHO_O
{rho.rjust(20)}                   0
#                E11                 E22                NU12
{E11.rjust(20)}{E22.rjust(20)}{NU12.rjust(20)}                   0
#                G12                 G23                 G31
                  10                  10                  10
#                R_E                              ZEROSTRESS          FSCALE_POR   SENS_ID
                .001     
"""

    with st.expander("材料定義"):
        st.code(code)
    
    return code

def Mat_ELAST(mat_title, matid, df_mat, HEAT_Flag):
    matid = matid
    rho = str(df_mat.iloc[0,1])
    E = str(df_mat.iloc[1,1])
    Nu = str(df_mat.iloc[2,1])
    code = \
        f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/MAT/ELAST/{matid}
{mat_title}                                                                                         
#              RHO_I
{rho.rjust(20)}
#                  E                  nu
{E.rjust(20)}{Nu.rjust(20)}
"""
    if HEAT_Flag:
        code += \
        f"""\
/HEAT/MAT/{matid}
#                 T0             RHO0_CP                  AS                  BS     IfORM
                                                                                        
#                 T1                  AL                  BL               EFRAC  
"""

    with st.expander("/MAT/ELAST"):
        st.code(code)
    
    return code

def Mat_PLAS_TAB(mat_title, matid, df_mat):
    matid = str(matid)
    rho = str(df_mat.iloc[0,1])
    E = str(df_mat.iloc[1,1])
    Nu = str(df_mat.iloc[2,1])
    code = \
        f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/MAT/PLAS_TAB/{matid}
{mat_title}
#              RHO_I
{rho.rjust(20)}                   0
#                  E                  Nu           Eps_p_max               Eps_t               Eps_m
{E.rjust(20)}{Nu.rjust(20)}                   0                   0                   0
#  N_funct  F_smooth              C_hard               F_cut               Eps_f                  VP
         1         0                   0                   0                   0                   0
#  fct_IDp              Fscale   Fct_IDE                EInf                  CE
         0                   0         0                   0                   0
# func_ID1  func_ID2  func_ID3  func_ID4  func_ID5
        14
#           Fscale_1            Fscale_2            Fscale_3            Fscale_4            Fscale_5
                   1
#          Eps_dot_1           Eps_dot_2           Eps_dot_3           Eps_dot_4           Eps_dot_5
                   0 
"""

    with st.expander("/MAT/PLAS_TAB"):
        st.code(code)
    
    return code