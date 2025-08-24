import json
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# Load the data from the JSON file
with open('/home/ubuntu/upload/pasted_content.txt', 'r') as f:
    data = json.load(f)

# Extract the Journey Map data
journey_data = data['visualizations'][0]
categories = journey_data['data']['categories']
personal_series = journey_data['data']['series'][0]
societal_series = journey_data['data']['series'][1]

# Create the figure
fig = go.Figure()

# Add Personal Experience line
fig.add_trace(go.Scatter(
    x=categories,
    y=personal_series['values'],
    mode='lines+markers',
    name=personal_series['name'],
    line=dict(color=personal_series['color'], width=3),
    marker=dict(size=8),
    showlegend=False
))

# Add Societal Impact line
fig.add_trace(go.Scatter(
    x=categories,
    y=societal_series['values'],
    mode='lines+markers',
    name=societal_series['name'],
    line=dict(color=societal_series['color'], width=3),
    marker=dict(size=8),
    showlegend=False
))

# Add divergence zone (area between lines starting from Regular Use)
divergence_start_idx = 2  # Regular Use phase
x_divergence = categories[divergence_start_idx:]
y_upper = personal_series['values'][divergence_start_idx:]
y_lower = societal_series['values'][divergence_start_idx:]

fig.add_trace(go.Scatter(
    x=x_divergence + x_divergence[::-1],
    y=y_upper + y_lower[::-1],
    fill='toself',
    fillcolor='rgba(255, 167, 38, 0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    name='Divergence Zone',
    hoverinfo='skip',
    showlegend=False
))

# Update layout - minimal version with transparent background
fig.update_layout(
    xaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)'
    ),
    yaxis=dict(
        range=[journey_data['y_axis']['min'], journey_data['y_axis']['max']],
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor='rgba(128,128,128,0.5)'
    ),
    hovermode='x unified',
    width=1000,
    height=600,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=50, r=50, t=50, b=50)
)

# Save as static PNG
fig.write_image('/home/ubuntu/ai_sentiment_charts/journey_map_naked.png', width=1000, height=600, scale=2)

print("Naked Journey Map chart created successfully!")
print("File saved: journey_map_naked.png")

