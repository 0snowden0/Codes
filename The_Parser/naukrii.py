from sqlalchemy import create_engine,Table,Integer,Column,String,text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
import requests
import bs4




engine = create_engine('postgresql+psycopg2://Prakash:pass123@localhost:5432/naukri')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

con = text("drop table if exists jobdetails;")
engine.execute(con)



class JobDetails(Base):
	__tablename__ = 'jobdetails'
	
	Slno = Column(Integer(), primary_key = True)
	Title = Column(String())
	job_id = Column(String())
	company_name = Column(String())
	jd_URL = Column(String())
	job_desc = Column(String())

Base.metadata.create_all(engine)




url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&k=python&l=bangalore&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong="
Header = {'appid':'109' , 'systemid':'109'}
response = requests.get(url , headers = Header)
data = response.json()
jobs = data['jobDetails']


for i in jobs:
	soup=bs4.BeautifulSoup(i['jobDescription'], 'html.parser')
	jd = str(soup.text)
	c = JobDetails(Title=i['title'],job_id=i['jobId'],company_name=i['companyName'],jd_URL = i['jdURL'],job_desc=jd)
	session.add(c)
	session.commit()
