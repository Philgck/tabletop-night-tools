# Tabletop Night Tools

## Overview
A single site with tools to enable to easier hosting of board gaming nights or similar tabletop experiences. Currently, at time of writing, only contains the first app (The MVP, a board game library that can filter games by maximum player count for ease of hosting a night), but with room for significant expansion. 

## UX Design Process
- User Stories and Project Board
  - [Tabletop Night Tools Project Board](https://github.com/users/Philgck/projects/11)
- **Wireframes:**
  - [Attach or link to accessible wireframes used in the design process, ensuring high colour contrast and alt text for visual elements.]
  - [Explain the rationale behind the layout and design choices, focusing on usability and accessibility for all users, including those using assistive technologies.]
- **Design Rationale:**
  - [Explain key design decisions, such as layout, colour scheme, typography, and how accessibility guidelines (e.g., WCAG) were integrated.]
  - [Highlight any considerations made for users with disabilities, such as screen reader support.]
- **Reasoning For Any Final Changes:**
  - [Summarise significant changes made to the design during development and the reasons behind them.]
  - [Reflect on how these changes enhance inclusivity and accessibility.]

## Key Features
- **BGG API, Autopopulating Form 1:** This took the most work due to the nature of the API. When a user presses add game, a modal appears allowing manual entry of game details. If they enter a search term and press search, the API will fetch associated games (And only base games, no expansions or add ons as of time of writing.) and populate a dropdown list of choices. Upon selection, this auto fills the relevent fields (Title, Description, Minimum Player Count and Maximum Player Count). The other field (Review) is left blank and is intended for user reviews of games, currently for personal notes, but with space for future expansion
- **Maximum Player Count Feature:** The board games are currently displayed in a paginated list. The maximum player count feature allows users to put the upper bound on how many people might be attending an evening, and only displays games that can be played with this player count.
- **Inclusivity Notes:** 
  - The font choice was made after consulting with a dyslexic friend about readability, and is deliberately similar to Comic Sans as this is a very readable font. 

## Deployment
- **Platform:** [Platform used, e.g., Heroku, AWS, etc.]
- **High-Level Deployment Steps:** 
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]
- **Verification and Validation:**
  - Steps taken to verify the deployed version matches the development version in functionality.
  - [Include any additional checks to ensure accessibility of the deployed application.]
- **Security Measures:**
  - Use of environment variables for sensitive data.
  - Ensured DEBUG mode is disabled in production.

## AI Implementation and Orchestration

### Use Cases and Reflections:
(Highlight how prompts, such as reverse, question-and-answer or multi-step, were used to support learners with SEND or ALN where relevant.)

  - **Code Creation:** 
    - Both copilot and ChatGPT were used throughout the product with testing and implementing code. On a personal level, I have preferred using ChatGPT as it is easier to get it to query a singular piece of code, rather than the code in context. ChatGPT helped walk me through the debugging of the bgg_api.py file and its output and was essential in implementing the filters that prevented erroneous entries.
    - Whilst I did not save and record the prompts in question, after the initial issues with the API implementation I used ChatGPT to try and build a scraper using beautifulsoup. This turned out to be a dead end as the way the pages are populated involved javascript and I did not want to have to implement further libraries, and returned to tweaking the partially functional API in order to bring it to the standard required.
  - **Debugging:** 
    - Whilst building the API I limited the amount of results it could pull down to 20, in order to make it load significantly faster as there were extreme delays. Once the filters were in place, Copilot itself flagged the limit on results as no longer necessary. However I found copilot kept reintroducing a bug in the template language: For some reason it would add extra space in the second argument of player count (Maximum player count), breaking it every single time that it recommended changing code. 
    - 
  - **Performance and UX Optimization:** 
    - Changes to the API recommended by AI tools significantly improved performance of the API. However, any changes made to UX were discarded and replaced with human intervention. I would rather make sure that UX was designed for humans, instead of ammended to fit the output of an AI.
  - **Automated Unit Testing:**
    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

- **Overall Impact:**
  - AI tools definitely streamlined tasks and were necessary for the development of parts of the project. I have learned more about how to prompt the revelant tools from this project alone than any of the others. Realising what a solution might be, and working with an AI to implement it, was an amazing learning experience and significantly less frustrating that attempting to work things out completely by myself.
  - Particularly with the API, ChatGPT was used in debugging output. I used it as a walkthrough guide where to add console logs to triple check where the points of failure might be.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

## Testing Summary
- **Manual Testing:**
  - **Devices and Browsers Tested:** [List devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers or keyboard-only navigation.]
  - **Features Tested:** [Summarise features tested manually, e.g., CRUD operations, navigation.]
  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]
- **Automated Testing:**
  - Tools Used: [Mention any testing frameworks or tools, e.g., Django TestCase.]
  - Features Covered: [Briefly list features covered by automated tests.]
  - Adjustments Made: [Describe any manual corrections to AI-generated test cases, particularly for accessibility.]

## Future Enhancements
- The intent of the project was to create multiple tools to enhance the ability to host board game evenings. Currently there is just one, and a single filter by maximum player count. Other features might include storing tags for specific games so a host can filter by "Euro Game" or similar.
- A could have feature I wanted to implement was a friends list that would enable a user to share their library with others. Board game evenings are a fundamentally social experience, and being able to know what is in your own library and your friends libraries would be extremely helpful.
- The name itself belies the aim: It is supposed to be several tools. I want to add features that help with the hosting of Role Playing Games as well. 
- With regards to accessibility, directly in the tabletop space linking to specific sites dedicated to accessbility and potentially integrating some of their recommendations would be useful. The site 

Initial commit and readme. This project was created using the code institute template. 

The intent of this project is to create a single site that contains multiple different tools that will help with running tabletop gaming nights. The primary functionality I intend to implement is a boardgame library app, built using Django, that enables users to store their board game library in a single location with access to information like "Player count" and "Average play length". Users will be able to update their library of games, delete entries from it, create entries to it, and view its contents. 

Could haves with regards to this project are a friends list so you can share your library with other users, view your shared library between friends, and create events that will automatically consider the maximum player counts and who is attending in order to show what games could potentially be played. Further intent is to add other apps that will help with running role playing games, and the sharing of "homebrew" content with other users. 

This initial commit and intial readme exists to record the intent of the project as it started, and to try and limit scope to make sure that the above is completed prior to adding further tools. 