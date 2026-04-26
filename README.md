# ThaneJobs
ThaneJobs is a location-focused job portal designed specifically for the Thane region, connecting local employers with job seekers in a simple and efficient way. Employer can create jobs and Job seekers can filter and apply to jobs.

Setup 
1. Initial Django project setup
2. Add apps: accounts and jobs
3. Install and configure DRF

User and Auth
1. Create custom user model with roles (employer/jobseeker)
2. Configure JWT authentication
3. Add user registration API
4. Add login API with JWT

Models
1. Add Job model
2. Add Application model
3. Run migrations

APIs
1. Create serializers for Job and Application
2. Add Job CRUD APIs
3. Add Application APIs (apply to job)

Permission
1. Add custom permission for employer-only job creation
2. Restrict job update/delete to owner

Features
1. Add filtering and search for jobs
2. Add pagination
