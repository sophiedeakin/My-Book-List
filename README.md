# My Book List 

**Link to website and IAMRESPONSIVE IMAGE**

# Introduction 

Welcome to My Book List, your go-to website for tracking books you are reading, completed and want to read in the future. This simple website helps you stay organised and motivates you to read more books or achieve personal goals.

---

# UX

## Strategy

### Target Audience 

For the target audience, my main focus was the book community who have a passion for reading and books. After researching other book review/tracking websites like Goodreads I found the average age range for users is 18-34 years old. My other focuses are readers who lead a busy lifestyle and want to keep track of their reading progress that fits into their schedule, and book collectors who want to organise and catalogue their book collections.

### Business Goals

The business goals for My Book List are:

1. Create a Reliable Product
   - Provide users with a seamless experience.
   - Listening and acting on user feedback by fixing any bugs or errors.
   - Push out stable updates and provide users with patch notes.

2. Feature Development
   - Implement a feedback form and signup/login form.
   - Improve the look of current features.
   - Introduce discussion forums for users to interact with each other.
  
3. User Experience (UX) and Interface (UI) Improvements:
   - Conduct user research to identify areas of improvement in the website design and functionality.
   - Optimise the app for different devices and screen sizes to ensure a seamless user experience.

4. Data Security and Privacy
   - Comply with data protection regulations such as GDPR to ensure transparency and user control over their data.
  
### User Goals 

The user goals of My Book List are:

1. Organising Reading Lists
   - Users will want a website that will allow them to create and manage reading lists to keep track of books they are reading, completed and want to read in the future.

2. Tracking Reading Progress
   - Users will want a website that tracks progress as they read books. The website should provide features for updating reading progress and displaying it visually.

3. Reliable Performance and Easy Navigation
   - Users expect the website to load quickly and respond promptly to their interactions, without experiencing slowdowns, errors, or downtime.
   - Users want to navigate the website easily and intuitively, finding what they're looking for without getting lost or confused.

4. Compatibility and Mobile Responsiveness
   - Users want the website to work seamlessly across different web browsers, operating systems, and internet connections, ensuring a consistent  user experience.
   - Users want the website responsive and functional on various devices and screen sizes, including smartphones, tablets and desktop computers.

## Scope

To accomplish the business and user goals the features that will be added in the first release of My Book List are: 

1. Logo
   - The logo will be located at the top of the website, designed and edited using Canva and a background removal tool. In addition, since the logo I have picked will have light colours I will be making the header a dark colour and changing the opacity so users can still see the background image.
  
2. Background Image
   - For the background, I will be choosing an image of books on bookshelves to make the website athletically pleasing then have a plain background colour.

3. Book Form
   - For My Book List I will be designing and building a form which will allow users to add new books, the form will consist of the following fields:
     - Book Title
     - Author
     - Comments - Any comments users wish to make about the book or reminders of what chapter/page they are on.
     - Status - Allow users to write in their current status of the book such as Reading, Completed and Want To Read. This field will be set as text to allow users more flexibility with how they want to set their status.
     - "Add Book" Button - When users click on this button it will submit their book data and will be displayed visually in the table. Additionally, when users submit book data the information will be saved to a database which will save their data and retrieve it when returning to the website.

4. Book Table
   - When users submit their book information it will be shown in a table under the correct table heading and allow multiple rows to be added. I will also be adding an extra column called "Actions", this will have the "Edit" and "Delete" buttons.

5. Edit Button
   - This interactive feature will allow users to edit their current books by opening up the form and displaying the book information, users will then make any changes they want and click on the "Save" button, this will automatically redirect them back to the Home page and show the updates they've made.

6. Delete Button
   - This interactive feature will allow users to delete any books in the table.

### Future Planned Releases 

In the future, I have planned to release the following features:

1. Sign Up / Login Page
   - This feature will allow users to create an account and log in on different devices, it will also allow any information to stay on their account unless the user decides to delete it.

