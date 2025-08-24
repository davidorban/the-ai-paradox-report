import json
import plotly.graph_objects as go
import numpy as np

# Load the data from the JSON file
with open('/home/ubuntu/upload/pasted_content.txt', 'r') as f:
    data = json.load(f)

# Extract the Tension Web data
radar_data = data['visualizations'][2]
dimensions = radar_data['dimensions']
data_series = radar_data['data_series']
scale = radar_data['scale']

# Create the figure
fig = go.Figure()

# Extract dimension names
dimension_names = [dim['axis'] for dim in dimensions]

# Add each data series to the radar chart
for series in data_series:
    fig.add_trace(go.Scatterpolar(
        r=series['values'] + [series['values'][0]],  # Close the polygon
        theta=dimension_names + [dimension_names[0]],  # Close the polygon
        fill='toself',
        fillcolor=series['color'].replace('opacity', str(series['opacity'])),
        line=dict(color=series['color'], width=2),
        opacity=series['opacity'],
        showlegend=False
    ))

# Update layout for radar chart with transparent background
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[scale['min'], scale['max']],
            tickvals=list(range(scale['min'], scale['max'] + 1, 2)),
            gridcolor='rgba(128,128,128,0.3)',
            linecolor='rgba(128,128,128,0.5)'
        ),
        angularaxis=dict(
            tickfont=dict(size=12),
            rotation=90,
            direction='clockwise',
            gridcolor='rgba(128,128,128,0.3)',
            linecolor='rgba(128,128,128,0.5)'
        ),
        bgcolor='rgba(0,0,0,0)'
    ),
    showlegend=False,
    width=1155,
    height=800,
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=50, r=50, t=50, b=50)
)

# Save as static PNG
fig.write_image('/home/ubuntu/ai_sentiment_charts/tension_web_naked.png', width=1155, height=800, scale=2)

print("Naked Tension Web chart created successfully!")
print("File saved: tension_web_naked.png")

