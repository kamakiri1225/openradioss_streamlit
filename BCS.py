import streamlit as st
import pandas as pd

def bcs(bcstitle, bcsid, df_bsc):
    bcstitle = str(bcstitle)
    bcsid = str(bcsid)
    Tra = str(df_bsc.iloc[0,1])
    rot = str(df_bsc.iloc[1,1])
    grnod_ID = str(df_bsc.iloc[2,1])
    code = \
        f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/BCS/{bcsid}
{bcstitle}
#  Tra rot   skew_ID  grnod_ID
{Tra.rjust(6)}{rot.rjust(4)}         0{grnod_ID.rjust(10)}
"""

    with st.expander("固定境界"):
        st.code(code)
    
    return code