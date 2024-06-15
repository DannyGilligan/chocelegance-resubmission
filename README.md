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

Chocelegance if the 5th and final project submission as part of the Code Institute DIploma in Full Stack Software Engineering.
<br><br>
It is an e-Commerce platform built using the Django framework, HTML 5, CSS 3, Javascript, Python, Heroku, Stripe and AWS.
<br><br>
The site allows an artisan chocolatier to sell hand crafted chocolates for customers with specific dietary requirements (such as Keto, Vegan and Gluten-Free requirements).
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
<br>
<br>
<br>
</details>
<!-- Colour scheme section section ends above this line -->





<details>
<summary><b> Font </b></summary>



<tr><th> <b>Urbanist (from Google Fonts)</b> </th></tr>
<tr><td>
The site uses the 'Urbanist' front from Google Fonts. This font was chosen as I felt it's appearance was clean, crisp and modern and consistent with the Chocelegance brand.
</td></tr>
<tr><td>

![Chocelegance font](documentation/urbanist-font-example.webp)

</td></tr>
</table> 
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
The site was designed following the principles of mobile first design. All initial CSS style rules were implemented for use on mobile devices with a min-width screen size of 320px, from there the layout was adapted as needed for progressively larger screens using media queries.
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

<br>
<br>
<br>
</details>
<!-- Responsiveness section ends above this line -->



<!-- spacer -->
<details>
  <summary><b> Wireframes </b></summary>
<br>
<details>  
  <summary>  <i>Enter Username</i> </summary>  <!-- whitespace character used in heading '  ' to add indentation -->
<br>
<!-- Wireframe 1 1 begins -->
The initial landing page will display the 'FIFA Women's World Cup Quiz 2023' logo, along with an input field to enter a username, and an 'enter' button. 

Validation will occur here, if the username does not meet the requirements a dialogue box will be displayed. If the input is accepted, the value will be assigned to a 'userName' variable.

The 'Enter' button will run the validation function and display the 'Quiz Rules' screen.

To note, the quiz will exist on a single page of HTML, with different sections being displayed to, or hidden from, the user depending on the context.

![Wireframe_01](assets/documentation/wireframe01_enter_username.webp)
</details>
<!-- Wireframe 1 ends -->
<!-- Wireframe 2 begins -->
<details>
  <summary>  <i>Quiz Rules</i> </summary>
<br>
Once the username is accepted, the rules of the quiz will then be displayed using the displayRules() function.

In summary, there will be 11 questions related to the 2023 Women's World Cup, with 4 choices per question along with a VAR Assist feature that will remove 2 incorrect answers. The VAR Assist name comes from the 'Video Assistant Referee' which is a controversial technology used in football to assist in refereeing decisions (hopefully it will only do good things in this quiz). The user will be granted 3 VAR Assists at the beginning, and can use a max of 1 per question until they run out. (To disambiguate completely, there is no relationship to the VAR variable declaration keyword!)

When a question is answered correctly, the user will score a goal, otherwise the attempt will be considered a miss.

The button on this screen will have an inner text of 'Kick Off!' and will call a function to display the quiz content.

![Wireframe Quiz Rules](assets/documentation/wireframe02_display_rules.webp)
</details>
<!-- Wireframe 2 ends -->
<!-- Wireframe 3 begins -->
<details>
  <summary>  <i>Display Quiz</i> </summary>
<br>
After the user kicks off the quiz, the questions and choices will be displayed using the displayQuiz() function. 

The inner HTML of the question and choice containers will be driven by the content of an object data structure existing in the javascript file, the object will be assigned to a variable named quizEngine. A 'Questions' property will have associated string values that will be accessed using dot notation and their index numbers, this will also be the case for the 'Choices' property, except the Choices property will have a nested array of 4 string values at each index. A questionCounter variable will be created and incremented after each question to drive the content displayed to the user by iterating over the Question and Choices properties accordingly.

A radio input will be used to allow the user to submit their choice, when checking the answer the radio inputs will be assigned as a HTML collection to a userChoice variable, then an IF conditional statement will determine which input is checked, the checked input will be compared against the correct answer (which will be stored as a string value in an 'Answers' property of the quizEngine). The 'Goals Scored' variable will then be incremented by 1 if the answer is correct.

The main button on this screen will have an inner text of 'Shoot!' and will be assigned the checkAnswer() function. 

A VAR Assist button will also be displayed to the user along with the remaining assists available.

In the bottom right hand corner, a score tracker will be visible showing the user's current score.

Just below the logo, a progress tracker will be located that gives the user feedback on the current active question and the questions they answered correctly or incorrectly. The active question will be styled with a prominent glowing effect to aid accessibility.

