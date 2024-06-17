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
The business is operated by a small team of artisan chocolatiers who share a passion for the nuances involved in fine chocolate making, and want to share this passion with a niche set of customers that are not well served by the current offerings on the market.
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
The marketing strategy will initially include a newsletter subscription, and a Facebook page. Content will be published on a weekly basis, with the goal of creating rich and engaging media that has potential to be organically 'shareable' on social media.
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

The campaign in Mailchimp stores all user email address to be included in future newsletter publications.

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
It would also serve as a way for customers to contact Chocelegance directly with any queries.
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
<details>  
  <summary> <i>Enter Username</i> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>
<!-- Wireframe 1 1 begins -->
The initial landing page will display the 'FIFA Women's World Cup Quiz 2023' logo, along with an input field to enter a username, and an 'enter' button. 

Validation will occur here, if the username does not meet the requirements a dialogue box will be displayed. If the input is accepted, the value will be assigned to a 'userName' variable.

The 'Enter' button will run the validation function and display the 'Quiz Rules' screen.

To note, the quiz will exist on a single page of HTML, with different sections being displayed to, or hidden from, the user depending on the context.

![Wireframe_01](assets/documentation/wireframe01_enter_username.webp)
</details>
<!-- Wireframe 1 ends -->

</details>
<!-- Wireframe section ends here -->


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
<br>
6 custom database models were developed for the project:
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

<!-- The Credits section is shown below, this will be disaplyed in a collapsible format, with a sub section for reference content/materials and a sub section for images, with each item shown in tabular form -->
<details>
    <summary><b>Reference Materials Used</b></summary>
<br>
<table>
<tr><th><b> Description </b></th><th><b> Link </b></th></tr>
<!-- Reference Material 1 begins -->
<tr><td> Code Institute LMS Javascript Essentials Content </td>
<td> 

