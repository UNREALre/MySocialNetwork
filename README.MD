# Simple Social Network API. Test task.

## Basic information
Object if this task is to create a simple REST API. You have to use Django and DRF.

Basic models: User, Post.

Basic features: user signup, user login, post creation, post like, post unlike.

Optional: Implemented integrations with Clearbit for data enrichment and with Emailhunter for email validation.

## Technologies

Django, DRF, Requests.

## Installation
All you have to do is to rename env_db_example to .env.db and env_example to .env. After that configure that files with required data (for the testing purposes you can left everything as is).

After that run from the root of the project:
>docker-compose up -d --build

Project will be up and running on http://localhost:8009/

## API information
You can check all available methods in swagger auto generated document here: http://localhost:8009/swagger/

Also, you can use Postman collection with all methods: https://www.getpostman.com/collections/36569d33e3f8c54b76cc

## Testing
For test purposes there is a special bot here https://github.com/UNREALre/SocialNetworkBot that was also a part of this test task.