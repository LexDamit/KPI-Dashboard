

''''import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import os
import plotly.graph_objects as go
import graphviz
import json
from streamlit_echarts import st_echarts
import streamlit as st
from streamlit_echarts import st_echarts
import json

# Load your JSON data
def load_data():
    with open('data.json', 'r') as f:  # Replace 'data.json' with your actual JSON file path
        return json.load(f)

data = load_data()

# Main app logic
def main():
    st.set_page_config(layout="wide")
    
    # Load data
    data = load_data()
    
    
    option = {
        "series": [
            {
                "type": "tree",
                "layout": "orthogonal",
                "orient": "horizontal",
                "data": [data],
                "initialTreeDepth": 4,
                "top": "1%",
                "left": "7%",
                "bottom": "1%",
                "right": "20%",
                "symbol": "rect",
                "symbolSize": [100, 30],
                "label": {
                    "position": "inside",
                    "color": "black",
                    "fontSize": 12,
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

    # Render the ECharts tree in Streamlit
    st_echarts(options=option, height="1000px")

if __name__ == "__main__":
    main()

from graphviz import Digraph

data = {
    "name": "Performance",
    "value": "Performance",
    "description": "Placeholder description for Performance.",
    "children": [
      {
        "name": "Biomechanics",
        "value": "Biomechanics",
        "description": "Placeholder description for Biomechanics.",
        "children": [
          {
            "name": "Kinematics",
            "value": "Kinematics",
            "description": "Placeholder description for Kinematics.",
            "children": [
              {
                "name": "Velocity",
                "value": "Velocity",
                "description": "Placeholder description for Velocity.",
                "children": [
                  {
                    "name": "Spatiotemporal",
                    "value": "Spatiotemporal",
                    "description": "Placeholder description for Spatiotemporal.",
                    "children": []
                  },
                  {
                    "name": "Acceleration",
                    "value": "Acceleration",
                    "description": "Placeholder description for Acceleration.",
                    "children": []
                  }
                ]
              }
            ]
          },
          {
            "name": "Kinetics",
            "value": "Kinetics",
            "description": "Placeholder description for Kinetics.",
            "children": []
          }
        ]
      }
    ]
}

import streamlit as st
import graphviz

# Function to create and return the graph
def create_graph(change_color=False):
    # Create a graphlib graph object
    graph = graphviz.Digraph()
    graph.attr('node', shape='box', style='filled', fillcolor='lightgray', color='black', fontcolor='black')  # Set all nodes to have rectangle shape


    # Define edges
    edges = [
        ('Performance (=Time [s])', 'Biomechanics'),
        ('Performance (=Time [s])', 'Anthropometrics'),
        ('Performance (=Time [s])', 'Tactical'),

        ('Biomechanics', 'Kinematics'),
        ('Biomechanics', 'Kinetics'),
        ('run', 'kernel'),
        ('kernel', 'zombie'),
        ('kernel', 'sleep'),
        ('kernel', 'runmem'),
        ('sleep', 'swap'),
        ('swap', 'runswap'),
        ('runswap', 'new'),
        ('runswap', 'runmem'),
        ('new', 'runmem'),
        ('sleep', 'runmem')
    ]

    # Add edges to the graph
    for edge in edges:
        graph.edge(*edge)

    # If change_color is True, change the fill color of the first 3 layers to red
    if change_color:
        # Nodes to change fill color
        nodes_to_color = ['run', 'intr', 'runbl', 'kernel']
        # Update node attributes to change fill color
        for node in nodes_to_color:
            graph.node(node, style='filled', fillcolor='red')

    return graph

# Initialize session state variable if not already done
if 'color_changed' not in st.session_state:
    st.session_state.color_changed = False

# Button to toggle the color change
if st.button('Toggle Fill Color of First 3 Layers'):
    # Toggle the color_changed state
    st.session_state.color_changed = not st.session_state.color_changed

# Generate and display the graph based on the current state
graph = create_graph(change_color=st.session_state.color_changed)
st.graphviz_chart(graph)'''






#Code to run Streamlit Application to Display the performance indicators of Athletics Running Events

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Set the page layout
st.set_page_config(layout="wide")
#Set columns
col1, col2,col3 = st.columns(3, gap = 'small')

with col1:
    st.caption(" ")

with col2:
    st.image('logo.png', width=250,)

    with col3:
        st.caption(" ")


#Title and Page Layout
st.markdown("<h1 style='text-align: center;'>Athletics Running Events: Key Performance Indicators </h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left;'>  </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left;'>Introduction </h5>", unsafe_allow_html=True)
st.markdown("This dashboard introduces a systematic analysis of key performance indicators (KPIs) pertinent to track and field events. With the help of this dashboard, the biomechanical factors of running performance can be better understood. The aim of this dashboard is to facilitate Key Performance indicator choice in the context of post race performance analysis")

st.header("1.Categorisation of Athletics Running Events")
st.markdown("Athletics holds a distinguished position as one of the most contested sports in the Olympic Games, offering a diverse array of competitive events that test the limits of human speed, strength, and endurance. The sport is traditionally divided into three main categories: track, field, and multi-events, collectively encompassing a total of 44 distinct events. \n \nThis section specifically addresses the track category, providing a detailed exploration of its composition and the systematic classification of running events.")
st.image('/Users/lexdamit/Documents/MTAthleticsStories/Treemap/Athletics.png')
st.markdown("**Figure 1:** Categorization of Running Events in Athletics. This diagram classifies events into Sprints, Distance, and Relays, with further subdivisions based on track configuration, distance, and team gender composition. ")


