---
title: "Populate Descriptions for Power BI using AI"
source: "https://medium.com/microsoft-power-bi/populate-all-descriptions-for-power-bi-using-ai-bef5ebf8c3af"
author:
  - "[[Jpbydesign Com]]"
published: 2026-08-04
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
Descriptions help Power BI developers and Users see the purpose and relationships for each of the objects in the Model. One part of my Data Quality Analysis measures whether there is a description (see **Tabular Editor 2’s Best Practice Analyzer** documentation). The ability to quickly have those descriptions created, when not already specified, is a bonus. AI to the rescue.

I don’t generally trust AI to create stuff on its’ own… there are too many opportunities for processes to quietly break — introducing hidden issues. But, I am comfortable with having it create the descriptions because they are easily modified and shouldn’t dynamically impact the model.

Additionally, I like to include a dynamic Data Dictionary in my models… and the descriptions should not be blank. The following process quickly and efficiently modifies the model to include descriptions for each table, column and measure in the model.

## Assumptions:

- This should be one of the last steps in your development process
- Each of the sources being used have been added to the Power BI model
- The sources have been transitioned to tables (using Power Query )
- Most of the calculated columns and measures have been created

## Steps:

Get original TMDL code

- Open your Power BI Report
- On the left-hand side click the TMDL icon
- On the right-hand side click on the \[Data\] fly-out. It should show \[Tables\] and \[Model\] options… choose \[Model\]
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*TXm2AycLNgAi2LEjWj5O9Q.png)

- With the \[Semantic model\] expanded, one of the bottom options should be \[Tables (..)\]
- Note: there should be a number in the parenthesis () which is the number of tables in your model
- Right-Click on \[Tables\] and hover over \[Script TMDL to\] and choose \[Clipboard\] to copy the code to your clipboard

Save TMDL code to file

- Open your favorite text editor (I like Notepad++)
- Paste ((ctrl + v) in Windows) into your editor
- Save the file as a.txt or.tmdl (if that is an option)
- Note: check that your favorite AI engine will accept the file type you are saving in

Have AI update code for descriptions

- In your favorite AI engine
- (I will be using [Claude.ai](http://claude.ai/) today)
- Drag your saved text file to the request
- Put in the following prompt in the description area

> Task: Add missing descriptions to a Power BI TMDL file
> 
> Attached is a TMDL extract from my Power BI semantic model (a text file).
> 
> Please:
> 
> *\* Add a description to every table, column, and measure object that doesn’t already have one.*
> 
> *\* Use the format /// \<description text> on its own line, directly above the object it describes, indented to match that object’s existing indentation level.*
> 
> *\* Skip any object that already has a /// description — leave it exactly as-is.*
> 
> *\* Base each description on the object’s name, table context, and (for measures/calculated columns) its DAX expression — write a concise, accurate, business-readable sentence, not a generic placeholder.*
> 
> *\* Output the result as a complete, updated text file (same structure/formatting/line endings as the original), ready for me to paste back into Tabular Editor or the TMDL view.*

- Have your AI run the process
- Download provided output file

Paste the updated TMDL code back into Power BI

- Note: I compare the before and after files (I generally use the compare plugin in Notepad++ to check differences) to see if anything changed ( red vs green (items added) )
- If you closed or changed Power BI while the AI was working, please re-step through section \[Get original TMDL code\] above
- Open the output file in your favorite text editor
- Select all (CTRL + a) of the code
- Copy selection (CTRL + c)
- In Power BI, on the TMDL view, at the bottom should be a plus (+) white surrounded by green
- Click on that to create a new script window
- Paste the updated TMDL code (CTRL + v)
- Press “Apply” button (should be in green toward the top left of the window)

Steps are complete

## To validate process worked (spot check)

- Go to Model View (Left-hand side menu — icon looks like 3 boxes linked together)
- Hover over tables, columns and measures to see that each of the items has a description.
- If you need to change a description, click on the object and in the Properties window you can edit the description field.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*IE1qMXLqXBq2ZRxs-xrFrw.png)

Properties fly-out in Model view for changing descriptions as needed

## Thanks to:

[Anmol Malviya](https://medium.com/u/aa49b8faf220?source=post_page---user_mention--bef5ebf8c3af---------------------------------------) of Power BI Corner

[linkedin.com/in/anmol-malviya/?originalSubdomain=in](https://www.youtube.com/redirect?event=channel_description&redir_token=QUM4Zm9rUW9xeG40WDc3MDJlOG43emFneVJOcnxBR3JiS2FrMlJjN3ZqQjdSdnF0NU5ZRWk5YTZHUGZVc0V4Smt1SG5pNG81bVVfUldESjJPcDFOYXVDUkJWbFBUWUJZYjV1ejNxWmZnNjlTV3IwZ0l0MW5ZaUlfazB6VUF2emct&q=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fanmol-malviya%2F%3ForiginalSubdomain%3Din)

[How to Add Descriptions to Tables, Columns & Measures Using TMDL View in Power BI](https://www.youtube.com/watch?v=KpGEhmIcIss)