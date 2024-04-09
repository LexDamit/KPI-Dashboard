import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide")
col1, col2,col3 = st.columns(3, gap = 'small')

with col1:
    st.caption(" ")

with col2:
    st.caption("")

    with col3:
        st.caption(" ")


st.markdown("<h1 style='text-align: center;'>Athletics Running Events: Key Performance Indicators </h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left;'>  </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left;'>Introduction </h5>", unsafe_allow_html=True)
st.markdown("This dashboard introduces a systematic analysis of key performance indicators (KPIs) pertinent to track and field events. With the help of this dashboard, the biomechanical factors of running performance can be better understood. The aim of this dashboard is to facilitate Key Performance indicator choice in the context of post race performance analysis")

st.header("1.Categorisation of Athletics Running Events")
st.markdown("Athletics holds a distinguished position as one of the most contested sports in the Olympic Games, offering a diverse array of competitive events that test the limits of human speed, strength, and endurance. The sport is traditionally divided into three main categories: track, field, and multi-events, collectively encompassing a total of 44 distinct events. \n \nThis section specifically addresses the track category, providing a detailed exploration of its composition and the systematic classification of running events.")
st.image('./Athletics.png')
st.markdown("**Figure 1:** Categorization of Running Events in Athletics. This diagram classifies events into Sprints, Distance, and Relays, with further subdivisions based on track configuration, distance, and team gender composition. ")
#st.image('Athletics-3.png')

st.header("2. Treemaps")

interaction_mode = st.checkbox('Choose the interaction of 2 grading criteria')

criteria_options = ['LiteratureSupport', 'PerformanceImpact', 'Measurability', 'Storytelling']

if interaction_mode:
    col1, col2, col3 = st.columns([5, 1, 5])

    with col1:
        st.write("")
        criteria1 = st.selectbox(
            'Select the first criteria for grading:',
            criteria_options, 
            key='first'
        )
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.markdown('<h6 style="text-align: center">X</h6>', unsafe_allow_html=True)
    with col3:
        st.write("")
        filtered_options = [option for option in criteria_options if option != criteria1]
        criteria2 = st.selectbox(
            'Select the second criteria for grading:',
            filtered_options, 
            key='second'
        )

else:
    criteria1 = st.selectbox(
        'Select the data for grading:',
        criteria_options,
        key='single'
    )
    criteria2 = None

def load_and_apply_criteria(sheet_name, criteria1, criteria2):
    df = pd.read_excel('./KPIs.xlsx', sheet_name)
    if interaction_mode:
        df['Interaction'] = df[criteria1] * df[criteria2]
        return df, 'Interaction'
    else:
        return df, criteria1

df_general, grading_option_general = load_and_apply_criteria('General', criteria1, criteria2)
df_sprint_start, grading_option_sprint_start = load_and_apply_criteria('Sprint Start', criteria1, criteria2)
df_obstacles, grading_option_obstacles = load_and_apply_criteria('Obstacles', criteria1, criteria2)

def create_treemap(df, grading_option):
    hover_text = df['labels'] + '<br>' + df['Description'] + '<br>' + f'{grading_option} Score: ' + df[grading_option].astype(str)
    fig = go.Figure(go.Treemap(
        ids=df.id,
        labels=df['labels'],
        parents=df.parents,
        values=df[grading_option],
        maxdepth=4,
        hoverinfo='text',
        text=hover_text,
        root_color="lightgrey",
        textinfo="label",
        branchvalues="remainder",
        pathbar=dict(visible=True),
    ))
    fig.update_layout(height=500, margin=dict(t=40, l=5, r=5, b=5))
    return fig

fig_general = create_treemap(df_general, grading_option_general)
fig_sprint_start = create_treemap(df_sprint_start, grading_option_sprint_start)
fig_obstacles = create_treemap(df_obstacles, grading_option_obstacles)

st.subheader("General")
st.plotly_chart(fig_general, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Sprint Start")
    st.plotly_chart(fig_sprint_start, use_container_width=True)

with col2:
    st.subheader("Obstacles")
    st.plotly_chart(fig_obstacles, use_container_width=True)



import streamlit as st
import json
from streamlit_echarts import st_echarts
st.header("2. Deterministic Model")

def load_data():
    with open('./updated_data.json', 'r') as f:
        return json.load(f)

# Main app logic
def main():
    
    # Load data
    data = load_data()
    
    option = {
        "series": [
            {
                "type": "tree",
                "layout": "orthogonal",
                "orient": "horizontal",
                "data": [data],
                "initialTreeDepth": 2,
                "top": "1%",
                "left": "7%",
                "bottom": "1%",
                "right": "20%",
                "symbol": "rect",
                "symbolSize": [100, 30],
                "label": {
                    "position": "inside",
                    "color": "black",
                    "fontSize": 9,
                    "align": "center",
                    "verticalAlign": "middle",
                    "formatter": "{b}",
                },
                "itemStyle": {
                    "borderWidth": 0,
                    "opacity": 1,
                },
                "lineStyle": {
                    "width": 2,
                },
                "emphasis": {"focus": "ancestor"},
                "expandAndCollapse": True,
                "animationDuration": 550,
                "animationDurationUpdate": 750,
            }
        ]
    }

    st_echarts(options=option, height="1000px")

if __name__ == "__main__":
    main()

st.header("3. Table")

df_general['Category'] = 'General'
df_sprint_start['Category'] = 'Sprint Start'
df_obstacles['Category'] = 'Obstacles'

df_combined = pd.concat([df_general, df_sprint_start, df_obstacles], ignore_index=True)
df_display_filtered = df_combined[df_combined['Description'].str.lower() != "node"]

columns_to_display = ['Category', 'labels', 'LiteratureSupport', 'PerformanceImpact', 'Measurability', 'Storytelling']
df_display = df_display_filtered[columns_to_display]



st.dataframe(df_display)