2. Account Customisation
   - Allow users to customise their account by choosing a profile picture, cover photo, about me section, interest, favourite books to read, and more.

3. Table Filter
   - Allow users to change the order of their shown in the table, such as alphabetical order of Authors or Book Titles.

4. Date Started and Finished
   - This feature will be added to the form to allow users to input what day they started reading their book and when they finished it. This feature will be suitable for users who like to keep track of how long it takes them to read a book.

5. Stars
   - This feature will be added to the form to allow users to rate their books out of 5.

6. Feedback Form
   - This feature will allow users to provide the business with necessary feedback regarding bugs and issues, improving the website design and functionality.

7. Discussion Forums
   - This will allow users to connect and talk about books they are reading, completed and want to read. Rules will be pinned at the top of the forum and require users to read and react for the business to know users understand the rules set in place to keep everyone in the community safe.

## Structure

For the structure plan for My Book List, I will outline the interaction design and information architecture of the website's pages and features to ensure users have an uninterrupted experience. 

1. Home Page
   - Table: Visually displays the user's books, and will also include the "Edit" and "Delete" buttons.
   - Form: Allow users to fill out the form with their book information to be displayed in the table.

2. Edit Page
   - Form: Prefilled with book information when users click on the "Edit" button, users can press save and will be redirected back to the Home page.

3. Footer
   - Copyright information

4. Responsive Design
   - Ensure the website layout adapts consistently to different screen sizes and devices. 

## Skeleton

### Wireframes 

![My Book List Wireframes for desktop, tablet and mobile](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/wireframes.png)

The wireframes shown above are the original plans and ideas of how I want My Book List's layout to look. During the building process of the website, I decided to make a few changes to the features and layout. 

The first change I made was the form on the home page. I decided to change the input field for Status, my original idea was to have a dropdown menu which allowed users to select an option but I realised this didn't give users the flexibility to have custom status. Now the Status will have an input field where users can write in the status and any other information like chapter or page number. The next change I made was the layout of the home page, I decided to swap the position of the form and table because the table will be first seen when the page loads. Finally, the last change made was I added a new page called "Edit Page", when the user clicks on the edit button in the table the page will load. 

### Prototypes 

For My Book List, I wanted to create prototypes to get a rough idea of how I want the overall website to look with all the features together and how it looks when viewing different screen sizes. Below are the desktop, tablet and mobile prototypes I have made.

#### Desktop Prototype

![My Book List Desktop Prototype](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/desktop_prototype_home.png)

#### Tablet Prototype

![My Book List Tablet Prototype](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/tablet_prototype_home.png)

#### Mobile Prototype

![My Book List Mobile Prototype](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/mobile_prototype_home.png)

## Surface 

### Colours 

For the first release of My Book List, I wanted to pick a colour palette that fits the brand, allows me to influence user behaviour and at the same time keeps the colour selection limited to less than 5 colours. The colours used throughout the website are:

- `#212529` Bootstrap: $dark: $gray-900;
- `#6c757d` Bootstrap: $secondary: $gray-600;
- `#ffffff` White
- `#0d6efd` Bootstrap: $primary: $Blue;
- `#f8f9fa` Bootstrap: $light: gray-100;
- `#dc3545` Bootstrap: $danger: $Red;
- `#000000` Black

### Imagery 

For the first release of My Book List, I wanted to choose the right images because most of the initial information users consume on websites is visual and first impressions are important, imagery should be expressive and capture the spirit of the business. 

#### Background Image

