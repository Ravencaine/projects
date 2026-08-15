---
created: 2026-08-10
note_type: index
tags: [power-automate, index]
---

# Power Automate — Knowledge Base Index

| ## Patterns  (14 notes)

|| Note | Description |
||------|-------------|
|| [[VIP-Email-to-Teams-Alert-Flow]] | VIP email filter → adaptive card in Teams channel |
|| [[PDF-Form-Processing-to-SharePoint-Excel]] | AI Builder Form Processing → Excel table or SharePoint List |
|| [[Weekly-Status-Report-Aggregator]] | Recurrence → Adaptive Card form → SharePoint List or email draft |
|| [[Multi-Level-Document-Approval-Engine]] | SharePoint trigger → Approvals app → move file |
|| [[Email-Attachment-Archiver-to-SharePoint]] | Email attachments → SharePoint folders by date/sender |
|| [[Flagged-Email-to-Planner-Task]] | Flagged email → Microsoft Planner task → unflag |
|| [[Onboarding-Offboarding-User-Access-Flow]] | HR trigger → parallel branches: IT, Facilities, Payroll, Teams |
|| [[Stale-File-Cleanup-Bot]] | Monthly recurrence → Last Modified check → archive or notify |
|| [[Calendar-Deep-Work-Time-Blocker]] | Sunday recurrence → find 2hr+ gaps → Busy/Out of Office blocks |
|| [[Failed-Flow-Monitoring-Alerting]] | Power Automate Management → teams/SMS on flow failure |
|| [[Power-BI-DAX-Query-Data-Validation-Flow]] | Scheduled Recurrence → Run a Query against Dataset → Compose rules → Condition → Email/Teams alert |
||| [[Email-Keyword-Conditional-Send]] | Email trigger → keyword condition → extract table row → send conditional response |
||| [[PA-Finance-Report-Pipeline]] | 5-stage end-to-end PA pipeline: Collect → Process → Generate → Distribute → Monitor |
||| [[Template-Based-Report-Generation-PA-Excel]] | Populate Excel template with live processed data on schedule |
||| [[Dynamic-PowerPoint-Chart-Updates-via-PA]] | Update PowerPoint charts with latest data before distribution |

## References  (1 note)

|| Note | Description |
||------|-------------|
|| [[Performance-Analyzer-Visual-Query-Capture]] | Performance Analyzer → Copy query → DAX EVALUATE; DAX Query View for testing |
|| [[AI-Builder-Prediction-Approval-Routing]] | Dataverse row added → AI Builder Predict → 3-branch confidence routing (>0.7 auto-approve, 0.4–0.7 manager, <0.4 escalate) |
|| [[SQL-to-Report-End-to-End-Automation]] | SQL query → Excel export → VBA pivot → datetime filename → Outlook delivery; variables as objects through the chain |

## Workflows  (1 note)

||| [[Power-Automate-Flow-Design-Principles]] | Quality over complexity — pick 2 high-friction flows |
||| [[Data-Cleaning-Automation-PA]] | Remove duplicates + standardise date formats; guard null dates |

## Author Notes  (2 notes)

||| [[Author-Patricia-Udorji]] | Freelance finance analyst; PA for management reporting |
||| [[Automation-Frees-Analyst-Time-for-Deeper-Work]] | Automation shifts analyst role from data-wrangling to insight |

## Sources  (7 notes)

||| [[Source-Gunarathinam-Power-BI-Data-Validation]] | Gunarathinam M · 2024-09-18 · Medium |
||| [[Source-Kaklotar-10-Power-Automate-Flows]] | Rahul Kaklotar · 2026-07-22 · Medium |
||| [[Source-Belanger-Email-Processing]] | Denis Bélanger · 2024-06-08 · Medium |
||| [[Source-Arunachalam-AI-Builder-Approval]] | Tamilarasu Arunachalam · 2026-06-15 · Medium |
||| [[Source-Wedodo-Routine-Task-Automation]] | Wedodo · 2024-09-13 · Medium |
||| [[Source-Westendorp-Lightweight-Workflows-Power-BI-Automate]] | Jacob Westendorp · 2026-08-04 · Medium |
||| [[Source-Patricia-Udorji-PA-Finance-Reports]] | Patricia Udorji · 2024-07-28 · Medium |

