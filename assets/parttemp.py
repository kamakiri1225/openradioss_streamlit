import streamlit as st
import pandas as pd

def Part_test(parttitle, pid, propid, matid):
    parttitle = str(parttitle)
    pid = str(pid)
    propid = str(propid)
    matid = str(matid)
    code = \
f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/PART/{pid}
{parttitle}
  #prop_ID   #mat_ID#subset_ID              #Thick
{propid.rjust(10)}{matid.rjust(10)}
"""

    with st.expander("パートの定義"):
        st.code(code)
    
    return code