[here](https://codeinstitute.net/) 

</td></tr>
<!-- Reference Material 1 ends -->
<tr><td> Javascript tutorial video produced by 'Bro Code' YouTube Channel</td>
<td> 

[here](https://www.youtube.com/watch?v=8dWL3wF_OMw)  

</td></tr>
<!-- spacer -->
<tr><td> Javascript 30 for 30 tutorials produced by Wes Bos</td>
<td> 

[here](https://javascript30.com/)

</td></tr>
<!-- spacer -->
<tr><td> W3 Schools Javascript Tutorial, Exercises and Quiz, published by w3schools.com </td>
<td> 

[here](https://www.w3schools.com/js/default.asp) 

</td></tr>
<!-- spacer -->
<tr><td> JS Challenger exercises, published by jschallenger.com </td>
<td> 

[here](https://www.jschallenger.com/)

</td></tr>
<!-- spacer -->
<tr><td> Guide on using the transform property, published by geeksforgeeks.org </td>
<td> 

[here](https://www.geeksforgeeks.org/how-to-rotate-an-html-div-element-90-degrees-using-javascript/)

</td></tr>
<!-- spacer -->
<tr><td> Code Institute README.md Tutorial by Kasia Bogucka </td>
<td> 

[here](https://www.youtube.com/watch?v=l1DE7L-4eKQ)  

</td></tr>
<!-- spacer -->
<tr><td> Code Institute Guide to MVP (PP2) by Kasia Bogucka </td>
<td> 

[here](https://www.youtube.com/watch?v=wsOvkf22B_A)  

</td></tr>
<!-- spacer -->
<tr><td> Official FIFA 2023 Women's World Cup colour scheme published by schemecolor.com </td>
<td> 

[here](https://www.schemecolor.com/fifa-womens-world-cup-2023-logo.php)  

</td></tr>
<!-- spacer -->
<tr><td> Official FIFA 2023 Women's World Cup font, downloaded from fontshub.pro </td>
<td> 

[here](https://fontshub.pro/font/fwwc-2023-download)

</td></tr>
<!-- spacer -->
<tr><td> Flexbox guide, published by css-tricks.com </td>
<td> 

[here](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)  

</td></tr>
<!-- spacer -->
<tr><td> Guide to self-hosting fonts, published by Kevin Powell </td>
<td> 

[here](https://www.youtube.com/watch?v=zK-yy6C2Nck)

</td></tr>
<!-- spacer -->
<tr><td> Centering items using Flexbox, published by MDN Web Docs </td>
<td> 

[here](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Aligning_items_in_a_flex_container)  

</td></tr>
<!-- spacer -->
<tr><td> Code used for spherical shading on main button developed by 'The Anonymous Koder' </td>
<td> 

[here](https://codepen.io/theanonymouskoder/pen/PomjmeY?editors=1100)  

</td></tr>
<!-- spacer -->
<tr><td> Code used for CSS gradient effects provided by cssgradient.io </td>
<td> 

[here](https://cssgradient.io/)

</td></tr>
<!-- spacer -->
<tr><td> Guide for using the CSS 'fade in' animation, published by Jamie Juviler </td>
<td> 

[here](https://blog.hubspot.com/website/css-fade-in)

</td></tr>
<!-- spacer -->
</td></tr>
<tr><td> Guide on scaling an element up and down gracefully on hover, by Stackoverflow user Roy </td>
<td> 

[here](https://stackoverflow.com/a/36227036)

</td></tr>
<!-- spacer -->
<tr><td> Guide for styling input placeholder text, published by MDN Web Docs </td>
<td> 

[here](https://developer.mozilla.org/en-US/docs/Web/CSS/::placeholder) 

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
<tr><td> Github emojis cheatsheet, by Github user ikatyang </td>
<td> 

[here](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

</td></tr>
<!-- spacer -->
<tr><td> Site used to convert png to favicon, favicon.io </td>
<td> 

[here](https://favicon.io/favicon-converter/)

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
<tr><td> Introduction to the pillars of OOP, by Chandrakishor Gupta </td>
<td> 

[here](https://datatrained.com/post/four-pillars-of-oops/)

</td></tr>
<!-- spacer -->
<tr><td> Guide on HTML Radio Input Tags, published by w3schools.com </td>
<td> 

[here](https://www.w3schools.com/tags/att_input_type_radio.asp)

</td></tr>
<!-- spacer -->
<tr><td> How to use a submit button outside the form, by joshbranchaud </td>
<td> 

[here](https://til.hashrocket.com/posts/v2s2gxgifj-submit-a-form-with-a-button-outside-the-form)

</td></tr>
<!-- spacer -->
<tr><td> Guide to mobile first responsive design, published by Code Institute </td>
<td> 

[here](https://www.youtube.com/watch?v=JcaX60ZscgA)

</td></tr>
<!-- spacer -->
<tr><td> Guide to displaying a 'flash' effect animation, by Stackoverflow user Rohith </td>
<td> 

[here](https://stackoverflow.com/questions/16791851/a-flash-of-color-using-pure-css-transitions)

</td></tr>
<!-- spacer -->
<tr><td> Guide on adding minlength and maxlength HTML attributes, published by MDN Web Docs </td>
<td> 

[here](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/minlength)

</td></tr>
<!-- spacer -->
<tr><td> Guide on the syntax for CSS animations, published by w3schools.com </td>
<td> 

[here](https://www.w3schools.com/cssref/css3_pr_animation.php)

</td></tr>
<!-- spacer -->
<tr><td> How to add whitespace characters to README.md, by Stackoverflow user Tim Smith </td>
<td> 

[here](https://stackoverflow.com/questions/44810511/how-to-add-empty-spaces-into-md-markdown-readme-on-github)

</td></tr>
<!-- spacer -->
<tr><td> How to align text in table headers in README.md markdown, published by markdownguide.org </td>
<td> 

[here](https://www.markdownguide.org/extended-syntax/)

</td></tr>
<!-- spacer -->
</table>
</details>
<!-- Reference Materials credits section ends here -->


<!-- The Images sub section is shown below, this will be disaplyed in a collapsible format, with each item shown in tabular form, the images represent thumbnails of the actual pictures used on the live site (they've been scaled down to 10% of the original size, approx 50px by 50px) -->
<details>
  <summary><b>Images</b></summary>
<br>

<table>
<tr><th><b> Thumb </b></th><th><b> Production File Name </b></th><th><b> Source </b></th></tr>
<!-- image 1 begins -->
<tr><td width="50">

![dark-choc-gluten-free-coffee-date-final](documentation/image_credits/dark-choc-gluten-free-coffee-date-final.webp)
</td>
<td>dark-choc-gluten-free-coffee-date-final</td>

<td>

[here](https://www.sbs.com.au/news/article/what-must-happen-for-matildas-to-progress-to-world-cup-knockout/hn6ggt6eq)
</td>
</tr>
<!-- image 1 ends -->
<tr><td width="50">

![miss_image_1_thumb](assets/documentation//thumbnails/miss_image_1_thumbnail.webp)
</td>
<td>miss_image_1</td>

<td>

[here](https://www.ctvnews.ca/mobile/sports/italians-in-tears-after-loss-to-south-africa-knocks-them-out-of-women-s-world-cup-1.6503519)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_2_thumb](assets/documentation/thumbnails/miss_image_2_thumbnail.webp)
</td>
<td>miss_image_2</td>

<td>

[here](https://www.forbes.com/sites/maryroeloffs/2023/08/06/us-knocked-out-of-womens-world-cup-after-dramatic-loss-to-sweden/)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_3_thumb](assets/documentation/thumbnails/miss_image_3_thumbnail.webp)
</td>
<td>miss_image_3</td>

<td>

[here](https://www.forbes.com/sites/asifburhan/2023/08/16/england-defeat-hosts-australia-to-reach-first-womens-world-cup-final/)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_4_thumb](assets/documentation/thumbnails/miss_image_4_thumbnail.webp)
</td>
<td>miss_image_4</td>

<td>

[here](https://edition.cnn.com/sport/live-news/uswnt-sweden-womens-world-cup-knockout/h_9d56c79135d15aab65841753a8692a16)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_5_thumb](assets/documentation/thumbnails/miss_image_5_thumbnail.webp)
</td>
<td>miss_image_5</td>

<td>

[here](https://domesticolammy.medium.com/salma-paralluelo-and-my-uneven-connection-with-womens-football-a8a99bc4dd10)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_6_thumb](assets/documentation/thumbnails/miss_image_6_thumbnail.webp)
</td>
<td>miss_image_6</td>

<td>

[here](https://www.the-express.com/sport/soccer/109905/USWNT-lose-top-spot-FIFA-Rankings)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_7_thumb](assets/documentation/thumbnails/miss_image_7_thumbnail.webp)
</td>
<td>miss_image_7</td>

<td>

[here](https://www.foxsports.com.au/football/world-cup/changed-sport-forever-australia-reacts-to-matildas-devastating-world-cup-exit/news-story/de2c94a88de3019c2af2e7eae2f81774)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_8_thumb](assets/documentation/thumbnails/miss_image_8_thumbnail.webp)
</td>
<td>miss_image_8</td>

<td>

[here](https://www.bbc.com/sport/football/66611861)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_9_thumb](assets/documentation/thumbnails/miss_image_9_thumbnail.webp)
</td>
<td>miss_image_9</td>

<td>

[here](https://www.abc.net.au/news/2023-07-25/womens-world-cup-live-updates-new-zealand-philippines-var/102644612)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![miss_image_10_thumb](assets/documentation/thumbnails/miss_image_10_thumbnail.webp)
</td>
<td>miss_image_10</td>

<td>

[here](https://www.goal.com/en/news/shock-germany-out-womens-world-cup-group-stages-south-korea/bltb2277dcbc1244f38)
</td>
</tr>
<!-- Miss Images end here -->
<!-- Goal Images start here -->
<tr><td width="50">

![goal_image_0_thumb](assets/documentation/thumbnails/goal_image_0_thumbnail.webp)
</td>
<td>goal_image_0</td>

<td>

[here](https://www.theguardian.com/football/commentisfree/2023/aug/16/womens-world-cup-2023-matildas-fan-guide)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_1_thumb](assets/documentation/thumbnails/goal_image_1_thumbnail.webp)
</td>
<td>goal_image_1</td>

<td>

[here](https://www.flashscore.com/news/soccer-world-cup-women-south-africa-s-joy-at-women-s-world-cup-win-brings-hope-of-change-back-home/n9c0NhLj/)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_2_thumb](assets/documentation/thumbnails/goal_image_2_thumbnail.webp)
</td>
<td>goal_image_2</td>

<td>

[here](https://www.latimes.com/sports/soccer/story/2023-08-19/womens-world-cup-sweden-beats-australia-bronze-medal)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_3_thumb](assets/documentation/thumbnails/goal_image_3_thumbnail.webp)
</td>
<td>goal_image_3</td>

<td>

[here](https://eu.usatoday.com/story/sports/soccer/2023/08/11/sweden-stakes-claim-as-a-women-s-world-cup-favorite-by-stopping-japan-2-1-in-quarterfinals/70572973007/)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_4_thumb](assets/documentation/thumbnails/goal_image_4_thumbnail.webp)
</td>
<td>goal_image_4</td>

<td>

[here](https://newsrnd.com/sports/2023-08-08-france-morocco-(4-0)--les-bleues-join-the-quarters-of-the-women-s-world-cup-without-trembling.BJXjfpknn.html)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_5_thumb](assets/documentation/thumbnails/goal_image_5_thumbnail.webp)
</td>
<td>goal_image_5</td>

<td>

[here](https://www.nzherald.co.nz/sport/fifa-womens-world-cup-2023-football-ferns-crash-back-down-to-earth-with-shock-loss-to-the-philippines/PCDJNAO7SRCRTFMBTGIB5RNWNM/)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_6_thumb](assets/documentation/thumbnails/goal_image_6_thumbnail.webp)
</td>
<td>goal_image_6</td>

<td>

[here](https://www.skysports.com/football/story-telling/37390/12944561/20-of-the-best-images-from-the-womens-world-cup)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_7_thumb](assets/documentation/thumbnails/goal_image_7_thumbnail.webp)
</td>
<td>goal_image_7</td>

<td>

[here](https://www.forbes.com/sites/asifburhan/2020/03/02/fifa-inspectors-assess-potential-hosts-of-the-2023-womens-world-cup/)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_8_thumb](assets/documentation/thumbnails/goal_image_8_thumbnail.webp)
</td>
<td>goal_image_8</td>

<td>

[here](https://www.theguardian.com/football/2023/jul/27/brazil-womens-world-cup-fans-france-revival)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_9_thumb](assets/documentation/thumbnails/goal_image_9_thumbnail.webp)
</td>
<td>goal_image_9</td>

<td>

[here](https://shekicks.net/matildas-end-lionesses-30-game-unbeaten-run/)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![goal_image_10_thumb](assets/documentation/thumbnails/goal_image_10_thumbnail.webp)
</td>
<td>goal_image_10</td>

<td>

[here](https://www.uefa.com/womensworldcup/news/0283-1876eee8e56e-635398217fd4-1000--republic-of-ireland-at-the-2023-women-s-world-cup-fixtures-r/)
</td>
</tr>
<!-- Goal images end here -->
<!-- Miscellaneous images start here -->
<tr><td width="50">

![hero_image_updated_thumb](assets/documentation/thumbnails/official_logo_thumbnail.webp)
</td>
<td>hero_image_updated</td>

<td>

[here](https://www.printmag.com/branding-identity-design/2023-fifa-womens-world-cup/)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![favicon_source_thumb](assets/documentation/thumbnails/favicon_source_thumbnail.webp)
</td>
<td>favicon</td>

<td>

[here](https://seeklogo.com/vector-logo/495259/fifa-womens-world-cup-2023)
</td>
</tr>
<!-- spacer -->
<tr><td width="50">

![favicon_source_thumb](assets/documentation/thumbnails/quiz_over_pic_thumb.webp)
</td>
<td>end_quiz_image</td>

<td>

[here](https://www.uefa.com/womensworldcup/news/027a-166817b8be17-9e0082e122cd-1000--spain-win-2023-women-s-world-cup-all-the-results/)
</td>
</tr>
<!-- spacer -->
</table>
</details>
<!-- Images credits end here -->



<br>
<br>
<br>










[Back to Top](#chocelegance)

<!--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ACKNOWLEDGEMENTS SECTION -->
<br>
<br>
<br>

## Acknowledgements
