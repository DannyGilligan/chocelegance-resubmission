## Chocelegance

![hero image](documentation/readme-hero-image.webp)

<br>
<br>
<br>

## Table of Contents

* [Introduction](#introduction)
* [Business Model](#business-model)
* [Features](#features)
* [Design](#design)
* [User Stories](#user-stories)
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
The project is an e-Commerce platform that allows an artisan chocolatier to sell hand crafted chocolates for customers with specific dietary requirements (such as Keto, Vegan and Gluten-Free requirements). The features include the ability to make purchases directly from the site, registering a user profile and email verification, generating email confirmations upon successful purchases, security protocols preventing access to unauthorised views/pages and CRUD functionality for superusers.
<br><br>
The site was built using the Django framework, HTML 5, CSS 3, Javascript, Bootstrap, Python, Heroku, ElephantSQL, Stripe and AWS.
<br><br>
A link to the deployed site can be found [here](https://chocelegance-resubmission-4fbe05dd3cfa.herokuapp.com/).

<br>

[Back to Top](#chocelegance)

<br>
<br>
<br>

## Business Overview

Business and customer goals, marketing and Facebook mockup.

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

There are several chocolate makers in Amsterdam with an online presence and established customer base. These are well entrenched competitiors with diverse product ranges. Some examples are listed below:
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
Of the competitors listed above, Puccini has been used as a source of inspiration for the Chocelegance site. The images and descriptions present on their site have been used for the purposes of this project.
<br><br>
All images have been credited in the credits section.
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
6 custom models were developed for the project:
<br>
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
This model holds all the relevant details about the chocolates sold on the site. This model can be created, updated, edited and deleted by a superuser directly from the site without the need to log in to the admin panel. Located in 'Chocolate' app.
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
This model holds the testimonials that are injected into the home page carousel. This content is updated in the admin panel by a superuser. Located in 'Home' app.
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



<!-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- TECHNOLOGIES USED SECTION -->

## Technologies Used 

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
<td>App hosting</td>
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



## Credits

## Acknowledgements
