# Bookstore.co.uk
A Django milestone project for Code Institute. This shop was created for the purpose to demonstrate both potential future employers and tutors skills acquired during my study at Code Institute. 

# Demo
A live demo can be found [here:](https://ksiegarnia77.herokuapp.com/)

# UX
The purpose of the website is selling books to customers.

A primary aim in creating the design was the simplicity of the form so that the users know how to use the shop without being instructed. The developer used as less as possible elements to obtain such an effect. Colours that the developer used are bright and give a nice contrast between sections. The website is divided into sections to meet user expectations, which are:
1.	As a user, I want to be able to get every part of the site so that I could discover content quickly.
2.	As a user, I want a home button, so that if I got lost, I could go back to the homepage. 
3.	As a user, I want to be able to view products so that I could decide what to buy.
4.	As a user, I want to be able to view product details of a given item so I could know more about it.
5.	As a user, I want to be able to see what is in the bag so that I know what items I added.
6.	As a user, I want to be able to register so that the shop could keep my details for future purcheses.
7.	As a user, I want a log in functionality so that I could login to the store and use previously saved personal information. 
8.	As a user, I want a confirmation email after registration so that I could be assured that I registered correctly.
9.  As a user, I want a reset password functionality so that if I forgot password I could retrieve it easily.
10. As a user, I want a function to store my personal information like order history, delivery address for future reference.
11. As a user, I want to sort product by category so that I could focus on particular types of product.
12. As a user, I want to purchase functionality so that I could add products to the bag.
13. As a user, I want a select quantity function so that I could add to the bag given quantity of the product.
14. As a user, I want to be able to adjust items in the bag so that I could change it when I want it.
15. As a user, I want an  order confirmation so that I know that my order is being processed correctly.
16. As an owner, I want to be able to add products to the site so that I could maintain new items.
17. As an owner, I want to be able to edit/update products in the shop so I could maintain them easily.
18. As an owner, I want to be able to delete the product, so that I could remove the item that is no longer available in the store.
20.	As a user, I want the website to have calm colours so that my eyes not get tired quickly.
21. As a user, I want to able to search the store so that I could find items which interest me.

 

# Technologies
- This project uses HTML, CSS, Javascript and Python programming languages.
- [Gitpod](https://gitpod.io/) - This developer used **Gitpod** for their IDE while building the website.
- [Bootstrap](https://www.getbootstrap.com/)
    - The project uses **Bootstrap4** to simplify the structure of the website and make the website responsive easily.
- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google fonts** to style the website fonts.
- [jQuery](https://jquery.com/)
    - The project uses **jQuery** to reference Javascript needed for the responsive navbar.
- [Popper.js](https://popper.js.org/)
    - The project uses **Popper.js** reference Javascript needed for the responsive navbar.
- [Django](https://www.djangoproject.com/)
    - The project uses **Django** to build the website application.
- [Heroku](https://www.heroku.com/)
    - The project uses **Heroku** to host the website.
- [Python](https://www.python.org/)
    - The project uses **Python** to build the website application.
- [AWS](https://aws.amazon.com/)
    - The project uses **AWS** to host static and media files.
# Features

- The site uses the navbar feature provided by the Bootstrap framework, which is responsive regardless of what device user use. 

- A login functionality for registered users.
- A registration functionality to register users.
- Add to the bag functionality to buy products.
- Remove from the bag functionality to adjust items in the bag.
- A search function that allows for finding items in the store.
- A validation quantity input that preventing user to add invalid values. 
- A function that shows last added books to the store.
- A function that shows nest rated books in the store. 


# Features left to implement

- A read more button for longer description texts.
- Webhooks for Stripe payment system. 



# Testing

The developer used **the W3C CSS Validation Service** and **W3C  Markup Validation Service** to check the validity of the website code.

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- [W3C Markup Validation]( https://validator.w3.org/)


**UX testing**
- As a user, I want to be able to get every part of the site so that I could discover content quickly.
    - The website is contained on a single website. The information provided is reasonably placed and well-sized. 
    - The Navbar occupies the whole width of the website.
    - In the upper part, there are links to login and register pages.
    - The Login and register links are separated from other parts of the navbar by the horizontal line.
    - Below them, there are the following elements:
        - Toggler icon on the left; when is clicked it shows all categories of the books.
        - Name of the bookstore; when is clicked it takes the user to the home page
        - Searchbar allowing customers searching the products.
        - Icon basket, when is clicked it takes the user to the bag page.
        - Information about the total price of items added to the bag. 
    - In mobile devices, register and login page are contained in toggler icon, avoiding the cluttering of the screen. 
    - Under the middle part of the navbar, there is a section with the names of the categories.

- As a user, I want a home button, so that if I got lost, I could go back to the homepage. 
    - The name of the bookshop is a link that takes the user to the main page. 

- As a user, I want to be able to view products so that I could decide what to buy.
    - The user has a few options to view the products:
        - On the front page, two sections are showing the newest and best-rated books.
        - In the navbar part, there are links to categories of the books.
        - On mobile devices, all categories sections appear; when is clicked it shows the table with the categories.
        - Toggler icon when is clicked it shows all the categories.
        
- As a user, I want to be able to view product details of a given item so I could know more about it.
    - Each card of the product takes the user to the detailed page of the given product.
    
- As a user, I want to be able to see what is in the bag so that I know what items I added.
    - In the right part of the browser, there is the bag icon; when is clicked it takes the user to bag page  

- As a user, I want to be able to register so that the shop could keep my details for future purchases.
    - There is a register button in the navbar and also in the footer. When is clicked it takes the user to the registration page.

- As a user, I want a login functionality so that I could log in to the store and use previously saved personal information.
    - Next to the register link there is login link, when clicked it takes the user to the login page.

- As a user, I want a confirmation email after registration so that I could be assured that I registered correctly.
    In the registration page, there is a registration form. When filled correctly confirms to the user and sends a confirmation email to the user.

- As a user, I want a reset password functionality so that if I forgot password I could retrieve it easily.
    - When the user forgot the password, he can reset it on the login page choosing forgot password button

- As a user, I want a function to store my personal information like order history, delivery address for future reference.
    - When the user is logged in, in the right corner of the navbar there is My Profile link that takes the user to his profile.
    - On the profile page he can:
        - Update his details
        - View order history   

- As a user, I want to sort product by category so that I could focus on particular types of product.
    - Under the main navbar, there are links to particular categories of the product
    - On mobile devices, all categories sections appear; when is clicked it shows the table with the categories.

- As a user, I want to purchase functionality so that I could add products to the bag.
    - Each card of the product has the add to bag button, when is clicked it adds the product to the bag.


- As a user, I want a select quantity function so that I could add to the bag given quantity of the product.
    - On the detailed page of the product, there is an input field, where customer can choose the required quantity. 

- As a user, I want to be able to adjust items in the bag so that I could change it when I want it.
    - In the bag view, there is a list of items added to the bag. 
    - Each item has an input field when the user can adjust the quantity or remove the item from the bag.

- As a user, I want an  order confirmation so that I know that my order is being processed correctly.
    - When the order is paid, the user receives the confirmation of the order with the summary of the order. 

- As an owner, I want to be able to add products to the site so that I could maintain new items.
    - When admin is logged in, there is Management Product dropdown in the navbar. From the dropdown, he has to click add product link that takes him to add product page where he can add products. 

- As an owner, I want to be able to edit/update products in the shop so I could maintain them easily.
    - When admin is logged in, each card contains the edit button. The edit button takes the admin to the edit page where he can edit the product. The delete button removes the product from the shop.    

- As an owner, I want to be able to delete the product, so that I could remove the item that is no longer available in the store.
    - When admin is logged in, each card contains remove button. The delete button removes the product from the shop.

- As a user, I want the website to have calm colours so that my eyes not get tired quickly.
    - The colour scheme used is easy on the eye. Cool colours are not tiring the eyes, giving a sense of peace to the user.

- As a user, I want to able to search the store so that I could find items which interest me.
    - In the middle of the navbar, the search bar is placed. The user can use it to find a product in the shop.


A website was manually tested on various mobile devices(iPhone5,6,7, Ipad, Samsung Galaxy, Sony Xperia) and multiple web-browsers (Chrome, Mozilla Firefox, Opera, Internet Explorer, Edge, Safari) to ensure compatibility and responsiveness. 





# Deployment
The website is published using hosting service Heroku taking files straight from a repository on GitHub. The site is updated automatically after new commits pushed.

### To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Log in to Heroku platform.
2. Click the New button.
3. Choose „Create new app”
4. Give it a name.
4. Choose the closest region.
5. Click „Create app button”
6. Click the Resources tab.
7. Find Heroku Postgress add-ons and provision it.

### In Gitpod environment:

1. Pip3 install dj-database-url
2. Pip3 install psycopg2-binary
3. Pip3 freeze > requirements.txt for Heroku

### In settings.py in Gitpod:

1. import dj_database_url

2. Replace default database settings:
~~~
DATABASES = {
    'default': dj_database_url.parse('Heroku database url')

}
~~~
3. The Heroku database url you can obtain from Config Vars in Settings in Heroku.

### Apply migrations for the database in Heroku and set the server

1. Python3 manage.py migrate
2. Load all the fixtures
    - Python3 manage.py loadddata -name of the fixture
3. Install gunicorn
    - Pip3 install gunicorn
4. Pip3 freeze > requirements
5. Create Procfile
    - In Procfile 
        - ```web: gunicorn ksiegarnia.wsgi:application```

6. In CLI:
    - ```Heroku login```
    -   ```Heroku config:set DISABLE_COLLECTSTATIC=1 --app ksiegarnia77```
     to prevent Heroku from collecting static files while deploying
7. In settings.py add:
    - ```ALLOWED_HOSTS = [‘ksiegarnia77.herokuapp.com’, ‘localhost’]```
8. Commit changes:
    - ```git add .```
    - ```git commit ```
    - ```heroku git:remote -a ksiegarnia77```
    - ```git push Heroku master```

### To automatically deploy when push to GitHub:
- In Heroku:
    - Click Deploy
    - Connect to Github
    - Find ksiegarnia repository
    - Click connect
    - Enable Automatic Deploys           


### To host static files images on S3:
1. Sign in to aws.amazon.com account
2. Find service S3
3. Create the bucket in S3
4. Give it a name
5. Secect the closest region
6. Uncheck block public access
7. Acknowledge that the bucket will be public
8. Click create bucket

### Set setting for a new bucket:
1. Choose the bucket
2. Click Properties tab
3. Static website hosting
4. Provide default values
5. Save

6. Click Permissions tab
7. CORS configuration:
 ~~~~<?xml version="1.0" encoding="UTF-8"?>
 <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
 <CORSRule>
 <AllowedOrigin>*</AllowedOrigin>
 <AllowedMethod>GET</AllowedMethod>
 <MaxAgeSeconds>3000</MaxAgeSeconds>
 <AllowedHeader>Authorization</AllowedHeader>
 </CORSRule>
 </CORSConfiguration>
~~~~
8. Save

9. Bucket policy tab
10. Click policy generator
11. Policy type S3: S3 Bucket Policy
12. Principal: *
13. Actions: GetObject
14. Copy ARN from Bucket Policy tab
15. Paste it to the input provided
16. Click Add statement
17. Click Generate policy
18. Copy the policy to the Bucket policy editor
19. Add after the ARN “ /* ”
20. Save
21. Go to Access Control List
22. In Public access click everyone
23. Select List objects
24. Save

### Create a user to access the bucket:
1. Use service Identity and Access Management
2. Open IAM service
3. Click Groups then Create New Group:
4. Give it a name ksiegarnia
5. Next, Next, Create a group
6. Then Policies:
7. Create a policy
8. Select JSON tab
9. Click Import managed policy
10. In the search bar type s3
11. Select AmazonS3FullAccess
12. Import
13. Copy ARN from Bucket Policy tab in S3
14. Add in “Resource”: ```[“ARN”,“ARN/*”]```
15. Click Review Policy
16. Give it a name ksiegarnia-policy
17. Create Policy

### Attach the policy to the created group:
1. Go to group
2. Click ksiegarnia
3. Click Attach policy
4. Search the policy just created: ksiegarnia policy
5. Select it and click Attach Policy

### Create user to put in a group
1. Click Users
2. Add user
3. Name it ksiegarnia-staticfiles
4. Select Programmatic Access
5. Click Next:Permission
6. Add user to the group
7. Click next till the end
8. Click create user
9. Download .csv file which contains users access key and secret access key

### Connecting Django to S3:
1. Pip3 install boto3
2. Pip3 install Django-storages
3. Pip3 freeze > requirements.txt
4. Add storages in installed apps in settings.py
5. In settings add:
    ``` if 'USE_AWS' in os.environ:

    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'ksiegarnia77'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/' ```

### In Heroku add env variables:
1. 'AWS_ACCESS_KEY_ID'
2. 'AWS_SECRET_ACCESS_KEY’
3. The values come from the  csv file we download earlier
4. USE_AWS = True
5. Remove DISABLE_COLLECTSTATIC variable

### Create custom_storages.py in the root directory
1. Inside:
    ```from django.conf import settings	 
  	from storages.backends.s3boto3 import S3Boto3Storage 
  	 	 
  	class StaticStorage(S3Boto3Storage):
	    location = settings.STATICFILES_LOCATION	 
  	class MediaStorage(S3Boto3Storage):	 
  	    location = settings.MEDIAFILES_LOCATION```
	 
### Commit changes
1. git add .
2. git commit
3. git push

### Preparing media folder on S3
1. Create Media folder in the bucket on S3 for media files
2. Upload all images
3. Next
4. Select Grant public read access to this object
5. Next
6. Upload

### Adding Stripe’s Publishing key and Secret key in Heroku as env variables.

1. In settings.py add
    - ```STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')```
    - ```STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '') ```



## Content
All images and descriptions were taken from Amazon.co.uk

## Acknowledgements
- The idea how create a sidebar was taken [here](https://www.w3schools.com/howto/howto_js_sidenav.asp).
- Remove and update buttons scripts were written by my tutor.
- Solution to place footer at the bottom was find [here](https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/).