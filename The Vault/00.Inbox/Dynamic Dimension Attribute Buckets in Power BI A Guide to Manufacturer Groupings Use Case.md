---
title: "Dynamic Dimension Attribute Buckets in Power BI: A Guide to Manufacturer Groupings Use Case"
source: "https://medium.com/microsoft-power-bi/dynamic-dimension-attribute-buckets-in-power-bi-a-guide-to-manufacturer-groupings-use-case-eed3144b65c8"
author:
  - "[[Mateusz Mossakowski]]"
published: 2024-12-09
created: 2026-08-12
description: "This time, I want to walk you through a use case recently requested by our stakeholders. They wanted the ability to dynamically define key competitors, allowing for easy business analyses that compare them with our company’s performance, while still keeping other (more minor) competitors visible in the picture. Importantly, the manufacturer selections should not affect the overall grand total. In short, the manufacturer selections within a slicer should not limit the data — it should only determine which manufacturers fall into the “key competitors” bucket and which ones are categorized as “other competitors”."
Processed: "Unprocessed"
---
## This time, I want to walk you through a use case recently requested by our stakeholders. They wanted the ability to dynamically define key competitors, allowing for easy business analyses that compare them with our company’s performance, while still keeping other (more minor) competitors visible in the picture. Importantly, the manufacturer selections should not affect the overall grand total. In short, the manufacturer selections within a slicer should not limit the data — it should only determine which manufacturers fall into the “key competitors” bucket and which ones are categorized as “other competitors”.

### Model Setup and Product Dimension Transformations in PySpark

First things first — we need some setup for the semantic model. Unfortunately, the scenario described above cannot be covered within a single product dimension. That’s why we are going to create a duplicated dimension. This duplicated dimension can be much smaller than the original one, as it does not need to “go down” to the individual product ID level. It is enough for the duplicated dimension to include the manufacturer attribute along with other attributes needed for the analysis (in our simplified case — product category and subcategory). While in the dummy example the data volume savings for the duplicated dimension are not that impressive, in real-life scenarios, they can result in huge volume savings.

To make the slimmer duplicated dimension work, we need an artificial column on which we can build a one-to-many relationship between the duplicated and original product dimensions. In our case, this will be a concatenation of the product category, subcategory, and manufacturer, which will later be hashed using the MD5 function. We will add this key column to both the original and duplicated dimensions.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7ktqOxhU__Ehtwxc-g4i4A.png)

“basic” product dimension (subset of the data)

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*huOCoaKES5tBZfcEyrGLUg.png)

“adjusted” product dimension — enriched with the artificial\_key column (subset of the data)

On top of that, from the perspective of the duplicated dimension, we need to have a key\_competitors column that retains the company’s name for our company, while for any other manufacturer, the value “Key Competitors” is hardcoded. Moreover, we also need to expand the table in terms of rows by adding artificial “Other competitors” rows for every combination of all non-manufacturer product dimension attributes that exist in the duplicated dimension.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*EeFZWbv2nwbjnAtoJOjpIQ.png)

duplicated and “aggregated” product dimension enriched with key\_competitors and artificial\_key columns

Below, you can find the PySpark code to achieve both the main and duplicated product dimensions.

```c
from pyspark.sql.functions import col, lit, when, md5, concat_ws

our_company_name = "Our Company"
other_name = "Other competitors"
key_competitors_name = "Key competitors"

all_columns = ["Category", "SubCategory", "Manufacturer", "Manufacturer_sort"]

hash_columns = ["Category", "SubCategory", "Manufacturer"]

hash_columns_wo_manufacturer = ["Category", "SubCategory"]

####################################
### duplicated product dimension ###
####################################

# select only relevant columns for the duplicated dimension and keep distinct values
# the puropose here is to have both our company and other competitors as in the original product dimension

prod_dim_dupl = prod_dim.select(*all_columns).distinct()

# select only relevant columns (with out manufacturer column) and keep distinct values
# hardcode manufacturer column with Other competitors string
# hardcode manufacturers sort to be 3 so that it always lands at the bottom of the list
# the purpose here is to artificialy add Other competitors combinations with hardoced name and sorting columns

prod_dim_dupl_other = (
    prod_dim.select(*hash_columns_wo_manufacturer)
    .distinct()
    .withColumn("Manufacturer", lit(other_name))
    .withColumn("Manufacturer_sort", lit(3))
)

# union both dataframes that we created in previous steps
prod_dim_dupl = prod_dim_dupl.union(prod_dim_dupl_other)

# create key competitors column so that we end up with three options - Our company, Key competitors and Other competitors
# create artificial key column as a "hashed" concatenation of product attributes
prod_dim_dupl = (
    prod_dim_dupl.withColumn(
        "key_competitors",
        when(col("Manufacturer") == lit(our_company_name), lit(our_company_name))
        .when(col("Manufacturer") == lit(other_name), lit(other_name))
        .otherwise(lit(key_competitors_name)),
    )
    .withColumn("artificial_key", md5(concat_ws("_", *hash_columns)))
)

##############################
### main product dimension ###
##############################

# create artificial key column as a "hashed" concatenation of product attributes
prod_dim = prod_dim.withColumn("artificial_key", md5(concat_ws("_", *hash_columns)))
```

### Measures Logic and Report Setup

When it comes to the report setup, we need to use the manufacturer column from the main dimension in the slicer, while other product attribute slicers should source from the duplicated dimension. The same applies to the product dimension attributes used in the matrix.

When it comes to the fancy workaround for the sales value measure, we need to perform a couple of checks within a SWITCH statement and apply different approaches to ‘assign’ different manufacturers into the Key Competitors and Other Competitors buckets.

We also need a little trick to ensure that the sales share measure functions correctly.

Once this is done, end users can view either the aggregated figures for key competitors or the individual figures for each key competitor, while other competitors are always aggregated into a single line, as they are, by definition, ‘not that interesting’.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*OJNDPSH0_fUoSfnkm8TS_w.png)

aggregated key competitors figures

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*s6qO6ZagKFyzc8oWBYC2pQ.png)

individual key competitors figures

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Twitter, Instagram | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----eed3144b65c8---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee