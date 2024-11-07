# OTJ Logger

## What is OTJ Logger?
The OTJ Logger is a GUI-based Python tool built using Tkinter and Python 3.8. If you're having trouble running it, try switching to a Python 3.8 interpreter.

## Why Use OTJ Logger?
As a DTS apprentice, I found filling out my OTJ logs manually quite time-consuming, especially when I missed a few weeks. This tool helps streamline the process!

## How Does OTJ Logger Work?
The OTJ Logger simplifies the process by allowing users to create multiple activity entries at once without needing to look up details like KSBs on Blackboard for each module. No more switching between Word documents, calendars, and Blackboard! Users can:

1. Select the dates they want to log.
2. Enter details such as time, duration, description, and module.
3. Use the **Report Generation** feature to create a Word document ready for uploading.

---

## Features

### The OTJ Logger
![Home](https://github.com/user-attachments/assets/155db89f-061b-4265-a2ef-8da660b6f5eb)

### Date Selection
![DatePicker](https://github.com/user-attachments/assets/bfd5837d-b3cb-4003-a819-825b54d53328)

### Activity Creation
- Enter and customize your activity entries quickly!
  
![Activity3](https://github.com/user-attachments/assets/2d564eb9-3f8d-4bbb-9a54-1d910591b2ae)
![Activity2](https://github.com/user-attachments/assets/2f413bc7-d31e-452f-ad14-d94d96138290)
![Activity1](https://github.com/user-attachments/assets/943f1575-a63d-4771-a5c1-a91cdae3f945)

### Viewing Created Activities _(Work in Progress)_
![ActivityList](https://github.com/user-attachments/assets/eed5eafc-7a6d-49a5-9f2c-be695e71524c)

### Report Generation
- Generate a complete Word document for your activities, ready for uploading.

![ReportGeneration](https://github.com/user-attachments/assets/98a67f3b-9de3-4a61-980a-651e5fc63f06)

### Example Report
![GeneratedReport](https://github.com/user-attachments/assets/89ed0ca6-3689-4f94-bf04-59511426480f)

### KSB Insights
- Unique selling point: gain insights on your progress with KSBs.

![KSBInsights](https://github.com/user-attachments/assets/0016b0b5-b938-4937-acbf-68621e8fa0d5)

---

## Considerations and Thoughts
- **University Formatting Requirements**: It's unclear if this format will meet the university's OTJ form requirements. The report template can be adjusted if items like a university logo are needed.
- **User Experience**: The tool may streamline the process depending on individual experience. Personally, I found the university-provided OTJ template to be prone to issues and time-consuming to edit, especially with many old entries.

---

## Important Information

### Customizing Modules and KSBs
You can add your own modules and corresponding KSBs by modifying the ENUM list in `services.py`:

![KSBList](https://github.com/user-attachments/assets/7c839a38-ec54-4b06-9595-24b541c90e6d)

### Updating Student Info
Update the Student ID and Name sections to match your own details in `services.py`:

![StudentInfo](https://github.com/user-attachments/assets/cb1797c7-ecc5-44f1-81ac-7ece0261f258)

---

## Contributing
This tool is a work in progress! If you have suggestions for improvement, please feel free to contribute by:
1. Making suggestions
2. Forking the repository and customizing it as you like

---

Thank you for using OTJ Logger! I hope this tool saves you time and effort.
