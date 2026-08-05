---
title: "Power BI Info Panel: Add Interactive Overlays with PowerPoint"
source: "https://databear.com/power-bi-info-panel/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-05-18
created: 2026-08-04
description: "Create a Power BI info panel using PowerPoint and bookmarks. Add interactive overlays to guide users without any design experience."
Processed: "Unprocessed"
---
Creating a **Power BI info panel** is a simple but powerful way to enhance report usability. With just PowerPoint and bookmarks, you can build interactive overlays that guide your users through key features without cluttering the design.

##### Why Add an Info Panel to Your Power BI Report?

Power BI dashboards often contain valuable features and filters that go unnoticed by users. An **info panel overlay** helps:

- Educate users on available visuals and filters
- Highlight key features
- Improve usability without cluttering the report layout

---

##### 1: Finalize Your Power BI Report

Before creating the info panel, ensure your report is complete:

- All visuals finalized
- Layout and filters in place
- Ready to publish

Changes after adding an info panel may require rework, so hold off until the design is locked.![](99.System/Attachments/Screenshot-2025-05-11-130414.png)

---

##### 2: Take a Screenshot of Your Report

To build an accurate overlay:

1. Open your report in Power BI Desktop.
2. Use a tool like **Snipping Tool**, **Snagit**, or just hit `Print Screen` on your keyboard.
3. Capture the entire report canvas as precisely as possible.![](99.System/Attachments/Screenshot-2025-05-11-130619.png)

---

##### 3: Design the Info Panel in PowerPoint

You don’t need Photoshop— **PowerPoint works perfectly** for this. Follow these steps:

##### Insert and Size the Screenshot

- Open PowerPoint (default resolution is 16:9, which matches Power BI).
- Paste the screenshot onto a blank slide.
- Resize the image to cover the entire canvas.

##### Create the Transparent Overlay

- Insert a rectangle shape.
- Snap it to all four corners of the slide.
- Format it with a color of your choice and set **transparency to around 80%**.

##### Add Informative Callouts

- Insert callout shapes or text boxes.
- Label key areas of the report like:  
	*“Click here to filter by region”* or *“Hover for tooltip info”*.
- Customize the style (text color, shadows, borders) to make it visually distinct.![](99.System/Attachments/Screenshot-2025-05-11-131131.png)

---

##### 4: Export the Overlay as a Transparent Image

To preserve the transparent background:

1. Select all elements (`Ctrl + A`).
2. Right-click → **Save as Picture**.
3. Choose **PNG format** and name it (e.g., `info-panel.png`).

**Important:** Avoid using PowerPoint’s file menu > Save As. That method won’t preserve transparency.![](99.System/Attachments/Screenshot-2025-05-11-131515.png)

---

##### 5: Add the Info Panel Image to Your Power BI Report

Now jump back into Power BI:

- Go to your report canvas.
- Insert the saved **PNG image**.
- Resize and align it to match the original layout.

You may notice faint borders—this is typical with PowerPoint exports. If precision is critical, consider using a tool like Photoshop for edge refinement.![](99.System/Attachments/Screenshot-2025-05-11-131737.png)

---

##### 6: Use Bookmarks and Buttons to Toggle Visibility

This is where the interactivity comes alive.

##### Create Bookmarks

1. With the image visible, open **Bookmarks pane**.
2. Create a bookmark called **“Info Panel Open”**.
3. Uncheck **Data** in bookmark settings to avoid altering visuals.
4. Hide the image and create a second bookmark called **“Info Panel Closed”**.

##### Add a Toggle Button

1. Insert a **blank button** on your report.
2. Set its fill to match your overlay color and adjust **transparency** (~57%).
3. On **hover**, set the transparency to 100% for a visual cue.
4. Set the **action type to Bookmark** → **Info Panel Open**.

##### Make the Info Panel Dismissible

- Select the info panel image.
- Turn on **Action** → set it to **Info Panel Closed**.
- This way, clicking the overlay hides it.![](99.System/Attachments/Screenshot-2025-05-11-131945.png)

---

##### Final Result: Smooth User Guidance

Now, users can click a button to reveal the info panel and click again to hide it. You’ve added guidance and clarity without redesigning the report—just smart layering and bookmarking.

---

##### Conclusion

Using PowerPoint, transparent PNGs, and Power BI bookmarks, you can create a polished, interactive **info panel** that boosts usability. Whether you’re guiding first-time users or surfacing advanced filters, this trick keeps things simple and stylish.

---

Want to go deeper into Power BI design techniques?  
[Check out Power BI Training from Data Bear](https://databear.com/power-bi-training/)