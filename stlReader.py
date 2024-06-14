import streamlit as st
import pyvista as pv
from stpyvista import stpyvista

def stlReader():
    main_container = st.empty()

    main_container.empty()
    selection = "stl"
    st.query_params["gallery"] = selection

    ## Streamlit layout
    st.header("📤   Upload a STL file", divider="rainbow")

    placeholder = st.empty()

    with placeholder:
        uploadedFile = st.file_uploader(
            "Upload a STL file:",
            type=["stl"],
            accept_multiple_files=False,
            key="fileuploader",
        )
    # with tempfile.NamedTemporaryFile(suffix="_streamlit") as f:

    if uploadedFile:
        stlTemp = "./temp.stl"
        with open(stlTemp, "wb") as f: 
            f.write(uploadedFile.getbuffer())
            reader = pv.STLReader(stlTemp)
            mesh = reader.read()
            plotter = pv.Plotter(border=False, window_size=[500, 400])
            plotter.background_color = "#f0f8ff"
            plotter.add_mesh(mesh, color="orange", specular=0.5)

        st.write("uploadedFile is Trune")
        plotter.view_isometric()

        stpyvista(
            plotter,
            panel_kwargs=dict(
                orientation_widget=True,
                interactive_orientation_widget=True,
            ),
            key="thermal sensitive"
    )