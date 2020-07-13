TwinkChat - A basic chat application
==============

The Project will soon be updated and the bugs will be fixed

A web project based on real-time group chat system with a user friendly design.
(Availability Supports: PC/Mobile - Web)

Version
--------------

Developed on python v3


Features
==============

Test the app: https://twinkchat.herokuapp.com/
    
The app is designed and developed with these features:-

Index Page
-----------

    ->(Particle JS) On the index page particle js is used to make the design look cool enough on itself.
    ->(Gradient Background) The background automatically changes colour time to time.
    ->The whole page is made responsive to support both PC & Mobile view.

Sign Up Page
--------------

    ->(Fixed emails support) I have fixed the emails that could be used for the sign up process [This could be further added with a code verification system to verify the users].
    ->(Checks is Entered Data exists on DB) After the submit button is pressed the Username and Emails are checked in the DB and is they exists then the user will be notified with the message that the data already exists.
    ->(Encrypted Passwords) Insted of storing the password data as plane text the passwords are stored after they are encryped.

Sign In Page
--------------

    ->The page is designed as a simple sign in page that will verify and redirect User to the Chat page if they authentication is successful without any errors.
    ->Contact Developer lines are given on the same page to help Users connect directly with the developer in case of any query/problem.


Chat Page
----------

    ->(Unauthorised Access) This page is prevented to be accessed by any user if they are not logged in.
    ->(Responsive Design) The whole page is designed to support both mobile view and desktop view.
    ->(Multiple Groups) Insted of just having to chat on a single group, users can switch to multiple groups and chat on them.
    ->(Automated System Messages) When a user joins/leaves a group then a system message is passed to every person logged in on the same group with an alert that {user} has joined/left {group name}.


Cyber Attact Preventions
--------------------------
    ->A basic XSS protection is added on every page.
    ->A time delay is added to prevent Brute Force Attacks.


Possible Upgrades
===================

- Messages could be made persistent i.e. could be stored & accessed from the Data Base.
- On Sign Up page a verification code system could be added for the Emails. 
- No. of attemps that a User can take for Logging in could be limited to prevent Unauthorised Logins.

For any kind of bug please:

- Email: vaibhavmishra658@gmail.com 
- Twitter: https://www.twitter.com/imvaibhavmishra
- Instagram: https://www.instagram.com/itsvaibhavmishra
- LinkedIn: https://www.linkedin.com/in/itsvaibhavmishra

TwinkChat is still in development phase.

Any contribution is invited. 


