---
title: "TMDL View on the web: Edit semantic models as code in your browser (Preview)"
source: "https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/TMDL-View-on-the-web-Edit-semantic-models-as-code-in-your/ba-p/5332653?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
published: 2026-08-10
created: 2026-08-13
description: "The wait is over! A few months ago, we shared that TMDL View on the Web was coming soon to preview. Now it’s here, bringing the code-first semantic"
Processed: "Unprocessed"
---
The wait is over! A few months ago, we [shared that TMDL View on the Web was coming soon to preview.](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/TMDL-View-on-the-Web-Preview/ba-p/5173917) Now it’s here, bringing the code-first semantic modeling experience directly to your browser.

With this capability, Power BI developers can script, modify, and apply changes to semantic model objects using the [Tabular Model Definition Language (TMDL)](https://learn.microsoft.com/analysis-services/tmdl/tmdl-overview?view=sql-analysis-services-2025) —a human-readable code format that describes your entire semantic model as code—without switching to Power BI Desktop or downloading model files.

## What is TMDL View on the Web?

TMDL View on the Web is a feature in Power BI that enables developers to view and edit semantic models as code directly in the browser using TMDL. It expands the Power BI web modelling experience by introducing a rich code editor for working with TMDL scripts—giving pro developers full transparency into the semantic model code and enabling more efficient workflows through code editing.

TMDL View was initially introduced in Power BI Desktop in January 2025 and became generally available in September 2025. Now, we’re bringing the same code-first modelling experience to published semantic models in the workspace—directly in your browser.

No downloads. No switching tools. Just seamless modelling on the web.

## Key capabilities and benefits of TMDL View on the Web

Whether you're investigating model metadata, making bulk updates, reusing model components, or recovering from mistakes, TMDL View on the Web helps keep advanced semantic modeling workflows inside the browser.

TMDL View on the Web provides the following capabilities:

### Explore your published semantic model metadata

Get full visibility into all objects and properties within your semantic model, including advanced properties not exposed in the standard UI.

To view the TMDL definition of any object, simply drag and drop it into the editor, or open the context menu and select “Script TMDL to Script tab” or “Script TMDL to Clipboard”.

This makes exploring and understanding your model structure faster and more efficient.

![Exploring published semantic model metadata in TMDL View on the Web by scripting the TMDL definition of an object, including advanced properties not exposed in the standard modelling UI](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357425iF9A92994E9248810/image-size/large?v=v2&px=999)

Exploring published semantic model metadata in TMDL View on the Web by scripting the TMDL definition of an object, including advanced properties not exposed in the standard modelling UI

### Enhanced development efficiency

TMDL View on the Web includes a modern code editor designed to boost productivity with built-in IntelliSense, multiline editing for bulk updates, search and replace capabilities and more. For example, you can use IntelliSense and multiline editing to assign a display folder to all Sales-related DAX measures in a single operation—reducing repetitive work and improving consistency.

You can also take advantage of AI-powered tools such as GitHub Copilot to assist with authoring TMDL scripts. For instance, you can script your model as TMDL, use an AI assistant to generate or modify code, and then paste it back into the editor to preview and apply changes—streamlining your modelling workflow even further.

![Using multiline editing and IntelliSense in TMDL View on the Web to assign a display folder across multiple measures in a single operation.](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357427i0D4C81A459167399/image-size/large?v=v2&px=999)

Using multiline editing and IntelliSense in TMDL View on the Web to assign a display folder across multiple measures in a single operation.

### Modify any semantic model property/object

Edit properties and objects directly in the browser—including advanced settings such as partition definitions or properties like isAvailableInMdx, which are not exposed in the standard modelling interface. This capability gives developers full control over their semantic models, enabling advanced configurations without relying on external tools or downloading the model.

![Editing isAvailableInMdx property in TMDL View on the Web, with a side-by-side preview showing the before-and-after impact on the TMDL definition.](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357428iF801D49A889CC7DA/image-size/large?v=v2&px=999)

Editing isAvailableInMdx property in TMDL View on the Web, with a side-by-side preview showing the before-and-after impact on the TMDL definition.

### Increased reusability and collaboration

Easily share and reuse semantic model objects by sharing TMDL scripts.

For example, to reuse a Calendar table from another semantic model or from a centralized gallery such as [TMDL gallery](https://community.fabric.microsoft.com/t5/TMDL-Gallery/bd-p/pbi_tmdlgallery), copy its TMDL script, paste it into your target model, preview the changes, and apply them.

![TMDL Gallery page showcasing a Calendar table shared as a reusable TMDL script for reuse across semantic models.](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357429iD7777BF32BE4A241/image-size/large?v=v2&px=999)

TMDL Gallery page showcasing a Calendar table shared as a reusable TMDL script for reuse across semantic models.

![Reusing a TMDL script from the TMDL Gallery by pasting it into another model in TMDL View on the Web, previewing the changes, and applying them.](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357430i7487DB7AC4B6C1FC/image-size/large?v=v2&px=999)

Reusing a TMDL script from the TMDL Gallery by pasting it into another model in TMDL View on the Web, previewing the changes, and applying them.

### Recover changes with version history

Edit with confidence knowing you can go back. Semantic models edited on the web are automatically configured with [*version* history](https://learn.microsoft.com/power-bi/transform-model/service-semantic-model-version-history), so you can recover from critical mistakes when editing your model. Directly from TMDL View on the Web, use File > Save to version history to capture a version, or File > Version history to review previous versions—each storing both the metadata and data of the semantic model—and restore an earlier one when needed.

![Accessing version history from the File menu in TMDL View on the Web to save and restore previous versions of a semantic model.](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357431iE3D1BB979C4F7A6B/image-size/large?v=v2&px=999)

Accessing version history from the File menu in TMDL View on the Web to save and restore previous versions of a semantic model.

## Get started

TMDL View on the Web makes it easier to explore, edit, and manage semantic models without leaving the browser. Whether you're making targeted metadata updates, reusing model components, or working through larger modeling changes, the new experience brings the flexibility of TMDL directly to the Power BI Service.

Get started today! Open a workspace, select a semantic model, and switch to the TMDL View to start exploring and editing your model as code. Explore the [Tabular Model Definition Language (TMDL)](https://learn.microsoft.com/analysis-services/tmdl/tmdl-overview?view=sql-analysis-services-2025) documentation for detailed guidance.

As this feature is in preview, we’d love to hear from you. Try it out and share your feedback in the comments section bellow —it helps us shape TMDL View on the Web as we move toward general availability.