"""
AI Sentiment Analysis - Replication Code
========================================

This script reproduces the main visualizations from the AI Sentiment Dataset.
Requires: plotly, pandas, numpy

Usage: python analysis_code.py
"""

import pandas as pd
import plotly.graph_objects as go
import json

def load_data():
    """Load all dataset components"""
    journey_data = pd.read_csv('journey_map_data.csv')
    quadrant_data = pd.read_csv('paradox_quadrant_data.csv')
    tension_data = pd.read_csv('tension_web_data.csv')
    
    with open('complete_raw_data.json', 'r') as f:
        raw_data = json.load(f)
    
    return journey_data, quadrant_data, tension_data, raw_data

def create_journey_map(journey_data):
    """Reproduce the Journey Map visualization"""
    fig = go.Figure()
    
    # Personal Experience line
    fig.add_trace(go.Scatter(
        x=journey_data['phase'],
        y=journey_data['personal_sentiment'],
        mode='lines+markers',
        name='Personal Experience',
        line=dict(color='#2E7D32', width=3),
        marker=dict(size=8)
    ))
    
    # Societal Impact line
    fig.add_trace(go.Scatter(
        x=journey_data['phase'],
        y=journey_data['societal_sentiment'],
        mode='lines+markers',
        name='Societal Impact',
        line=dict(color='#C62828', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title="The Journey Map: Personal vs Societal AI Sentiment Over Time",
        xaxis_title="AI Experience Timeline",
        yaxis_title="Sentiment Score",
        yaxis=dict(range=[-10, 10]),
        width=1000,
        height=600
    )
    
    return fig

def create_paradox_quadrant(quadrant_data):
    """Reproduce the Paradox Quadrant visualization"""
    fig = go.Figure()
    
    # Color mapping for quadrants
    color_map = {
        'Win-Win Optimists': '#4CAF50',
        'Altruistic Skeptics': '#2196F3',
        'Pragmatic Paradox': '#FF9800',
        'Deep Skeptics': '#F44336'
    }
    
    fig.add_trace(go.Scatter(
        x=quadrant_data['personal_benefit'],
        y=quadrant_data['societal_benefit'],
        mode='markers+text',
        marker=dict(
            size=quadrant_data['weight'] * 10,
            color=[color_map[q] for q in quadrant_data['quadrant']],
            opacity=0.7
        ),
        text=quadrant_data['user_type'],
        textposition='top center'
    ))
    
    # Add quadrant lines
    fig.add_hline(y=0, line_width=2, line_color="black")
    fig.add_vline(x=0, line_width=2, line_color="black")
    
    fig.update_layout(
        title="The Paradox Quadrant: Personal Benefit vs Societal Impact",
        xaxis_title="Personal AI Benefit",
        yaxis_title="Perceived Societal Benefit",
        xaxis=dict(range=[-10, 10]),
        yaxis=dict(range=[-10, 10]),
        width=1000,
        height=800
    )
    
    return fig

def create_tension_web(tension_data):
    """Reproduce the Tension Web radar chart"""
    fig = go.Figure()
    
    # Get unique categories and axes
    categories = tension_data['category'].unique()
    axes = tension_data['axis'].unique()
    
    colors = {'High Concern Group': '#D32F2F', 
              'Moderate Concern Group': '#FFA726', 
              'Selective Concern Group': '#66BB6A'}
    
    for category in categories:
        cat_data = tension_data[tension_data['category'] == category]
        values = cat_data['value'].tolist()
        
        fig.add_trace(go.Scatterpolar(
            r=values + [values[0]],  # Close the polygon
            theta=list(axes) + [axes[0]],
            fill='toself',
            name=category,
            line=dict(color=colors[category])
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        title="The Tension Web: Navigating Multiple AI Concerns",
        width=1000,
        height=800
    )
    
    return fig

def calculate_statistics(quadrant_data):
    """Calculate key statistics"""
    # Quadrant distribution
    distribution = quadrant_data['quadrant'].value_counts(normalize=True) * 100
    
    # Center of mass (weighted by weight column)
    total_weight = quadrant_data['weight'].sum()
    center_x = (quadrant_data['personal_benefit'] * quadrant_data['weight']).sum() / total_weight
    center_y = (quadrant_data['societal_benefit'] * quadrant_data['weight']).sum() / total_weight
    
    return distribution, (center_x, center_y)

if __name__ == "__main__":
    # Load data
    journey_df, quadrant_df, tension_df, raw_json = load_data()
    
    # Create visualizations
    journey_fig = create_journey_map(journey_df)
    quadrant_fig = create_paradox_quadrant(quadrant_df)
    tension_fig = create_tension_web(tension_df)
    
    # Calculate statistics
    distribution, center_of_mass = calculate_statistics(quadrant_df)
    
    # Save visualizations
    journey_fig.write_html('journey_map_reproduction.html')
    quadrant_fig.write_html('paradox_quadrant_reproduction.html')
    tension_fig.write_html('tension_web_reproduction.html')
    
    # Print statistics
    print("Quadrant Distribution:")
    for quadrant, percentage in distribution.items():
        print(f"  {quadrant}: {percentage:.1f}%")
    
    print(f"\nCenter of Mass: ({center_of_mass[0]:.1f}, {center_of_mass[1]:.1f})")
    
    print("\nVisualizations saved as HTML files.")

