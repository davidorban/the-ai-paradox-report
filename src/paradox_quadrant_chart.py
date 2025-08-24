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
quadrants = quadrant_data['quadrants']
statistics = quadrant_data['statistics']

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
labels = [point['label'] for point in data_points]
colors = [quadrant_colors[get_quadrant(point['x'], point['y'])] for point in data_points]

# Add scatter plot
fig.add_trace(go.Scatter(
    x=x_values,
    y=y_values,
    mode='markers+text',
    marker=dict(
        size=sizes,
        color=colors,
        opacity=0.7,
        line=dict(width=2, color='white')
    ),
    text=labels,
    textposition='top center',
    textfont=dict(size=10),
    hovertemplate='<b>%{text}</b><br>Personal Benefit: %{x}<br>Societal Benefit: %{y}<extra></extra>',
    name='Survey Respondents',
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

# Add quadrant labels
fig.add_annotation(
    x=-5, y=5,
    text=f"<b>{quadrants['top_left']['label']}</b><br>{quadrants['top_left']['description']}",
    showarrow=False,
    font=dict(size=12, color=quadrants['top_left']['color']),
    bgcolor="rgba(255,255,255,0.8)",
    bordercolor=quadrants['top_left']['color'],
    borderwidth=1
)

fig.add_annotation(
    x=5, y=5,
    text=f"<b>{quadrants['top_right']['label']}</b><br>{quadrants['top_right']['description']}",
    showarrow=False,
    font=dict(size=12, color=quadrants['top_right']['color']),
    bgcolor="rgba(255,255,255,0.8)",
    bordercolor=quadrants['top_right']['color'],
    borderwidth=1
)

fig.add_annotation(
    x=-5, y=-5,
    text=f"<b>{quadrants['bottom_left']['label']}</b><br>{quadrants['bottom_left']['description']}",
    showarrow=False,
    font=dict(size=12, color=quadrants['bottom_left']['color']),
    bgcolor="rgba(255,255,255,0.8)",
    bordercolor=quadrants['bottom_left']['color'],
    borderwidth=1
)

fig.add_annotation(
    x=5, y=-5,
    text=f"<b>{quadrants['bottom_right']['label']}</b><br>{quadrants['bottom_right']['description']}",
    showarrow=False,
    font=dict(size=12, color=quadrants['bottom_right']['color']),
    bgcolor="rgba(255,255,255,0.8)",
    bordercolor=quadrants['bottom_right']['color'],
    borderwidth=1
)

# Add center of mass point
center_x = statistics['center_of_mass']['x']
center_y = statistics['center_of_mass']['y']
fig.add_trace(go.Scatter(
    x=[center_x],
    y=[center_y],
    mode='markers',
    marker=dict(
        size=15,
        color='red',
        symbol='x',
        line=dict(width=3, color='darkred')
    ),
    name='Center of Mass',
    hovertemplate=f'<b>Center of Mass</b><br>Personal: {center_x}<br>Societal: {center_y}<extra></extra>'
))

# Update layout
fig.update_layout(
    title=dict(
        text=quadrant_data['title'],
        x=0.5,
        font=dict(size=20, family="Arial, sans-serif")
    ),
    xaxis=dict(
        title=quadrant_data['x_axis']['label'],
        range=[quadrant_data['x_axis']['min'], quadrant_data['x_axis']['max']],
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        zeroline=False
    ),
    yaxis=dict(
        title=quadrant_data['y_axis']['label'],
        range=[quadrant_data['y_axis']['min'], quadrant_data['y_axis']['max']],
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        zeroline=False
    ),
    width=1000,
    height=800,
    plot_bgcolor='white',
    paper_bgcolor='white',
    hovermode='closest'
)

# Add statistics box
stats_text = "Quadrant Distribution:<br>"
for quadrant, percentage in statistics['quadrant_distribution'].items():
    stats_text += f"• {quadrant}: {percentage}<br>"

fig.add_annotation(
    text=stats_text,
    xref="paper", yref="paper",
    x=0.02, y=0.98,
    xanchor="left", yanchor="top",
    showarrow=False,
    font=dict(size=11, color="black"),
    bgcolor="rgba(255,255,255,0.9)",
    bordercolor="gray",
    borderwidth=1
)

# Add key insight
fig.add_annotation(
    text=f"<b>Key Insight:</b><br>{quadrant_data['key_insight']}",
    xref="paper", yref="paper",
    x=0.98, y=0.15,
    xanchor="right", yanchor="bottom",
    showarrow=False,
    font=dict(size=11, color="darkblue"),
    bgcolor="rgba(255,255,255,0.9)",
    bordercolor="darkblue",
    borderwidth=1
)

# Add attribution
fig.add_annotation(
    text="davidorban.com",
    xref="paper", yref="paper",
    x=0.98, y=-0.08,
    xanchor="right", yanchor="bottom",
    showarrow=False,
    font=dict(size=10, color="gray")
)

# Save as interactive HTML
fig.write_html('/home/ubuntu/ai_sentiment_charts/paradox_quadrant_interactive.html')

# Save as static PNG
fig.write_image('/home/ubuntu/ai_sentiment_charts/paradox_quadrant_static.png', width=1000, height=800, scale=2)

print("Paradox Quadrant chart created successfully!")
print("Files saved:")
print("- Interactive: paradox_quadrant_interactive.html")
print("- Static: paradox_quadrant_static.png")

# Display key insight
print(f"\nKey Insight: {quadrant_data['key_insight']}")

# Display quadrant distribution
print("\nQuadrant Distribution:")
for quadrant, percentage in statistics['quadrant_distribution'].items():
    print(f"- {quadrant}: {percentage}")

