import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

st.header("Line chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']

)
st.write("chart data:",chart_data)
st.line_chart(chart_data)

c = alt.Chart(data=chart_data).mark_circle().encode(x='a', y='b', size='c', \
                                                    color='c', tooltip=['a', 'b', 'c'],).properties(title="This is title")
st.altair_chart(c, use_container_width=True)