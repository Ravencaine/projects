---
title: "ETL Process and Data Warehouse Design with SSIS in the Retail Industry"
source: "https://medium.com/womenintechnology/etl-process-and-data-warehouse-design-with-ssis-in-the-retail-industry-6ee458d9beac"
author:
  - "[[Ayşegül Yiğit]]"
published: 2025-08-13
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Hello, in this article I will try to explain how to create a data warehouse development package using SSIS, one of the business intelligence processes, and provide information about frequently used tasks. At the same time, we will examine together how performance is improved when transitioning from normalized structures in relational databases (OLTP) to denormalized structures.

To create our package, we first right-click the “SSIS Packages” box in the “Solution Explorer” window on the right side of the screen and select the *New SSIS Package* option.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*FRdVNhVsh_BM43zmNR22UA.png)

We have now created a new package as desired. The next step is to freely name our package. By clicking once on *Package1.dtsx* on the right, you can change “Package1” to the name of the package you want to create.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*P-iqzegGU7YaS2Jgu0CbUw.png)

Since I have already created a package named *DimSiparis*, I will continue the explanation using an existing package.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*99zg4ezGSo0o3Szln1hf0w.png)

From the SSIS Toolbox window, we drag and drop the “Data Flow Task” component into our Control Flow window. Since I will create an *Order* package, I named the DFT component *Siparis DF*. In the screenshot, you can also see the *Truncate dwhDimSiparis* component, but I will explain that at the end. At this stage, we simply drag the Data Flow Task into the Control Flow and rename it.

In the second stage, we double-click the *Siparis DF* component to switch to the Data Flow level. Since I have already created the package before, you will see all the components in my window, but for you, this window will be empty.

![](https://miro.medium.com/v2/resize:fit:1386/format:webp/1*-mGuvwNc0AfTnqDNxn9QoA.png)

We start by assigning a source from which we will pull data from our database. To do this, we drag the *OLE DB Source* component from the left-hand side into the Data Flow level.  
Before loading our source, let’s examine our table in SQL Server.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*kfDnZ4L1PwtZjpcy58D5Bg.png)

In its raw form, our *Orders* table contains the columns *OrderID*, *OrderDate*, and *SalesAmount*.  
In the source settings, we first select *SQL command* mode from the *Data Access mode* dropdown.

Then, in the *SQL command text* box that appears below, we write our SQL query according to our purpose.  
Since our goal involves multiple table columns, let’s first review the tables we will use.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*I0ofE5-YE1DmeynSlixm3A.png)

Our aim is to take the *InvoiceAddress* column from the *Invoice* table, create a new column based on neighborhood, and bring the invoice amount as a separate ordered column, then create a column in the Orders table according to its level. Additionally, to see which customers placed which orders, we can optionally include the *Customer* table. We relate these tables using an INNER JOIN, and after checking in the *Columns* tab that the desired columns are present, we move to the *Data Conversion* component.

We drag and drop the *Data Conversion* component under our *Orders DB* source. When you click on the Orders DB source, a blue arrow will appear beneath it — drag this arrow to the Data Conversion component to complete the connection.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aM4jSRIGEQRQvlYFDxSkrg.png)

Data conversion simply allows us to change column data types and convert data to the desired type.  
Your “Output Alias” field might appear as *Copy of SalesAmount*. Since we will use these columns later and to avoid confusion, we replace all instances of “Copy of” with “DC\_”.

After completing the Data Conversion step, we move to the *Derived Column* component.  
As the name suggests, a derived column is a column generated from existing data, used to make the data more meaningful or to add more meaning to it.

In ETL processes, Derived Column is quite popular — mainly because the “T” in ETL stands for *Transform*. Adding a new column or performing operations on an existing column represents transformation.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yfwHH2uzvCcyL0_0LCkbgg.png)