![My Book List Background Image](https://github.com/sophiedeakin/My-Book-List/blob/main/static/assets/books-bg.jpg)

The image above was chosen for the background image because it matches the overall concept of the website. To keep the website consistent both the home and edit pages will have the image cover the whole page, since the image is bright I will be turning the opacity down to 80%. 

#### Logo

![My Book List Logo](https://github.com/sophiedeakin/My-Book-List/blob/main/static/assets/mybooklistlogo.png)

The image above was chosen to be used for the logo of the website, the picture was created using Canva and a background removal tool. I wanted a logo that truly represents what the website is all about, memorable to users and a simple design. 

### Header and Footer 

To keep the website consistent the header and footer will have the same background colour of `#212529` and will have opacity also turned down to 80%, allowing users to see the background image through the header and footer. 

### Forms 

![Form on Home and Edit Page](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/form.png)

#### Colours 

The colours used in the form are:

- `#6c757d` Bootstrap: $secondary: $gray-600; - Background colour
- `#0d6efd` Bootstrap: $primary: $Blue; - "Add Book" & "Save" (Edit Page) Button
- `#ffffff` White - Input Fields

#### Interactive 

The forms will create a two-way communication method between users and the website by allowing them to write relevant information in each input field about their books and use the "Add Book" button to display it in the table visibly. For the edit page users can do the same thing, they can make changes to their books like status or comments and press the "Save" button which will override the original information.

### Table 

![Table on Home Page](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/table.png)

#### Colours

The colours used in the table are: 

- `#f8f9fa` Bootstrap: $light: gray-100; - Background colour
- `#0d6efd` Bootstrap: $primary: $Blue; - Edit Button
- `#dc3545` Bootstrap: $danger: $Red; - Delete Button

#### Interactive 

Users can interact with the table by pressing the "Edit" button under the Actions heading this will direct users to the Edit Page with a form where users can manage their books and make any changes. Also under Actions, there's a "Delete" button that allows users to delete their books. 

---

## Technologies Used 

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
  * Used for the basic building block for the project and to structure the content.

- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
  * Used for styling all the web content across the project.

- [Python](https://developer.mozilla.org/en-US/docs/Glossary/Python)
  * Used for back-end developing websites and software, task automation, data analysis, and data visualization.

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
  * Used for developing web applications using Python.

- [Google Developer Tools](https://developer.chrome.com/docs/devtools/)
  * Used for identifying any bugs and testing responsiveness.

- [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)
  * Used for improving the quality of web pages.

- [GitHub](https://github.com/)
  * Used for storing code for the project after being pushed.

- [Git](https://git-scm.com/)
  * Used for version control by utilising the VS Code terminal to commit to Git and Push to GitHub

- [Visual Studio Code](https://code.visualstudio.com/)
  * Free Open Source software used to code the project.

- [Figma](https://www.figma.com/)
  * Used for creating the wireframes for the project.

- [Canva](https://www.canva.com/)
  * Used for designing and editing the project logo and creating the prototypes

- [Grammaly](https://www.grammarly.com/)
  * Used for checking grammar and spelling mistakes throughout the project.

- [Background Remover](https://www.remove.bg/)
  * Used for removing the background around the logo and arrow buttons making them transparent.
 
---

## Testing 

### Automation Testing & Manual Testing 

For My Book List, I will be using automation testing over manual testing because it's very accurate and reliable for repetitive tests and there is less prone to human errors, automation is efficient and effective as it covers a wider range of scenarios, such as large, complex, and repetitive ones. Additionally, automation testing has a faster test cycle time because it's effective when testing the user experience as the UX typically involves judging the feeling or perception a user might have about the overall user-friendliness.

For this project, I will use Google Lighthouse, an open-source automated tool for improving the quality of web pages and has audits for performance, accessibility, progressive web apps, SEO, and more. I have chosen this automated tool because it's cost-effective and doesn't require me to sign up for a subscription service, I also have experience using this tool and am quite familiar with how it works. Google Lighthouse generates reports on how well the page did and you can use the failing tests as indicators of what you can do to improve your app, it also provides you with recommendations on how to improve it.

### User Stories 

#### User Story 1 

As a book reader, I want the ability to organise my reading list to keep track of books I am reading, completed and want to read in the future.

![User Story 1](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/user_stories1.png)

Users can use the form to log their books, the status field within the form allows users to input a custom status like Reading, Completed or Want to Read. Once users have completed the form they can submit it and the information will be visually displayed in the table above (reference image above). The developers will know when the user story has been accomplished by not receiving bug reports and the business has gained new and returning customers. 

#### User Story 2 

As a book reader, I want the ability to track the progress of my books by being able to make updates and see them visually displayed on the website.

![User Story 2](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/user_stories2.png)

Users can use the "Edit" button within the table (reference image above) this will direct them to the Edit page where they can use the form to update their book information, once they have made changes they can press the "Save" button this will redirect them back to the Home page and they will see the changes in the table. The developers will know when the user's story has been accomplished by users having a seamless experience. 

#### User Story 3

As a book reader, I want the website to have reliable performance and easy navigation where the website responds to interactions and I can find what I am looking for without getting lost or confused. 

![User Story 3 Home Page](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/user_stories3.png) ![User Story 3 Edit Page](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/user_stories3.1.png)

My Book List website has 2 pages Home page and an Edit page (reference image above), users can easily navigate the website without feeling overwhelmed. The website will go through automation testing to make sure the website loads quickly, responds to user interactions and doesn't experience errors or downtime.

#### User Story 4

As a book reader, I want the website to be compatible with different web browsers and be responsive to various devices and screen sizes. 

![User Story 4](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/user_stories4.png)

My Book List will go through testing using automation testing tools which give accurate reports, are less prone to human errors and effectively test user experience. During the testing, I will use Google Developer tools to test if the website is responsive to different devices and screen sizes, to test if the website works on other browsers I will open it on popular browsers like Firefox, Opera and Microsoft Edge.

### Lighthouse 

Google Lighthouse is a free automation testing tool that assesses web pages' overall quality and user experience. It provides quality scores across five categories:

- Performance
- Accessibility
- Best Practices
- SEO
- Qualification as a Progressive Web Application

Below are the results from the lighthouse test, I tested website on desktop and mobile mode:

![Lighthouse Desktop Results](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/lighthouse_desktop.png)

![Lighthouse Mobile Results](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/lighthouse_mobile.png)

### Google Developer Tools 

Google Developer Tools is a set of web developer tools built directly into Google Chrome, this tool helps you edit pages and diagnose problems quickly which makes your website looker better and build them faster.

Throughout the building process of the website I consistently used Google Developer Tools to identify bugs, it also allows me to test the responsiveness of the website by provding simulated devices like: 

- Galaxy S9+
- Galaxy Tab S4
- iPhone SE
- iPhone XR
- iPhone 12 Pro
- iPhone 14 Pro Max
- Pixel 7
- Samsung Galaxy S8+
- Samsung Galaxy S20 Ultra
- iPad Mini
- iPad Air
- iPad Pro
- Surface Pro 7
- Surface Duo
- Galaxy Fold
- Samsung Galaxy A51/71
- Nest Hub
- Nest Hub Max
- iPhone 4
- iPhone 5/SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad

### Known Bugs and Fixes

#### Edit Button Bug

When testing the "Edit" button in the table I noticed it didn't direct me to the Edit page instead it gave me an error "Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again." (Reference image below).

![Edit Button Bug](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/edit_button_bug.png)

The first step I took to resolve this issue was I look back at the code to see if I had mispelled something or forgotten to add a piece of code. After inspecting the index.html file I noticed I forgot to add "{{url_for('edit', id=book.id)}}". Once I added this code in and tested the "Edit" button again I was directed to the correct page.
See the image below of the bug fixed.

![Edit Button Bug Fixed](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/edit_button_bug_fixed.png)

#### Edit Page Form Visual Bug

When testing the form on the Edit page I noticed the form didn't look the same as the Home page. See the image below.

![Edit Form Visual Bug](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/edit_page_visual_bug.png)

Looking back at my code I noticed on both lines 11 and 17 I forgot to add the closing quotation marks. After adding them in and reloading the website the form has been fixed. See the image below. 

![Edit Form Visual Bug Fixed](https://github.com/sophiedeakin/My-Book-List/blob/main/readme_assets/edit_page_visual_bug_fixed.png)

#### Responsiveness Not Working On Mobile Devices

When using the Google Dev Tools to test the responsiveness 

