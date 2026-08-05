---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [azure-ml-designer, execute-python-script, matplotlib, scatter-plot, visualisation]
---

# Execute Python Script — matplotlib Scatter Plot in Azure ML Designer

Use Python code in the Designer to generate visualisations that are not available as built-in components.

## Purpose

The Designer has limited built-in visualisation components. The Execute Python Script component lets you run arbitrary Python code — including matplotlib for custom plots.

## Component

Azure ML Designer → Python / R → Execute Python Script

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Script | Python code | Must define an `azureml_main` function |
| Input ports | 1 or 2 | Pass DataFrames from upstream components |

## Structure

```python
def azureml_main(dataframe1 = None, dataframe2 = None):
    import matplotlib.pyplot as plt

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(dataframe1['Feature1'],
                dataframe1['Feature2'],
                c=dataframe1['Scored Labels'],
                alpha=0.5)
    plt.xlabel('Feature1')
    plt.ylabel('Feature2')
    plt.title('Prediction vs Actual')
    plt.show()

    # Must return a DataFrame
    return dataframe1
```

## Key Points

- The function **must** return a DataFrame (even if unused — minimum return is `return dataframe1`)
- matplotlib plots are captured as images in the pipeline output
- Common libraries pre-installed: pandas, numpy, matplotlib, scikit-learn
- Use right-click → Visualise on the output port to see the plot

## Related

- [[matplotlib-histogram-python-visual]]
- [[matplotlib-box-plot-python-visual]]
- [[azure-ml-designer-pipeline-components]]