From the *Command* section of the Toolbox, we drag and drop the *Derived Column* component under the Data Conversion component and connect them.  
In our first Derived Column operation, since we will find the neighborhood name from the Invoice Address (FINDSTRING) and take certain characters (SUBSTRING), we name it based on the Substring & Find functions we will soon see in the *String Function* section.

When we open the Substring&Find Derived Column component, we see the *Columns* tab on the left, which contains all the columns pulled from the Orders DB source. We had renamed them with “DC\_” in the Data Conversion step. Since we want the neighborhood names from the Invoice Address, we drag and drop the “DC\_InvoiceAddress” column from the Columns tab into the “Expression” box below.

![](https://miro.medium.com/v2/resize:fit:1270/format:webp/1*6oP5k9cz6kUk94SKJDNlRg.png)

Looking at the raw InvoiceAddress column in our main Invoice table, to extract neighborhood names like “Sinanoba Mah” or “Mecidiyeköy Mah” in a clean form, we apply the SUBSTRING and FINDSTRING functions mentioned earlier.  
Finally, in the *Derived Column Name* field, we enter the name for our new column, and since we are creating a new column, we select *\<add as new column>* for the Derived Column option.

After deriving the *Neighborhood* column, we move on to our second derived column operation.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xinf9-TlM4d9djgvw1EK5A.png)

In our gamification strategy, based on Jacques Lacan’s desire theory, our “desired object” concept will be *Position* and *Badge*.

For the *Position* column of our marketing strategy, our goal is for customers in Istanbul with Level 1 to have the position “Major.” From the Columns tab, we set DC\_Level equal to 1 and DC\_City equal to “Istanbul.”  
In the expression, we use “?” for a condition: if true, output “Major”; if false, output nothing (“ ”).

For the *Badge* column, we want to award the “Muhtar” badge to neighborhoods based on SalesAmount.  
We drag our previously derived Neighborhood column into the expression box, name it “Badge” in the Derived Column Name field, and since our Orders table already has an address column, we choose *Replace* instead of creating a new column.

Our goal is to give the Muhtar badge to neighborhoods in Istanbul with SalesAmount ≥ 2. Using “&&” for AND conditions, we write the condition, then use “?” to output “Muhtar” if true, or nothing (“ ”) if false.

Now, we move to the *OLE DB Destination* step.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5RyZv_7lkNBuiOn2S4hUNQ.png)

From the Destination section of the Toolbox, we drag and drop the OLE DB Destination component into the Data Flow level and connect it to our Badge component. Since we are creating a dimension table, we select *Table or view — fast load* from the *Data Access mode* dropdown. Then, by clicking the *New* button next to “Name of the table or the view,” we generate the SQL table creation code.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*wmnl9xdTT1L7ihVy3ipSvg.png)

In this code, we notice that DC-prefixed columns are repeated. We only want the DC columns, so we remove duplicates in SQL Server.  
To clean up, we also remove the “DC\_” prefix using Ctrl+H (Replace All).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XaHX8rlwtdJbgzuMAEm0hg.png)

After this, we name the table *dwh.DimSiparis*, return to SSIS, and finalize the table selection.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*YXEAeIoLty7UpjOrTt6fGw.png)

After checking the *Mapping* section, we go back to the Control Flow level.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*X5NEQ6DORpFHnMPN25zBPQ.png)

To prevent duplicate data when running the package multiple times, we add a Truncate step. We connect an Execute SQL Task to our Data Flow Task and write the SQL code to truncate the DimSiparis table.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*FOHS0yljuB8UCyNe7qlCOA.png)

Once done, running the DimSiparis table in SQL Server shows that it produces meaningful columns as intended.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jB6_e9VuR1GD4QnEcSpt2A.png)

Finally, we verify data consistency in our final table. For example, a customer with Level 1 should have the position “Major,” which is correct. Similarly, customers in Istanbul neighborhoods with SalesAmount ≥ 2 correctly receive the “Muhtar” badge.