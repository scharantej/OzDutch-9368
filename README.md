## Design for a Flask Application to Translate Australian Flashcards to Dutch

### HTML Files
- ***index.html***: 
   - Responsible for displaying the main page of the application.
   - Contains a form with input fields for the Australian saying and a submit button to translate it.
   - Displays the translated Dutch saying received from the server.
- ***stylesheet.css***: 
   - Defines the CSS styles for the application, including layout, font, and color scheme.

### Routes
- ***"/" (GET)***: 
   - Renders the ***index.html*** page, displaying the form for inputting the Australian saying.
- ***"/translate" (POST)***: 
   - Receives the submitted Australian saying using a form request.
   - Performs the translation to Dutch using a helper function or connecting to an external API.
   - Returns the translated Dutch saying as a JSON response.