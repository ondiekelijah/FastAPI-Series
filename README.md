# FastAPI Series
[![Build and test code](https://github.com/Dev-Elie/FastAPI-Series/actions/workflows/github-actions.yml/badge.svg)](https://github.com/Dev-Elie/FastAPI-Series/actions/workflows/github-actions.yml)
### Video recordings & Presentation slides

1. [Introduction to building APIs](https://stdntpartners-my.sharepoint.com/:v:/g/personal/felix_orinda_studentambassadors_com/ET7sE6SxRZ5Pha-S2Cn8THUBNte7kt87FR0IsoRCbSUvFw?e=ix0YgM)
2. [Effective testing with Python and Pytest](https://stdntpartners-my.sharepoint.com/personal/felix_orinda_studentambassadors_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ffelix%5Forinda%5Fstudentambassadors%5Fcom%2FDocuments%2FRecordings%2FREST%20API%20Testing%20Using%20Python%2D20220204%5F200410%2DMeeting%20Recording%2Emp4&parent=%2Fpersonal%2Ffelix%5Forinda%5Fstudentambassadors%5Fcom%2FDocuments%2FRecordings)
- [Canva Slides](https://www.canva.com/design/DAE3G9Cc6C0/view?utm_content=DAE3G9Cc6C0&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)
4. [Introduction to CI/CD with GitHub Actions](https://stdntpartners-my.sharepoint.com/:v:/g/personal/ondiek_ochieng_studentambassadors_com/EcPFpKoFIjdBk2z6LPl0cl4BunBtYRxTd5DASGMSvgMdow?e=iOiebh)
- [Canva Slides](https://www.canva.com/design/DAE33Yc4y9s/Ghyh11R-Fm6obZUhqwr4Vw/view?utm_content=DAE33Yc4y9s&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)


### Set up & Installation

1. Navigate into your desired folder, then clone this repo as shown, remember the dot (.) so as to avoid duplicating this repo's name again.

   `git clone https://github.com/Dev-Elie/FastAPI-Series.git .`

2. Change to that specific directory

   `cd directory path`

3. Create a virtual environment & activate it

   **Windows**
          
   ```bash
   #create a venv
   py -3 -m venv venv
   # activate venv
   venv\Scripts\activate
   ```
          
   **macOS/Linux**
          
   ```bash
   #create a venv
   python3 -m venv venv
   # activate venv
   source venv/bin/activate
   ```
      
4. Install the requirements from the requirements.txt file.

   `pip install -r requirements.txt`


5. Start the server

   `uvicorn app.main:app --reload`
   
   
   
  
