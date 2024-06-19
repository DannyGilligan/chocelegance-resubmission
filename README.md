## Chocelegance

![hero image](documentation/readme-hero-image.webp)

<br>
<br>
<br>

## Table of Contents

* [Introduction](#introduction)
* [Business Overview](#business-overview)
* [Design](#design)
* [Features](#features)
* [User Stories](#user-stories)
* [Manual Testing](#manual-testing)
* [Deployment](#deployment)
* [Technologies Used](#technologies-used)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)



<br>
<br>

## Introduction

Chocelegance is the 5th and final project submission as part of the Code Institute DIploma in Full Stack Software Development.
<br><br>
The project is an e-Commerce platform that allows an artisan chocolatier to sell hand crafted chocolates for customers with specific dietary requirements (such as Keto, Vegan and Gluten-Free).
<br><br>
The features include the ability to make purchases directly from the site, registering a user profile, user email verification, generating email confirmations upon successful purchases, user ratings and reviews, displaying testimonials and frequently asked questions, security protocols preventing access to unauthorised views/pages and CRUD functionality for superusers.
<br><br>
The site was built using the Django framework, Python, HTML 5, CSS 3, Javascript, Bootstrap, Heroku, ElephantSQL, Stripe and AWS.
<br><br>
A link to the deployed site can be found [here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/).
<br><br>
A link to the admin panel of the deployed site can be found [here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/admin) (credentials provided in submission form).


<br>

[Back to Top](#chocelegance)

<br>
<br>
<br>

## Business Overview

An overview of the business model, competitors, SEO and marketing strategy is included below.

<details>
  <summary><b> Business Model </b></summary>
<br>

Chocelegance is an online B2C operation offering hand crafted, diet friendly chocolates to customers with specialised dietary requirements.
<br><br>
The business is operated by a sole artisan chocolatier who has a passion for the nuances involved in fine chocolate making, and wants to share this passion with a niche set of customers that are not well served by the current offerings on the market.
<br><br>
A typical customer persona is a chocolate lover who wants to experience the rich taste of hand made chocolates, but needs to stay within a strict set of dietary parameters.
<br><br>
The business is currently at a small scale, with limited inventory being kept on hand. Chocolates will be made to order, as demand grows, a more sophisticated inventory management system will be implemented to faciliate scalable growth.
<br>
<br>
<br>
</details>


<details>
  <summary><b> Competitors </b></summary>
<br>

There are several chocolate makers in the Netherlands with an online presence and established customer base. These are well entrenched competitors with diverse product ranges. Some examples are listed below:
<br>

[Vanroselen](https://www.vanroselen.nl/)
<br>

[Ganache](https://www.ganacheamsterdam.com/)
<br>

[Artichoc](https://artichoc.nl/)
<br>

[Candela](https://chocolade-versturen.nl/)
<br>

[Puccini](https://puccinibomboni.com/)
<br><br>
All of these competitors offer high quality chocolates, however, they do not target customers with specific dietary requirements exclusively. The goal of Chocelegance is to capture this segement of the market and focus exclusively on serving their needs.
<br><br>
Of the competitors listed above, [Puccini](https://puccinibomboni.com/) has been used as a source of inspiration for the Chocelegance site. The images and descriptions present on their site have been used for the purposes of this project, the chocolate images and names have been fully customised for the project, however the chocolate descriptions and the text in the about page are almost entirely a direct copy from their site.
<br><br>
All images used have been credited in the credits section.
<br>
<br>
</details>

<details>
  <summary><b> Keyword Research </b></summary>
<br>

A list of broad general topics relevant to the business was created, then lists of short-tail and long-tail keywords were created and reviewed.
<br><br>
These keywords were then rationalised to remove any that Chocelegance would not have any authority on.
<br><br>
The remaining keywords were then checked in [wordtracker.com](https://www.wordtracker.com/) for relevance, see screenshot below.
<br><br>

<table>
<tr>
<td>

![keyword research](documentation/keyword-research.webp)
</td>
</tr>
</table>
<br>

An example of the keyword research on [wordtracker.com](https://www.wordtracker.com/) is shown below.
<br><br>

<table>
<tr>
<td>

![keyword research](documentation/word-tracker-example.webp)</td></tr></table>
<br>
<br>
<br>
</details>

<details>
  <summary><b> SEO Improvements </b></summary>
<br>
The keywords identified during the research stage have been incorporated throughout the site (e.g in headings, product descriptions, between strong tags etc).
<br><br>
An example is the hero section, which includes an SEO optimised heading and button containing keywords in an organic manner (as opposed to stuffing, or keyword spamming).
<br><br>
<table>
<tr>
<td>

![seo hero example](documentation/seo-hero-example.webp)
</td>
</tr>
</table>
<br>
The SEO keywords have been included in the head of the base.html file, in the <b>'keywords'</b> and <b>'description'</b> meta tags to further improve the SEO aspect of the site.
<br><br>

![seo-meta-tags](documentation/seo-meta-attributes.webp)
<br>
<br>
A <b>sitemap.xml</b> file has been included in the root directory of the project that will allow search engine spiders to identify and crawl through the site's pages.
<br>
<br>
A <b>robots.txt</b> file has also been added to the root directory of the project that will define what areas of the site are accessible to search engine spiders.

<br>
<br>
<br>
</details>

<details>
<summary><b> Marketing </b></summary>
<br>
As Chocelegance is currently a small operation, the preference is to leverage cost-effective marketing strategies that are suitable for a limited budget.
<br><br>
The marketing strategy will initially include a newsletter subscription, and a Facebook page. Content will be published on a weekly basis, with the goal of creating rich and engaging media that has the potential to be organically 'shareable' on social media.
<br><br>
<details>
<summary> <i>Newsletter</i> </summary>
<br>
A newsletter sign up form has been added to the footer of the site, and a Mailchimp campaign has been created to capture the subscriber email addresses.
<br><br>
Once a user subscribes, their email address is saved to the campaign.
<br><br>


<table>
<tr>
<th>
Newsletter Signup Form
</th>
</tr>

<tr>
<td>

![newsletter-signup](documentation/marketing-newsletter.webp)
</td>
</tr>
</table>

<br>

The campaign in Mailchimp stores all user email addresses to be included in future newsletter publications.

<br>
<table>
<tr>
<th>
Mailchimp Campaign
</th>
</tr>

<tr>
<td>

![mailchimp](documentation/marketing-mailchimp.webp)
</td>
</tr>
</table>

<br>
<br>
<br>

</details>

<details>
<summary> <i>Facebook Page</i> </summary>
<br>
A Facebook page was set up as part of the marketing strategy.
<br></br>
This page will serve as a way to promote the business by sharing relevant communications and promotions with potential customers.
<br><br>
It will also serve as a way for customers to contact Chocelegance directly with any queries.
<br><br>

The page can be found [here](https://www.facebook.com/profile.php?id=61561170177708).
<br></br>
In the event that the page is deleted, a full screen capture is available below.
</br></br>

<details>
<summary>   <i>Facebook page screen capture</i></summary>
</br>
<table>
<tr>
<td>

![Facebook-page](documentation/facebook-page-full-capture.webp)
</td>
</tr>
</table>

[Back to Business Overview](#business-overview)
</br>
</br>
</br>
</details>


</details>


</details>






<br>

[Back to Top](#chocelegance)

<!--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- DESIGN SECTION -->
<br>
<br>
<br>

## Design 

An overview of the key design aspects is included below.

<details>
  <summary><b> Colour Scheme </b></summary>
<br>
4 primary colours are used throughout the site, these colours were chosen based on appropriateness, aesthetics and accessibility.
<br>
<br>

<!-- Table showing the 4 primary colour details -->
<table>
<tr><th>Colour</th><th>Details</th></tr>

<tr>
<td>
<br>

![color-1](documentation/primary-colour-1.webp)
<br><br>
</td>
<td>Purple<br><br>Hex: #551b8c<br><br>Primary colour used thoughout site for text, borders, container backgrounds and buttons.</td>
</tr>

<tr><td>
<br>

![color-2](documentation/primary-colour-2.webp)
<br><br>
</td><td><br>Light Purple<br><br>Hex: #882bde<br><br>Used for secondary button actions.</td></tr>

<tr><td>
<br>

![color-3](documentation/primary-colour-3.webp)
<br><br>
</td><td>Bright Purple/Violet<br><br>Hex: #c71585<br><br>Used for chocolate containers, text highlights and button glow effects.</td></tr>

<tr><td>
<br>

![color-4](documentation/primary-colour-4.webp)
<br><br>
</td><td>Light Violet/Pink<br><br>Hex: #ed82ed<br><br>Used for box shadows and glow effects.</td></tr>

</table>

<br>
Purple has a traditional association with chocolate which can be seen in popular brands such as Cadbury and Milka (which are two of my favourites!).
<br><br>
The more vibrant shades of bright purple/violet have associations with romance, as exemplified by tradional Valentine's day colour schemes.
<br><br>


<!-- Table showing brand examples to justify colour scheme -->
<table>
<tr><th>Cadbury Brand</th><th>Milka Brand</th><th>Valentine's Day Example</th></tr>

<tr>
<td>

![cadbury example](documentation/cadbury-brand-example.webp)
</td>

<td>

![cadbury example](documentation/milka-brand-example.webp)
</td>

<td>

![cadbury example](documentation/valentines-day-example.webp)
</td>
</tr>
</table>

[Back to Design](#design)
<br>
<br>
<br>

</details>
<!-- Colour scheme section section ends above this line -->





<details>
<summary><b> Font </b></summary>
<br>
<table>
<tr><th> Urbanist </th></tr>
<tr><td>
The site uses the 'Urbanist' font from Google Fonts.
<br>
<br>
This font was chosen as I felt it's appearance was clean, crisp, modern and consistent with the Chocelegance brand.
<br>
</td></tr>
<tr><td>

![Chocelegance font](documentation/urbanist-font-example.webp)

</td></tr>
</table> 

[Back to Design](#design)
<br>
<br>
<br>
</details>
<!-- Font section ends above this line -->




<details>
  <summary><b> Responsiveness </b></summary>
<br>
<table>
<tr><th> <b>Am I Responsive?</b> </th></tr>
<tr>
<td>
The site was designed following the principles of mobile first design. All initial CSS and Bootstrap style rules were implemented for use on mobile devices with a min-width screen size of 320px, from there the layout was adapted as needed for progressively larger screens using media queries.
<br>
<br>
The screenshot below was taken from the site:
<br>
<br>
https://ui.dev/amiresponsive
<br>
<br>
</td>
</tr>

<tr>
<td>

![am i responsive](documentation/am-i-responsive.webp)

</td>
</tr>
</table> 

[Back to Design](#design)
<br>
<br>
<br>
</details>
<!-- Responsiveness section ends above this line -->




<details>
  <summary><b> Wireframes </b></summary>
<br>

<!-- Wireframe begins -->
<details>  
  <summary> <I>Sign Up Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-sign-up.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Email Verification Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-verify-email.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Confirm Email Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-confirm-email.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Sign In Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-sign-in.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Home Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-home-page.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Main Chocolates Menu</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-main-chocolates-menu.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Chocolate Details Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-chocolates-details.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Shopping Cart</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-shopping-cart.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Checkout Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-checkout-page.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Order Confirmation</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-order-confirmation.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Add Chocolate Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-add-chocolate.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>Edit Chocolate Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-edit-chocolate.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>About Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-about-page.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> <I>User Profile Page</I> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-profile-page.webp)
</details>
<!-- Wireframe ends -->
<br>
<br>
<br>
</details>
<!-- Wireframe section ends above this line -->


<details>
  <summary><b> Entity Relationship Diagram </b></summary>
<br>

<table>
<tr>
<th>
ERD
</th>
</tr>

<tr>
<td>

The project uses [ElephantSQL](https://www.elephantsql.com/) to host the database.
<br><br>
6 custom database models have been developed to capture and store relevant data:
<br>

<ol>
<li>
<b>Faq Model</b>
<br>
This model holds the questions and answers that are displayed to the user in the 'About' page. This content is updated by the superuser directly from the admin panel. Located in 'About' app.
</li>
<br>
<li>
<b>ChocolateReview Model</b>
<br>
This model holds the chocolate reviews that are added by the user in the chocolate details page. The reviews are submitted with the 'publish' status set to 'No', once reviewed by the superuser in the admin panel, the 'publish' status can then be set to 'Yes', which will trigger the review to be displayed on the site. Located in 'Chocolate' app.
</li>
<br>
<li>
<b>Chocolate Model</b>
<br>
This model holds all the relevant details about the chocolates sold on the site. The values in this model can be created, read, updated, and deleted by a superuser directly from the site without the need to log in to the admin panel. Located in 'Chocolate' app.
</li>
<br>
<li>
<b>ChocolateCategory Model</b>
<br>
This model holds the different categories of chocolates sold on the site (e.g Dark Vegan Chocolate, Milk Gluten-Free Chocolate etc). These values are updated from the admin panel. Located in 'Chocolate' app.
</li>
<br>
<li>
<b>Testimonial Model</b>
<br>
This model holds the testimonials that are injected into the home page carousel. This content is updated in the admin panel by a superuser. Located in 'Testimonials' app.
</li>
<br>
<li>
<b>DietaryType Model</b>
<br>
This model holds the different dietary types that are catered to (e.g Keto, Vegan, Gluten-Free). This content is updated in the admin panel by a superuser. Located in 'Chocolate' app.
</li>
</ol>

<br>
The ERD below was generated using graphviz.
<br>
<br>
</td>
</tr>

<tr>
<td>

![erd](documentation/erd-final.webp)
</td>
</tr>

</table>

[Back to Design](#design)
<br>
<br>
<br>
</details>

<br>






[Back to Top](#chocelegance)

<!--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- FEATURES SECTION -->
<br>
<br>
<br>

## Features

An overview of the main features of the site is included below.

<details>
<summary><b> Existing Features</b></summary>
<br>

<!-- Feature starts below this line -->
<details>
<summary> <i>Header / Navbar</i> </summary>
<br>
<table>
<tr>
<th>
Header Navbar
</th>
</tr>

<tr>
<td>
A responsive navigation bar has been developed for the site that includes links to all key sections of the site:
<br><br>
<ul>
<li>
Main chocelegance logo
</li>
<li>
My account (includes register, log in and log out links)
</li>
<li>
Shopping cart
</li>
<li>
Search bar
</li>
<li>
All chocolates (includes 'sort by' dropdown menu)
</li>
<li>
Keto chocolates (includes chocolate type dropdown menu)
</li>
<li>
Vegan chocolates (includes chocolate type dropdown menu)
</li>
<li>
Gluten-free chocolate (includes chocolate type dropdown menu)
</li>
<li>
About page
</li>
</ul>
<br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-1-header-nav.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Allauth User Authentication</i> </summary>
<br><br>
<table>
<tr>
<th>
Allauth Security/Authentication
</th>
</tr>

<tr>
<td>
Django's Allauth package has been implemented in the site, and used to provide:
<br><br>
<ul>
<li>
User signup
</li>
<li>
Email verification
</li>
<li>
Email confirmation
</li>
<li>
User role based login features (e.g superuser with crud options and admin rights)
</li>
<li>
Account security
</li>

</ul>
<br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-2-allauth-verification.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>SEO Optimised Hero Section</i> </summary>
<br>
<table>
<tr>
<th>
SEO Optimised Hero Section
</th>
</tr>

<tr>
<td>
The main hero section contains an attention grabbing, high quality image relevant to the core business. The text and button have also been optimised using semantic HTML and relevant SEO keywords.
<br><br>

</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-3-seo-optimised-hero-section.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Testimonial Carousel</i> </summary>
<br>
<table>
<tr>
<th>
Testimonial Carousel
</th>
</tr>

<tr>
<td>
A responsive carousel has been developed to display user testimonials on the home page.
<br><br>
The content for this is entered by the superuser in the admin panel.
<br><br>

</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-4-testimonials-carousel.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Footer / Newsletter Signup</i> </summary>
<br>
<table>
<tr>
<th>
Footer / Newsletter Signup
</th>
</tr>

<tr>
<td>
A responsive footer has been developed that contains:
<br><br>
<ul>
<li>
Social media links (using 'no follow' and 'sponsored' rel attributes where appropriate)
</li>
<li>
Privacy policy link
</li>
<li>
Terms and conditions link
</li>
<li>
Mailhcimp newsletter subscribtion form (with space for confirmation messages)
</li>

</ul>
<br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-5-footer-newsletter.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Chocolate Main Menu</i> </summary>
<br>
<table>
<tr>
<th>
Chocolate Main Menu
</th>
</tr>

<tr>
<td>
A responsive main menu page for the chocolates offered on the site has been developed. This page includes:
<br><br>
<ul>
<li>
Chocolate sorting options
</li>
<li>
A bootstrap card for each chocolate containing a vibrant image
</li>
<li>
Chocolate name
</li>
<li>
Chocolate price
</li>
<li>
Chocolate type
</li>
<li>
Dietary category
</li>
<li>
Superuser options (edit and delete)
</li>
<li>
Chocolate rating
</li>

</ul>
<br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-6-chocolate-menu-sorting.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Chocolate Details Page</i> </summary>
<br>
<table>
<tr>
<th>
Chocolate Details Page
</th>
</tr>

<tr>
<td>
A responsive details page for the chocolates offered on the site has been developed. This page includes:
<br><br>
<ul>
<li>
A bootstrap card for the chocolate containing a vibrant image
</li>
<li>
Chocolate name
</li>
<li>
Chocolate price
</li>
<li>
Chocolate type
</li>
<li>
Dietary category
</li>
<li>
Chocolate Description
</li>
<li>
Number of chocolate pieces included
</li>
<li>
Ingredients
</li>
<li>
Nutrional information
</li>
<li>
Superuser options (edit and delete)
</li>
<li>
Chocolate rating
</li>
<li>
Number of reviews submitted
</li>
<li>
User reviews submitted (if any)
</li>
<li>
User review form and submit button
</li>
<li>
Quantity form
</li>
<li>
Add to cart button
</li>
<li>
Keep shopping button
</li>

</ul>
<br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-7-chocolate-details.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>User Reviews</i> </summary>
<br>
<table>
<tr>
<th>
User Reviews
</th>
</tr>

<tr>
<td>
Users are presented with reviews and ratings for each chocolate, if none exist, a prompt to log in and leave one will be displayed instead.
<br><br>
A form is also present on the chocolate details page with a drop down menu allowing users to leave a star rating (out of 5).
<br><br>
A textfield allows the user to input a brief review (this is a required field).
<br><br>
Once the rating and review is ready, the user can click the submit button to commit the review.
<br><br>
To note, the rating will be visible immediately, however the text will require approval by the superuser in the admin panel by setting the 'publish' status to 'Yes' (this is to prevent any inappropriate content being displayed on the site).
<br><br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-8-user-reviews.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Superuser Options</i> </summary>
<br>
<table>
<tr>
<th>
Superuser Options
</th>
</tr>

<tr>
<td>
If the user is authenticated as a superuser, additional options will be displayed on the main chocolate menu and chocolate details pages, these allow the superuser to edit or delete a chocolate without the need to log in to the admin panel.
<br><br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-9a-superuser-options.webp)
</td>
</tr>

<tr>
<td>
Clicking the edit button will display the 'edit chocolate' page.
<br><br>
Clicking the delete button will display an additional confirmation dialogue, this is a defensive feature to prevent accidental deletions.
<br><br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-9b-superuser-options.webp)
</td>
</tr>

</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Toast Messages</i> </summary>
<br>
<table>
<tr>
<th>
Toast Messages
</th>
</tr>

<tr>
<td>
Toast messages are used extensively throughout the site to provide the user with helpful messages and notifications to confirm user actions.
<br><br>
Signing in or logging out will trigger toast messages confirming the actions were successful.
<br><br>
Any error messages when filling out forms will trigger a toast error message.
<br><br>
Navigating to the 'edit chocolate' page will trigger a toast info message alerting the user they are about to edit the chocolate details.
<br><br>
Deleting a chocolate will trigger a toast message confirming the deletion was successful.
<br><br>
Adding chocolates to the cart, and completing a purchase will trigger a toast message confirming the actions were successful.
<br><br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-10-toast-messages.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Shopping Cart</i> </summary>
<br>
<table>
<tr>
<th>
Shopping Cart
</th>
</tr>

<tr>
<td>
The shopping cart page displays relevant details relating to the order:
<br><br>
<ul>
<li>
Vibrant chocolate image
</li>
<li>
Chocolate name
</li>
<li>
Item price
</li>
<li>
A quantity form allowing user to update the quantity, or remove completely from cart
</li>
<li>
A subtotal field
</li>
<li>
Total quanity of items in cart
</li>
<li>
Cart total
</li>
<li>
Deliver cost
</li>
<li>
Order total
</li>
<li>
Prompt to spend more to reach free delivery threshold
</li>
<li>
Keep shopping button
</li>
<li>
Secure checkout button
</li>
</ul>

<br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-11-shopping-cart.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->


<!-- Feature starts below this line -->
<details>
<summary> <i>Checkout</i> </summary>
<br>
<table>
<tr>
<th>
Checkout
</th>
</tr>

<tr>
<td>
The shopping cart page displays an order summary, and forms allowing the user to enter the relevant details to process the transaction:
<br><br>
<ul>
<li>
Full name
</li>
<li>
Email address
</li>
<li>
Delivery details
</li>
<li>
Payment details
</li>
<li>
A notification box alerting the user to the amount that will be charged
</li>
<li>
Adjust cart button
</li>
<li>
Complete order button
</li>
</ul>
<br>
Once the details have been added successfully and 'complete order' has been clicked, a loading overlay will be displayed while the card details are being processed by Stripe.
<br>
To simulate a purchase on the site, please use the card details below:
<br><br>
Card No: 4242 4242 4242 4242 Exp: 04/25 CCV: 242 ZIP: 42424
<br><br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-11-shopping-cart.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Email Confirmations</i> </summary>
<br>
<table>
<tr>
<th>
Email Confirmations
</th>
</tr>

<tr>
<td>
Email confirmations will be sent to the email address entered by the user upon completion of a successful purchase.
<br><br>

</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-21-email-confirmation.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Stripe Webhooks</i> </summary>
<br>
<table>
<tr>
<th>
Stripe Webhooks
</th>
</tr>

<tr>
<td>
Stripe webhooks have been implemented for the site, allowing transactions to be captured and completed even if the user's connection to the site is affected during the checkout process.
<br><br>

</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-22-webhooks.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Order Confirmation</i> </summary>
<br>
<table>
<tr>
<th>
Order Confirmation
</th>
</tr>

<tr>
<td>
Upon completion of a successful purchase, the user is directed to an order confirmation screen containing all details relating to the order.
<br><br>

</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-13-order-confirmation.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Chocolate Management (Add Chocolate)</i> </summary>
<br>
<table>
<tr>
<th>
Chocolate Management (Add Chocolate)
</th>
</tr>

<tr>
<td>
If the user is authenticated, they will have access to the 'chocolate management' page from a link in the 'My Account' dropdown menu.
<br><br>
This page will allow the user to add a chocolate to the 'Chocolate' model without the need to log in to the admin panel.
<br><br>

</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-14-chocolate-management-add.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Chocolate Management (Edit Chocolate)</i> </summary>
<br>
<table>
<tr>
<th>
Chocolate Management (Add Chocolate)
</th>
</tr>

<tr>
<td>
If the user is authenticated, they will have access to the 'edit' button on the main chocolate menu screen and the chocolate details page.
<br><br>
This page will allow the user to edit a chocolate to the 'Chocolate' model without the need to log in to the admin panel.
<br><br>

</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-15-chocolate.management-edit.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Profile Page</i> </summary>
<br>
<table>
<tr>
<th>
Profle Page
</th>
</tr>

<tr>
<td>
If the user has registered for an account, and is currently authenticated, they will be provided with access to the 'My Profile' link in the 'My Account' drop down menu.
<br><br>
This allows the user to save their default delivery delivery details which can then be used to prepopulate the checkout form on future purchases, and also provides them with their order history which allows them to conveniently review past purchases.
<br><br>
Another benefit of registering for an account is the ability to leave reviews on the site.
<br><br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-16-user-profile.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>About Us</i> </summary>
<br>
<table>
<tr>
<th>
About Us
</th>
</tr>

<tr>
<td>

An 'About Us' section provides the user with more information about the business, this text has been adapted from the [Puccini Bomboni](https://puccinibomboni.com/over-ons) site.
<br><br>
The text has also been optimised by using SEO keywords in appropriate semantic tags.
<br><br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-17-seo-optimised-about.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Contact Us</i> </summary>
<br>
<table>
<tr>
<th>
Contact Us
</th>
</tr>

<tr>
<td>
A 'Contact Us' section provides the user with more information on how to make contact with the business.
<br><br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-18-contact-us.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>FAQs</i> </summary>
<br>
<table>
<tr>
<th>
FAQs
</th>
</tr>

<tr>
<td>
A responsive bootstrap accordion has been included in the 'About' page and injected with data from the FAQs model using DTL loops and variables.
<br><br>
The content for this section is updated by the superuser directly from the admin panel.
<br><br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-19-faqs-accordion.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

<!-- Feature starts below this line -->
<details>
<summary> <i>Admin</i> </summary>
<br>
<table>
<tr>
<th>
Admin
</th>
</tr>

<tr>
<td>
The admin panel allows the superuser to update all models directly, and provides them with the ability to control the access rights of users.
<br><br>
The admin panel can also be accessed directly from the site through the admin panel link in the 'My Account' drop down menu (once user is authenticated as a superuser).
<br><br>
</td>
</tr>

<tr>
<td>

![feature](documentation/features/features-20-admin-panel.webp)
</td>
</tr>
</table>

</details>
<!-- Feature ends above this line -->

[Back to Features](#features)
<br>
<br>
<br>
</details>
<!-- Existing Features ends above this line -->



<details>
<summary><b> Future Features</b></summary>
<br>
<details>
<summary> <i>Event Catering Quote Model</i></summary>
<br>
Chocelegance is in a prime position to offer catering for special events and occasions to customers.
<br><br>
This will be a new service that will be bookable through the site in future iterations. Part of the process will involve calculating a quote to provide customers with an upfront fee.
<br><br>
A model will be created with private methods that will generate a quote amount based on the user inputs (e.g, from a form capturing the necessary data.)
<br><br>
Once all the data has been submitted, an amount will be displayed to the user which they can then either accept or reject.
<br>
<br>
<br>
</details>


<details>
<summary> <i>Inventory Management System</i></summary>
<br>
As the business grows, it will become necessary to implement a more sophisticated inventory management system.
<br><br>
In future iterations, a system will be developed that will give the superuser a forecasted amount of the inventory required for the period ahead, and send alerts if stock is running low.
<br><br>
With time this system will become more 'intelligent' and perhaps feed into a financial management system to project costs and profits for future periods.
<br>
<br>
<br>
</details>


[Back to Features](#features)
<br>
<br>
<br>
</details>


<br>

[Back to Top](#chocelegance)

<!--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- USER STORIES SECTION -->
<br>
<br>
<br>

## User Stories

An overview of the User Stories related to the project is shown below.

<details>
<summary> <b>User Stories</b></summary>
<br>
<table>
<tr>

<th>
Issue ID
</th>

<th>
Epic ID
</th>

<th>
User Story
</th>

<th>
Status
</th>

</tr>

<!-- User Story starts below here -->
<tr>

<!-- Issue ID -->
<td>

[#3](https://github.com/DannyGilligan/chocelegance-project/issues/3)
</td>

<!-- Epic ID -->
<td>

[#8](https://github.com/DannyGilligan/chocelegance-project/issues/8)
</td>

<!-- User Story -->
<td>
As a user, I can view range of chocolates available on the site, so I can choose which chocolates to purchase.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->

<!-- User Story starts below here -->
<tr>

<!-- Issue ID -->
<td>

[#9](https://github.com/DannyGilligan/chocelegance-project/issues/9)
</td>

<!-- Epic ID -->
<td>

[#8](https://github.com/DannyGilligan/chocelegance-project/issues/8)
</td>

<!-- User Story -->
<td>
As a role user, I can view the details of an individual chocolate, so that I can decide whether to purchase or not.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#10](https://github.com/DannyGilligan/chocelegance-project/issues/10)
</td>

<!-- Epic ID -->
<td>

[#8](https://github.com/DannyGilligan/chocelegance-project/issues/8)
</td>

<!-- User Story -->
<td>
As a user, I can see the Keto, Vegan or Gluten-Free dietary types in the navbar, so that I can quickly access the chocolates I am interested in.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#11](https://github.com/DannyGilligan/chocelegance-project/issues/11)
</td>

<!-- Epic ID -->
<td>

[#8](https://github.com/DannyGilligan/chocelegance-project/issues/8)
</td>

<!-- User Story -->
<td>
As a user, I can see the current total of my shopping cart, so that I can stay informed of the amount I am spending.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#13](https://github.com/DannyGilligan/chocelegance-project/issues/13)
</td>

<!-- Epic ID -->
<td>

[#8](https://github.com/DannyGilligan/chocelegance-project/issues/8)
</td>

<!-- User Story -->
<td>
As a user, I can see the Dark Chocolate, Milk Chocolate and White chocolate categories in the navbar dropdown menus, so that I can choose the chocolate category I am interested in.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#14](https://github.com/DannyGilligan/chocelegance-project/issues/14)
</td>

<!-- Epic ID -->
<td>

[#12](https://github.com/DannyGilligan/chocelegance-project/issues/12)
</td>

<!-- User Story -->
<td>
As a user, I can easily and quickly register for an account, so that I can create a profile, leave chocolate reviews and have access to my order history.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#15](https://github.com/DannyGilligan/chocelegance-project/issues/15)
</td>

<!-- Epic ID -->
<td>

[#12](https://github.com/DannyGilligan/chocelegance-project/issues/12)
</td>

<!-- User Story -->
<td>
As a user, I can easily log in and log out of the site, so that I can use the site effectively.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#16](https://github.com/DannyGilligan/chocelegance-project/issues/16)
</td>

<!-- Epic ID -->
<td>

[#12](https://github.com/DannyGilligan/chocelegance-project/issues/12)
</td>

<!-- User Story -->
<td>
As a user, I can retrieve my password in the event that it is forgotten, so that I can access the site.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#17](https://github.com/DannyGilligan/chocelegance-project/issues/17)
</td>

<!-- Epic ID -->
<td>

[#12](https://github.com/DannyGilligan/chocelegance-project/issues/12)
</td>

<!-- User Story -->
<td>
As a user, I can verify my email address, so that my account can be verified using Allauth.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#18](https://github.com/DannyGilligan/chocelegance-project/issues/18)
</td>

<!-- Epic ID -->
<td>

[#12](https://github.com/DannyGilligan/chocelegance-project/issues/12)
</td>

<!-- User Story -->
<td>
As a user, I can create a personal user profile, so that I can save default delivery information, leave chocolate reviews, view my order history.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#20](https://github.com/DannyGilligan/chocelegance-project/issues/20)
</td>

<!-- Epic ID -->
<td>

[#19](https://github.com/DannyGilligan/chocelegance-project/issues/19)
</td>

<!-- User Story -->
<td>
As a user, I can sort the chocolates on the main menu page, so that I can see navigate the chocolate menu and see the chocolates from lowest price to highest etc.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#21](https://github.com/DannyGilligan/chocelegance-project/issues/21)
</td>

<!-- Epic ID -->
<td>

[#19](https://github.com/DannyGilligan/chocelegance-project/issues/19)
</td>

<!-- User Story -->
<td>
As a user, I can sort the chocolates within a specific dietary type, so that I can browse the selection using my preferred sorting method.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#22](https://github.com/DannyGilligan/chocelegance-project/issues/22)
</td>

<!-- Epic ID -->
<td>

[#19](https://github.com/DannyGilligan/chocelegance-project/issues/19)
</td>

<!-- User Story -->
<td>
As a user, I can use the search form to search for a chocolate, so that I can make a selection to purchase.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#23](https://github.com/DannyGilligan/chocelegance-project/issues/23)
</td>

<!-- Epic ID -->
<td>

[#19](https://github.com/DannyGilligan/chocelegance-project/issues/19)
</td>

<!-- User Story -->
<td>
As a user, I can see the results of my search, so that I can browse the returned results.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#25](https://github.com/DannyGilligan/chocelegance-project/issues/25)
</td>

<!-- Epic ID -->
<td>

[#24](https://github.com/DannyGilligan/chocelegance-project/issues/24)
</td>

<!-- User Story -->
<td>
As a user, I can select of adjust the quantity of chocolates I wish to purchase, so that I can purchase the desired amount.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#27](https://github.com/DannyGilligan/chocelegance-project/issues/27)
</td>

<!-- Epic ID -->
<td>

[#24](https://github.com/DannyGilligan/chocelegance-project/issues/24)
</td>

<!-- User Story -->
<td>
As a user, I can enter the necessary details, so that I can complete the purchase.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#28](https://github.com/DannyGilligan/chocelegance-project/issues/28)
</td>

<!-- Epic ID -->
<td>

[#24](https://github.com/DannyGilligan/chocelegance-project/issues/24)
</td>

<!-- User Story -->
<td>
As a user, I can view an order confirmation after successful purchase, so that I can review the details of the purchase.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here -->


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#29](https://github.com/DannyGilligan/chocelegance-project/issues/29)
</td>

<!-- Epic ID -->
<td>

[#24](https://github.com/DannyGilligan/chocelegance-project/issues/24)
</td>

<!-- User Story -->
<td>
As a user, I can receive an email confirmation after a successful purchase, so that I can review the details.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here --> 


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#31](https://github.com/DannyGilligan/chocelegance-project/issues/31)
</td>

<!-- Epic ID -->
<td>

[#30](https://github.com/DannyGilligan/chocelegance-project/issues/30)
</td>

<!-- User Story -->
<td>
As a superuser, I can add a chocolate, so that the chocolate selection can be managed.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here --> 


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#32](https://github.com/DannyGilligan/chocelegance-project/issues/32)
</td>

<!-- Epic ID -->
<td>

[#30](https://github.com/DannyGilligan/chocelegance-project/issues/30)
</td>

<!-- User Story -->
<td>
As a superuser, I can edit the chocolate details directly from site, so that I can make amendments quickly to the chocolates on the site.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here --> 


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#33](https://github.com/DannyGilligan/chocelegance-project/issues/33)
</td>

<!-- Epic ID -->
<td>

[#30](https://github.com/DannyGilligan/chocelegance-project/issues/30)
</td>

<!-- User Story -->
<td>
As a superuser, I can delete a chocolate directly from the site, so that I can administer changes efficiently without accessing the admin panel.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here --> 


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#35](https://github.com/DannyGilligan/chocelegance-project/issues/35)
</td>

<!-- Epic ID -->
<td>

[#34](https://github.com/DannyGilligan/chocelegance-project/issues/34)
</td>

<!-- User Story -->
<td>
As a user, I can leave a star rating for a chocolate, so that I can let other users know my perception of the quality.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here --> 



<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#36](https://github.com/DannyGilligan/chocelegance-project/issues/36)
</td>

<!-- Epic ID -->
<td>

[#34](https://github.com/DannyGilligan/chocelegance-project/issues/34)
</td>

<!-- User Story -->
<td>
As a user, I can leave a review in the textfield in the review section of the chocolate detail page, so that I can let other customers know my perception of the quality.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here --> 


<!-- **** User Story starts below here **** -->
<tr>

<!-- Issue ID -->
<td>

[#37](https://github.com/DannyGilligan/chocelegance-project/issues/37)
</td>

<!-- Epic ID -->
<td>

[#34](https://github.com/DannyGilligan/chocelegance-project/issues/34)
</td>

<!-- User Story -->
<td>
As a superuser, I can review submitted review and publish if appropriate, so that the review is displayed on the chocolate details page.
</td>

<!-- Status -->
<td>
Closed
</td>

</tr>
<!-- User Story ends above here --> 

</table>
<!-- User Story table ends above here --> 

</details>
<!-- User Story section ends above here --> 

<br>

[Back to Top](#chocelegance)

<!--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- MANUAL TESTING SECTION -->
<br>
<br>
<br>

## Manual Testing

An overview of the manual testing performed for the project is included below.

<details>
<summary><b>Browser Compatibility</b></summary>
<br>
Several popular browsers were tested for functionality. The site behaved as expected on all browsers tested.
<br>
<br>
<table>

<tr>
<th>
Browser
</th>

<th>
Status
</th>
</tr>

<tr>
<td>
Google Chrome
</td>

<td>
:heavy_check_mark:
</td>
</tr>

<tr>
<td>
Mozilla Firefox
</td>

<td>
:heavy_check_mark:
</td>
</tr>

<tr>
<td>
Microsoft Edge
</td>

<td>
:heavy_check_mark:
</td>
</tr>

<tr>
<td>
Apple Safari
</td>

<td>
:heavy_check_mark:
</td>
</tr>

</table>
<br>
<br>
<br>
</details>


<details>
<summary><b>Lighthouse Testing</b></summary>
<br>
The site performed well in the SEO, Accessibility and Best Practises categories, however performance requires further optimisation.
<br><br>
I suspect that the Heroku platform may be contributing to the poor score (the app is hosted on the free tier level).
<br><br>
To note, initially the Lighthouse testing resulted in an error being logged to the console relating to a 3rd party extension/cookie. The test was then reperformed in 'Incognito' mode, which eliminated the issue.
<br><br>

<table>
<tr>
<th>
Lighthouse Testing Results
</th>
</tr>

<tr>
<td>

![lighthouse](documentation/manual_testing/testing-lighthouse.webp)
</td></tr>
</table>

<br>
<br>
<br>
</details>

<details>
<summary><b>Code Validation</b></summary>
<br>

<!-- ************************************************************************************************************************************************************* -->

<!-- HTML validation starts below this line -->
<details>
<summary> <i>HTML</i> </summary>
<br>

To validate the HTML, each page rendered on the website was visited, then the 'page source' was copied, then pasted into the [W3C Validator](https://validator.w3.org/) as a direct input. Results below:
<br><br>

<details>
<summary>  Home Page</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-1-home-page.webp)
</td>
</tr>
<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>


<details>
<summary>  Main Chocolates Menu</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/chocolates/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-2-main-chocolates-menu.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>


<details>
<summary>  Chocolate Details Page</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/chocolates/8/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-3-chocolate-details.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>


<details>
<summary>  Shopping Cart</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/cart/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-4-shopping-cart.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>


<details>
<summary>  Checkout</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/checkout/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-5-checkout.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>


<details>
<summary>  Order Confirmation</summary>
<br>
<table>
<tr>
<th>

Direct link not applicable, however checkout_success.html is the template being rendered.
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-6-order-confirmation.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>


<details>
<summary>  Error 404 Page</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/404test)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-7-404-error.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>


<details>
<summary>  About Page</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/about/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-8-about-page.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>



<details>
<summary>  Chocolate Management (Add Chocolate)</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/chocolates/add/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-9-add-choc.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>



<details>
<summary>  Profile Page</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/profile/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-11-profile-page.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>



<details>
<summary>  Logout Page</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/accounts/logout/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-12-logout-page.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>



<details>
<summary>  Signup Page</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/accounts/signup/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-13-signup-page.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>



<details>
<summary>  Signin Page</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/accounts/login/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-14-signin-page.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>




<details>
<summary>  Forgot Password</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/accounts/password/reset/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-15-forgot-password.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>



<details>
<summary>  Privacy Policy</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/privacy/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-16-privacy-policy.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>



<details>
<summary>  Terms and Conditions</summary>
<br>
<table>
<tr>
<th>

[Link Here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/terms/)
</th>
</tr>

<tr>
<td>

![image](documentation/manual_testing/html_validation/html-17-terms.webp)
</td>
</tr>

<tr>
<td>
No Errors :heavy_check_mark:
</td>
</tr>
</table>
<br>
</details>

<br>
<br>
<br>
</details>
<!-- HTML Validation ends above this line -->

<!-- CSS Validation begins below this line -->
<details>
<summary> <i>CSS</i> </summary>
<br>

The CSS files used throughout the project were checked in the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Results below:
<br>
<table>
<tr>
<th>
Filename
</th>

<th>
Location
</th>

<th>
Validation
</th>

<th>
Result
</th>
</tr>

<tr>
<td>
about.css
</td>

<td>
About App
</td>

<td>

![image](documentation/manual_testing/css_validation/css-about.webp)
</td>

<td>
No Errors
<br>
:heavy_check_mark:
</td>
</tr>

<tr>
<td>
checkout.css
</td>

<td>
Checkout App
</td>

<td>

![image](documentation/manual_testing/css_validation/css-checkout.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>

<tr>
<td>
base.css
</td>

<td>
Project root directory
</td>

<td>

![image](documentation/manual_testing/css_validation/css-base.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>


<tr>
<td>
profile.css
</td>

<td>
Profiles App
</td>

<td>

![image](documentation/manual_testing/css_validation/css-profile.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>
<br>
</table>
<br>
<br>
<br>
</details>
<!-- CSS Validation ends above this line -->


<!-- Javascript Validation starts below this line -->
<details>
<summary> <i>Javascript</i> </summary>
<br>

All Javascript code blocks were passed through the [JSHint validator](https://jshint.com/) (with the exception of the Mailchimp script). Results below:
<br><br>
<table>

<tr>
<th>
File Name
</th>

<th>
File Location
</th>

<th>

Validation
</th>

<th>Result</th>
</tr>

<!-- spacer -->

<tr>
<td>
cart.html
</td>

<td>
Cart App
</td>

<td>

![image](documentation/manual_testing/js_validation/js-cart-html.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>

<!-- spacer -->

<tr>
<td>
stripe_elements.js
</td>

<td>
Checkout App
</td>

<td>

![image](documentation/manual_testing/js_validation/js-stripe-elements.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>

<!-- spacer -->

<tr>
<td>
quantity_input_script.html
</td>

<td>
Chocolates App
</td>

<td>

![image](documentation/manual_testing/js_validation/js-quantity-input-script.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>

<!-- spacer -->

<tr>
<td>
chocolate_detail.html
</td>

<td>
Chocolates App
</td>

<td>

![image](documentation/manual_testing/js_validation/js-chocolate-detail-html.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>


<!-- spacer -->

<tr>
<td>
chocolates.html
</td>

<td>
Chocolates App
</td>

<td>

![image](documentation/manual_testing/js_validation/js-chocolate-html.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>


<!-- spacer -->

<tr>
<td>
add_chocolate.html
</td>

<td>
Chocolates App
</td>

<td>

![image](documentation/manual_testing/js_validation/js-add-chocolate-html.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>


<!-- spacer -->

<tr>
<td>
edit_chocolate.html
</td>

<td>
Chocolates App
</td>

<td>

![image](documentation/manual_testing/js_validation/js-edit-chocolate-html.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>

<!-- spacer -->

<tr>
<td>
countryfield.js
</td>

<td>
Profiles App
</td>

<td>

![image](documentation/manual_testing/js_validation/js-countryfield.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>


<!-- spacer -->

<tr>
<td>
main-nav.html
</td>

<td>
Root Templates Directory
</td>

<td>

![image](documentation/manual_testing/js_validation/js-main-nav.webp)
</td>

<td>
No Errors 
<br>
:heavy_check_mark:
</td>
</tr>

</table>
<br>
<br>
<br>
</details>
<!-- Javascript validation ends above this line -->



<!-- Python validation starts below this line -->
<details>
<summary> <i>Python</i> </summary>
<br>

All Python Code was passed through the [Code Institute Python Linter](https://pep8ci.herokuapp.com/#). 
<br><br>
The App location, name and result for each file are shown below:
<br><br>

<!-- spacer -->
<details>
<summary>  About App - admin.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/about-admin.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  About App - models.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/about-models.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  About App - urls.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/about-urls.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  About App - views.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/about-views.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Cart App - contexts.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/cart-contexts.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Cart App - urls.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/cart-urls.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Cart App - views.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/cart-views.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Checkout App - admin.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/checkout-admin.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Checkout App - forms.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/checkout-forms.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Checkout App - models.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/checkout-models.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Checkout App - signals.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/checkout-signals.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Checkout App - urls.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/checkout-urls.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Checkout App - views.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/checkout-views.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Checkout App - webhook_handler.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/checkout-webhook-handler.webpp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Checkout App - webhooks.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/checkout-webhooks.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Chocelegance App - urls.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/chocelegance-urls.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Chocelegance App - views.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/chocelegance-views.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Chocelegance App - wsgi.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/chocelegance-wsgi.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Chocolates App - admin.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/chocolates-admin.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Chocolates App - forms.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/chocolates-forms.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Chocolates App - models.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/chocolates-models.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Chocolates App - urls.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/chocolates-urls.webp)
</tr>
</table>
</details>


<!-- spacer -->
<details>
<summary>  Chocolates App - views.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/chocolates-views.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Chocolates App - widgets.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/chocolates-widgets.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Home App - urls.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/home-urls.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Home App - views.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/home-views.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Profiles App - forms.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/profiles-forms.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Profiles App - models.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/profiles-models.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Profiles App - urls.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/profiles-urls.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Profiles App - views.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/profiles-views.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Testimonials App - admin.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/testimonials-admin.webp)
</tr>
</table>
</details>

<!-- spacer -->
<details>
<summary>  Testimonials App - models.py</summary>
<br>
<table>
<tr>
<th>
No Errors :heavy_check_mark:
</th>
</tr>
<tr>

![image](documentation/manual_testing/python_validation/testimonials-models.webp)
</tr>
</table>
</details>

<br>
<br>
<br>
</details>
<!-- Python validation ends above this line -->
<br>
<br>
<br>
</details>
<!-- Code validation ends above this line -->


<details>
<summary><b>User Story Testing</b></summary>
<br>
The User Stories were tested for functionality and to ensure no errors were encountered in the code execution. Results below:
<br><br>


<!-- spacer -->
<details>
<summary>  #3 As a user, I can view range of chocolates available on the site, so I can choose which chocolates to purchase. </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
Chocolates are displayed correctly in chocolate main menu
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #9 As a role user, I can view the details of an individual chocolate, so that I can decide whether to purchase or not.  </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
Chocolate details are displayed correctly in chocolate details page
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #10 As a user, I can see the Keto, Vegan or Gluten-Free dietary types in the navbar, so that I can quickly access the chocolates I am interested in. </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The dietary categories are displayed correctly in the navbar.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #11 As a user, I can see the current total of my shopping cart, so that I can stay informed of the amount I am spending.  </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
Current total in cart updates correctly after items added.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #13 As a user, I can see the Dark Chocolate, Milk Chocolate and White chocolate categories in the navbar dropdown menus, so that I can choose the chocolate category I am interested in.   </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The Dark, Milk and White chocolate links in the drop down menu are displayed correctly.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>

<!-- spacer -->
<details>
<summary>  #14 As a user, I can easily and quickly register for an account, so that I can create a profile, leave chocolate reviews and have access to my order history.    </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The account registration procees flow works correctly.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #15 As a user, I can easily log in and log out of the site, so that I can use the site effectively.     </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The Allauth login and logout functionality works correctly.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #16 As a user, I can retrieve my password in the event that it is forgotten, so that I can access the site.</summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The 'forgot password' process flow works correctly.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #17 As a user, I can verify my email address, so that my account can be verified using Allauth. </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The email verification functionality works as expected.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #18 As a user, I can create a personal user profile, so that I can save default delivery information, leave chocolate reviews, view my order history.  </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The profile functionality works as expected, default delivery information can be updated, and the order history is displayed correctly.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>



<!-- spacer -->
<details>
<summary>  #20 As a user, I can sort the chocolates on the main menu page, so that I can see navigate the chocolate menu and see the chocolates from lowest price to highest etc.</summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The sorting function works correctly, for name, price and category, however a bug has been identified with the rating from user reviews. This is documented in the unresolved bugs section, and also in the agile project board.
</td>
<td>
Criteria not met
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #21 As a user, I can sort the chocolates within a specific dietary type, so that I can browse the selection using my preferred sorting method. </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
Chocolates can be sorted within the category by name and price, however a bug has been identified with the rating sorting.
</td>
<td>
Criteria not met
</td>
</tr>

</table>

<br>
</details>

<!-- spacer -->
<details>
<summary>  #22 As a user, I can use the search form to search for a chocolate, so that I can make a selection to purchase.   </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The search form functions as expected.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #23 As a user, I can see the results of my search, so that I can browse the returned results.    </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
Search results are displayed correctly.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #25 As a user, I can select of adjust the quantity of chocolates I wish to purchase, so that I can purchase the desired amount.  </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
Quantity form functions as excpected.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #27 As a user, I can enter the necessary details, so that I can complete the purchase.   </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The forms on the checkout page work as expected.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #28 As a user, I can view an order confirmation after successful purchase, so that I can review the details of the purchase.    </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The order confirmation page displays correctly after a successful purchase.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #29 As a user, I can receive an email confirmation after a successful purchase, so that I can review the details.    </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The email confirmations are received successfully.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #31 As a superuser, I can add a chocolate, so that the chocolate selection can be managed.    </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
Chocolates can be added successfully.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #32 As a superuser, I can edit the chocolate details directly from site, so that I can make amendments quickly to the chocolates on the site.     </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The functionality to edit chocolate details from the site directly behaves as expected.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #33 As a superuser, I can delete a chocolate directly from the site, so that I can administer changes efficiently without accessing the admin panel.      </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The functionality to delete chocolate details from the site directly behaves as expected.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #35 As a user, I can leave a star rating for a chocolate, so that I can let other users know my perception of the quality.      </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
Star ratings can be left successfully in the chocolate details page.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #36 As a user, I can leave a review in the textfield in the review section of the chocolate detail page, so that I can let other customers know my perception of the quality.      </summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
Reviews can be successfully left in the textfield in the review section and submitted.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>


<!-- spacer -->
<details>
<summary>  #37 As a superuser, I can review submitted review and publish if appropriate, so that the review is displayed on the chocolate details page.</summary>
<br>
<table>
<tr>
<th>
Acceptance Criteria
</th>
<th>
Result
</th>
</tr>

<!-- **** -->

<tr>
<td>
The functionality to approve the review in the admin panel behaves as expected.
</td>
<td>
Criteria met :heavy_check_mark:
</td>
</tr>

</table>

<br>
</details>

</details>
<!-- User story testing ends above this line -->

<details>
<summary><b>Bugs</b></summary>
<br>

<details>
<summary>  <i>Resolved Bugs</i></summary>
<br>
I was unable to add all the bugs I resolved to the readme, I'm quickly adding 3 that come to mind as particularly troubelsome. 
<table>
<tr>
<td>
When trying to install Django AllAuth 0.41.0 I ran into the error message below<br>
<b>"Python setup.py egg_info did not run successfully when installing"</b><br>
This was preventing me from installing the correct AllAuth package, after trying different approaches such as installing different versions of Django and Python, I found a post that suggested installing a specific version of 'Setuptools', I installed Setuptools version 67.4.0 which appears to have resolved the issue regarding the AllAuth installation

https://github.com/openai/openai-cookbook/issues/154
</td>
</tr>
</table>


<table>
<tr>
<td>
<b>ImproperlyConfiguredException, could not load boto3 S3 bindings when running collectstatic in heroku</b>
<br><br>
Issue preventing deployment in heroku, was a serious issue, eventually found a solution with amazing help from my mentor Martina Terlevic. Issue was compatibility with Django verions.<br><br>
Updgraded <b>urlibb3</b>, and upgraded <b>boto3</b> and upgraded <b>requests</b>.<br><br>
Issue was then resolved, and could deploy app to heroku.
</td>
</tr>
</table>


<table>
<tr>
<td>
<b>SMTP.starttls() unexpected argument 'keyfile'</b>
<br><br>
Issue preventing confirmation emails being sent from Django, no emails were being sent, resulted in Server 500 error.<br><br>
Found solution in Code Institute Slack channel, needed to add runtime.txt to root directory with python version 3.9.18, Roman Racik credited in credits section.
</td>
</tr>
</table>
<br>
<br>
<br>
</details>
<!-- Resolved bugs end above this line -->




<details>
<summary>  <i>Unresolved Bugs</i></summary>
<br>

The choc_rating field in the Chocolate model is not being updated as expected when user ratings are added from the form in the chocolate details page.<br><br>
I've attempted to overwrite the default save behavious of the Chocolate model with a 'private method', however it is not functioning as expected and will need further investigation.<br><br>
Ratings can still be added manually via the admin panel by selecting a chocolate and updating the choc_rating field as needed.

</details>
<!-- Unresolved bugs ends above this line -->


</details>
<!-- Bugs ends above this line -->




<br>

[Back to Top](#chocelegance)

<!--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- TECHNOLOGIES USED -->
<br>
<br>
<br>

## Technologies Used 

An overview of the technologies used throughout the development of the project is shown below.

#### 
<table>
<tr><th>Logo</th><th>Name</th><th>Primary Role</th><th>Link</th></tr>
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-django.webp" alt="Django" title="Django"/></code>
</div>
</td>
<td>Django</td>
<td>Site Framework</td>
<td>https://www.djangoproject.com/</td>
</tr>
<!-- spacer -->
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-python.webp" alt="Python" title="Python"/></code>
</div>
</td>
<td>Python</td>
<td>Site logic</td>
<td>https://www.python.org/</td>
</tr>
<!-- spacer -->
<!-- Technology Used 1 begins -->
<tr><td>
<div>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png" alt="JavaScript" title="JavaScript"/></code>
</div>
</td>
<td>Javascript</td>
<td>Site interaction</td>
<td>https://developer.mozilla.org/en-US/docs/Web/JavaScript</td>
</tr>
<!-- Technology Used 1 ends -->
<tr><td>
<div>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png" alt="HTML" title="HTML"/></code>
</div>
</td>
<td>HTML 5</td>
<td>Site structure</td>
<td>https://dev.w3.org/html5/spec-LC/</td>
</tr>
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png" alt="CSS" title="CSS"/></code>
</div>
</td>
<td>CSS 3</td>
<td>Site Styling</td>
<td>https://www.w3.org/TR/2001/WD-css3-roadmap-20010523/</td>
</tr>
<!-- spacer -->
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-bootstrap.webp" alt="Bootstrap" title="Bootstrap"/></code>
</div>
</td>
<td>Bootstrap</td>
<td>CSS/Javascript Styling Framework</td>
<td>https://getbootstrap.com/</td>
</tr>
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-github.webp" alt="GitHub" title="GitHub"/></code>
</div>
</td>
<td>Github</td>
<td>Site repository</td>
<td>https://docs.github.com/en</td>
</tr>
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-gitpod.webp" alt="Gitpod" title="Gitpod"/></code>
</div>
</td>
<td>Gitpod</td>
<td>Site development, IDE</td>
<td>https://www.gitpod.io/docs/introduction</td>
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-postgresql.webp" alt="Heroku" title="Heroku"/></code>
</div>
</td>
<td>ElephantSQL</td>
<td>Database hosting</td>
<td>https://www.elephantsql.com/</td>
</tr>
<!-- spacer -->
</tr>
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" height="50" src="documentation/icon-heroku.webp" alt="Heroku" title="Heroku"/></code>
</div>
</td>
<td>Heroku</td>
<td>App deployment/hosting</td>
<td>https://www.heroku.com</td>
</tr>
<!-- spacer -->
<tr>
<td>
<div>
	<code><img width="50" src="documentation/icon-aws.webp" alt="aws" title="aws"/></code>
</div>
</td>

<td>Amazon Web Services</td>

<td>Media & Static file hosting</td>

<td>https://aws.amazon.com/<td>
</tr>
<!-- spacer -->
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-stripe.webp" alt="stripe" title="stripe"/></code>
</div>
</td>
<td>Stripe</td>
<td>Payment Processing</td>
<td>https://www.stripe.com/<td>
</tr>
<!-- spacer -->
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-mailchimp.webp" alt="mailchimp" title="stripe"/></code>
</div>
</td>
<td>Mailchimp</td>
<td>Newsletter Marketing</td>
<td>https://www.mailchimp.com/<td>
</tr>
<!-- spacer -->
<!-- Technology Used 1 ends -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-code-institute.webp" alt="Python Linter" title="Python Linter"/></code>
</div>
</td>
<td><br>Code Institute Python Linter<br><br></td>
<td>Python PEP8 validation</td>
<td>https://pep8ci.herokuapp.com/#</td>
</tr>
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-w3c.webp" alt="W3C" title="W3C"/></code>
</div>
</td>
<td>W3C</td>
<td>HTML & CSS Validation</td>
<td>https://validator.w3.org/docs/</td>
</tr>
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-jshint.webp" alt="JSHint" title="JSHint"/></code>
</div>
</td>
<td>JSHint</td>
<td>Javascript Validation</td>
<td>https://jshint.com/docs/</td>
</tr>
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-balsamiq.webp" alt="Balasmiq" title="Balasmiq"/></code>
</div>
</td>
<td>Balsamiq</td>
<td>Wireframing</td>
<td>https://balsamiq.com/docs/</td>
</tr>
<!-- spacer -->

<tr><td>
<div>
	<code><img width="50" src="documentation/icon-coffee.webp" alt="Coffee" title="Coffee"/></code>
</div>
</td>
<td>Coffee</td>
<td>Soul Enhancer</td>
<td>https://en.wikipedia.org/wiki/Coffee</td>
</tr>
<!-- spacer -->
<tr><td>
<div>
	<code><img width="50" src="documentation/icon-google.webp" alt="Google" title="Google"/></code>
</div>
</td>
<td>Google</td>
<td>Brain Enhancer</td>
<td>https://www.google.com/</td>
</tr>
<!-- spacer -->
</table>
<!-- Technologies Used section ends here -->

[Back to Top](#chocelegance)
<br>
<br>
<br>

## Deployment

An overview of the deployment steps for the project is shown below.

<details>
<summary><b>Required Installs</b></summary>
<br>
asgiref==3.8.1<br>
boto3==1.34.124<br>
botocore==1.34.124<br>
chardet==3.0.4<br>
dj-database-url==0.5.0<br>
Django==3.2.25<br>
django-allauth==0.41.0<br>
django-countries==7.2.1<br>
django-crispy-forms==1.14.0<br>
django-extensions==3.2.3<br>
django-storages==1.14.3<br>
docutils==0.15.2<br>
graphviz==0.20.3<br>
gunicorn==20.0.4<br>
idna==2.8<br>
jmespath==0.10.0<br>
oauthlib==3.2.2<br>
pillow==10.3.0<br>
psycopg2==2.9.9<br>
pydot==2.0.0<br>
pydotplus==2.0.2<br>
pyparsing==3.1.2<br>
python3-openid==3.2.0<br>
pytz==2024.1<br>
requests==2.32.3<br>
requests-oauthlib==2.0.0<br>
s3transfer==0.10.1<br>
setuptools==67.4.0<br>
sqlparse==0.5.0<br>
stripe==9.9.0<br>
<br>
<br>
<br>
</details>



<details>
<summary><b>ElephantSQL</b></summary>
<br>
<ol>
<li>

Create account at [ElephantSQL](https://www.elephantsql.com/)
</li>
<li>
Click on create new instance
</li>
<li>
Enter a name for the instance
</li>
<li>
Select region and data center, click review
</li>
<li>
Click create instance
</li>
<li>
Note database URL
</li>
</ol>
<br>
<br>
<br>
</details>
<!-- deployment for elephantSQL ends above this line -->


<details>
<summary><b>Heroku</b></summary>
<br>
<ol>
<li>

Create account at [Heroku](heroku.com)
</li>
<li>
Click on New, then Create New App
</li>
<li>
Enter an App name, select region, then create app
</li>
<li>
Navigate to settings
</li>
<li>
Enter database URL noted from ElephantSQL instance
</li>
<li>
In IDE, install dj_database_url and psycopg2
</li>
<li>
Connect to ElephantSQL database and migrate
</li>
<li>
In Heroku, navigate to Deploy tab and connect to Github repository
</li>
<li>
Enable automatic deployments to ensure changes are pushed to Heroku
</li>
</ol>
<br>
<br>
<br>
</details>
<!-- deployment for heroku ends above this line -->


<details>
<summary><b>AWS</b></summary>
<br>
<ol>
<li>

Create account at [AWS](aws.amazon.com)
</li>
<li>
Navigate to S3 and create bucket
</li>
<li>
Enter a bucket name
</li>
<li>
Ensure 'Block All Public Access' is unticked
</li>
<li>
Click create bucket
</li>
<li>
Navigate to properties and edit static website hosting
</li>
<li>
Click enable and and give default index.html and error.html values, then click save
</li>
<li>
Navigate to permissions and update CORS values as shown in image

![aws](documentation/deployment/aws-cors.webp)
</li>
<li>
Edit bucket policy
</li>
<li>
Generate policy
</li>
<li>
Ensure ACLs is enabled and save
</li>
<li>
Ensure ACL is set to 'list' and save
</li>
<li>
Create User Group
</li>
<li>
Attach policy Group
</li>
<li>
Import AmazonS3FullAccessPolicy
</li>
<li>
Review and create policy
</li>
<li>
Create User and add to Group
</li>
</ol>
</details>

<!-- AWS deployment ends above this line -->


<details>
<summary><b>Stripe</b></summary>
<br>
<ol>
<li>

Sign up for an account at [Stripe](https://stripe.com/en-nl)
</li>
<li>
Navigate to the developer page
</li>
<li>
Save the API keys as config variables in heroku (STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET)
</li>
<li>
Set up the event listeners for webhooks and add endpoint
</li>
</ol>
<br>
<br>
<br>
</details>

<br>

[Back to Top](#chocelegance)

<!--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- CREDITS SECTION -->
<br>
<br>
<br>

## Credits

An overview of materials referenced and images used during the development of the project is shown below.

<!-- The Credits section is shown below, this will be disaplyed in a collapsible format, with a sub section for reference content/materials and a sub section for images, with each item shown in tabular form -->
<details>
    <summary><b>Reference Materials Used</b></summary>
<br>
<table>
<tr><th><b> Description </b></th><th><b> Link </b></th></tr>
<!-- Reference Material 1 begins -->
<tr><td> Code Institute 'Boutique Ado' Walkthrough Project </td>
<td> 

[here](https://codeinstitute.net/) 

</td></tr>
<!-- Reference Material 1 ends -->
<tr><td> Code Institute PP5 Walkthrough Video, by Kasia Bogucka</td>
<td> 

[here](https://youtu.be/i7clFOYiwS0)  

</td></tr>
<!-- spacer -->
<tr><td> Code Institute README.md guide, by Kasia Bogucka</td>
<td> 

[here](https://youtu.be/l1DE7L-4eKQ?si=YlDWOkkzvTBjbgs3)

</td></tr>
<!-- spacer -->
<tr><td> Code Institute E-Commerce Guide to MVP, by Kasia Bogucka </td>
<td> 

[here](https://youtu.be/i7clFOYiwS0) 

</td></tr>
<!-- spacer -->
<tr><td> Chocolate descriptions, about texxt and images used across site, www.puccinibomboni.com </td>
<td> 

[here](https://puccinibomboni.com/)

</td></tr>
<!-- spacer -->
<tr><td> Guide on using the transform property, published by geeksforgeeks.org </td>
<td> 

[here](https://www.geeksforgeeks.org/how-to-rotate-an-html-div-element-90-degrees-using-javascript/)

</td></tr>
<!-- spacer -->
<tr><td> Boostrap carousel implentation in Django, by Stackoverflow user simopopov </td>
<td> 

[here](https://stackoverflow.com/questions/27219078/bootstrap-carousel-implementation-in-django)  

</td></tr>
<!-- spacer -->
<tr><td> Advice on Python 'setup.py egg_info' error, by Github user ocona </td>
<td> 

[here](https://github.com/openai/openai-cookbook/issues/154)  

</td></tr>
<!-- spacer -->
<tr><td> Slide effect on bootstrap dropdown menus, by Stackoverflow user cogell </td>
<td> 

[here](https://stackoverflow.com/questions/12115833/adding-a-slide-effect-to-bootstrap-dropdown)  

</td></tr>
<!-- spacer -->
<tr><td> How to style a checkbox, published by www.sentry.io </td>
<td> 

[here](https://sentry.io/answers/how-to-style-a-checkbox-using-css/)

</td></tr>
<!-- spacer -->
<tr><td> How to style a Bootstrap accordion, by Stackoverflow user Sahil Dhir </td>
<td> 

[here](https://stackoverflow.com/questions/75398511/style-header-of-bootstrap-accordion-that-has-the-class-collapse-show)  

</td></tr>
<!-- spacer -->
<tr><td> Text used for user testimonials, published by www.thehappychocolatier.com </td>
<td> 

[here](https://www.thehappychocolatier.com/testimonials/)

</td></tr>
<!-- spacer -->
<tr><td> Change style of carousel control buttons, by Stackoverflow user nifoem bar </td>
<td> 

[here](https://stackoverflow.com/questions/46249541/change-arrow-colors-in-bootstraps-carousel)  

</td></tr>
<!-- spacer -->

<tr><td> Thread on hiding parent elements with onclick function, by Stackoverflow user DextrousDave </td>
<td> 

[here](https://stackoverflow.com/questions/17399897/hide-parent-element-with-onclick-function)

</td></tr>
<!-- spacer -->
<tr><td> Tutorial on creating product reviews in Django, by YouTube channel 'Code With Stein' </td>
<td> 

[here](https://www.youtube.com/watch?v=8iCqlFyFu2s)

</td></tr>
<!-- spacer -->
</td></tr>
<tr><td> Rounding a value in a DTL variable, by Stackoverflow user arulmr </td>
<td> 

[here](https://stackoverflow.com/questions/18185351/how-can-i-round-a-value-in-django-template-without-using-the-filter)

</td></tr>
<!-- spacer -->
<tr><td> Text used for FAQs section in About page, published by www.chocolatecompany.nl </td>
<td> 

[here](https://www.chocolatecompany.nl/en/service/faq/) 

</td></tr>
<!-- spacer -->
<tr><td> Code Institute README.md Template, published by Code Institute </td>
<td> 

[here](https://github.com/Code-Institute-Solutions/readme-template)  

</td></tr>
<!-- spacer -->
<tr><td> Github README.md Markdown Guide, by Github user lifeparticle </td>
<td> 

[here](https://github.com/lifeparticle/Markdown-Cheatsheet)  

</td></tr>
<!-- spacer -->
<tr><td> Github README.md Cheatsheet, by Github user tchapi </td>
<td> 

[here](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md)

</td></tr>
<!-- spacer -->
<tr><td> The hex values of the Github background colour were obtained using imagecolorpicker.com </td>
<td> 

[here](https://imagecolorpicker.com/en)

</td></tr>
<!-- spacer -->
<tr><td> How to create anchor links in README.md, by Github user Rachel Hyman </td>
<td> 

[here](https://gist.github.com/rachelhyman/b1f109155c9dafffe618)  

</td></tr>
<!-- spacer -->
<tr><td> How to add collapsible items to README.md, by Github user pierrejoubert73 </td>
<td> 

[here](https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab)

</td></tr>
<!-- spacer -->
</td></tr>
<tr><td> Advice to add documentation folder to README.md, Code Institute Slack message by Kera Cudmore </td>
<td> 

[here](https://code-institute-room.slack.com/archives/C01UE4ND3H7/p1701601763768449?thread_ts=1701600346.836459&cid=C01UE4ND3H7)

</td></tr>
<!-- spacer -->
<tr><td> How to add a tickmark to README.md, by Stackoverflow user Waylan </td>
<td> 

[here](https://stackoverflow.com/questions/54694160/adding-checkbox-in-markdown-table-does-not-work)

</td></tr>
<!-- spacer -->
<tr><td> Sticky footer guide, published by www.css-tricks.com </td>
<td> 

[here](https://css-tricks.com/a-clever-sticky-footer-technique/)

</td></tr>
<!-- spacer -->
<tr><td> Site used to convert png to favicon, favicon.io </td>
<td> 

[here](https://realfavicongenerator.net/)

</td></tr>
<!-- spacer -->
<tr><td> Guide to making atomic git commits, by Aleksandr Hovhannisyan </td>
<td> 

[here](https://www.aleksandrhovhannisyan.com/blog/atomic-git-commits/)

</td></tr>
<!-- spacer -->
<tr><td> Library of front end icons used for README.md, by Github user marwin1991 </td>
<td> 

[here](https://marwin1991.github.io/profile-technology-icons/)

</td></tr>
<!-- spacer -->
<tr><td> Site containing open source icons used for README.md, published by iconduck.com </td>
<td> 

[here](https://iconduck.com/)

</td></tr>
<!-- spacer -->
<tr><td> Site used to convert svg to png, svgtopng.com </td>
<td> 

[here](https://svgtopng.com/)

</td></tr>
<!-- spacer -->
<tr><td> How to make a cell span a row, used in README.md, by Stackoverflow user Nisse Engström </td>
<td> 

[here](https://stackoverflow.com/questions/26400006/make-a-td-span-the-entire-row-in-a-table)

</td></tr>
<!-- spacer -->
<tr><td> Site used to generate sitemap.xml </td>
<td> 

[here](https://www.xml-sitemaps.com/)

</td></tr>
<!-- spacer -->
<tr><td> Adding admin panel to a DTL url, by Stackoverflow user Arpit Solanki </td>
<td> 

[here](https://stackoverflow.com/questions/45122421/refer-to-admin-site-using-url-admin-in-app-django)

</td></tr>
<!-- spacer -->
<tr><td> Udemy Masterclass course, by instructor Ashutosh Pawar </td>
<td> 

[here](https://uber.udemy.com/course/django-course/learn/lecture/16355734#overview)

</td></tr>
<!-- spacer -->
<tr><td> Guide on the syntax for CSS animations, published by w3schools.com </td>
<td> 

[here](https://www.w3schools.com/cssref/css3_pr_animation.php)

</td></tr>
<!-- spacer -->
<tr><td> Solution to Django email error (runtime.txt fix), in Code Institute Slack channel, by Roman Rakic </td>
<td> 

[here](https://code-institute-room.slack.com/archives/C026VTHQDNY/p1711548670431029?thread_ts=1711547601.933219&cid=C026VTHQDNY)

</td></tr>
<!-- spacer -->
<tr><td> Tips on installing GraphViz, in Code Institute Slack channel, by Sean Young_Hackteam
 </td>
<td> 

[here](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1618224655315000?thread_ts=1618179147.312700&cid=C7HS3U3AP)

</td></tr>
<!-- spacer -->
<tr><td> Tips on saving favicon in static folder, in Code Institute Slack channel, by Jo Heyndels
 </td>
<td> 

[here](https://code-institute-room.slack.com/archives/C7EJUQT2N/p1667981758347029?thread_ts=1667981265.461969&cid=C7EJUQT2N)

</td></tr>
<!-- spacer -->
<tr><td> Tips on fixing JS quantity form bug, in Code Institute Slack channel, by Ed Bradley
 </td>
<td> 

[here](https://code-institute-room.slack.com/archives/C7EJUQT2N/p1668538758607109?thread_ts=1668535011.445709&cid=C7EJUQT2N)

</td></tr>
<!-- spacer -->
<tr><td> How to set max and min validators in model field, by Stackoverflow user Tom
 </td>
<td> 

[here](https://stackoverflow.com/questions/42425933/how-do-i-set-a-default-max-and-min-value-for-an-integerfield-django)

</td></tr>
<!-- spacer -->
<tr><td> How to allow only positive decimal numbers in model field, by Stackoverflow user Alasdair
 </td>
<td> 

[here](https://stackoverflow.com/questions/12384460/allow-only-positive-decimal-numbers)

</td></tr>
<!-- spacer -->
<tr><td> Tip on using incognito mode for Lighthouse testing to eliminate errors caused by extensions, in Code Institute Slack channel, by Niki Tester
 </td>
<td> 

[here](https://code-institute-room.slack.com/archives/C7HD37Q1F/p1679439880325099?thread_ts=1679428205.806569&cid=C7HD37Q1F)

</td></tr>
<!-- spacer -->
<!-- spacer -->
<tr><td> Solution to duplicate ID/Class HTML validation error in 'Add Chocolate' and 'Edit Chocolate' pages, by Code Institute Student Katie Dunne (see resolved bugs section in the linked repository)
 </td>
<td> 

[here](https://github.com/KSDunne/summit_style)

</td></tr>
<!-- spacer -->






<!-- TABLE ENDS BELOW THIS LINE! -->
</table>
<br>
<br>
<br>
</details>
<!-- Reference Materials credits section ends here -->


<!-- The Images sub section is shown below, this will be disaplyed in a collapsible format, with each item shown in tabular form, the images represent thumbnails of the actual pictures used on the live site (they've been scaled down to 10% of the original size, approx 50px by 50px) -->
<details>
  <summary><b>Images</b></summary>
<br>

<table>
<tr><th><b> Image </b></th><th><b> Production File Name </b></th><th><b> Source </b></th></tr>
<!-- image 1 begins -->
<tr><td width="50">

![dark-choc-gluten-free-coffee-date-final](documentation/image_credits/dark-choc-gluten-free-coffee-date-final.webp)
</td>
<td>dark-choc-gluten-free-coffee-date-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/coffee)
</td>
</tr>
<!-- image 1 ends -->
<tr><td width="50">

![miss_image_1_thumb](documentation/image_credits/dark-choc-gluten-free-cognac-crown-final.webp)
</td>
<td>dark-choc-gluten-free-cognac-crown-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/cognac)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_2_thumb](documentation/image_credits/milk-choc-gluten-free-cranberry-zombie-final.webp)
</td>
<td>milk-choc-gluten-free-cranberry-zombie-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/cranberry)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_3_thumb](documentation/image_credits/milk-choc-gluten-free-manjari-magic-final.webp)
</td>
<td>milk-choc-gluten-free-manjari-magic-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/manjari)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_4_thumb](documentation/image_credits/white-choc-gluten-free-currant-crunch-final.webp)
</td>
<td>white-choc-gluten-free-currant-crunch-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/rum-currant)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_5_thumb](documentation/image_credits/white-choc-gluten-free-vanilla-victory-final.webp)
</td>
<td>white-choc-gluten-free-vanilla-victory-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/vanilla-poppyseed)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_6_thumb](documentation/image_credits/dark-choc-keto-amarena-delight-final.webp)
</td>
<td>dark-choc-keto-amarena-delight-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/amarena-cherry)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_7_thumb](documentation/image_credits/dark-choc-keto-caramel-fusion-final.webp)
</td>
<td>dark-choc-keto-caramel-fusion-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/caramel)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_8_thumb](documentation/image_credits/milk-choc-keto-apple-embrace-final.webp)
</td>
<td>milk-choc-keto-apple-embrace-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/apple)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_9_thumb](documentation/image_credits/milk-choc-keto-plum-paradise-final.webp)
</td>
<td>milk-choc-keto-plum-paradise-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/plum)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_10_thumb](documentation/image_credits/white-choc-calvados-final.webp)
</td>
<td>white-choc-calvados-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/calvados)
</td>
</tr>
<!-- Miss Images end here -->
<!-- Goal Images start here -->
<tr><td width="50">

![goal_image_0_thumb](documentation/image_credits/white-choc-limoncello-liaison-final.webp)
</td>
<td>white-choc-limoncello-liaison-final</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/limoncello)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_1_thumb](documentation/image_credits/dark-choc-vegan-thyme-adventure-updated.webp)
</td>
<td>dark-choc-vegan-thyme-adventure-updated</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/thyme)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_2_thumb](documentation/image_credits/dark-choc-vegan-walnut-wonder-updated.webp)
</td>
<td>dark-choc-vegan-walnut-wonder-updated</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/walnut)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_3_thumb](documentation/image_credits/milk-choc-vegan-pepper-surprise-updated.webp)
</td>
<td>milk-choc-vegan-pepper-surprise-updated</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/pepper)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_4_thumb](documentation/image_credits/milk-choc-vegan-plush-pecan-updatedl.webp)
</td>
<td>milk-choc-vegan-plush-pecan-updated</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/pecan)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_5_thumb](documentation/image_credits/white-choc-vegan-currant-affair-updated.webp)
</td>
<td>white-choc-vegan-currant-affair-updated</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/rum-currant)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_6_thumb](documentation/image_credits/white-choc-vegan-villianous-vanilla-updated.webp)
</td>
<td>white-choc-vegan-villianous-vanilla-updated</td>

<td>

[here](https://puccinibomboni.com/en/bonbon/vanilla-poppyseed)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_7_thumb](documentation/image_credits/hero-image-credit.webp)
</td>
<td>hero-image</td>

<td>

[here](https://www.freepik.com/free-photo/closeup-shot-chocolate-candy-isolated_15520864.htm#fromView=search&page=1&position=50&uuid=eb6bdc3a-bad6-494e-adec-5352ef9d1007)
</td>
</tr>
<!-- spacer -->

<!-- spacer -->
</table>
<br>
<br>
<br>
</details>
<!-- Images credits end here -->


<br>

[Back to Top](#chocelegance)

<!--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ACKNOWLEDGEMENTS SECTION -->
<br>
<br>
<br>

## Acknowledgements
