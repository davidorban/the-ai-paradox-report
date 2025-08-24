import json
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Load the data from the JSON file
with open('/home/ubuntu/upload/pasted_content.txt', 'r') as f:
    data = json.load(f)

# Extract the Paradox Quadrant data
quadrant_data = data['visualizations'][1]
data_points = quadrant_data['data_points']

# Add missing point in upper left quadrant (Altruistic Skeptics)
data_points.append({"id": 13, "x": -4, "y": 3, "size": 1, "label": "Social Advocate"})

quadrants = quadrant_data['quadrants']

# Create the figure
fig = go.Figure()

# Define quadrant colors
quadrant_colors = {
    'Win-Win Optimists': quadrants['top_right']['color'],
    'Altruistic Skeptics': quadrants['top_left']['color'],
    'Pragmatic Paradox': quadrants['bottom_right']['color'],
    'Deep Skeptics': quadrants['bottom_left']['color']
}

# Function to determine quadrant for each point
def get_quadrant(x, y):
    if x >= 0 and y >= 0:
        return 'Win-Win Optimists'
    elif x < 0 and y >= 0:
        return 'Altruistic Skeptics'
    elif x >= 0 and y < 0:
        return 'Pragmatic Paradox'
    else:
        return 'Deep Skeptics'

# Prepare data for scatter plot
x_values = [point['x'] for point in data_points]
y_values = [point['y'] for point in data_points]
sizes = [point['size'] * 10 for point in data_points]  # Scale up for visibility
colors = [quadrant_colors[get_quadrant(point['x'], point['y'])] for point in data_points]

# Add scatter plot without labels
fig.add_trace(go.Scatter(
    x=x_values,
    y=y_values,
    mode='markers',
    marker=dict(
        size=sizes,
        color=colors,
        opacity=0.7,
        line=dict(width=2, color='white')
    ),
    showlegend=False
))

# Add quadrant background rectangles
fig.add_shape(
    type="rect",
    x0=-10, y0=0, x1=0, y1=10,
    fillcolor=quadrants['top_left']['color'],
    opacity=0.1,
    layer="below",
    line_width=0,
)

fig.add_shape(
    type="rect",
    x0=0, y0=0, x1=10, y1=10,
    fillcolor=quadrants['top_right']['color'],
    opacity=0.1,
    layer="below",
    line_width=0,
)

fig.add_shape(
    type="rect",
    x0=-10, y0=-10, x1=0, y1=0,
    fillcolor=quadrants['bottom_left']['color'],
    opacity=0.1,
    layer="below",
    line_width=0,
)

fig.add_shape(
    type="rect",
    x0=0, y0=-10, x1=10, y1=0,
    fillcolor=quadrants['bottom_right']['color'],
    opacity=0.1,
    layer="below",
    line_width=0,
)

# Add quadrant lines
fig.add_hline(y=0, line_width=2, line_color="black")
fig.add_vline(x=0, line_width=2, line_color="black")

# Update layout - minimal version with transparent background
fig.update_layout(
    xaxis=dict(
        range=[quadrant_data['x_axis']['min'], quadrant_data['x_axis']['max']],
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        zeroline=False
    ),
    yaxis=dict(
        range=[quadrant_data['y_axis']['min'], quadrant_data['y_axis']['max']],
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        zeroline=False
    ),
    width=1000,
    height=800,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    hovermode='closest',
    margin=dict(l=50, r=50, t=50, b=50)
)

# Save as static PNG
fig.write_image('/home/ubuntu/ai_sentiment_charts/paradox_quadrant_naked.png', width=1000, height=800, scale=2)

print("Naked Paradox Quadrant chart created successfully!")
print("File saved: paradox_quadrant_naked.png")

