## Chocelegance

![hero image](documentation/readme-hero-image.webp)

<br>
<br>
<br>

## Table of Contents

* [Introduction](#introduction)
* [Business Overview](#business-overview)
* [Design](#design)
* [User Stories](#user-stories)
* [Features](#features)
* [Bugs](#bugs)
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
<br><br>

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

There are several chocolate makers in the Netherlands with an online presence and established customer base. These are well entrenched competitiors with diverse product ranges. Some examples are listed below:
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
<summary>  <i>Newsletter</i> </summary>
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
<summary>  <i>Facebook Page</i> </summary>
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
  <summary> Sign Up Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-sign-up.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Email Verification Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-verify-email.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Confirm Email Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-confirm-email.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Sign In Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-sign-in.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Home Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-home-page.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Main Chocolates Menu </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-main-chocolates-menu.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Chocolate Details Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-chocolates-details.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Shopping Cart </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-shopping-cart.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Checkout Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-checkout-page.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Order Confirmation </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-order-confirmation.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Add Chocolate Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-add-chocolate.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> Edit Chocolate Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-edit-chocolate.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> About Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-about-page.webp)
</details>
<!-- Wireframe ends -->

<!-- Wireframe begins -->
<details>  
  <summary> User Profile Page </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>

![Wireframe_01](documentation/wireframes/wireframe-about-page.webp)
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







## User Stories







## Manual Testing

Responsive, browser compatibility, bugs (resolved and unresolved), Lighthouse testing, code validation, user story testing, features testing.


### Resolved Bugs

When trying to install Django AllAuth 0.41.0 I ran into the error message below<br>
"Python setup.py egg_info did not run successfully when installing"<br>
This was preventing me from installing the correct AllAuth package, after trying different approaches such as installing different versions of Django and Python, I found a post that suggested installing a specific version of 'Setuptools', I installed Setuptools version 67.4.0 which appears to have resolved the issue regarding the AllAuth installation

https://github.com/openai/openai-cookbook/issues/154

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
<tr><td>
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

Prerequisties, installs, IDE, deployments, forking, cloning, heroku, AWS, Stripe.





[Back to Top](#chocelegance)

<!--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Required Installs-->
<br>
<br>
<br>

### Required Installs

Django 3.2.25<br>
Django AllAuth 0.14.0<br>
asgiref==3.8.1<br>
django-crispy-forms==1.14.0<br>
oauthlib==3.2.2<br>
pillow==10.3.0<br>
python3-openid==3.2.0<br>
pytz==2024.1<br>
requests-oauthlib==2.0.0<br>
setuptools==67.4.0<br>
sqlparse==0.5.0<br>
stripe==9.9.0<br>



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
<tr><td> Code used for spherical shading on main button developed by 'The Anonymous Koder' </td>
<td> 

[here](https://codepen.io/theanonymouskoder/pen/PomjmeY?editors=1100)  

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