## Patterns — Power BI + SharePoint Integration (Jacob Westendorp, 2026-08)

||| [[Lightweight-Workflows-Power-BI-Automate-Conceptual-Model.md]] | Power BI + Power Automate + SharePoint: Layered System Architecture |

Each tool has one clear job. Power BI anchors facts and defines the population. Power Automate reconciles. SharePoint captures mutable operational context. Core contract fields are fixed; status/ownership/notes are user-managed. Integration is additive — never overwrites source data. |

||| [[SharePoint-List-Sync-Orchestration-Pattern.md]] | SharePoint List Sync: Power Automate Orchestration Pattern |

Upsert loop: Get items → Apply to Each → update if ContractID exists in SharePoint, create if not. Idempotent: repeat runs are safe. Dedicated SharePoint view for Get items efficiency. Only Power BI-sourced fields are overwritten; user context preserved. |

||| [[Inactive-Record-Flag-Instead-of-Delete.md]] | Flag Fallen-Out-of-Scope Records Instead of Deleting Them |

When contracts drop out of the active scope, flag them rather than deleting. Curated SharePoint views separate active from inactive. Human reviews flagged records and decides retention. Keeps the active surface clean while preserving historical context. |

## Gotchas — JSON Schema (Jacob Westendorp, 2026-08)

||| [[Power-Automate-Parse-JSON-Schematization-Discipline.md]] | Parse JSON Schema: Validate Before Wiring Up Downstream Actions |

Power Automate Parse JSON: generate schema from a real sample payload. Validate one-to-one match with DAX SELECTCOLUMNS output before wiring downstream. Common issues: extra nesting, bracketed property names, type mismatches. Shift from implicit (DAX) to explicit (JSON schema) mindset is nontrivial. |

## Sources — Power Automate (Jacob Westendorp, 2026-08)

||| [[Source-Westendorp-Lightweight-Workflows-Power-BI-Automate.md]] | Designing Lightweight Workflows with Power BI and Power Automate |

DAX EVALUATE/SELECTCOLUMNS scoping; JSON schema discipline; SharePoint upsert sync loop; flag vs delete; bring data back into Power BI as secondary dataset. 2026-08-04. |


## Imported from Raindrop / Medium Reading List
- [[CHANGELOG|Changelog]]


