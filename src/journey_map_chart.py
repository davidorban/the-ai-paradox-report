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
    hovertemplate='<b>%{fullData.name}</b><br>%{x}<br>Sentiment: %{y}<extra></extra>'
))

# Add Societal Impact line
fig.add_trace(go.Scatter(
    x=categories,
    y=societal_series['values'],
    mode='lines+markers',
    name=societal_series['name'],
    line=dict(color=societal_series['color'], width=3),
    marker=dict(size=8),
    hovertemplate='<b>%{fullData.name}</b><br>%{x}<br>Sentiment: %{y}<extra></extra>'
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
    showlegend=True
))

# Add annotations for key quotes
annotations = []
for annotation in personal_series['annotations']:
    # Adjust arrow length for "Learning from AI teachers" annotation
    ay_value = -20 if annotation['text'] == '"Learning from AI teachers"' else -40
    
    annotations.append(dict(
        x=categories[annotation['point']],
        y=personal_series['values'][annotation['point']],
        text=annotation['text'],
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor=personal_series['color'],
        ax=0,
        ay=ay_value,
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor=personal_series['color'],
        borderwidth=1,
        font=dict(size=10)
    ))

for annotation in societal_series['annotations']:
    annotations.append(dict(
        x=categories[annotation['point']],
        y=societal_series['values'][annotation['point']],
        text=annotation['text'],
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor=societal_series['color'],
        ax=0,
        ay=40,
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor=societal_series['color'],
        borderwidth=1,
        font=dict(size=10)
    ))

# Update layout
fig.update_layout(
    title=dict(
        text=journey_data['title'],
        x=0.5,
        font=dict(size=20, family="Arial, sans-serif")
    ),
    xaxis=dict(
        title=journey_data['x_axis']['label'],
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)'
    ),
    yaxis=dict(
        title=journey_data['y_axis']['label'],
        range=[journey_data['y_axis']['min'], journey_data['y_axis']['max']],
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor='rgba(128,128,128,0.5)'
    ),
    annotations=annotations,
    hovermode='x unified',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    width=1000,
    height=600,
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Add note about sentiment scale
fig.add_annotation(
    text=journey_data['y_axis']['note'],
    xref="paper", yref="paper",
    x=0.02, y=0.98,
    xanchor="left", yanchor="top",
    showarrow=False,
    font=dict(size=10, color="gray"),
    bgcolor="rgba(255,255,255,0.8)",
    bordercolor="gray",
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
fig.write_html('/home/ubuntu/ai_sentiment_charts/journey_map_interactive.html')

# Save as static PNG
fig.write_image('/home/ubuntu/ai_sentiment_charts/journey_map_static.png', width=1000, height=600, scale=2)

print("Journey Map chart created successfully!")
print("Files saved:")
print("- Interactive: journey_map_interactive.html")
print("- Static: journey_map_static.png")

# Display insights
print("\nKey Insights:")
for insight in journey_data['insights']:
    print(f"- {insight}")

