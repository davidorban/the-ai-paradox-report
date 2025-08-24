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
insights = radar_data['insights']
hover_details = radar_data['hover_details']

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
        name=f"{series['name']} ({series['percentage']})",
        opacity=series['opacity'],
        hovertemplate='<b>%{fullData.name}</b><br>%{theta}: %{r}<extra></extra>'
    ))

# Create custom hover text with detailed information
hover_text = {}
for dim_name, details in hover_details.items():
    hover_text[dim_name] = "<br>".join([f"• {detail}" for detail in details])

# Update layout for radar chart
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[scale['min'], scale['max']],
            tickvals=list(range(scale['min'], scale['max'] + 1, 2)),
            ticktext=[scale['labels'][i] if i < len(scale['labels']) else str(i) 
                     for i in range(scale['min'], scale['max'] + 1, 2)],
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
        bgcolor='white'
    ),
    title=dict(
        text=radar_data['title'],
        x=0.5,
        font=dict(size=20, family="Arial, sans-serif")
    ),
    showlegend=True,
    legend=dict(
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.05
    ),
    width=1155,
    height=800,
    paper_bgcolor='white'
)

# Add annotations for insights
insights_text = "<b>Key Insights:</b><br>"
for insight in insights:
    # Break long insights into shorter lines for better wrapping
    if "Truth & Reality scores highest" in insight:
        insights_text += f"• Truth & Reality scores highest<br>  across all groups (avg 7.3)<br>"
    elif "Human Connection and Identity" in insight:
        insights_text += f"• Human Connection and Identity<br>  cluster as top personal concerns<br>"
    elif "Military/Conflict shows largest" in insight:
        insights_text += f"• Military/Conflict shows largest<br>  variance between groups<br>"
    elif "Technical Reliability concerns" in insight:
        insights_text += f"• Technical Reliability concerns<br>  correlate with professional use<br>"
    else:
        insights_text += f"• {insight}<br>"

fig.add_annotation(
    text=insights_text,
    xref="paper", yref="paper",
    x=1.05, y=0.15,
    xanchor="left", yanchor="bottom",
    showarrow=False,
    font=dict(size=10, color="black"),
    bgcolor="rgba(255,255,255,0.9)",
    bordercolor="gray",
    borderwidth=1,
    width=180,
    align="left"
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

# Add dimension labels and descriptions in alphabetical order, aligned with legend
sorted_dimensions = sorted(dimensions, key=lambda x: x['axis'])
y_start = 0.85
y_step = 0.036  # Increased spacing by one-third (from 0.027 to 0.036)

for i, dim in enumerate(sorted_dimensions):
    y_pos = y_start - (i * y_step)
    
    fig.add_annotation(
        text=f"<b>{dim['axis']}</b><br><i>{dim['description']}</i>",
        xref="paper", yref="paper",
        x=1.05, y=y_pos,
        xanchor="left", yanchor="top",
        showarrow=False,
        font=dict(size=9, color="darkblue"),
        align="left"
    )

# Save as interactive HTML
fig.write_html('/home/ubuntu/ai_sentiment_charts/tension_web_interactive.html')

# Save as static PNG
fig.write_image('/home/ubuntu/ai_sentiment_charts/tension_web_static.png', width=1155, height=800, scale=2)

print("Tension Web radar chart created successfully!")
print("Files saved:")
print("- Interactive: tension_web_interactive.html")
print("- Static: tension_web_static.png")

# Display insights
print("\nKey Insights:")
for insight in insights:
    print(f"- {insight}")

# Display group percentages
print("\nGroup Distribution:")
for series in data_series:
    print(f"- {series['name']}: {series['percentage']}")

# Calculate and display average scores per dimension
print("\nAverage Concern Scores by Dimension:")
avg_scores = {}
for i, dim_name in enumerate(dimension_names):
    total_score = sum(series['values'][i] * float(series['percentage'].rstrip('%')) / 100 for series in data_series)
    avg_scores[dim_name] = round(total_score, 1)

# Sort by average score
sorted_dims = sorted(avg_scores.items(), key=lambda x: x[1], reverse=True)
for dim_name, avg_score in sorted_dims:
    print(f"- {dim_name}: {avg_score}/10")