![Display Quiz](assets/documentation/wireframe03_display_quiz.webp)
</details>
<!-- Wireframe 3 ends -->
<!-- Wireframe 4 begins -->
<details>
  <summary>  <i>VAR Assist Feature</i> </summary>
<br>
The user can decide to trigger the varAssist() feature in order to remove 2 wrong answers from the screen. A 'varAssists' property will be included in the quizEngine object, this property will have 2 choice IDs held as string values in an array at each index that correspond to the wrong answers for each question, these choice IDs will be used to access the related HTML elements and set the display attribute to 'none'. The 'VAR Assists remaining' counter will be decremented upon use until it reaches 0, at this point the VAR Assist button will be disabled for the remainder of the quiz.

Once a choice has been made by the user. the 'Shoot!' button will then trigger the checkAnswer() function.

![VAR Assist Feature](assets/documentation/wireframe04_var_assist_feature.webp)
</details>
<!-- Wireframe 4 ends -->
<!-- Wireframe 5 begins -->
<details>
  <summary>  <i>Check Answer</i> </summary>
<br>
Once the user has decided on their choice and selected the corresponding radio input, they can then trigger the checkAnswer() function by clicking on the 'Shoot!' button. This will then assign the radio inputs to a HTML collection by utilising the getElementsByClass method (the radio inputs will have a class attribute of 'choices'). 

This HTML collection will then be iterated over using a 'for loop' to determine which input has been checked (using an IF conditional statement). Once the checked input has been identified, this will be stored in a variable named userChoice, which will be compared against the corresponding correct answer for the question held in the 'Answers' property of the quizEngine object (this will be accessed using dot notation and assigned to a variable named correctAnswer).

If the userChoice and correctAnswer variables are equal (===), then feedback will be presented to the user with a 'GOAL!' message and a picture being displayed, the HTML element of the corresponding tracker item will be assigned a class of .correct and the colour will be changed to green (the .active class will be removed). The 'Goals Scored' counter will also be incremented by 1.

If the userChoice and correctAnswer variables are not equal, the feedback will be presented to the user with a 'MISS!' message and a picture being displayed, the HTML element of the corresponding tracker item will be assigned a class of .incorrect and the colour will be changed to red  (the .active class will be removed). The 'Goals Scored' counter will not be incremented. 

The inner HTML of the main button will change to 'Play On!' which when pressed will invoke a nextQuestion() function that will increment the questionCounter variable and display the content of the next question and set of choices to the user.

![Check Answer](assets/documentation/wireframe05_check_answer.webp)
</details>
<!-- Wireframe 5 ends -->
<!-- Wireframe 6 begins -->
<details>
  <summary>  <i>Display Next Question</i> </summary>
<br>
The nextQuestion() function will continue the process of iterating over the quizEngine object using the value of the questionCounter variable to access the corresponding index of the questions and choices to display until the final question has been reached. 

This function will also change the HTML class attribute of the current question to .active in order to give the glowing effect on the tracker panel.

When the last question has been answered, the nextQuestion() function will change the inner HTML of the main button to 'View Result!' instead of 'Play On!' and assign to it a function of displayResult().

![Display Next Question 1](assets/documentation/wireframe06_display_next_question(1).webp)
![Display Next Question 2](assets/documentation/wireframe06_display_next_question(2).webp)
</details>
<!-- Wireframe 6 ends -->
<!-- Wireframe 7 begins -->
<details>
  <summary>  <i>Display Result</i> </summary>
<br>
Once the last question has been answered, the user can click on the 'View Result!' button. This will display feedback to the user on the total goals scored out of the 11 attempts along with a text message congratulating the user on completing the quiz.

An image will also be displayed to the user.

The main button's inner HTML will be changed to 'Rematch!' and have a rematch() function assigned to it.

This screen is the end of the current quiz session.

![Display Result](assets/documentation/wireframe07_display_result.webp)
</details>
<!-- Wireframe 7 ends -->
<!-- Wireframe 8 begins -->
<details>
  <summary>  <i>Rematch</i> </summary>
<br>
The end screen prompts the user with a 'Rematch!' that will guide them back to the start screen.

This will effectively reset the quiz.

![Rematch](assets/documentation/wireframe08_rematch.webp)
</details>
<!-- Wireframe 8 ends -->
<!-- Wireframe 9 begins -->
<details>
  <summary>  <i>Whiteboard Wireframe</i> </summary>
<br>
A little bonus for the whiteboard lovers :cupid:
<br>
<br>

![Whiteboard Wireframe](assets/documentation/wireframe09_whiteboard.webp)
</details>
<!-- Wireframe 9 ends -->
</details>
<!-- Wireframe section ends here -->

[Back to Top](#fifa-2023-womens-world-cup-quiz)
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
