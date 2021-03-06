# **Milestone 4: XELOR**

### **Project - Full-Stack Frameworks with Django - Code Institute.**
This is the fourth milestone project from CI with a focus on HTML, CSS, JavaScript, Python+Django, relational database(Postgres), stripe payments, and AWS. The project goal is to build a full-stack site based on business logic used to control a centrally-owned dataset. Also, to set up an authentication mechanism. XELOR is an e-commerce store for unisex luxury watches with brands like Omega, Rolex, Armani, and Gucci. 

A deployed link to the website can be found **[here](https://xelor-watches.herokuapp.com/)**.

![Logo](readme-images/readme_logo.jpg)

## **Contents**
***
- [**User Experience (UX)**](<#user-experience-(ux)>)
  - [User Stories](<#user-stories>)
  - [Importance and Feasibility chart](<#importance-and-feasibility-chart>)
  - [Design Choices from UXD](<#design-choices-from-uxd>)
    - [Color Scheme](<#color-scheme>)
    - [Images](<#images>)
    - [Typography](<#typography>)
  - [Wireframes](<#wireframes>)
  - [Design Changes](<#design-changes>)

- [**Features**](<#features>)
  - [Existing Features](<#existing-features>)
  - [Features left to implement](<#features-left-to-implement>)

- [**Database**](<#database>)

- [**Technologies**](<#technologies>)

- [**Testing**](<#testing>)

- [**Deployment**](<#deployment>)

- [**Credits**](<#credits>)

<br>

## **User Experience** (UX)
***

### **User stories**

* As a **user**, I want to be able to navigate through the whole site smoothly.
* As a **user**, I want to understand the purpose of the site upon loading it.
* As a **user**, I want the website to be responsive so that I can view the web pages 
<br> from my mobile, tablet, or desktop.
* As a **user**, I want to be able to return to the main site without having to use the browser buttons 
<br> so that I can easily return to the website if I navigate to a page that does not exist.
* As a **user**, I want to be able to contact the site owner.
- As a **user**, I want to be able to view a list of products so that I can select some to purchase.
- As a **user**, I want to be able to view individual product details so that I can identify the price, 
<br> description, and product image.
- As a **user**, I want to be able to access a blog. 


#### Registration and User Account
- As a **user**, I want to be able to easily register for an account so that I can have a 
<br> personal account and be able to view my profile.
- As a **user**, I want to be able to easily log in or log out so that I can access 
<br> my personal account information.
- As a **user**, I want to be able to easily recover my password in case I forget it so 
<br> that I can recover access to my account.
- As a **user**, I want to be able to receive an email confirmation after registering so that 
<br> I can verify that my account registration was successful.
- As a **user**, I want to be able to have a personalized user profile so that I can view my 
<br> personal order history and order confirmation.

#### Sorting and Searching
- As a **user**, I want to be able to sort the list of available products so that I can easily 
<br> identify the best-priced and categorically sorted products.
- As a **user**, I want to be able to sort a specific category of product so that I can find the
<br> best-priced product in a specific category, or sort the products in that category by name.
- As a **user**, I want to be able to search for a product by name or description so that I can 
<br> find a specific product I would like to purchase.
- As a **user**, I want to be able to easily see what I have searched for and the number of results 
<br> so that I can quickly decide whether the product I want is available.

#### Purchasing and Checkout
- As a **user**, I want to be able to easily select the quantity of a product when purchasing.
- As a **user**, I want to be able to view items in my bag to be purchased.
- As a **user**, I want to be able to easily enter my payment information so that I can check out quickly.
- As a **user**, I want to have my personal and payment information safe and secure.
- As a **user**, I want to be able to view an order confirmation after checkout.
- As a **user**, I want to be able to receive an email confirmation after checking out with order confirmation. 

#### Admin and Store Management
- As a **site owner**, I want to be able to add products to the store.
- As a **site owner**, I want to be able to edit/update a product.
- As a **site owner** I want to be able to remove products.
- As a **site owner** I want to be able to edit/update a blog post.
- As a **site owner** I want to be able to delete a blog post

#### [Back to top](<#contents>)

<br>

### **Importance and Feasibility chart**

**Opportunity/Problem** | **Importance** | **Viability/Feasibility**
| :--- | ---: | :---:
A. CRUD Functionality | 5 | 5
B. Postgress to store data | 5 | 5
C. Login Functionality | 5 | 5
D. Register Functionality | 5 | 5 
E. Logout Functionality | 5 | 5 
F. Showcase Products | 5 | 5 
G. Ability to search for products | 3 | 4 
H. Responsive design | 5 | 5 
I. Profile | 5 | 5 
J. Contact page, form, response, and sending an email.| 3 | 4 
K. Payment functionality| 5 | 5 
L. 404 and 500 pages | 3 | 5 
M. Navigation | 5 | 5 
N. Order and verification confirmation email | 4 | 4 

#### [Back to top](<#contents>)

<br>

### **What is needed now and in the future?**

* The developer wants an aesthetically pleasing and minimalistic website. This is to better showcase the main point: the watches. There will be a landing page to grab attention and options to log in or register to the site. The user has the option to browse the shop and buy products without being registered. But also get additional functions/services if the user has registered and logged in,

* The owner could have their needs and more by using a mobile-first approach to a fully responsive website which would allow for easy navigation, use, and no diminished experiences on all viewport sizes.

* Other features further down the line will give the website an even better user experience by incorporating: a rating/like-system to showcase the most popular watches from customers. Also, to include a comment section(with avatar images): where users can give feedback on individual watches but also on the blog posts. Including more product images to improve users' view and perspective of the products. 


#### [Back to top](<#contents>)

<br>

### **Design Choices from UXD**
***

The style is based on a minimalistic, readable, and contrasting design for easy flow and navigation, as well as maintaining consistency to allow the user to easily familiarise themselves with the website efficiently and intuitively.

#### [Back to top](<#contents>)

<br>

### **Color Scheme**
The general color scheme is white, red, grey and black. These colors will create a consistent style for the site. There are also other colors; from the hero image and product/blog images. 

![Color Scheme](readme-images/colorscheme.png)

<br>

### **Images**
The images are consistent of: 
1. Hero image from Unsplash.
2. Product and blog images which are taken from Omega, Rolex, Gucci and Armani websites and Unsplash.
3. Not Found search image, empty shopping bag, 404 and 500, made through Figma. 

<br>

### **Typography**
To keep a consistent and modern style, and for easy readability, the font used is Arial, and as backups; Helvetica and Sans-Serif.  

#### [Back to top](<#contents>)

<br>

### **Wireframes**
|Mobile|Tablet|Desktop|Designs|                         
|:-----:|:----:|:----:|:----:|
|[Mobile](readme-images/wireframes/wireframes-mobile.jpg)| [Tablet](readme-images/wireframes/wireframes-tablet.jpg)| [Desktop](readme-images/wireframes/wireframes-desktop.jpg)| [Designs](readme-images/wireframes/designs.jpg)

<br>

### **Design changes**

* No extra underneath the landing/home page, with blog, info etc. 
* Simplified shopping bag UX. 
* No subscribe to newsletter in Footer.
* No wish list feature.
* Changed Naw items: e.g from Rolex, Gucci, Armani to IWC Schaffhausen, Breitling and Patek Philippe.
* Search design got simplified, and also changed to an input form on larger screens instead of as a click on with animation. 
* Xelor copyright text from red to white color. 
* Discover more button changed to shop now on home page.
* Added a sort field and products home link and number of products.  

#### [Back to top](<#contents>)

<br>

## **Features**
***

### **Existing Features**

Included in the **website** is:

- **Navbar**: gives consistency and allows users to navigate the site easily and intuitively.
- **Xelor Logo**: allows users to go back to the Home page from any part of the page.
- **Home mobile**: allows users to go back to the Home page from any part of the page.
- **Omega, Rolex, Gucci, Armani**: allows users to see products for specific brands.
- **Contact**: allows users to contact the site owner.
- **Blog**: allows users to check out the site Xelor blog. 
- **Shopping Bag Icon**: allows users to access the Shopping Bag page from any part of the site.
- **Back to top button**: allows the user to go back to the top of the page when scrolling down.
- **Account/User Icon**: opens a dropdown that shows different features depending on the user type:
    - Anonymous users can see a ???Register??? and a ???Login??? link
    Registered users can see a ???My Profile???, and ???logout??? links
    Superusers can see the same ???My Profile???,  and ???Logout??? links. Including ???Product Management 
    - Add Product??? and ???Product Management - Add Blog Post??? 
    <br>

- **Footer**:
  - **Contact Us**: allows users to contact the site owner.
  - **Follow Us**: allows users to view the shop's (fake) social accounts.
  - **Copyright**:  showcase the owners of the site. 

### [Back to top](<#contents>)

**Home Page**:
  - **Landing image**: works as a call to action and includes a button for the users to go directly to the All Products page.

**Products Page**:
  - **Products Count**: shows the user how many products there are. If the user filters by category, it will show how many products there are in that specific category
  - **Filtering**: allows the user to filter the products by price, name, and category.
  - **Product**: each product has an image, name, size, and price so the user can quickly identify and find the product they are interested in. 
  If the user is a superuser, they will see an **Update link** and a **Delete link**.
 
**Product Detail Page**:
  - Each product page provides some information about and description  of the product:
    - **Product Name and Price**
    - **Size**
  - **Quantity button and add to bag**: allow the user to adjust the amount they want of this product and add it to their shopping bag
  - If the user is a superuser, they'll see an **Update link** and a **Delete link**.

**Bag Page**:
  - For each product, the shopping bag will show the following information:
    - **Product Image**
    - **Product Name and Price**
    - **SKU Number**
    - **Quantity Selected**
    - **Size Selected**
  - Besides this information, the user can adjust the **quantity** and also **delete** the product and see each products' **subtotal**
      - **Total**: allows the user to see the **Order Total**, the **Delivery Fee**, and the **Grand Total**
  - **Secure Checkout button**: allows the user to go to the **secure checkout page** to proceed with the payment. Alternatively, the user can click on the **Keep Shopping** button.

**Checkout Page**
  - **Order Summary**: for each product, it includes the product image, name, quantity, and subtotal.
  - **Total**: allows the user to see the **Order Total**, the **Delivery Fee**, and the **Grand Total**.
  - **Form**: allows the user to fill in the form with their name, email, phone number, address, town, county, postal code, and country. The user can save this information to their profile.
  - **Payment**: allows the user to fill in the form with their credit card details.
  - **Pay button**: allows the user to confirm the details and complete their order. Alternatively, the user can click on the **Adjust Bag** button and go back to the bag page.

**Checkout Success Page**
  - **Order Information**: this includes the order number, order date, order details, delivering details, and billing info.

**Profile Page**
  - **Default Delivery Information**: allows the user to save their delivery address so they don't have to type it in every time they purchase any products.
  - **Order History**: allows the user to keep track of their past orders.

#### [Back to top](<#contents>)

**Blog Page**
  - **Blog Post**: each product has an image and title. If the user is a superuser, they can update or delete the blog post directly on this page.

**Blog Post Page**
  - **Title**
  - **Author and Date**
  - **Image**
  - **Text**
  - **Back to Blog Button**: this allows the user to go back to the main blog page. 
  - If the user is a superuser, they'll see an **Update link** and a **Delete link**

**Register Page**
  - **Register form**: allows the user to register a new account by filling in the email, username, and password.

**Login Page**
- **Login form**: allows the user to login into their account.

**Logout Page**
- **Logout Confirmation button**: allows the user to log out from their account.

#### [Back to top](<#contents>)

<br> 

### **Restricted to Superusers**

**Add Product Page**
  - **Add Product form**: allows the superuser to add a new product to the shop.

**Edit Product Page**
  - **Edit Product form**: allows the superuser to update a product in the shop.

**Add Blog Post Page**
  - **Add Blog Post form**: allows the superuser to add a new post to the blog.

**Edit Blog Post Page**
  - **Edit Blog Post form**: allows the superuser to update a post in the blog.

**Error Pages**
  - **400, 403, 404, and 500 Error Pages**: allow the user to know more about the error and allow them to navigate back to the page easily.

#### [Back to top](<#contents>)
<br>

### **Features Left to Implement(Possible features)**
- Add pagination to the products page.
- Update the blog content to be more readable.
- Add a wishlist function and more to the profile.
- A rating/like-system to showcase the most popular watches from customers.
- Section(with avatar images): where users can give feedback on products and blog posts. 
- Including more product images to improve users' view and perspective of the products.

#### [Back to top](<#contents>)

<br>

## **Database**
***

![Database](readme-images/database.jpg)

<br>

**Security:**
Database connection details are for security reasons, set up in an [env.py](https://pypi.org/project/env.py/) and not uploaded to GitHub. This is to ensure that the database and connection details are not visible to users. In production, these are stored in Heroku.

#### [Back to top](<#contents>)

<br>

## **Technologies**
***

### **Languages**
* [HTML5](https://en.wikipedia.org/wiki/HTML5 "HTML5") - provides the content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "CSS3") - provides the styling.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) -provides interactivity and functionality.
* [Python](https://www.python.org/) - provides the back-end logic and the means to run/view the website.

### **Frameworks & Libraries**
* [Bootstrap](https://getbootstrap.com/) is used to create the layout of the project and some styling.
* [jQuery](https://jquery.com/) complements JavaScript.
* [Django](https://www.djangoproject.com/) is used to get rapid development and a clean, pragmatic design.
* [PostgresSQL](https://www.postgresql.org/) is the database used to store all the models in the production environment. 
* [SQLite](https://sqlite.org/index.html) is used as the database in the development environment.
* [AWS](https://aws.amazon.com/) is used to host media and static files on the cloud.
* [Stripe](https://stripe.com/) is used for payment handling.
* [Font Awesome](https://fontawesome.com/) is used to provide some icons.

#### Project Management
* [Git](https://git-scm.com/) is used for version control.
* [GitHub](https://github.com/) is used to host the project.
* [Heroku](https://www.heroku.com/) is used to deploy the app.
* [Gitpod](https://gitpod.io/) was used to develop the website.

#### Design
* [Figma](https://figma.com/ "Figma") - used to create the project's wireframes, designs, database and logo.
* [FavIcon](https://favicon.io/) -used for compressing logo into favIcons.
* [Unsplash](https://unsplash.com/) was used to get images for the project.
* [TinyJPG](https://tinyjpg.com/) - used to reduce image file sizes.
* [ILoveImages](https://www.iloveimg.com/) - used to reduce image file sizes.
* [Photopea](https://www.photopea.com/ "Photopea") - used to fix the product images.


#### Testing

* [Lighthouse](https://developers.google.com/web/tools/lighthouse) for performance review.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) -used to inspect page elements, test different CSS styles, debug issues, and responsiveness.
* [Responsive Design Checker](https://responsivedesignchecker.com/) -used to check responsiveness.
* [Chrome Plugin HTML Validator](https://chrome.google.com/webstore/detail/html-validator/mpbelhhnfhfjnaehkcnnaknldmnocglk/related) was used to check the HTML code for any errors.
* [W3C HTML Validator](https://validator.w3.org/) was used to check the HTML code for any errors.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check the CSS code for any errors.
* [JS Hint](https://jshint.com/) was used to check the JavaScript code for any errors.
* [PEP8](http://pep8online.com/) was used to check the Python code for any errors.



#### [Back to top](<#contents>)

<br>

## **Testing**
***

Test results can be found **[here](TESTING.md)**.

HTML Code must pass through the **[W3C HTML Validator](https://validator.w3.org/ "W3C HTML Validator")**.
* Used a Chrome Html Validator Plugin since WC3 was not working before submission. 

CSS Code must pass through the **[W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "W3C CSS Validator")**.

JavaScript Code must pass through the **[JSHint Validator](https://jshint.com/ "JSHint Validator")**.

Python Code must pass through the **[PEP8 Validator](http://pep8online.com/ "PEP8 Validator")**.

#### [Back to top](<#contents>)

<br>

## **Deployment**
***
### **Requirements** 
- Python3 
- Github account 
- Heroku account
- An IDE of choice 
- Stripe account
- AWS Amazon account
- Gmail account

<br>

### **Project Creation**
Navigate to the **[template](https://github.com/Code-Institute-Org/gitpod-full-template)** and click 'Use this template. Put in Repository name (velour) and check the Include all branches checkbox. Then navigate to the new **[repository](https://github.com/VTwin90/xelor)**.

The following commands were used for version control throughout the project:
+ ```git status``` (checks which files have been modified or added, and ready to be committed)
+ ```git add . ``` or ```git add <filename>``` (add all changed files or specific files within the project directory to be committed)
+ ```git commit -m "[TYPE] Reason"``` (commit changes to the local repository)
+ ```git push``` (push all committed changes to the GitHub repository)

#### [Back to top](<#contents>)

<br>

### **Deployment to Heroku**

<br>

**Create application:**
1. Navigate to Heroku.com and log in.
2. Click on the new button.
3. Select create a new app.
4. Enter the app name.
5. Select the region closest to you.

The live link for the site is here: **[https://vgames-app.herokuapp.com/](https://vgames-app.herokuapp.com/)**

<br>

**Set up the connection to Github Repository:**

1. Click the deploy tab and select GitHub - Connect to GitHub.
2. A prompt to find a GitHub repository to connect to will then be displayed.
3. Enter the repository name(xelor) for the project and click search.
4. Once the repo has been found, click the connect button.

<br>

**Add PostgreSQL Database:**

1. Click the resources tab.
2. Under Add-ons: search for Heroku Postgres.
3. Click on it when it appears.
4. Select Plan name Hobby Dev - Free.
5. Click Submit Order Form.

<br>

**Set environment variables:**

1. Click on the settings tab and then click reveal config vars.
2. Variables added:<br>

| KEY      | VALUE     |
  |----------------|---------------|
  | AWS_ACCESS_KEY_ID | `<aws access key>` |
  | AWS_SECRET_ACCESS_KEY | `<aws secret access key>` |
  | DATABASE_URL| `<postgres database url>` |
  | EMAIL_HOST_PASS | `<email password(generated by Gmail)>` |
  | EMAIL_HOST_USER| `<email address>` |
  | SECRET_KEY | `<your secret key>` |
  | STRIPE_PUBLIC_KEY| `<your stripe public key>` |
  | STRIPE_SECRET_KEY| `<your stripe secret key>` |
  | STRIPE_WH_SECRET| `<your stripe wh key>` |
  | USE_AWS | `True` |


*Please note the values for these variables depend on your setup. For security reasons, I will not add the values here.*

<br>

**Enable automatic deployment:**
1. Click the Deploy tab
2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

#### [Back to top](<#contents>)

<br> 

### **Hosting static and media files with AWS**
This project uses the AWS S3 bucket to host the static and media files. To host them you will need an account and create an S3 bucket and set a group, policy, and user in the IAM environment.

### **Create a local clone**
1. Open GitHub and navigate to the repository **[here](https://github.com/VTwin90/xelor)**.
2. Click the Code drop-down menu. 
3. Options: 
* Download the ZIP file, unpack locally and open with IDE.  
* Copy git URL from HTTPS dialogue box. 
4. Open your chosen IDE and open the terminal in a directory. 
5. Use the ```git clone``` command with the copied git URL after.
6. Clone of the project is created locally on your machine.

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:
> pip install -r requirements.txt


### **Fork Project**

1. Navigate to the GitHub Repository you want to **[fork](https://github.com/VTwin90/xelor)**.
2. On the top right of the page under the header, click the fork button.
3. Creates a duplicate of the full project in your GitHub Repository.

#### [Back to top](<#contents>)

<br>

## **Credits**
***

### **Code**

- This project was developed following the Boutique Ado project tutorial from [Code Institute](https://codeinstitute.net/). 
<br>The code was adapted to fit the purpose of this project.

General:
* https://www.w3schools.com
* https://css-tricks.com
* https://getbootstrap.com/
* https://developer.mozilla.org/
* CI Boutique Ado Tutorial

Back to top button code:
* https://mdbootstrap.com/docs/standard/extended/back-to-top/

<br>

### **Media & Content**

#### Hero Image
* https://unsplash.com/photos/WwJhYcX-pFI

#### Blog Posts and Images
* https://www.omegawatches.com/en-us/

#### Product Images and Descriptions:
* https://www.omegawatches.com/en-us/
* https://www.berrysjewellers.co.uk/

Logo and other images, as well as all other content, are owned by the site owner.

<br>

### **Acknowledgments**
I would like to thank my mentor **[Antonija ??imi??](https://github.com/tonkec)** for all help throughout our project calls.

Thanks to **[Daisy McGirr](https://github.com/Daisy-McG)** for letting me use her test template and structure for making my testing document.

Thanks to the **CI Slack Community** for feedback, motivation, and assistance. 

Thanks to tutor support for helping me with my contact form and general enquiries. 

Also, a thank you to my family and friends, who have helped me throughout this project with motivation, help, feedback, and testing.

**This project is for educational use only and was created for the Code Institute Module of Full Stack Frameworks with Django**

**Created by Vanja Torp 2022**

#### [Back to top](<#contents>)
