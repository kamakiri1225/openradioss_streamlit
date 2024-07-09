import streamlit as st
import pandas as pd

def prpo_SHELL(prop_title, propid, df_prop):
    propid = str(propid)
    Ishell = str(int(df_prop.iloc[0,1]))
    Thick = str(df_prop.iloc[1,1])
    code = \
        f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/PROP/SHELL/{propid}
{prop_title}                                                                                         
#   Ishell    Ismstr     Ish3n    Idrill                            P_Thick_Fail
{Ishell.rjust(10)}                                                                      
#                 Hm                  Hf                  Hr                  Dm                  Dn
                                                                                                    
#        N   Istrain               Thick              Ashear              Ithick     Iplas
                    {Thick.rjust(20)}                                       1         1
"""

    with st.expander("プロパティ"):
        st.code(code)

    return code


def prpo_SH_ORTH(prop_title, propid, df_prop):
    propid = str(propid)
    Ishell = str(int(df_prop.iloc[0,1]))
    Thick = str(df_prop.iloc[1,1])
    code = \
        f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/PROP/SH_ORTH/{propid}
{prop_title}
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

def prpo_SH_COMP(prop_title, propid, df_prop):
    propid = str(propid)
    Ishell = str(int(df_prop.iloc[0,1]))
    Thick = str(df_prop.iloc[1,1])
    code = \
        f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/PROP/SH_COMP/{propid}
{prop_title}                                                                                         
#   Ishell    Ismstr     Ish3n    Idrill                            P_thick_fail
{Ishell.rjust(10)}                                                                                
#                 Hm                  Hf                  Hr                  Dm                  Dn
                                                                                                    
#        N   Istrain               Thick              Ashear              Ithick     Iplas
         1         0{Thick.rjust(20)}                                                                          
#                 Vx                  Vy                  Vz
                                                            
#              Phi_1               Phi_2               Phi_3               Phi_4               Phi_5
                 0.0
"""

    with st.expander("プロパティ"):
        st.code(code)

    return code


def prpo_BEAM(prop_title, propid, df_prop):
    propid = str(propid)
    Ismstr = str(int(df_prop.iloc[0,1]))
    Area = str(df_prop.iloc[1,1])
    code = \
        f"""\
#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|---10----|
/PROP/BEAM/{propid}
{prop_title}                                                                                          
#             Ismstr
{Ismstr.rjust(20)}      
#                 Dm                  Df
                                        
#               Area                 Iyy                 Izz                 Ixx
{Area.rjust(20)}                                                                    
#     Wdof    Ishear
   000 000   
"""

    with st.expander("プロパティ"):
        st.code(code)

    return code