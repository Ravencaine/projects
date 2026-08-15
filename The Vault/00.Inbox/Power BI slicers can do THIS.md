---
title: Power BI slicers can do THIS?
source: https://mail.google.com/mail/u/0/?hl=en-GB#inbox/FMfcgzQhVqzPqZkZrVBhkKblnkflGDGb
author:
published:
created: 2026-08-09
description:
Processed: Unprocessed
---
Slicers are usually one of the first things people click on in a report. You want that to be a great first experience with your report.

So here is one worth building. A button slicer where the selected category comes forward with a full color image and the unselected ones drop back with smaller images and transparency. You can build this without custom visuals, you just need a few formatting tricks.

| ![](https://ci3.googleusercontent.com/meips/ADKq_NZvCnMR4bL19CzFnuUIehJ6b2k2WX74wWVsn96aEC9E_hA3_zQUo0KgL71aiSggqeY_EcZpBD8p3sJj4GppbPrCmeVYwZHfmVsDzu6s7sT-SoKok910eNkSpeo-CT23YFmGJLKYMutGU5iInNY6RTGQ=s0-d-e1-ft#https://storage.mlcdn.com/account_image/910688/nKyx7GlA77dL4TjObT2eGIQTwhncCHxZoquFLn0V.png) |  | ![](https://ci3.googleusercontent.com/meips/ADKq_NbiDgAWBklDn6CWdkSSDFu_zfxOvxfYjvUslyLiP82QyOOjFvDYlSTTzV9UbK1e8g9sDyR9g0dD9qZYl_GsFj7x13zBM9rIYfXazKmc038GRwkSTEK6epdnJxWKAJP4zGglEhwZpI06vWlGhXsliq37=s0-d-e1-ft#https://storage.mlcdn.com/account_image/910688/D2D11VG2mESOSxRpaAARiIf8MTAOSNV4JGJ2rcON.png) |
| --- | --- | --- |

Our example uses three categories: Furniture, Office Supplies, and Technology. Each has its own image hosted online and referenced in DAX.

**Last live cohort of the year starts 3 September.**

The Design Transformation program is where I teach the method behind every report I build.

*[Power BI Design Transformation](https://mlvarv.clicks.mlsend.com/tf/c/eyJ2Ijoie1wiYVwiOjkxMDY4OCxcImxcIjoxOTUzMzIxODA5NDcyNDA1NDMsXCJyXCI6MTk1MzMyMTkzNTE2NTIxMjQwfSIsInMiOiJlNWYzYmZiM2NjM2U2YTgwIn0)*

****Step 1 - Create the image measure****

The measure returns the image URL for whichever category is in context. Swap in your own URLs.

![](https://ci3.googleusercontent.com/meips/ADKq_Nabp-OzhWIW7qHCsBkOkiOxchHs62_G75VOdHFfIhnF6Vj6q0dx7mhy0tC41skzMzgZWl07NPl129aOb9onVuyA-IMEg64YJMvu8Su96k4vyhJP_vZXh8yWc31wMVdl69mPmbMUG-pXVdKuGcuRDjS5=s0-d-e1-ft#https://storage.mlcdn.com/account_image/910688/CBI3nG4rD0rGhdIiFcd798K8SQxBq0zdEmKzdPnq.png)

| ****Step 2 - Insert a button slicer and set up the layout****  Insert a **button slicer** and add Category to the Value field well. Clean it up first:  - Turn off the title - For the buttons, turn off the border and background and set padding to 0  Then go to **Multi-button layout** - Layout and set it up:  - Arrangement - Horizontal - Style - Tiles |  | ![](https://ci3.googleusercontent.com/meips/ADKq_NazINuHnouU1h1B7-20rXYyvdzLLJZ_bOvvDH1D6up7ku46_Mdq-0GqmJD9yB_dmPtT5UZZAsbBe5W-HL4xyuORckoA_6ME9MS9obpaJu7-FZKcpDspYYXGdvULQ4gq0HDuylzZl3XCj6LvwIfr2Yph=s0-d-e1-ft#https://storage.mlcdn.com/account_image/910688/bOJeqohUKXgcWdRaVuDiuIYUieAIazu21EjQ5KAX.png) |
| --- | --- | --- |

**Step 3 - Set up the Images**

Go to Image formatting. This is where you assign the category image and control how it behaves per state.

**All states (Advanced off):**

- Turn on Image
- Image source - Select from data
- Field - Img Product Category
- Image fit - Fill
- Transparency - 50%
- Image effects - off
- Set as background - on
- Ignore padding - off

Turn on Advanced to access the Selected and Unselected states.

**Selected state:**

- Transparency - 0%
- Set as **background - OFF**

**Unselected state:**

- Transparency - 66%
- Set as **background – ON**

It should now look like below:)

![](https://ci3.googleusercontent.com/meips/ADKq_NY_9ZE3DegdlYnBh0Btv4vEiEUJvBk28iMISOxcUZX334mAOu_vy5fG5LT3rLqEnQd5pjN6efz5rUWJZBYFBf_sU5rQpcQKaiuL6shZpaxYmP-COLE4bBCrUjP4Y56n6v_YYM-_uU7NZRzJ6qcb8ku6=s0-d-e1-ft#https://storage.mlcdn.com/account_image/910688/ysD17Jv7Yc1ftyXrDSHpzEae6haJc2jPULDWiyIu.png)

| **Step 4 - Set the button shape**  Go to Buttons and change the shape. I went for slightly rounded corners.  - Shape - Rounded Rectangle - Corner radius - 8px |  | ![](https://ci3.googleusercontent.com/meips/ADKq_NaKL3xeRTy_rI8CmctdAo_Nh5bLre93Q_lcrNmaEXxFMumnBxWhfud4AZd6029xsXkQAtni0qbjuQc9fwsNv5w900JVzlKYk08kXPL5RTBm88grJodtmTXiBwYqLtCd6FFlCUweQkb1ZdHSdzDaMk8A=s0-d-e1-ft#https://storage.mlcdn.com/account_image/910688/KNYfzxVZ0xmOFal6yw3Ya19OJW5bYfWZc4a82bLN.png) |
| --- | --- | --- |

**Step 5 - Set up the Callout**

Go to callout > **All states**

Under Layout:

- Hug content - on,
- Vertical alignment - Bottom

Under Value:

- Turn on Value, Set color and transparency - 0%
- Horizontal alignment – Center

For the **selected state** change the font color to black.

| **Step 6 - Format the Buttons**  Now the important part:) the effect that make the unselected ones smaller and disappear in the background.  Go to Buttons and turn on Advanced.  **Selected state:**  - Padding - custom, Top 0, Left 0, Right 0, Bottom 16px - Background - on, light blue - Shadow – off |  | ![](https://ci3.googleusercontent.com/meips/ADKq_NadhUhXO7w31c9hlY_2xMAIK6VdE9niCItMQOdI9MF34c9Xfep9yHQNYbEnHfz6yivwlH6n7WtZdZE4GDZ3ccGwgZGrFG7BskMjIUSkuwvXVplbDgzQXsILGKlA9ZrFsfCZfcczygOxHbgvsf7X0PTd=s0-d-e1-ft#https://storage.mlcdn.com/account_image/910688/gUL8r8ZreA3eZm8E8t7LxPF5bqJcY93N1J90FsYx.png) |
| --- | --- | --- |

**Unselected state**

- Padding - custom, all 0
- Background – on, fill color black and 80% transparency
- Shadow - on, color white, custom position (for example size 10px, blur 25px, angle 135 degrees, distance 10px, transparency 100%)

| ![](https://ci3.googleusercontent.com/meips/ADKq_NZUuRXK2YE4sqZhbGqhU-LmVN-Y6pj_a8A-MYTvmBTgsy3ZhV6DLzH-aYogkabiQTv8K1lKHrefHiYDyZDrFowQRTwXaxqu7juwRJ_C5DtJfGKYbLXgwpfRpU9S9YF5h7Y6okr4GJesS3uh89rIvd1i=s0-d-e1-ft#https://storage.mlcdn.com/account_image/910688/fmYGyw14RMOx5mrsQsSFNzoXlSMgmKVjfQ9gVLTa.png) |  | ![](https://ci3.googleusercontent.com/meips/ADKq_NYpl2TaYyIvXDZfhL4sZMXptPKmmwjjVl5tf8myy9QR-DX1w_E6vRn9IHyU0xozZIAwsknUwRTrR0Fyy6UcWkSiFqw1TGtm4wMR0HihflHdZpOqo9tDWN2qeugTtWq-nQ2jzqlIUuOk9aBN5iIXUzal=s0-d-e1-ft#https://storage.mlcdn.com/account_image/910688/cg3FIEgihRRJx143QxwdnqoISSaVeu95P1ZU44BL.png) |
| --- | --- | --- |

And that's it already. Now you just have to refine the formatting a bit further and also don't forget to setup the pressed and hover states.
