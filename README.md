## Chocelegance

![hero image](documentation/readme-hero-image.webp)
<br>
<br>
<br>

## Table of Contents

* [Introduction](#introduction)
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
<br>


## Introduction

Chocelegance if the 5th and final project submission as part of the Code Institute DIploma in Full Stack Software Development.
<br><br>
It is an e-Commerce platform that allows an artisan chocolatier to sell hand crafted chocolates for customers with specific dietary requirements (such as Keto, Vegan and Gluten-Free requirements). The features include the ability to make purchases directly from the site, register a user profile, generating email notifications upon successful registration or successful purchases, security protocols preventing access to unauthorised views/pages and CRUD functionality for superusers.
<br><br>
The site was built using the Django framework, HTML 5, CSS 3, Javascript, Bootstrap, Python, Heroku, Stripe and AWS.
<br>
<br>
<br>

## Business Model

Business and customer goals, marketing and Facebook mockup.


<!--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- DESIGN SECTION -->

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
This model holds the questions and answers that are displayed to the user in the 'About' page. This content is updated by the superuser directly from the admin panel.
</li>
<br>
<li>
<b>ChocolateReview Model</b>
This model holds the chocolate reviews that are added by the user in the chocolate details page. The reviews are submitted with the 'publish' status set to 'No', once reviewed by the superuser in the admin panel, the 'publish' status can then be set to 'Yes', which will trigger the review to be displayed on the site.
</li>
<br>
<li>
<b>Chocolate Model</b>
This model holds all the relevant details about the chocolates sold on the site. This model can be created, updated, edited and deleted by a superuser directly from the site without the need to log in to the admin panel.
</li>
<br>
<li>
<b>ChocolateCategory Model</b>
This model holds the different categories of chocolates sold on the site (e.g Dark Vegan Chocolate, Milk Gluten-Free Chocolate etc). These values are updated from the admin panel.
</li>
<br>
<li>
<b>Testimonial Model</b>
This model holds the testimonials that are injected into the home page carousel. This content is updated in the admin panel by a superuser.
</li>
<br>
<li>
<b>DietaryType Model</b>
This model holds the different dietary types that are catered to (e.g Keto, Vegan, Gluten-Free). This content is updated in the admin panel by a superuser.
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


[Back to Top](#chocelegance)
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


## Technologies Used

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
