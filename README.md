# **Milestone 4: XELOR**

### **Project - Full-Stack Frameworks with Django - Code Institute.**
This is the fourth milestone project from CI with a focus on HTML, CSS, JavaScript, Python+Django, relational database(Postgres), stripe payments, and AWS. The point is to build a full-stack site based on business logic used to control a centrally-owned dataset. Also, to set up an authentication mechanism. XELOR is an e-commerce store for unisex luxury watches with brands like Omega, Rolex, Armani, and Gucci. 

A deployed link to the website can be found **[here](https://xelor-watches.herokuapp.com/)**.

![Mockup](readme/images/mockup.png)

## **Contents**
***
- [**User Experience (UX)**](<#user-experience-(ux)>)
  - [Project Goals](<#project-goals>)
  - [Importance and Feasibility chart](<#importance-and-feasibility-chart>)
  - [User Stories](<#user-stories>)
  - [Website Structure](<#website-structure>)
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

## **User Experience** (UX)
***

### **User stories**

* As a **user**, I want to be able to navigate through the whole site smoothly.
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
- As a **user**, I want to be able to read access a blog. 


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