## Imported from Raindrop / Medium Reading List
- [[approval-system-with-prediction-model-in-power-automate-e6ec7995d50b|Approval System With Prediction Model In Power Automate E6ec7995d50b]]
- [[automate-power-bi-building-intelligent-data-workflows-that-transform-business-in|Automate Power Bi Building Intelligent Data Workflows That Transform Business Intelligence 49793e266330]]
- [[automatic-process-on-power-automate-to-reduce-efforts-of-routine-tasks-e31a0306c|Automatic Process On Power Automate To Reduce Efforts Of Routine Tasks E31a0306cf3c]]
- [[built-power-automate-flow-just-to-remove-copy-paste-and-that-was-the-point-ba3c7|Built Power Automate Flow Just To Remove Copy Paste And That Was The Point Ba3c71632f99]]
- [[by-step-guide-to-creating-your-first-power-automate-flow-1813de9548c7|By Step Guide To Creating Your First Power Automate Flow 1813de9548c7]]
- [[comprehensive-guide-to-attaching-files-in-power-automate-approval-flows-0b43eb5a|Comprehensive Guide To Attaching Files In Power Automate Approval Flows 0b43eb5a937b]]
- [[connected-claude-mcp-to-power-bi-and-it-completely-changed-my-bi-development-wor|Connected Claude Mcp To Power Bi And It Completely Changed My Bi Development Workflow B405775bfb4d]]
- [[data-validation-in-power-bi-reports-using-power-automate-6deea7b04dbb|Data Validation In Power Bi Reports Using Power Automate 6deea7b04dbb]]
- [[do-look-after-my-power-automate-flows-aadb94ed5130|Do Look After My Power Automate Flows Aadb94ed5130]]
- [[excel-to-automation-how-eliminated-repetitive-tasks-with-power-automate-064a04ed|Excel To Automation How Eliminated Repetitive Tasks With Power Automate 064a04eda453]]
- [[goodbye-to-manual-hsse-reports-the-ultimate-automation-guide-with-power-automate|Goodbye To Manual Hsse Reports The Ultimate Automation Guide With Power Automate Powerbi And 644d2c29d1a6]]
- [[lightweight-workflows-with-power-bi-and-power-automate-a843e66d5906|Lightweight Workflows With Power Bi And Power Automate A843e66d5906]]
- [[log-tracker-using-power-automate-df587c872905|Log Tracker Using Power Automate Df587c872905]]
- [[microsoft-power-apps-power-automate-power-bi-created-real-business-impact-intell|Microsoft Power Apps Power Automate Power Bi Created Real Business Impact Intelligence In D90de13606a2]]
- [[of-power-automate-flow-efb88f-efb88f-efb88f-efb88f-e470115d77d|Of Power Automate Flow %ef%b8%8f %ef%b8%8f %ef%b8%8f %ef%b8%8f E470115d77d]]
- [[power-automate-ai-the-ultimate-productivity-setup-f225f275f7fd|Power Automate Ai The Ultimate Productivity Setup F225f275f7fd]]
- [[power-automate-flows-that-actually-save-hours-not-just-demos-78646527c0f3|Power Automate Flows That Actually Save Hours Not Just Demos 78646527c0f3]]
- [[power-automate-to-set-up-automated-email-reminders-in-sharepoint-134640a3121e|Power Automate To Set Up Automated Email Reminders In Sharepoint 134640a3121e]]
- [[power-automate-use-cases-08dd44f325f5|Power Automate Use Cases 08dd44f325f5]]
- [[power-bi-modeling-mcp-server-what-it-actually-means-for-your-bi-workflow-b7afe99|Power Bi Modeling Mcp Server What It Actually Means For Your Bi Workflow B7afe99eef80]]
- [[power-bi-with-power-apps-and-power-automate-using-sharepoint-list-e0e29612d29b|Power Bi With Power Apps And Power Automate Using Sharepoint List E0e29612d29b]]
- [[practical-workflow-for-building-better-power-bi-dashboards-with-chatgpt-and-copi|Practical Workflow For Building Better Power Bi Dashboards With Chatgpt And Copilot Ad9f2f65a0cd]]
- [[quarterly-financial-reporting-for-using-power-bi-and-power-automate-22b07300a706|Quarterly Financial Reporting For Using Power Bi And Power Automate 22b07300a706]]
- [[sensitive-data-in-power-automate-3f565a212584|Sensitive Data In Power Automate 3f565a212584]]
- [[task-flows-just-hit-ga-they-quietly-change-what-power-bi-report-actually-is-5ee6|Task Flows Just Hit Ga They Quietly Change What Power Bi Report Actually Is 5ee6c93de43d]]
- [[the-black-box-building-intelligent-error-handling-in-power-automate-5d1b8270e5ba|The Black Box Building Intelligent Error Handling In Power Automate 5d1b8270e5ba]]
- [[to-automate-csv-entries-to-sharepoint-list-in-power-automate-975f144405e3|To Automate Csv Entries To Sharepoint List In Power Automate 975f144405e3]]
- [[to-automatically-send-excel-reports-via-email-using-power-automate-4bb0304c0b7c|To Automatically Send Excel Reports Via Email Using Power Automate 4bb0304c0b7c]]
- [[to-build-your-first-power-automate-flow-step-by-step-9f3e411c4bf0|To Build Your First Power Automate Flow Step By Step 9f3e411c4bf0]]
- [[to-build-your-first-power-automatøùe-flow-step-by-step-9f3e411c4bf0|To Build Your First Power Automat}°­øùe Flow Step By Step 9f3e411c4bf0]]
- [[to-connect-excel-with-power-automate-step-by-step-guide-4d589adfa202|To Connect Excel With Power Automate Step By Step Guide 4d589adfa202]]
- [[to-convert-csv-to-excel-xlsx-in-power-automate-da0e40d9953d|To Convert Csv To Excel Xlsx In Power Automate Da0e40d9953d]]
- [[to-convert-excel-xlsx-files-to-csv-format-in-power-automate-and-logic-apps-d64a5|To Convert Excel Xlsx Files To Csv Format In Power Automate And Logic Apps D64a5ac61462]]
- [[to-design-custom-approval-buttons-in-outlook-email-using-power-automate-step-by-|To Design Custom Approval Buttons In Outlook Email Using Power Automate Step By Step Guide 7ff3e1b46c8e]]
- [[to-extract-data-from-power-bi-with-power-automate-55fe3d797913|To Extract Data From Power Bi With Power Automate 55fe3d797913]]
- [[to-get-started-with-microsoft-power-automate-5eb3e464172c|To Get Started With Microsoft Power Automate 5eb3e464172c]]
- [[to-get-started-with-power-automate-7a8ff3804c38|To Get Started With Power Automate 7a8ff3804c38]]
- [[to-merge-excel-files-in-power-automate-049430fc78b7|To Merge Excel Files In Power Automate 049430fc78b7]]
- [[to-stop-power-automate-errors-from-going-unnoticed-927fd1afe072|To Stop Power Automate Errors From Going Unnoticed 927fd1afe072]]
- [[to-trigger-flows-with-power-automate-button-246f6fec0702nlìù|To Trigger Flows With Power Automate Button 246f6fec0702¥nlìù]]
- [[to-trigger-flows-with-power-automate-button-246f6fec0702|To Trigger Flows With Power Automate Button 246f6fec0702]]
- [[to-use-the-search-rows-preview-action-in-power-automate-for-smarter-dataverse-qu|To Use The Search Rows Preview Action In Power Automate For Smarter Dataverse Queries 384363e07596]]
- [[up-your-automation-triggering-flows-with-conditions-in-power-automate-229c1317b1|Up Your Automation Triggering Flows With Conditions In Power Automate 229c1317b1de]]
- [[use-power-automate-as-finance-analyst-to-prepare-management-reports-904fd056b2b8|Use Power Automate As Finance Analyst To Prepare Management Reports 904fd056b2b8]]
- [[user-creation-with-power-automate-though-sharepoint-list-623c81249fe6|User Creation With Power Automate Though Sharepoint List 623c81249fe6]]
- [[workflow-with-power-automate-for-email-processing-2dfed29641ef|Workflow With Power Automate For Email Processing 2dfed29641ef]]
- [[your-data-workflow-how-power-automate-streamlines-power-bi-data-retrieval-dcc9d9|Your Data Workflow How Power Automate Streamlines Power Bi Data Retrieval Dcc9d904c045]]
- [[your-power-bi-report-into-power-automate-flows-b13e2b623aac|Your Power Bi Report Into Power Automate Flows B13e2b623aac]]
- [[what-are-ui-flows|What Are UI Flows]]
- [[automating-microsoft-forms-creation-ui-flows|Automating Microsoft Forms Creation (UI Flows + Selenium)]]
- [[creating-a-web-ui-flow-selenium-ide|Creating a Web UI Flow (Selenium IDE)]]
- [[ui-flows-limitations|UI Flows Limitations]]
- [[qr-code-generation-from-forms-url|QR Code Generation from Forms URL]]
[[CHANGELOG]]
