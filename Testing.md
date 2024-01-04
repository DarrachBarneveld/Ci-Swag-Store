Go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#JavaScript)
    - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [User Story Testing](#user-story-testing)
- [Stripe](#stripe)

## Code Validation
### HTML
|Page|Validator|Result|
| --- | --- | --- |
| Home |![home](./assets/readme-images/testing/html/home.PNG) | <mark>PASS<mark> |
| All products |![products](./assets/readme-images/testing/html/products.PNG) | <mark>PASS<mark> |
| Authors |![authors](./assets/readme-images/testing/html/authors.PNG) | <mark>PASS<mark> |
| FAQ |![FAQ](./assets/readme-images/testing/html/faq.png) | <mark>PASS<mark> |
| about |![about](./assets/readme-images/testing/html/about.PNG) | <mark>PASS<mark> |
| product |![product](./assets/readme-images/testing/html/single-products.PNG) | <mark>PASS<mark> |
| author |![author](./assets/readme-images/testing/html/single-author.PNG) | <mark>PASS<mark> |
| privacy policy |![privacy policy](./assets/readme-images/testing/html/privacy-policy.PNG) | <mark>PASS<mark> |
| edit review |![edit review](./assets/readme-images/testing/html/review-edit.PNG) | <mark>PASS<mark> |
| delete review |![delete review](./assets/readme-images/testing/html/review-delete.PNG) | <mark>PASS<mark> |
| my profile |![my profile](./assets/readme-images/testing/html/my-profile.PNG) | <mark>PASS<mark> |
| my orders |![my orders](./assets/readme-images/testing/html/my-orders.PNG) | <mark>PASS<mark> |
| my wishlist |![my wishlist](./assets/readme-images/testing/html/my-wishlist.PNG) | <mark>PASS<mark> |
| admin dashboard |![admin dashboard](./assets/readme-images/testing/html/admin-dash.PNG) | <mark>PASS<mark> |
| admin add product |![admin add product](./assets/readme-images/testing/html/admin-add-product.PNG) | <mark>PASS<mark> |
| admin add author |![admin add author](./assets/readme-images/testing/html/admin-add-author.PNG) | <mark>PASS<mark> |
| admin edit product |![admin edit product](./assets/readme-images/testing/html/admin-edit-product.PNG) | <mark>PASS<mark> |
| admin delete product |![admin delete product](./assets/readme-images/testing/html/admin-delete-product.PNG) | <mark>PASS<mark> |
| admin orders page |![admin orders page](./assets/readme-images/testing/html/admin-orders.PNG) | <mark>PASS<mark> |
| admin order edit |![admin order edit](./assets/readme-images/testing/html/admin-edit-order-status.PNG) | <mark>PASS<mark> |
| admin discount codes |![admin discount codes](./assets/readme-images/testing/html/admin-codes.PNG) | <mark>PASS<mark> |
| admin edit code |![admin edit code](./assets/readme-images/testing/html/admin-edit-code.PNG) | <mark>PASS<mark> |
| admin delete code |![admin delete code](./assets/readme-images/testing/html/admin-delete-code.PNG) | <mark>PASS<mark> |
| order success |![order success](./assets/readme-images/testing/html/order-success.PNG) | <mark>PASS<mark> |
| shopping cart |![shopping cart](./assets/readme-images/testing/html/cart.PNG) | <mark>PASS<mark> |
| shopping cart empty |![shopping cart empty](./assets/readme-images/testing/html/cart-empty.PNG) | <mark>PASS<mark> |
| checkout |![checkout](./assets/readme-images/testing/html/checkout.PNG) | <mark>PASS<mark> |
| login |![login](./assets/readme-images/testing/html/sign-in.PNG) | <mark>PASS<mark> |
| sign out |![sign out](./assets/readme-images/testing/html/sign-outPNG.PNG) | <mark>PASS<mark> |
| sign up |![sign up](./assets/readme-images/testing/html/sign-up.PNG) | <mark>PASS<mark> |
| email confirmation |![email confirmation](./assets/readme-images/testing/html/verify_email.PNG) | <mark>PASS<mark> |
| email confirmation 2|![email confirmation](./assets/readme-images/testing/html/email-conf-2.PNG) | <mark>PASS<mark> |
| password reset 1 |![password reset ](./assets/readme-images/testing/html/pass-reset.PNG) | <mark>PASS<mark> |
| password reset 2 |![password reset ](./assets/readme-images/testing/html/pass-reset-enter-pass.PNG) | <mark>PASS<mark> |
| password reset 3 |![password reset ](./assets/readme-images/testing/html/pass-reset-email-sent.PNG) | <mark>PASS<mark> |
| password reset 4 |![password reset ](./assets/readme-images/testing/html/pass-reset-done.PNG) | <mark>PASS<mark> |

### CSS
|file|Validator|Result|
| --- | --- | --- |
| style.css |![style](./assets/readme-images/testing/style.PNG) | <mark>PASS<mark> |
| checkout.css |![style](./assets/readme-images/testing/checkout.PNG) | <mark>PASS<mark> |

## JavaScript
|file|Validator|Result|Comment|
| --- | --- | --- |----|
| admin_filter.js |![js](./assets/readme-images/testing/js/admin_filter.PNG) | <mark>PASS<mark> ||
| index page |![js](./assets/readme-images/testing/js/index.PNG) | <mark>PASS<mark> |This is mailchimp js script. It has 2 warning and 2 undefined variables|
| products.js |![js](./assets/readme-images/testing/js/products.PNG) | <mark>PASS<mark> ||
| stripe |![js](./assets/readme-images/testing/js/stripe.PNG) | <mark>PASS<mark> |This is Stripe js script. It has one undefined variable|
| toast.js |![js](./assets/readme-images/testing/js/toasts.PNG) | <mark>PASS<mark> ||

## Python

|File|App|Image|Result|Comment|
| --- |----| --- | --- |----|
| urls | Admin |![python](./assets/readme-images/testing/python/admin-url.PNG) | <mark>PASS<mark> ||
| views | Admin |![python](./assets/readme-images/testing/python/admin-views.PNG) | <mark>PASS<mark> ||
| urls | book_heaven |![python](./assets/readme-images/testing/python/book_heaven_urls.PNG) | <mark>PASS<mark> ||
| views | book_heaven |![python](./assets/readme-images/testing/python/book_heaven_views.PNG) | <mark>PASS<mark> ||
| bag_tools | Cart |![python](./assets/readme-images/testing/python/cart-bag-tools.PNG) | <mark>PASS<mark> ||
| context | Cart |![python](./assets/readme-images/testing/python/cart-context.PNG) | <mark>PASS<mark> ||
| test | Cart |![python](./assets/readme-images/testing/python/cart-test.PNG) | <mark>PASS<mark> ||
| urls | Cart |![python](./assets/readme-images/testing/python/cart-urls.PNG) | <mark>PASS<mark> ||
| views | Cart |![python](./assets/readme-images/testing/python/cart-views.PNG) | <mark>PASS<mark> ||
| admin | Checkout |![python](./assets/readme-images/testing/python/checkout-admin.PNG) | <mark>PASS<mark> ||
| apps | Checkout |![python](./assets/readme-images/testing/python/checkout-apps.PNG) | <mark>PASS<mark> ||
| forms | Checkout |![python](./assets/readme-images/testing/python/checkout-forms.PNG) | <mark>PASS<mark> ||
| models | Checkout |![python](./assets/readme-images/testing/python/checkout-models.PNG) | <mark>PASS<mark> ||
| signals | Checkout |![python](./assets/readme-images/testing/python/checkout-signals.PNG) | <mark>PASS<mark> ||
| urls | Checkout |![python](./assets/readme-images/testing/python/checkout-urls.PNG) | <mark>PASS<mark> ||
| views | Checkout |![python](./assets/readme-images/testing/python/checkout-views.PNG) | <mark>PASS<mark> ||
| webhook-handler | Checkout |![python](./assets/readme-images/testing/python/checkout-webhook-handler.PNG) | <mark>PASS<mark> ||
| webhooks | Checkout |![python](./assets/readme-images/testing/python/checkout-webhook-handler.PNG) | <mark>PASS<mark> |Warning line too long, it is part of the webhook so it was left as is|
| admin | discount_codes |![python](./assets/readme-images/testing/python/discount-code-admin.PNG) | <mark>PASS<mark> ||
| forms | discount_codes |![python](./assets/readme-images/testing/python/discount-code-forms.PNG) | <mark>PASS<mark> ||
| models | discount_codes |![python](./assets/readme-images/testing/python/discount-code-models.PNG) | <mark>PASS<mark> ||
| test | home |![python](./assets/readme-images/testing/python/home-tests.PNG) | <mark>PASS<mark> ||
| urls | home |![python](./assets/readme-images/testing/python/home-urls.PNG) | <mark>PASS<mark> ||
| views | home |![python](./assets/readme-images/testing/python/home-views.PNG) | <mark>PASS<mark> ||
| admin | products |![python](./assets/readme-images/testing/python/products-admin.PNG )| <mark>PASS<mark> ||
| forms | products |![python](./assets/readme-images/testing/python/products-forms.PNG )| <mark>PASS<mark> ||
| models | products |![python](./assets/readme-images/testing/python/products-models.PNG )| <mark>PASS<mark> ||
| test | products |![python](./assets/readme-images/testing/python/products-test.PNG )| <mark>PASS<mark> ||
| url | products |![python](./assets/readme-images/testing/python/products-urls.PNG )| <mark>PASS<mark> ||
| utils | products |![python](./assets/readme-images/testing/python/products-utils.PNG )| <mark>PASS<mark> ||
| views | products |![python](./assets/readme-images/testing/python/products-views.PNG )| <mark>PASS<mark> ||
| widgets | products |![python](./assets/readme-images/testing/python/products-widgets.PNG )| <mark>PASS<mark> ||
| admin | profiles |![python](./assets/readme-images/testing/python/profiles-admin.PNG )| <mark>PASS<mark> ||
| forms | profiles |![python](./assets/readme-images/testing/python/profiles-forms.PNG )| <mark>PASS<mark> ||
| models | profiles |![python](./assets/readme-images/testing/python/profiles-models.PNG )| <mark>PASS<mark> ||
| tests | profiles |![python](./assets/readme-images/testing/python/profiles-tests.PNG )| <mark>PASS<mark> ||
| url | profiles |![python](./assets/readme-images/testing/python/profiles-urls.PNG )| <mark>PASS<mark> ||
| views | profiles |![python](./assets/readme-images/testing/python/profiles-views.PNG )| <mark>PASS<mark> ||
| admin | reviews |![python](./assets/readme-images/testing/python/reviews-admin.PNG )| <mark>PASS<mark> ||
| forms | reviews |![python](./assets/readme-images/testing/python/reviews-forms.PNG )| <mark>PASS<mark> ||
| models | reviews |![python](./assets/readme-images/testing/python/reviews-models.PNG )| <mark>PASS<mark> ||
| url | reviews |![python](./assets/readme-images/testing/python/profiles-urls.PNG )| <mark>PASS<mark> ||
| views | reviews |![python](./assets/readme-images/testing/python/profiles-views.PNG )| <mark>PASS<mark> ||

## Responsiveness
During development the pages were created to be responsive from 320px and above. No specific breakpoint were used, instead I made sure that the content appears as it should on all sizes.

![responsiveness](./assets/readme-images/testing/responsive.PNG)

## Browser Compatibility

|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | PASS | --- |
| Firefox | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS | ---|

## Lighthouse

|Page|Validator|Result|
| --- | --- | --- |
| Home Desktop |![home](./assets/readme-images/testing/lighthouse/home-desktop.PNG) | <mark>PASS<mark> |
| Home mobile |![home](./assets/readme-images/testing/lighthouse/home-desktop.PNG) | <mark>PASS<mark> |
| products Desktop |![home](./assets/readme-images/testing/lighthouse/products-desktop.PNG) | <mark>PASS<mark> |
| products mobile |![home](./assets/readme-images/testing/lighthouse/products-desktop.PNG) | <mark>PASS<mark> |
| Profile Desktop |![home](./assets/readme-images/testing/lighthouse/my-profile-desktop.PNG) | <mark>PASS<mark> |
| Profile mobile |![home](./assets/readme-images/testing/lighthouse/my-profile-desktop.PNG) | <mark>PASS<mark> |
| checkout Desktop |![home](./assets/readme-images/testing/lighthouse/checkout-desktop.PNG) | <mark>PASS<mark> |
| checkout mobile |![home](./assets/readme-images/testing/lighthouse/checkout-desktop.PNG) | <mark>PASS<mark> |
| cart Desktop |![home](./assets/readme-images/testing/lighthouse/cart-desktop.PNG) | <mark>PASS<mark> |
| cart mobile |![home](./assets/readme-images/testing/lighthouse/cart-desktop.PNG) | <mark>PASS<mark> |
| admin Desktop |![home](./assets/readme-images/testing/lighthouse/admin-desktop.PNG) | <mark>PASS<mark> |
| admin mobile |![home](./assets/readme-images/testing/lighthouse/admin-desktop.PNG) | <mark>PASS<mark> |

## Manual Testing

## Manual Testing
- Home Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Navbar|Click on logo in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on the links in Navbar|Redirect to correct page |Pass|Navbar present on all pages |
||Click on the links in My Account|All redirect to correct page |Pass|Navbar present on all pages |
||Click on the cart icon| Redirect to shopping cart |Pass|Navbar present on all pages |
|Searchbar|type keywords|returns correct results |Pass|searchabar present on all pages |
|Hero section|Open Home page. Ensure the hero section loads as it should|Hero section loads as it should |Pass| |
|Hero section|Click on the shop now button, ensure it leads to products page|It leads to products page |Pass| |
|Listing Card| Click on the listing card. Ensure it redirects to the correct single product page |When clicked each card redirects to the correct single listing page |Pass| |
|| Click on the product card button add to cart. Ensure the item is added to cart |When clicked each card button adds the correspondint product to cart |Pass| |
|| Click on the product card button add to wishlist. Ensure the item is added to wishlist |When clicked each card button adds the correspondint product to wishlist |Pass| |
|Newsletter| Enter valid email. Ensure the thank you fo subscribing text appears |Pass| |
|Footer|Click on all of the social links in the footer. Ensure each external link opens the correct page in a new tab |All external links open the correct page in a new tab |Pass| |

- Products Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Pagination| Click on all of the links in the pagination. Ensure they redirect to the appropriate page. |All links redirect to the correct page. |Pass| |
|Pagination| Use the search bar to search products. Click on all of the links in the pagination. Ensure they redirect to the appropriate page displaying only the search results. |All links redirect to the correct page displaying the correct results. |Pass| |
|Sorting| Click on the select element and ensure that each sorting method returns the correct results |Each sorting method returns the correct results |Pass| |

- Single Product Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Product details|Open the product page. Ensure all the relevant information is correct for the specific product|All the relevant information is correct for the specific product|Pass||
|Save to favourites button|Click on the heart icon. Ensure the page reloads, a flash message is displayed with confirmation and the icon changes to full heart|When clicked the page reloads, a flash message is displayed with confirmation and the icon changes to full heart|Pass||
||As not authenticated user, Click on the heart icon. Ensure the page redirects to the login page|When clicked the page redirects to the login page|Pass||
||Click add to cart button and ensure the product is added to cart|When clicked the product is added to cart |Pass||
||Select higher quantity than in stock and click add to cart button and ensure an error message is displayed|When clicked error message is displayed not enough stock |Pass||
|Description|Select description tag and ensure description is displayed| description is displayed |Pass||
|details|Select details tag and ensure details is displayed| details is displayed |Pass||
|reviews|Select reviews tag and ensure reviews is displayed| reviews is displayed |Pass||
|reviews|As authenticated user fill in the form and add review. Observe if the reating is calculated correctly and the review appears on the page| the reating is calculated correctly and the review appears on the page |Pass||


- Shopping Cart 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Shopping cart|Add product to cart and ensure it appears correctly in the cart|The product appears correctly in the cart|Pass||
|Product|Click on product link and ensure it leads to the product page.|The link leads to the product page|Pass||
|Update quantity|From the drop down select new quantity and update. Ensure the total is calculated correctly|The product updates correctly in the cart|Pass||
|remove product|Click on the remove button and ensure the product is removed from cart|The product is removed from the cart|Pass||
|add discount|enter a valid discount code and ensure the total is calculated correclty|the total is calculated correclty and a message appears|Pass||
|add discount|enter a invalid discount code and ensure an error message displays and the total is unchanged|An error message displays and the total is unchanged|Pass||
|remove discount|After discount has been applied click on the remove button and ensure the total is calculated and a message appears|The total is calculated and a message appears|Pass||

- Checkout

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Checkout|Fill in the form and click on save details. Use stripe test card and confirm the order is successfull by checking stripe. Confirm the address is saved to profile|The address is saved to my profile. The purchase is successfull. Stripe logs show success.|Pass||
|Checkout|Visit the page as unauthenticated user. Ensure the form is not prefilled and does not allow to save details|The form is not prefilled and does not allow to save details.|Pass||
|Checkout|Click on back button and ensure it takes the user to the previous page|The back button work as it should.|Pass||

- My Profile

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Profile|Fill in the form and click on update. Ensure the details are updated|The details are updated|Pass||

- My Orders

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Orders|Open the orders page and ensure the orders showing are correct. |The orders are correct|Pass||
|Orders |Click on the order link and ensure it leads to the order page|The link leads to the order page|Pass||

- My Wishlist

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|wishlist|Visit my wishlist page. Click on the heart button on the card. Ensure the card is removed from favourites |The card is removed from favourites|Pass||
|wishlist|Visit my wishlist page. Click on the add to cart button on the card. Ensure the product is added to cart |The product is added to cart|Pass||
|wishlist|Visit my wishlist page. Click on the card. Ensure it redirects to the product's page. |It redirects to product's page|Pass||

- Admin

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Admin dashboard|Visit admin page. Ensure the refine drop down works by selecting all available options |The refine drop down works as expected|Pass||
|Admin dashboard|Click on the edit product button, ensure it redirects to the edit product page |it redirects to the edit product page|Pass||
|Admin dashboard|Click on the delete product button, ensure it redirects to the delete product page |it redirects to the delete product page|Pass||
|Admin dashboard|Click on the add product button, ensure it redirects to the add product page |it redirects to the add product page|Pass||
|Orders|Visit orders page. Ensure the refine drop down works by selecting all available options |The refine drop down works as expected|Pass||
|Orders|Click on the edit order button, ensure it redirects to the edit order page |it redirects to the edit order page|Pass||

|Discount code|Visit discount code page. Ensure the refine drop down works by selecting all available options |The refine drop down works as expected|Pass||
|Discount code|Click on the edit code button, ensure it redirects to the edit code page |it redirects to the edit code page|Pass||
|Discount code|Click on the delete code button, ensure it redirects to the delete code page |it redirects to the delete code page|Pass||
|Discount code|Click on the add code button, ensure a pop up with form appears to add code | A pop up with form appears to add code|Pass||



## Automated testing
Some automated testing was done to check if the pages return the correct response and template. Due to time limits there was no scope to expand.

## User Story Testing

|User Story|Screenshot|Result|
| --- | --- | --- |
| As a developer I can set up a new Django project so that I can create the project's structure | The project was set up successfully| <mark>PASS<mark>  |
| As a developer I can connect database and media storage so that the user's stored data is stored successfully | Database and media storage were connected successfully| <mark>PASS<mark> |
| As a developer I can deploy the application early so that I can confirm that the initial setup is working and can continue testing the application during development | The application was deployed after the initial set up to confirm everything is working as expected| <mark>PASS<mark> |
| As a User I can navigate through the website so that I can access different sections efficiently |![feature](./assets/readme-images/features/feature-desktop.PNG)| <mark>PASS<mark> |
| As a user I can visit the home page so that I can identify the purpose of the website |![feature](./assets/readme-images/home-page.PNG)| <mark>PASS<mark> |
| As a user I want to be able to view a list of all available products in the bookshop so that I can browse and choose books to purchase |![feature](./assets/readme-images/all-products.PNG)| <mark>PASS<mark> |
| As a user I want to be able to view detailed information about a single product so that I can make an informed decision before purchasing |![feature](./assets/readme-images/single-product.PNG)| <mark>PASS<mark> |
|As a user I want to be able to refine the list of available products by selecting a specific category so that I can easily find books that match my interests |![feature](./assets/readme-images/refine-products.PNG)| <mark>PASS<mark> |
|As a User I want to be able to view detailed information about a product's author, including their name, a short biography, and a list of books available for sale on the website so that I can learn more about the author and explore their other works. |![feature](./assets/readme-images/author.PNG)| <mark>PASS<mark> |
|As a User I want to be able to search for products in the bookshop by entering keywords so that I can quickly find specific books or topics of interest |![feature](./assets/readme-images/search.PNG)| <mark>PASS<mark> |
|As a User I want to be able to browse through a large list of products in the bookshop so that I can view all books in an organised way |![feature](./assets/readme-images/pagination.PNG)| <mark>PASS<mark> |
|As a an authenticated user I want to be able to add a review for a book product so that I can share my feedback and experiences with other potential buyers |![feature](./assets/readme-images/reviews.PNG)| <mark>PASS<mark> |
|As a user I want to be able to register an account so that I can have access to all functionality of BookHeaven. |![feature](./assets/readme-images/sign-up.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to log in to my account so that I can access my personalized features and make purchases on BookHeaven. |![feature](./assets/readme-images/sign-in.PNG)| <mark>PASS<mark> |
|As a registered user I want to be able to reset my password so that I can regain access to my account in case I forget my password |![feature](./assets/readme-images/password-reset.PNG)| <mark>PASS<mark> |
|As a registered user I want to be able to see my profile page so that I can update my information |![feature](./assets/readme-images/features/profile.PNG)| <mark>PASS<mark> |
|As a authenticated user, I want to be able to save books to my wishlist so that I can revisit and consider purchasing them later on BookHeaven. |![feature](./assets/readme-images/features/my-wishlist.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to add products to my shopping cart so that I can conveniently review and purchase multiple items at once on BookHeaven. |![feature](./assets/readme-images/features/card.png)| <mark>PASS<mark> |
|As a user, I want to be able to remove products from my shopping cart so that I can adjust my order before making a purchase on BookHeaven. |![feature](./assets/readme-images/cart-remove.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to adjust the quantity of products in my shopping cart so that I can control the quantity of items I want to purchase on BookHeaven. |![feature](./assets/readme-images/cart-remove.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to apply discount codes to my orders so that I can enjoy savings and discounts on my purchases at BookHeaven. |![feature](./assets/readme-images/discount_code.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to securely make payments using Stripe so that I can complete my purchases on BookHeaven with confidence. |![feature](./assets/readme-images/stripeintegration.PNG)| <mark>PASS<mark> |
|As an administrator, I want to have access to an admin dashboard so that I can monitor and view simple statistics related to the orders made on BookHeaven. |![feature](./assets/readme-images/features/admin-dashboard.PNG)| <mark>PASS<mark> |
|As an administrator, I want to be able to add new products to the website so that I can expand the product catalog on BookHeaven. |![feature](./assets/readme-images/features/add-product.PNG)| <mark>PASS<mark> |
|As an administrator, I want to be able to remove products from the website so that I can manage the product catalog on BookHeaven. |![feature](./assets/readme-images/features/delete-product-confirmation.PNG)| <mark>PASS<mark> |
|As an administrator, I want to be able to edit existing products on the website so that I can update and manage the product catalog on BookHeaven. |![feature](./assets/readme-images/features/edit-product.PNG)| <mark>PASS<mark> |
|As an administrator, I want to be able to edit the stock levels of products so that I can manage inventory and ensure product availability on BookHeaven. |![feature](./assets/readme-images/features/edit-product.PNG)| <mark>PASS<mark> |
|As a user, I want to be able to submit a testimonial about my overall experience with the website so that I can provide feedback and share my positive experiences on BookHeaven. || Won't Have |
|As a user, I want to be able to view testimonials submitted by other users so that I can read about the experiences and feedback of fellow users on BookHeaven. || Won't Have |
|As a website owner, I want to improve the website's search engine optimization (SEO) so that the website can rank higher in search engine results and attract more organic traffic.  |Descriptive meta tags were added to the main template, including title, description and keywords. A sitemap was generated using xml-sitemaps This was generated using the deployed website. The file is included in the root level of the project. Robots.txt file was created at the root level of the project. This file tells the search engine crawlers which URLs they can access on the website.| <mark>PASS<mark> |
|As a user, I want to sign up for newsletters on the website so that I can keep up with updates and deals. |![feature](./assets/readme-images/features/newsletter.PNG)| <mark>PASS<mark> |
|As a user I want to be able to sort the list of available products by name and price so that I can easily find books that match my interests |![feature](./assets/readme-images/product-sort.PNG)| <mark>PASS<mark> |
|As a User I want to be able to complete the checkout process for my shopping cart so that I can purchase the items I've added to my cart |![feature](./assets/readme-images/checkout.PNG)| <mark>PASS<mark> |
|As a an authenticated user I want to be able to delete my reviews for a book product so that I can manage and maintain the accuracy and relevance of my feedback |![feature](./assets/readme-images/delete-review.PNG)| <mark>PASS<mark> |
|As a an authenticated user I want to be able to edit my reviews for a book product so that I can manage and maintain the accuracy and relevance of my feedback |![feature](./assets/readme-images/edit-review.PNG)| <mark>PASS<mark> |

## Stripe
- Order created successfully

![order](./assets/readme-images/order.PNG)

- Stripe webhooks

![order](./assets/readme-images/webhooks.PNG)

- Stripe Events

![order](./assets/readme-images/events.PNG)