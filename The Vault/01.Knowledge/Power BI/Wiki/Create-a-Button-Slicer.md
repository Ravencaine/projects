---
created: 2026-08-06
updated: 2026-08-06
source: Button Slicer Level Up Your Power BI Reports!
note_type: workflow
tags: [button-slicer, power-bi, slicer, new-card-visual]
---

# Create a Button Slicer

Enable interactive button-based filtering in Power BI using the New Card visual in slicer mode.

## Prerequisites

- Power BI Desktop (latest version)
- **Preview feature enabled:** File → Options → Preview features → tick "New card visual"

## Steps

1. **Enable the preview feature**  
   File → Options → Preview features → tick "New card visual"

2. **Add the New Card visual**  
   In the Visualization pane, locate the "New slicer" visual (actually a New Card visual) and drag it onto the report canvas.

3. **Select the field to filter by**  
   Right-click the visual → Format → Values → pick the data field to slice (e.g., product categories, regions, employee roles).

4. **Switch to slicer mode**  
   In the Format pane, ensure the visual is in slicer mode (not card mode).

5. **Choose a shape**  
   Size & Style → explore shape options → switch from default rectangle to rounded rectangle, ellipse, or custom shape.

6. **Apply color and styling**  
   Colors section → set button colors, borders, and gradients. Create visual hierarchy with subtle shades or make buttons pop with vibrant hues.

7. **Add images (optional)**  
   Call out values → Add data field → choose an image URL field from the data model.

8. **Apply conditional formatting (optional)**  
   Use conditional formatting to dynamically adjust button appearance based on data values (e.g., gold for top performers, faded for underperformers).

9. **Link to drill-through pages (optional)**  
   Configure button actions to link to other pages in the report for interactive drill-down experiences.

## Variations

- **Image button slicer:** Display product photos, country flags, or other images alongside text labels.
- **Color-coded slicer:** Use conditional formatting rules to highlight categories above/below thresholds.
- **Hover-effect slicer:** Dim image saturation on hover to provide subtle feedback on the selected button.

## Common Errors

- Image not displaying: ensure the column's **Data category → Image URL** is set in the model view.
- Slicer not filtering: confirm the field is added to the slicer's Field well, not just the visual.

## Related

- [[New-Power-BI-Slicer-Features]] — general new slicer capabilities
- [[Dynamic-Text-Titles-in-Power-BI]] — pair with dynamic titles for data storytelling
