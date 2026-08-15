---
title: "How to display measure descriptions directly in Power BI reports? (part 2)"
source: "https://medium.com/microsoft-power-bi/how-to-display-measure-descriptions-directly-in-power-bi-reports-part-2-8a28a1a2c56f"
author:
  - "[[Mateusz Mossakowski]]"
published: 2024-11-21
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
### In my previous article, I discussed how to display measure descriptions for report consumers in Power BI. However, the “basic” solution has one drawback: the alignment of the description text inherits the right alignment from the numerical measures. While this alignment is suitable for numbers, it may not be ideal for text values. Left alignment would likely be more appropriate for text descriptions. Furthermore, if the description is lengthy and you don’t insert line breaks directly in the description property window, you may end up with a long, continuous line of text that is difficult and frustrating to read. In today’s article, I will address this issue.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://topmate.io/powerbi_masterclass/1198509) **🎁**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bV5fnQtoLg7elTInW5lOmA.png)

relatively long measure description with no line breaks

Assuming we might have lengthy measure descriptions without any line breaks, the initial approach would fail in terms of readability.

Even if a measure description contains line breaks, it will still be right-aligned, which can look a bit strange for text values.

### Potential solution

Below, let me guide you through a potential solution. Let’s assume we have an oversimplified measure catalog stored in the Databricks metastore in a form of a two-column table that contains both measure names and their descriptions.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*S6J7VmIFPVFC71tpClPxqQ.png)

oversimplified measure catalog example

The idea here is to perform the following steps:

1. First, split the measure catalog into two data frames: one for measures that contain line breaks in their descriptions, and another for those that do not.
2. For the first data frame, transform it so that each measure name has its lines exploded into separate rows. For the second data frame, handle the absence of line breaks using a predefined approach; in this example, we will split the descriptions into 10-word chunks and explode each chunk into a separate line.
3. Once we have both data frames “exploded,” we will union them. Next, retrieve the maximum length of a single line string from the measure descriptions and define a non-breaking space character (NBSP).
4. Now comes the tricky part: the idea is to add as many NBSPs as needed after the single line strings to reach the maximum length retrieved in the previous step. This will allow us to artificially enforce the right alignment of the descriptions. *Assuming that a given single line has 65 characters and the maximum length string has 80 characters, we will need to add 15 NBSPs.*
5. The final step is to “merge” all single-line descriptions for each measure name, separating them with a line break.
6. Instead of using a calculated table built on top of the **INFO.VIEW.MEASURES** function (as in the original simplified solution from the previous article), we will utilize the output (measure\_definition table) from the code below. Aside from this change, everything else remains exactly the same as in the original solution.
```c
from pyspark.sql.functions import *
from pyspark.sql.types import StringType, ArrayType

# split measure catalog into two dataframes
# one with the description that already have a break line
# another one for those that do not have a break line
measures_with_newline = measure_catalog.filter(col("measure_definition").contains("\n"))

measures_without_newline = measure_catalog.filter(~col("measure_definition").contains("\n"))

############################
## measures with new line ##
############################

# for the measures with the break line explode each line to a new row
measures_with_newline = measures_with_newline.withColumn(
    "measure_definition", split(col("measure_definition"), "\n")
).withColumn("measure_definition", explode("measure_definition"))

###############################
## measures without new line ##
###############################

# parameter for the maximum number of words per line
number_of_words_per_line = 10

# function to split definitions into chunks (10 words in this example)
def split_definitions(definitions):
    words = definitions.split()
    return [
        " ".join(words[i : i + number_of_words_per_line])
        for i in range(0, len(words), number_of_words_per_line)
    ]

split_definitions_udf = udf(split_definitions, ArrayType(StringType()))

# apply the function and explode the result
measures_without_newline = measures_without_newline.withColumn(
    "chunks", split_definitions_udf(col("measure_definition"))
).select(col("measure_name"), explode(col("chunks")).alias("measure_definition"))

######################
## measures unioned ##
######################

measures_union = measures_with_newline.unionByName(measures_without_newline)

# retrieve overal maximum length of a single line
max_length = measures_union.select(max(length("measure_definition"))).collect()[0][0] 
char_to_repeat = " "  # NBSP

# adjust measure definition column so that it is filled with the NBSP until it reaches the overall maximum length of a single line within whole measure catalog
measures_union = measures_union.withColumn(
    "measure_definition",
    concat(
        col("measure_definition"),
        repeat(lit(char_to_repeat), (max_length - length(col("measure_definition")))),
    ),
)

##########################
## measures definitions ##
##########################

# aggregate the single-line measure definitions into a single string per measure name, separated by newline
measures_definitions = measures_union.groupBy("measure_name").agg(
    concat_ws("\n", collect_list("measure_definition")).alias("measure_definition")
)

measures_definitions.write.format("delta").mode("overwrite").saveAsTable(f"{schema}.measure_definitions")
```

Here is the output of the exercise explained above:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6pj2kam8QHbsL4Exxh5HXw.png)

measure\_definition table

Once I display all the characters in my beloved Notepad++, it will likely provide you with a clearer insight into what actually happened with the data from the measure catalog. 😉

We are almost there, but the alignment is still not perfect 😥. The reason for this is that I was using the Segoe UI font within the report visuals. While I do like this font, it is not a monospaced font (where each character has the same width), which is why the solution remains less than ideal.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*5d6r2_3Pf80Bt8nLC8nlAg.png)

variable width font version

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*0rlajwgSBTWqe_p69xAXag.gif)

However, once we switch from a variable-width font to a monospaced font (Consolas, in my example), it looks exactly as expected — meaning that the text of the measure definition is now left-aligned.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*Pj1CcpR2bp4b1C989hnw9Q.png)

monospaced font version

![](https://miro.medium.com/v2/resize:fit:1280/format:webp/1*Sp9uzt7khpYTGxHjU_pIBQ.gif)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?source=post_page-----8a28a1a2c56f---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Visualization, DAX

**Tags:** Tutorial, Data Visualization, DAX