import streamlit as st
import pandas as pd

def Mat_test(matid, df_mat):
    matid = str(matid)
    rho = str(df_mat.iloc[0,1])
    E11 = str(df_mat.iloc[1,1])
    E22 = str(df_mat.iloc[2,1])
    NU12 = str(df_mat.iloc[3,1])
    code = \
        f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/MAT/FABRI/{matid}
FABRIC
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