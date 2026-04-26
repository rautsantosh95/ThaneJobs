How to test in postman

1. Register employer

POST /api/register/

Body
{
  "username": "employer1",
  "password": "test1234",
  "is_employer": true
}

Create 2 users:
Employer (is_employer = true)
Jobseeker (is_employer = false)

2. Login → get token 

POST /api/token/
Body
{
  "username": "employer1",
  "password": "test1234"
}

will get
{
  "access": "access_token",
  "refresh": "refresh_token"
}
Copy access token
3. Create job 

POST /api/jobs/
Headers
Authorization: Bearer <employer_token>
Body
{
  "title": "---------",
  "description": "-------",
  "company": "-----",
  "location": "----",
  "salary": ---
}
4. List of Jobs (Public)

GET /api/jobs/

5. Login jobseeker 

POST /api/token/
Body
{
  "username": "jobseeker1",
  "password": "test1234"
}
Copy this token
6. Apply to job as jobseeker with token

POST /api/applications/apply/
Headers
Authorization: Bearer <jobseeker_token>
Body
{
  "job": 1
}
7. Viewed Applied Token

GET /api/applications/my_applications/