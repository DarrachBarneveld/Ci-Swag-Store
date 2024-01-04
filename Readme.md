# Book-Heaven-PP5
![BookHeaven website preview](./assets/readme-images/responsive.PNG)

[Link to deployed site](https://book-heaven-e537b3f88787.herokuapp.com/)
Book Heaven is an online book shop, built using Python, Django, HTML, CSS, JavaScript, Amazon S3 and Stripe. 


# Table Of Content

-   [User Experience](#user-experience)
    -   [User Stories](#user-stories)
    -   [Site Goals](#site-goals)
    -   [Scope](#scope)
-   [Design](#design)
    -   [Colour Scheme](#colour-scheme)
    -   [Database Schema](#Database-Schema)
    -   [Fonts](#Fonts)
    -   [Wireframes](#Wireframes)
    -   [Agile Methodology](#Agile-Methodology)
         -   [Overview](#overview)
         -   [EPICS(Milestones)](#epicsmilestones)
         -   [User Stories issues](#user-stories-issues)
         -   [MoSCoW prioritization](#moscow-prioritization)
         -   [GitHub Projects](#github-projects)
-   [Features](#features)
    -   [Navbar](#Navbar)
    -   [Footer](#Footer)
    -   [Home](#Home)
        -   [Hero Section](#hero-section)
        -   [Search Form](#search-form)
        -   [Product Card](#product-card)
    -   [Profile Page](#profile-page)
    -   [Sign In Page](#sign-in-page)
    -   [Sign Up Page](#sign-up-page)
    -   [Sign Out Confirmation](#sign-out-confirmation)
    -   [Password reset](#password-reset)
    -   [Password reset email sent](#password-reset-email-sent)
    -   [Enter a new password](#enter-a-new-password)
    -   [Password Reset Completed](#password-reset-completed)
    -   [Error Pages](#error-pages)
-   [Future Features](#future-features)
-   [Marketing](#marketing)
-   [Search Engine Optimization SEO](#search-engine-optimization-seo)
-   [Testing](#testing)
-   [Bugs](#Bugs)
-   [Technologies And Languages](#technologies-and-languages)
    -   [Languages Used](#languages-used)
    -   [Python Modules](#python-modules)
    -   [Technologies and programs](#technologies-and-programs)
-   [Deployment](#deployment)
    -   [Before Deployment](#before-deployment)
    -   [Deployment on Heroku](#deployment-on-heroku)
    -   [Creating A Fork](#creating-a-fork)
    -   [Cloning Repository](#cloning-repository)
-   [Credits](#credits)
    -   [Media](#media)
    -   [Code](#code)
    -   [Acknowledgements](#acknowledgements)
    -   [Comments](#comments)


## User Experience

### User Stories
1. As a developer I can setup a new Django project so that I can create the project's structure
2. As a developer I can connect database and media storage so that the user's stored data is stored successfully
3. As a developer I can deploy the application early so that I can confirm that the initial setup is working and can continue testing the application during development
4. As a User I can navigate through the website so that I can access different sections efficiently
5. As a user I can visit the home page so that I can identify the purpose of the website
6. As a user I want to be able to view a list of all available products in the bookshop so that I can browse and choose books to purchase
7. As a user I want to be able to view detailed information about a single product so that I can make an informed decision before purchasing
8. As a user I want to be able to refine the list of available products by selecting a specific category so that I can easily find books that match my interests
9. As a User I want to be able to view detailed information about a product's author, including their name, a short biography, and a list of books available for sale on the website so that I can learn more about the author and explore their other works.
10. As a User I want to be able to search for products in the bookshop by entering keywords so that I can quickly find specific books or topics of interest
11. As a User I want to be able to browse through a large list of products in the bookshop so that I can view all books in an organised way
12. As a an authenticated user I want to be able to add a review for a book product so that I can share my feedback and experiences with other potential buyers
13. As a user I want to be able to register an account so that I can have access to all functionality of BookHeaven.
14. As a user, I want to be able to log in to my account so that I can access my personalized features and make purchases on BookHeaven.
15. As a registered user I want to be able to reset my password so that I can regain access to my account in case I forget my password
16. As a registered user I want to be able to see my profile page so that I can update my information
17. As a authenticated user, I want to be able to save books to my wishlist so that I can revisit and consider purchasing them later on BookHeaven.
18. As a user, I want to be able to add products to my shopping cart so that I can conveniently review and purchase multiple items at once on BookHeaven.
19. As a user, I want to be able to remove products from my shopping cart so that I can adjust my order before making a purchase on BookHeaven.
20. As a user, I want to be able to adjust the quantity of products in my shopping cart so that I can control the quantity of items I want to purchase on BookHeaven.
21. As a user, I want to be able to apply discount codes to my orders so that I can enjoy savings and discounts on my purchases at BookHeaven.
22. As a user, I want to be able to securely make payments using Stripe so that I can complete my purchases on BookHeaven with confidence.
23. As an administrator, I want to have access to an admin dashboard so that I can monitor and view simple statistics related to the orders made on BookHeaven.
24. As an administrator, I want to be able to add new products to the website so that I can expand the product catalog on BookHeaven.
25. As an administrator, I want to be able to remove products from the website so that I can manage the product catalog on BookHeaven.
26. As an administrator, I want to be able to edit existing products on the website so that I can update and manage the product catalog on BookHeaven.
27. As an administrator, I want to be able to edit the stock levels of products so that I can manage inventory and ensure product availability on BookHeaven.
28. As a user, I want to be able to submit a testimonial about my overall experience with the website so that I can provide feedback and share my positive experiences on BookHeaven.
29. As a user, I want to be able to view testimonials submitted by other users so that I can read about the experiences and feedback of fellow users on BookHeaven.
30. As a website owner, I want to improve the website's search engine optimization (SEO) so that the website can rank higher in search engine results and attract more organic traffic.
31. As a user, I want to sign up for newsletters on the website so that I can keep up with updates and deals.
32. As a user I want to be able to sort the list of available products by name and price so that I can easily find books that match my interests
33. As a User I want to be able to complete the checkout process for my shopping cart so that I can purchase the items I've added to my cart
34. As a an authenticated user I want to be able to delete my reviews for a book product so that I can manage and maintain the accuracy and relevance of my feedback
35. As a an authenticated user I want to be able to edit my reviews for a book product so that I can manage and maintain the accuracy and relevance of my feedback

### Site Goals
1. To provide users with a place to purchase books of their interest.
2. To provide the users the ability to search and browse books and authors.
3. To provide the users with the ability to save books to their wishlist
4. To provide the users with the ability to check their order history.
5. To provide the users with the most recents titles on the market.
6. To provide the users with the ability to leave a feedback for books they have purchased.

### Scope
The project aims to develop an e-commerce website offering books to customers. The website will be responsive and user-friendly, providing the user with the ability to:
 - Register and Login
 - Reset Password
 - Browse, search and refine books for sale
 - Add books to shopping cart
 - Apply discount codes
 - View product stock levels
 - Update quantity in shopping cart
 - Delete items from shopping cart
 - Pay for items securely by using the integrated Stripe payment system
 - Save books to wishlist
 - Update personal information
 - View past orders

Key Features:

1. Initial Project Setup:
- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.
2. Products:
- Users can view books for sale and refine them by category and genre
- Users can sort products by price, title, genre or category
- Users can view details about each product including image, description, author, stock level and reviews
- Search products by title, author or description
- Registered users can leave reviews.
3. User Authentication:
- Users can register an account, allowing them access to all of the website's functionality.
- Registered users can login and access wishlist, reviews, past orders and saving personal details.
- Users can reset their password
- Users can add or remove items from their wishlist
4. Orders and checkout:
- Users can add items to their shopping cart
- Users can update the quantity of the items in the shopping cart
- Users can remove products from their shoppingcart
- Users can apply discount codes
- Users can use secure checkout functionality to pay for their items
5. Admin functionality:
The functionality in this section is limited to superusers or admins.
- Admins can access the admin dashboard, containing of a list of products and summary of orders and revenue.
- Admins can add products (books) for sale.
- Admins can delete products from the system.
- Admins can edit products and stock levels.
- Admins can access Orders section, where the order status can be updated.
- Admins can sort orders by status (In Progress, Completed, Cancelled)
- Admins can access the discount codes page, where codes can be created, deactivated or deleted.
6. Notification Messages:
Users will receive notification messages when performing CRUD operations, login/logout, and signup actions.

Benefits:

1. User-Centric Experience: The platform focuses on the user's needs, allowing efficient browsing and product purchasing.
2. Efficient Navigation: Users can easily navigate through different sections of the website for seamless access.
4. Effective Communication: Sending emails and notification messages features, enhances user interaction.

## Design
### Colour Scheme
The website harmoniously blends warm tones of light coral and red-orange with accents of light grey and white, all anchored by a cool grey undertone. This carefully curated color scheme establishes a sense of vibrancy and professionalism while ensuring a visually engaging experience for the users.
The main colours set as variables are

    1. --orange: #f58669;
    2. --dark-orange: #de502c;
    3. --white: #ffff;
    4. --brown: #63453d;
    5. --background: #ebeae5;
    6. --gray: #938c8c;

The below colours were used to compliment the main colours. Due to the fact that these colours have been used with very little repetition, there was no need to set them as variables
- #6f6a6a
- #2b221f
- #333
- #0d0d0d
- #888
- #97908e
- #eeebe3
- #8f8f8f
- #a5d9a5
- #f1f1f1
- #ff7a7a
- #cdc8c8
- #f0bc00
- #aab7c4
- #c7dbd2
- #eccccf
- #f2e8c5
- #dc3545
- #c5d7f2


![Colour Scheme](./assets/readme-images/colour-schema.PNG)
### Database Schema
![database schema](./assets/readme-images/database.png)

1. User:
The User model is part of Django Allauth. The model comes with predefined fields as standard. Some of them are username, email, name, password, and more. This model is used for user authentication, hence why changes directly to this model are not advisory. The User model is connected to the UserProfile model with one to one relationship.

2. UserProfile:
The UserProfile model is a custom custom-created model to handle the user profile details. Signals are used to reflect the changes between the User and UserProfile models.

3. Category
This model was created for the purpose of defining categories for the products

4. Genre
This model was created to add genre section for the products. It is connected to Category with a ForeignKey

5. Author
This model stores the infor for each author. It consist of name, image, bio and id.

6. Book
This is a custom product model. It is connected to Genre as a ForeignKey and author as ManyToManyField. This allows adding more than one author per book. In addition to that it has fields for handling stock. Stock_amount holds the integer value of the stock levels. In_stock is a Boolean field which sets the product to being in stock or not. A method called product_in_stock determines if a product is in stock based on the stock_amount value. The result of this method updates the in_stock boolean field. 

7. Wishlist
This model stores the books or products to a wishlist for authenticated users. It is connected to UserProfile and Book models as a ForeignKey

8. ProductReview 
This model stores the user's reviews for a product. It is connected to the UserProfile and the Book models as a ForeignKey

9. Order 
This model holds all the information of the user's order. It is connected to the UserProfile as a ForeignKey.

10. OrderStatus
This model is connected to the Order model with OneToOneField. When an Order is created a signal creates OrderStatus. The default value is 'in progress' with additional options of Completed and Cancelled. 

11. OrderLineItem
This model is connected to the Order and Book as a ForeignKey. It is created for each item in the order

12. DiscountCode
This model has no specified relationship to the other models. It contains three fields - code, discount and active. It allows the admin to create discount codes, determine the amount of a discount and if the code is active. 

### Fonts
In addition to Bootstrap 5 built in font family the below two fonts were used throughout the application
1. Poppins

![Poppins](./assets/readme-images/font-poppins.PNG)
2. Libre Baskerville

![Libre Baskerville](./assets/readme-images/font-libre-baskerville.PNG)

### Wireframes
- Home
<details>
<summary>Home</summary>

![Home](./assets/readme-images/home-wireframe.jpg)

</details>

- Product

<details>
<summary>Product</summary>

![product](./assets/readme-images/product-wireframe.jpg)

</details>

### Agile Methodology
#### Overview
This project was created using agile principles. As this is my second full-stack project, using agile, it was easier to identify the relevant milestones. Using the agile approach allowed me to plan all the features of the website through user stories. Each user story has acceptance criteria and tasks to clearly outline the requirements for each feature to be completed.

#### Epics(Milestones)
The user stories are grouped into eight EPICS or Milestones. An additional Milestone called Project Backlog was created to manage any additional features, bugs, or tasks that may arise during development.

![Milestones](./assets/readme-images/milestones.PNG)

#### User Stories Issues
The structure of the user story issue consists of the user story, acceptance criteria, and tasks that outline the steps that are required for this issue to be completed. During development where possible, the commit messages are connected to their corresponding issues.

![User Story](./assets/readme-images/user-stories.PNG)

![User Story](./assets/readme-images/commits.PNG)

#### MoSCoW prioritization
This prioritization technique was used to effectively prioritize the features and requirements of the project based on their importance. The acronym "MoSCoW" stands for "Must have, Should have, Could have, and Won't have." Each category helps categorize and prioritize features to guide the development process and ensure that the most critical elements are addressed first.

![MoSCoW](./assets/readme-images/moscow.PNG)

#### GitHub Projects
The project was created using a basic Kanban Board structure, divided into columns such as Todo, In Progress, Done, and Backlog. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow.

![Project](./assets/readme-images/agile-project.PNG)

## Features
#### Navbar
The navbar was built using bootstrap 5 and it is fully responsive. The search bar allows the users to search for products by keywords from any page of the website. The My Account drop down gives the user the option to log in or sign up. If the user is authenticated additional menu options are displayed like my profile and admin (if the user is a superuser). The shopping cart icon is a link to the shopping cart and it also displays the total of the items in the cart.
The nav links allow the user to refine the products by category, genre, special offers or to browse through the authors page, FAQ and about us. The is a dropdown for special offers which allows the user to see the new arrivals and deals.

![navbar desktop](./assets/readme-images/features/nav-desktop.PNG)

![navbar desktop](./assets/readme-images/features/nav-mobile.PNG)

![navbar desktop](./assets/readme-images/features/nav-open-mobile.PNG)

### Toasts
Toasts from Bootstrap were implemented to provide customers with feedback regarding their actions on the website.

![toasts](./assets/readme-images/features/messages.PNG)

### Breadcrumbs
The implementation of breadcrumbs allows users to keep track of their current location on the website. Breadcrumbs are present on most pages throught the website including the products pages. They are located on the top left corner of the page.

![breadcrumbs](./assets/readme-images/features/breadcrumbs.PNG)

#### Footer
The footer consist of links to social media, business address and useful links including about us, faq, privacy policy and the main product categories

![footer](./assets/readme-images/features/footer.PNG)

### Home Page
#### Hero Section
The hero section is the beginning of the whole customer's journey. That is why I made it a priority to create appealing hero section. 
The text on the left communicates the essence of BookHeaven, portraying it as a Dublin-based family business offering a diverse range of books for different audiences
The hero section image was designed using photoshop by combining images of book covers. The added shadows made the hero section blend well with the rest of the website.
This is then followed by call-to-action button Shop Now which invites the user to browse through the available products.

![hero section](./assets/readme-images/features/hero-section.PNG)

#### Trust Badges
The trust badges serve as visual indicators to reassure the visitors about specific aspects of the services available. Animation effect was added to the icons to make them more eye catching.

![trust badges](./assets/readme-images/features/trust-badges.PNG)

#### Products
The products displayed on the home page are the most recently added 8 products which are in stock.

![products](./assets/readme-images/features/products-home.PNG)

#### Newsletter
The users can sign up to a newsletter to recieve the most recent offers and discount codes. The form was integrated using MailChimp.

![newsletter](./assets/readme-images/features/newsletter.PNG)

### Products Page
The all books page renders all products to the user. They have the option to sort the products by title, price, genre and category. This page also displays the number of the products available. The pages, which refine the products by category or genre render the same template as all products, prefilled with the relevant data.
At the end of the products result there is pagination to help the user navigate easily through multiple pages of products

![pagination](./assets/readme-images/features/pagination.PNG)

![all products](./assets/readme-images/features/all-products.PNG)

### Products Card
The product card consist of an image of the book cover, title, author and price. When hovered over the add to cart button appears at the bottom and a heart at the top to add to favourites. If the product is on sale, then the old price will be displayed with line through, followed by the new price and a little label at the top of the image showing the percentage of the discount.

![product card](./assets/readme-images/features/card.png)

![product card sale](./assets/readme-images/features/card-sale.PNG)

### Single Products Page
On the page's left side, a product image is displayed. On the right side, the most important information about the product is displayed. This includes the title, author, publisher, reviews rating, price, stock levels, add to wishlist icon, and add to cart button with quantity dropdown. 
Implementing stock levels in the product model, allowed for adding custom logic when it comes to adding items to the cart. The user should not be able to add to their cart a higher quantity than the stock levels and this logic also needs to account for items already in the cart. If the user tries to add more than what is in stock an error message appears to notify that there is not enough stock to fulfill the order.
Below the top section, there is a section with tabs allowing the user to switch between description, details, and reviews. The reviews section allows an authenticated user to submit a review for a product. The overall rating is calculated and the number of starts are displayed in the top section of the page. Authenticated users can edit and delete their reviews from the same tab. 
The description tab includes a short description of the book which helps the users in making informed decision if they wish to purchase this book
The details tab includes some book information like ISBN number, number of pages, and language.

![product page](./assets/readme-images/features/single-product.PNG)

![reviews](./assets/readme-images/features/reviews.PNG)

![not enough stock](./assets/readme-images/features/not-enough-stock.PNG)

![add to wishlist](./assets/readme-images/features/add-to-wishlist.PNG)

### Edit review page
This page allows the user to edit their review in the event they changed their mind. It renders prefilled with the original data. 

![edit-review](./assets/readme-images/features/edit-review.PNG)

### Delete review confirmation
This page asks the user for confirmation if they wish to delete their review

![delete-review](./assets/readme-images/features/delete-review.PNG)

### FAQ Page
The FAQ page consists of the most frequently asked questions.

![faq-page](./assets/readme-images/features/faq-page.PNG)

### About Us Page
The About Us Page consists of a bookshop image followed by a short About Us description. Below that there is an embedded Google map with the location and contact details.

![about-us](./assets/readme-images/features/about-us.PNG)

### All Authors Page
This page allows the users to browse through the available authors on the website.

![all authors](./assets/readme-images/features/authors.PNG)

### Author Page
This page allows the user to learn more about the author and find other books by this author available on the system.
It consists of the author's image, name, short bio, and product cards with the books available.

![author](./assets/readme-images/features/author.PNG)

### My Profile Page
This section is accessible only to authenticated users.
This section contains three pages - my profile, my orders, and my wishlist

#### Profile
This page renders a form for the user's address and phone number. If the user has any details saved, it renders prefilled.

![profile](./assets/readme-images/features//profile.PNG)

#### Order History
This page displays the past orders of this user.

![orders](./assets/readme-images/features/order-history.PNG)

#### My Wishlist
This page displays the items in the wishlist

![wishlist](./assets/readme-images/features/my-wishlist.PNG)

### Admin
The admin section can be accessed only by admin or superuser. This section allows admins to manage stock, orders and discount codes without the need of the built in Django admin.
#### Dashboard
The dashboard offers a quick overview of the number of orders to date, the number of products in the system, and the total revenue to date.
Below that the admin is presented with a button to add products which leads to the product creation page. This is followed by a drop-down offering the ability to refine by stock with the options of in-stock, low-stock, or out-of-stock.
A table with all the products is displayed below showing the title of the product and general stats like price, reviews, on sale, and stock amount. The admin is also presented with the action buttons to edit and delete products.
The stock level field clearly indicates the level of stock by using green colour for in stock, yellow colour for low stock (items with 5 or under units), and red for items out of stock.

Admin dashboard:

![admin dashboard](./assets/readme-images/features/admin-dashboard.PNG)

Refine Products:
![refine products admin](./assets/readme-images/features/refine-products.PNG)

#### Add Products
This page renders the product creation form and all required fields to add an item to the database. Admins can add products on sale by checking the on-sale box and adding the sale price. If the on_sale box is not checked the product will display with the original price. The Author field allows for multiple authors to be selected. If the author's name does not exist in the list, it can be added by clicking on the add author link

![add products](./assets/readme-images/features/add-product.PNG)

#### Add author
This page renders the add author form. The required fields are name and bio. The image is not manadatory and if none is uploaded a generic image appears.
![add author](./assets/readme-images/features/add-author.PNG)

#### Edit Product
This page renders the product form prefilled with the existing data in the database. It allows the admin to modify the stock levels and any other details about the products.

![edit product](./assets/readme-images/features/edit-product.PNG)

#### Delete Product
![delete product](./assets/readme-images/features/delete-product-confirmation.PNG)

#### Orders Admin
The orders page in the admin section provides a breakdown of the order stats based on status.
Below that there is a drop-down offering the ability to refine by order status. The options are In Progress, Completed, Cancelled, and All.
Below that the orders are displayed in a table with the order number, date, amount of items, order total, and status. The status field clearly indicates the status of the order. The used colours are red for canceled, green for completed, and blue for in progress. The admin can edit the order status by using the pencil icon on the side of each row.

About the order status feature:
    The orders, when created have a default status of In Progress. When developing this feature the initial idea was to add a status field to the order model. This led to some issues with the form when making a purchase. After some investigation the error was related to the fact that this field is not rendered on the checkout page or handled when making a purchase, however in the model blank was set to False as default. By allowing blank to be True this resolved the submission issue. Later on in the development process, I came up with a better solution. The order status was created as a separate model, which is connected to the order with the One-to-one relationship. When an order is created, signals are used to create the OrderStatus. Separating the status from the order allows for easier manipulation of the status field without the need to handle the rest of the fields in the order.

Admin Orders;

![admin orders](./assets/readme-images/features/admin-orders.PNG)

Orders Refine:

![admin orders refine](./assets/readme-images/features/admin-orders-refine.PNG)

#### Edit Order Status
This page renders a one-field form with a drop-down. It allows the admin the select from the available status choices.

![edit order status](./assets/readme-images/features/admin-order-edit-status.PNG)

#### Admin Discount Codes
This page has similar layout to the orders and dashboard. It presents the admin with a breakdown of the number of discount codes on the system by status.
There is a button to create code which opens a modal with the creation form. The discount code consist of the code, the amount of the discount in percentage and a checkbox to determine if the code is active or not.
The discount codes can be editted and deleted from this section without the need of using Django admin.

Admin Discounts

![admin codes](./assets/readme-images/features/admin-codes.PNG)

Admin Refine Codes

![admin refine codes](./assets/readme-images/features/admin-code-refine.PNG)

Admin Add Code

![admin add code](./assets/readme-images/features/admin-code-add.PNG)

Admin Edit Code

![admin edit codes](./assets/readme-images/features/admin-code-edit.PNG)

Admin Delete Code

![admin delete codes](./assets/readme-images/features/admin-code-delete.PNG)

### Shopping Cart
The shopping cart can be accessed from the main nav menu. The shopping cart table section provides a clear and organized representation of the items added to the shopping cart. Each item has a small image, title, author, price, quantity, and subtotal. The users can upgrade the quantity or delete items from the cart with the help of the buttons provided.
On the right side, there is a section allowing the user to input discount codes and view their subtotal, delivery charges, and total. 

![shopping cart](./assets/readme-images/features/cart.PNG)
![shopping cart empty](./assets/readme-images/features/cart-empty.PNG)

##### Stock Quantity
Stock amounts have been implemented into the product model. Every time a user adds an item or updates quantity the shopping cart checks the quantity selected + the quantity of that item in the cart (if any) and compares it to the stock levels of the product. The user cannot add to the cart more items that there are in stock. 
In the event that another user purchases all units of a product while the product is sitting in another cart, when the user refreshes the page or continues to checkout, the item will be removed from their cart and an error message will be displayed letting them know that this item is not out of stock. In the event that 2 orders go through at the same time, the admin can cancel the status of the order and contact the customer for a refund. 

Trying to update quantity to levels above stock

![shopping cart no stock](./assets/readme-images/features/cart-no-stock.PNG)

##### Discount Codes
When an active discount code is applied to subtotal is calculated minus the percentage of the discount code. This excludes delivery fees. The discount amount is presented to the user and the total is updated. The code can be removed by clicking the remove button. A notification message is displayed to the user and the total price is adjusted accordingly.

![discount code success](./assets/readme-images/features/discount-code-success.PNG)

The error messages recognise invalid and not active codes as well. 

![discount code invalid](./assets/readme-images/features/discount-code-invalid.PNG)

![discount code inactive](./assets/readme-images/features/discount-code-inactive.PNG)

### Checkout
This page contains a form for the user's delivery and payment information and a summary of the user's order. If the user has an account, they can save their delivery information on their profile to automatically be filled in the checkout.
- The checkout Form
In the checkout the user can add their details and if they're logged in, can check the box to save their details for future transactions. Users must enter their payment information before completing the checkout and all payments are handled via Stripe.

- Order summary
A final summary of the user's order is shown containing all the user's basket items, quantity and subtotal for each item. The user can also see their order total, delivery costs, any discounts that have been applied and the grand total in the summary.

![checkout](./assets/readme-images/features/checkout.PNG)

### Order confirmation page
After the order has been completed, the user is redirected to a confirmation page containing a final rundown of the order and what the user purchased. This page can be accessed again from the user's profile if they have an account on the site by clicking the order number from the list of past orders.

![order confirmation](./assets/readme-images/features/order-confirmation.PNG)

### Confirmation email
Once the order is processed and payment has been received, the user will receive an email with the order details.

![email confirmation](./assets/readme-images/features/confirmation-email.PNG)

### User Authentication
The website uses django allauth's built in functionality which allows the users to register and log in securely. There is also a reset password functionality which allows the user to input their email address and recieve a link where they can securely reset their password.

## Future Features
- Add a pop up with the current discount code which can be updated by the admin.
- Make dinamic the genres displayed in the nav. Every time new genre is added to the database should automatically be added to the nav.
- Allow admin to update only stock level fields as a quicker option to restock items. 
- Send email to customers when their order changes status.

## Search Engine Optimization SEO and Marketing

### Business Model
The B2C (Business-to-Consumer) ecommerce model for this online bookshop operates as a platform catering to individual consumers looking to purchase a wide array of books conveniently from their homes. This model revolves around offering a selection of genres, ranging from fantasy, fiction, horror, automotive, cookery, computing, to niche categories, providing an accessible and user-friendly interface for browsing, selecting, purchasing, and receiving books.

The target customers for this online bookshop encompass diverse demographics, including keen readers, students, professionals, and individuals passionate about learning and leisure reading. The business aims to attract book enthusiasts seeking convenience, variety, competitive pricing, and an engaging shopping experience. 

### SEO
- Descriptive meta tags were added to the main template, including title, description and keywords.
- A sitemap was generated using [xml-sitemaps](https://www.xml-sitemaps.com/) This was generated using the deployed website. The file is included in the root level of the project.
- Robots.txt file was created at the root level of the project. This file tells the search engine crawlers which URLs they can access on the website.


### Marketing
- Newsletter is included in the home page. This section facilitates user engagement and promotes the e-commerce store through effective email marketing and social media presence.

- Facebook Page

[Book Heaven](https://www.facebook.com/profile.php?id=61554036458390)
![Facebook Page](./assets/readme-images/facebook-page.PNG)


## Testing
Testing documentation can be found [here.](TESTING.md)
## Bugs
|Bug|Status|
| ---| ---|
|[BUG: Total was calculated as integer #35](https://github.com/Dayana-N/Book-PP5/issues/35)|Closed|
|[BUG: Items can be added to cart even when they exceed the stock levels #36](https://github.com/Dayana-N/Book-Heaven-PP5/issues/36)|Closed|
|[BUG: When item is not on sale anymore the sale price is displayed #37](https://github.com/Dayana-N/Book-Heaven-PP5/issues/37)|Closed|
|[BUG: Error on checkout if the item's quantity has been updated #39](https://github.com/Dayana-N/Book-Heaven-PP5/issues/39)|Closed|
|[BUG: Genre doesn't display correctly on all products page #40](https://github.com/Dayana-N/Book-Heaven-PP5/issues/40)|Closed|
|[BUG: Discount code case sensitivity #43](https://github.com/Dayana-N/Book-Heaven-PP5/issues/43)|Closed|
|[BUG: Error when adding item to cart with quantity above stock level #44](https://github.com/Dayana-N/Book-Heaven-PP5/issues/44)|Closed|
|[BUG: Pagination URL #45](https://github.com/Dayana-N/Book-Heaven-PP5/issues/45)|Closed|


## Technologies And Languages

### Languages Used
- HTML
- CSS
- JavaScript
- jQuery
- Bootstrap
- Python
- Django

### Python Modules
- Boto3 is the Amazon Web Services (AWS) SDK for Python. It allows to interact with AWS services, such as S3

- dj-database-url - This library is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.


- django-storages - Django Storages is a collection of custom storage backends for Django, including support for storing files on remote services like AWS S3.

- django-widget-tweaks - Django Widget Tweaks is a package that simplifies working with form widgets and templates in Django

- gunicorn - Gunicorn is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

- Pillow - Pillow is a Python Imaging Library (PIL) fork that provides tools for working with images in various formats.

- psycopg2 - Psycopg2 is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

- s3transfer - S3 Transfer is a library for managing file transfers to and from Amazon S3 storage.

- whitenoise - Whitenoise is a middleware for serving static files directly from your Django application.
### Technologies and programs
 - [Favicon Generator](https://favicon.io/favicon-converter/) was used to generate Favicon
 - [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Git](https://git-scm.com/) was used as a version control software to commit and push the code to the GitHub repository.
- [Photoshop](https://www.adobe.com/ie/products/photoshop.html) was used for creating the mockup images of the website during planning stage.
- [Google Fonts](https://fonts.google.com/) was used to import fonts.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used during the testing of the website.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging and making the website responsive.
- [AWS](https://aws.amazon.com/) was used to store media files.
- [Stripe](https://stripe.com/en-ie) was integrated to handle payment processing in a secure and convenient way.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Js Hint](https://jshint.com/) was used to validate the JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.
- [Online Convert](https://image.online-convert.com/convert-to-webp) used to convert images to webp format
- [Coolors.co](https://coolors.co/) was used to display the colour scheme.
- [Box Shadow Generator](https://cssgenerator.org/box-shadow-css-generator.html) was used to generate the shadows


## Deployment
### Before Deployment
To ensure the application is deployed correctly on Heroku it is mandatory to update the requirements.txt. This is a list of requirements that the application needs in order to run.

- To create the list of requirements we use the command pip3 freeze > requirements.txt. This will ensure the file with the requirements is updated.
- Then commit and push the changes to GitHub.

! Before pushing code to GitHub ensure all credentials are in an env.py file, which is included in the .gitignore file. This tells Git not to track this file which will prevent it from being added to Github and the credentials being exposed.

### Stripe setup
- Log in to [Stripe](https://stripe.com/en-ie)
- Navigate to developers section (link located at the top right)
- Go to API keys tab and copy the values of PUBLIC_KEY and SECRET_KEY and add them to your env.py file
- Navigate to the Webhooks page from the tab in the menu at the top and click on add endpoint.
- This section requires a link to the deployed application. The link should look like this https://your_website.herokuapp.com/checkout/wh/ 
- Choose the events the webhook should recieve and add endpoint.
- When the application is deployed, run a test transaction to ensure the webhooks are working. The events chan be checked in the webhooks page.

### AWS setup
- Log in to [AWS](https://aws.amazon.com/)
1. Create a new S3 bucket:
- Choose the closest AWS region.
- Add unique bucket name.
- Under Object Ownership select ACLs enabled to allow access to the objects in the bucket.
- Under Block Public Access settings unselect block all public access as the application will need access to the objects in the bucket.
- Click on create bucket.
2. Edit bucket settings.
- Bucket properties
  - Open the bucket page.
  - Go to properties tab and scroll down to website hosting and click on edit.
  - Enable static website hosting
  - Under the Hosting type section ensure Host a static website is selected.
  - Add Index.html to index document field and error.html to error document field and click save.
- Bucket permissions
    - Navigate and Click on the "Permissions" tab.
    - Scroll down to the "CORS configuration" section and click edit.
    - Enter the following snippet into the text box and click on save changes.

    ```
    [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
    ]
    ```
    - Scroll to bucket policy section and click edit. Take note of the bucket arn (Example: arn:aws:s3:::test-bucket)
    - Click on policy generator and set the following settings:

        1. Select Type of Policy - S3 Bucket Policy
        2. Effect Allow
        3. Principal *
        4. AWS Service Amazon S3
        5. Actions: GetObject
        6. Amazon arn: your arn from the previous page

    - Click on add statement and then generate policy.Copy the policy
    - Paste the policy into the bucket policy editor.
    - Add "/*" to the end of the resource key to allow access to all resources in this bucket.
    - Navigate and Click Save changes.
    - For the Access control list (ACL) section, click edit and enable List for Everyone (public access) and accept the warning box. If the edit button is disabled, you need to change the Object Ownership section above to ACLs enabled (refer to Create Bucket section above).

3. Identify and Access Management (IAM)
- Create User group
    - In the search bar, search for IAM. 
    - On the IAM page select user groups in the menu on the left.
    - Click on create user group, add a name and click create group. The users and permission policies will be added later.
- Create Permissions policy for the user group
    - Go to Policies in the left-hand menu and click create policy
    - Click on actions and import policy.
    - Search for "AmazonS3FullAccess", select this policy, and click "Import".
    - Click "JSON" under "Policy Document" to see the imported policy
    - Copy the bucket ARN from the bucket policy page and paste it into the "Resource" section of the JSON snippet. Be sure to remove the default value of the resource key ("*") and replace it with the bucket ARN.
    Copy the bucket ARN a second time into the "Resource" section of the JSON snippet. This time, add "/*" to the end of the ARN to allow access to all resources in this bucket.

    ``````
        {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:*",
                    "s3-object-lambda:*"
                ],
                "Resource": [
                    "arn:aws:s3:::your-project",
                    "arn:aws:s3:::your-project/*"
                ]
            }
        ]
    }

    ``````


    - On the next page add polcity name and description and click create policy.

- Attach Policy to User Group
    - Click on User Groups in the left-hand menu.
    - Click on the user group name created during the above step and select the permissions tab.
    - Click Attach Policy.
    - Search for the policy created during the above step, select it and click attach policy.

- Create User
    - Click on Users in the left-hand menu and click on add user.
    - Enter a User name .
    - Select Programmatic access and AWS Management Console access and click next.
    - Click on add user to group, select the user group created earlier and click create user.
    - Take note of the Access key ID and Secret access key as these will be needed to connect to the S3 bucket.
    - To save a copy of the credentials click Download .csv


### Deployment on Heroku
- To deploy the project on Heroku, first create an account.
- Once logged in, create a new app by clicking on the create app button
- Pick a unique name for the app, select a region, and click Create App.
- On the next page select the settings tab and scroll down to Config Vars. If there are any files that should be hidden like credentials and API keys they should be added here. In this project, there are credentials that need to be protected. This project requires credentials added for:

        1. Django's secret key
        2. Database Credentials
        3. AWS access key 
        3. AWS secret key
        4. Email host password.
        5. Stripe public key
        6. stripe secret key
        7. Stripe wh secret

- Scroll down to Buildpacks. The buildpacks will install further dependencies that are not included in the requirements.txt. For this project, the buildpack required is Python
- From the tab above select the deploy section.
- The deployment method for this project is GitHub. Once selected, confirm that we want to connect to GitHub, search for the repository name, and click connect to connect the Heroku app to our GitHub code.
- Scroll further down to the deploy section where automatic deploys can be enabled, which means that the app will update every time code is pushed to GitHub. Click deploy and wait for the app to be built. Once this is done, a message should appear letting us know that the app was successfully deployed with a view button to see the app.
### Creating a fork
1. Navigate to the [repository](https://github.com/Dayana-N/Book-Heaven-PP5)
2. In the top-right corner of the page click on the fork button and select create a fork.
3. You can change the name of the fork and add description 
4. Choose to copy only the main branch or all branches to the new fork. 
5. Click Create a Fork. A repository should appear in your GitHub

### Cloning Repository
1. Navigate to the [repository](https://github.com/Dayana-N/Book-Heaven-PP5)
2. Click on the Code button on top of the repository and copy the link. 
3. Open Git Bash and change the working directory to the location where you want the cloned directory. 
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.

## Credits
### Media
- [Defaut avatar image](https://www.pngwing.com/en/free-png-azzyd)
- [Default product image](https://birkhauser.com/product-not-found.png)
- [Book Shop Image](https://pixabay.com/photos/books-bookstore-book-reader-985954/)
- [Logo](https://www.pngegg.com/en/png-znuhb)
- [Stripe Image](https://www.google.com/imgres?imgurl=https%3A%2F%2Fwheelsinspain.com%2Fwp-content%2Fuploads%2F2017%2F09%2Fstripe.png&tbnid=u2zXJc4_mGU7EM&vet=12ahUKEwjk9dKiqeqCAxVaX0EAHebLAH8QMygCegQIARBO..i&imgrefurl=https%3A%2F%2Fwheelsinspain.com%2Fpayment%2F&docid=BGGpjBgfFZahZM&w=432&h=200&q=cars%20accepted%20by%20stripe&ved=2ahUKEwjk9dKiqeqCAxVaX0EAHebLAH8QMygCegQIARBO)



### Code
- Boutique Ado Walkthrough was used for the base of this project
- [Styling django all auth pages](https://builtwithdjango.com/blog/styling-authentication-pages)
- [The right way to use Many To Many Field](https://www.reddit.com/r/django/comments/l937f1/the_right_way_to_use_a_manytomanyfield_in_django/)
- [Looping through integer in templates](https://copyprogramming.com/howto/how-do-i-loop-a-intergerfield-in-django-templates#how-do-i-loop-a-intergerfield-in-django-templates)
- [Product Card](https://bestjquery.com/tutorial/product-grid/demo199/) - the product cards were modified to suit the project
- [How to create automated tests](https://learndjango.com/tutorials/django-testing-tutorial)

### Acknowledgements
- Huge thank you to my mentor Ronan McClelland for all the help and resources.
- The Slack community and especially Indrek who listened to my struggles during development once again.
### Comments
I really enjoyed working on this project. My idea was to develop a real world application with user friendly design. I wish i had more time to add automated testing and to describe in detail the manual testing performed as I usually do. That will be added on a later stage.