# Chicago Business Intelligence (Docker Edition) 

Chicago Business Intelligence is a back-end program written by Python, which is deployed on Docker. This Program can grasp the data from the Chicago Government Website, and intelligently generate 7 reports.

## Programming and Enviornment
Python and Docker.

## File Structure
- Chicago
    - docker-compose.yml
    - Dockerfile1
    - Dockerfile2
    - geo_loc.xlsx
    - get_data.py
    - main.py
    - report_airport.py
    - report_alert.py
    - report_ccvi.py
    - report_construction.py
    - report_infra_investment.py
    - report_loan.py
    - report_streetcaping.py
    - requirements_1.txt
    - requirements.txt

## Build
1. There should be four containers, including:
    - chicago_business_intelligence_getdata
    - chicago_business_intelligence_report
    - postgresdb
    - pgadmin
2. We should make the four containers in docker-compose.yml, and set different ports for them(applications)
3. Notice, we should create Dockerfile1 for container1(chicago_business_intelligence_getdata) and Dockerfile2 for container2(chicago_business_intelligence_report).
4. In Dockerfile, we should COPY all the local files to the WORKDIR, and install the libraries, according to the requirements.txt and requirements_1.txt, then Run the get_data.py and main.py.
5. Till now, all the actions are written in the docker-compose.yml, and we just run the file, and get the result.


## Run
Because all the steps and actions are written in the docker-compose.yml, 
we just open the Windows PowerShell, and:
    Run docker-compose up
    
Then, we would get the results we want:
    the 4 images are installed...
    the 4 containers are installed...
    the get_data.py and main.py are running simultaneously and never stop, unless stop manully...
Notice, main.py will judge whether there are any data in database, if not, main.py will sleep 60 seconds and try again. And get_data.py will run every 24 hours.
