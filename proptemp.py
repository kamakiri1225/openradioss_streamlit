import streamlit as st
import pandas as pd

def prpo_test(propid, df_prop):
    propid = str(propid)
    Ishell = str(int(df_prop.iloc[0,1]))
    Thick = str(df_prop.iloc[1,1])
    code = \
        f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/PROP/SH_ORTH/{propid}
FABRIC
#   Ishell    Ismstr     Ish3n    Idrill                            P_thick_fail
{Ishell.rjust(10)}        11         2         0                                       0
#         ismstr=1 + refgeo = ismstr=11
#                 hm                  hf                  hr                  dm                  dn
                 .05                 .05                   0                   0                   0
#        N   Istrain               Thick              Ashear              Ithick     Iplas
         1         1{Thick.rjust(20)}                   0                   0         0
#                 Vx                  Vy                  Vz                 Phi
                   1                   0                   0                   0
"""

    with st.expander("プロパティ"):
        st.code(code)

    return code