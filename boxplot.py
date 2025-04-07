import pandas as pd
import plotly.express as px

# Reading to dataframe and creating total count col
df = pd.read_csv('cell-count.csv')

populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']
df['total_count'] = df[populations].sum(axis=1)

# Reshaping the DataFrame using melt function to organize populations
df2 = pd.melt(
    df,
    id_vars=['sample', 'total_count', 'response'],
    value_vars=populations,
    var_name='population',
    value_name='count',)
df2['relative_freq'] = df2['count'] / df2['total_count']

# Sorting the values by the number in the sample column, and then by the population list order
df2 = df2.sort_values(
    by=['sample', 'population'],
    key=lambda col: (
        col.str.extract('(\d+)').astype(int)[0] if col.name == 'sample'
        else col.map({name: i for i, name in enumerate(populations)})
    )
).reset_index(drop=True)

df = pd.read_csv('cell-count.csv')

# Filtering to only treatment tr1 and PBMC samples
df3 = df[(df['treatment'] == 'tr1') & (df['sample_type'] == 'PBMC')]
keeplist = df3['sample'].tolist()

filtered_df = df2[df2['sample'].isin(keeplist)].drop(columns=['total_count', 'count']).reset_index(drop=True)
filtered_df['response'] = filtered_df['response'].replace({'y': 'responder', 'n': 'non-responder'})

fig = px.box(filtered_df, x="population", y="relative_freq", points="all", color='response')
fig.show()