#General
st.header("2. Treemaps")
# Dropdown to select the grading column
hover_text = ""
interaction_mode = st.checkbox('Choose the interaction of 2 grading criteria')

df_general = pd.read_excel('//Users/lexdamit/Documents/MTAthleticsStories/Treemap/KPIs.xlsx', 'General')

if interaction_mode:
    # If interaction mode is selected, show two dropdowns to pick the criteria to multiply
    criteria1 = st.selectbox('Select the first criteria for grading:', 
                             ('LiteratureSupport', 'PerformanceImpact', 'Measurability', 'Storytelling'), key='first')
    criteria2 = st.selectbox('Select the second criteria for grading:', 
                             ('LiteratureSupport', 'PerformanceImpact', 'Measurability', 'Storytelling'), key='second')
    
    # Ensure that the two selected criteria are different
    if criteria1 == criteria2:
        st.error("Please select two different criteria for interaction.")
        st.stop()
    else:
        # Create a new column that is the product of the two selected criteria
        df_general['interaction'] = df_general[criteria1] * df_general[criteria2]
        grading_option = 'interaction'
        hover_text = df_general['labels'] + '<br>' + df_general['Description'] + '<br> Interaction Score: ' + df_general['interaction'].astype(str)
else:
    # Single selection mode, show one dropdown
    grading_option = st.selectbox(
        'Select the data for grading:',
        ('LiteratureSupport', 'PerformanceImpact', 'Measurability', 'Storytelling')
    )
    hover_text = df_general['labels'] + '<br>' + df_general['Description'] + '<br>' + grading_option + ' Score: ' + df_general[grading_option].astype(str)


# General Treemap
fig_general = go.Figure(go.Treemap(
    ids=df_general.id,
    labels=df_general['labels'],
    parents=df_general.parents,
    values=df_general[grading_option],
    maxdepth=3,
    hoverinfo='text',
    text=hover_text,
    root_color="lightgrey",
    textinfo="label",
    branchvalues="remainder",
    pathbar=dict(visible=True),
))
fig_general.update_layout(height=500, uniformtext=dict(minsize=10), margin=dict(t=40, l=5, r=5, b=5))

st.subheader("General")
st.plotly_chart(fig_general, use_container_width=True)



# SPRINT START
df_sprint_start = pd.read_excel('//Users/lexdamit/Documents/MTAthleticsStories/Treemap/KPIs.xlsx','Sprint Start')
ss_hover_text = df_sprint_start['labels'] + '<br>' + df_sprint_start['Description'] + '<br>' + grading_option +' Score: '+ df_sprint_start[grading_option].astype(str)


fig_sprint_start = go.Figure(go.Treemap(
    ids=df_sprint_start.id,
    labels=df_sprint_start['labels'],
    parents=df_sprint_start.parents,
    values=df_sprint_start[grading_option],
    maxdepth=4,
    hoverinfo='text',
    text=ss_hover_text,
    root_color="lightgrey",
    textinfo = "label",
    branchvalues = "remainder",
    pathbar=dict(visible=True),      
))
fig_sprint_start.update_layout(height=500, margin=dict(t=40, l=5, r=5, b=5))


#OBSTACLES
df_obstacles = pd.read_excel('/Users/lexdamit/Documents/MTAthleticsStories/Treemap/KPIs.xlsx','Obstacles')
obs_hover_text = df_obstacles['labels'] +  '<br>' + df_obstacles.Description + '<br>' + 'Literature Score: '+ df_obstacles['litsupp'].astype(str)

fig_obstacles = go.Figure(go.Treemap(
    ids=df_obstacles.id,
    labels=df_obstacles['labels'],
    parents=df_obstacles.parents,
    #values=df_obstacles.litsupp,
    maxdepth=4,
    hoverinfo='text',
    text=obs_hover_text,
    root_color="lightgrey",
    textinfo = "label",
    branchvalues = "remainder",
    pathbar=dict(visible=True),
))
fig_obstacles.update_layout(height=500, margin=dict(t=40, l=5, r=5, b=5))


# Display the treemaps side by side
col1, col2 = st.columns(2)
with col1:
    st.subheader("Sprint Start")
    st.plotly_chart(fig_sprint_start, use_container_width=True)

with col2:
    st.subheader("Obstacles")
    st.plotly_chart(fig_obstacles, use_container_width=True)



#Create The Clickable FlowChart
import streamlit as st
import json
from streamlit_echarts import st_echarts
st.header("2. Deterministic Model")

# Load your JSON data
def load_data():
    with open('/Users/lexdamit/Documents/MTAthleticsStories/updated_data.json', 'r') as f:
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

    # Render the ECharts tree in Streamlit
    st_echarts(options=option, height="1000px")

if __name__ == "__main__":
    main()

st.header("3. Table")

alldata = pd.read_excel('/Users/lexdamit/Documents/MTAthleticsStories/Treemap/KPIs.xlsx','TableAll')


# Select specific columns
columns_to_select = ['Label', 'Description', 'LiteratureSupport', 'Performance', 'Measurability', 'Applicability']
filtered_data = alldata[columns_to_select]

# Display the selected data in Streamlit
st.dataframe(filtered_data)



