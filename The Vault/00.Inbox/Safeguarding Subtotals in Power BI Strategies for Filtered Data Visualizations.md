---
title: "Safeguarding Subtotals in Power BI: Strategies for Filtered Data Visualizations"
source: "https://medium.com/microsoft-power-bi/safeguarding-subtotals-in-power-bi-strategies-for-filtered-data-visualizations-20c6e35b4991"
author:
  - "[[Mateusz Mossakowski]]"
published: 2025-01-03
created: 2026-08-12
description: "The article will explain how to preserve subtotals at a specific level (in this case, the product category ) in a dimension hierarchy when lower-level attributes are filtered (such as product subcategory and/or product manufacturer). For example, if a user filters the data at the product category level, the data will be filtered accordingly. However, if selections are made at the product subcategory or product manufacturer level, the data will remain unfiltered. These selections will only impact the visibility of elements in the visual, while all other (non-selected) items will be grouped into the “All Other” bucket. Alternatively, if we do not prioritize the “All Other” bucket, we can omit it entirely, leading to significantly improved DAX performance. The larger and more complex the semantic model (specifically the cardinality of the dimension table) and visual, the greater the advantages of using the “No Other” approach."
Processed: "Unprocessed"
---
## The article will explain how to preserve subtotals at a specific level (in this case, the product category ) in a dimension hierarchy when lower-level attributes are filtered (such as product subcategory and/or product manufacturer). For example, if a user filters the data at the product category level, the data will be filtered accordingly. However, if selections are made at the product subcategory or product manufacturer level, the data will remain unfiltered. These selections will only impact the visibility of elements in the visual, while all other (non-selected) items will be grouped into the “All Other” bucket. Alternatively, if we do not prioritize the “All Other” bucket, we can omit it entirely, leading to significantly improved DAX performance. The larger and more complex the semantic model (specifically the cardinality of the dimension table) and visual, the greater the advantages of using the “No Other” approach.

### Ingredients

What do we need to make this stakeholders’ dream come true?

- A duplicated product dimension that is “expanded” with “All Other” elements for each and every category.
- A one-to-many relationship between the duplicated and regular product dimensions.
- Specific usage of objects from both product dimension tables — in the slicers and visuals (matrix in our case).
- Fancy DAX measures to make it eventually happen.

### Duplicated product dimension

Let me first explain what is needed to create the duplicated product dimension and why it is necessary. We require a duplicated dimension because we cannot achieve the functionality described above with a single dimension. However, a simple duplicate won’t suffice, as we want all data from non-selected subcategories and/or manufacturers to be presented and visible in the “All Other” bucket. This is why we need to implement the “All Other” logic. You can review the PySpark/Spark SQL approach below (keep in mind it is just a suggestion — there may be more effective implementations 😊).

The whole concept is based on expanding the duplicated dimension by adding all other elements for each product category, along with:

- An artificial product ID (which must be unique to establish a one-to-many relationship between the duplicated and regular product dimensions; it is created by taking the overall maximum product ID and increasing it by the dense rank of a given category).
- Artificial subcategory and manufacturer sorting, ensuring that the “All Other” bucket always appears at the bottom.
```c
from pyspark.sql.functions import lit
from pyspark.sql.window import Window

# Although we do not require subcategories to be sorted in any specific order other than alphabetical,
# we need this artificial sorting column to ensure that the "All Other" element appears at the bottom,
# below the "real" subcategories.
prod_dim = prod_dim.withColumn("SubCategory_sort", lit(0))

# Create a temporary view to facilitate the creation of a dynamic Spark SQL query later on.
prod_dim.createOrReplaceTempView("prod_dim_tempvw")

# Define the name we want to use for this artificial element.
other_name = "All Other"

# Write a query to create a new row for the "All Other" element for each category.
# This includes an artificial product_id, which must be unique to establish a one-to-many relationship
# with the "regular" product dimension. Therefore, we take the overall maximum product_id from
# the product dimension and increase it by the dense rank of each category,
# along with the artificial sorting columns:
# one for subcategories
# and one for manufacturers (resulting in three values: 0 for "Our Company" to present it at the top,
# 1 for selected competitors, and 2 for non-selected manufacturers, i.e., the "All Other" bucket).
prod_dim_all_other = spark.sql(
    f"""
select distinct
        Category
        , '{other_name}'                                                         as SubCategory
        , '{other_name}'                                                         as Manufacturer
        , max(product_id) over ()        + dense_rank() over (order by Category) as product_id
        , max(manufacturer_sort) over () + 1                                     as manufacturer_sort
        , max(subcategory_sort) over ()  + 1                                     as subcategory_sort
from
        prod_dim_tempvw
"""
)

# Union the above artificial component with the real product dimension to achieve the final structure
# of the duplicated product dimension.
prod_dim_dupl = prod_dim.unionByName(prod_dim_all_other)
```

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*Fuw61LcbVy3Kl88xLkVx4g.png)

Subset of the duplicated and enhanced product dimension

### Semantic model adjustments

Once we have completed the enhanced duplicated product dimension, we need to establish a one-to-many relationship with the regular product dimension.

### How to configure slicers and visuals

When it comes to determining which columns to use from which dimension table, the image below provides clarity. For the slicers, only the category column should be sourced from the duplicated dimension, while both the subcategory and manufacturer should be taken from the regular dimension. For the matrix, all product attributes should be sourced from the duplicated dimension.

### DAX measures

Last but not least, let me walk you through the DAX measures that are needed to make this work.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*w6wCZm4aLT8bfUEyfyPAOw.png)

Sales Value measure

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*kXtTu7ermUT7JuGhqjF_RQ.png)

Category Sales Share measure

### Result

As you can see in the screen below, the Category1 subtotal remains untouched even though we have filtered Subcategory11 and two manufacturers (Our Company and Competitor 1). All non-selected subcategories and manufacturers are grouped into the ”All Other” bucket.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zGhsWJ6gWq8iTIwSuxq45g.png)

### Simplification

If you do not have a strong preference for the ”All Other” bucket, you can choose a much simpler approach. First of all, a straightforward one-to-one duplicate of the product dimension is perfectly acceptable in this scenario (no ETL burden here). Secondly, the DAX measure will also be much simpler, resulting in a lighter implementation and better performance.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*zN_pDeZyt7yT_xyjYKIung.png)

Sales Value measure (no other)

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*JSKacskuDDW-7eMO6_bKgg.png)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Twitter, Instagram | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----20c6e35b4991---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee