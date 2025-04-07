import pandas as pd

# Reading to dataframe and creating total count col
df = pd.read_csv('cell-count.csv')

populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']
df['total_count'] = df[populations].sum(axis=1)

# Reshaping the DataFrame using melt function to organize populations
df2 = pd.melt(
    df,
    id_vars=['sample', 'total_count'],
    value_vars=populations,
    var_name='population',
    value_name='count',)
df2['relative_freq'] = df2['count'] / df2['total_count']

# Sorting the values by the number in the sample column, and then by the population list order
df2 = df2.sort_values(
    by=['sample', 'population'],
    key=lambda col: (
        col.str.extract(r'(\d+)').astype(int)[0] if col.name == 'sample'
        else col.map({name: i for i, name in enumerate(populations)})
    )
).reset_index(drop=True)

df2.to_csv('output.csv', index=False)