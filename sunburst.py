import pandas as pd
import plotly.express as px

# 讀取 R 整理好的 CSV
df = pd.read_csv("C:\\Users\\user01\\Documents\\sunburst_prepared_data.csv")

# 使用 plotly.graph_objects 進行高度客製化，或用 plotly.express
import plotly.graph_objects as go

fig = go.Figure(go.Sunburst(
    ids=df['ids'],
    labels=df['labels'],
    parents=df['parents'],
    values=df['compound_count'], # 扇形大小：使用 Sample 總面積 (也可以改 compound_count)
    branchvalues="total",
    marker=dict(
        colors=df['log2FC'],
        colorscale='RdBu_r',         # 紅藍漸層
        showscale=True,
        colorbar=dict(title="Log2FC")
    ),
    hovertemplate='<b>%{label}</b><br>總面積: %{value:.2e}<br>化合物數量: %{customdata[0]}<br>Log2FC: %{customdata[1]:.2f}<extra></extra>',
    customdata=df[['compound_count', 'log2FC']]
))

fig.update_layout(margin=dict(t=10, l=10, r=10, b=10))
fig.show()