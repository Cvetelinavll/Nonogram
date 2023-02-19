This is a React component that renders a grid of squares that the user can click to change the color of the square. The goal of the game is to match the grid pattern shown on the server, which is fetched using the fetchData() function.

Here are the step-by-step explanations of the code:

The import statements import the necessary React hooks and components.
The Matrix function is the main component that will be exported.

rows_cols is a state variable that stores the number of rows and columns for the grid. It is initialized with a value of 5.

rows and columns are variables that are initialized with the value of rows_cols.
grid is a state variable that stores the current state of the grid. It is initialized with an empty array.

sizeplayer is a state variable that stores the size of the player's grid. It is initialized with a value of 0.

data is a state variable that stores the data received from the server. It is initialized with a value of null.

matrixRef is a reference that is used to access the DOM elements of the grid squares.
ifwin is a state variable that stores whether the player has won or not. It is initialized with a value of 0.

The first useEffect() function is used to create a new grid of squares whenever the number of rows or columns changes. It initializes the grid state variable with an empty array and loops through the rows and columns to push a new row with 0 values to the grid. It depends on the rows and columns variables.

The second useEffect() function is used to fetch the grid pattern from the server using the fetch() function. It sets the data state variable with the JSON data received from the server. It is executed only once when the component is mounted.

handleBoxClick() function is a callback function that changes the color of a square when it is clicked. It takes the row and column indices as arguments and updates the grid state variable by making a copy of the current grid and changing the value of the clicked square to the opposite color.

renderMatrix() function loops through the rows and columns to create a new array of React components representing the grid squares. It checks the current value of each square in the grid state variable and sets the background color of the square accordingly. It also sets a reference to the DOM element of each square using the ref attribute. Finally, it returns the array of React components.

handleSetClick() function is a callback function that sets the size of the player's grid to the current value of sizeplayer state variable. It is called when the "Generate" button is clicked.

The third useEffect() function is used to check if the player has won by comparing the color of each square in the player's grid with the color of the corresponding square in the server's grid. It loops through the rows and columns and uses the matrixRef reference to access the DOM element of each square. It sets the ifwin state variable to "You Win" if the player's grid matches the server's grid, and "Still Not Winning..." otherwise. It is executed whenever data, rows, or columns change.


To deploy the FrontEnd React app to Firebase, follow these steps:

First, you'll need to create a Firebase account and create a new project.

Install the Firebase command-line interface (CLI) by running the following command in your terminal or command prompt:


Sudo npm install -g firebase-tools
After installing the Firebase CLI, log in to your Firebase account by running the following command and following the prompts:

firebase login
Next, navigate to the root directory of your React app in the terminal or command prompt.

Initialize Firebase in your app by running the following command and following the prompts:


firebase init
This command will initialize Firebase in your app and prompt you to choose the Firebase services you want to use. Select Hosting and follow the prompts to configure your hosting settings. DIR must be BUILD not Public!

Once you've configured your hosting settings, you'll need to build your React app for production. Run the following command to create a production-ready build:

npm run build
This command will create a build directory in your app's root directory with all the files you need to deploy your app.

Test local: nom start

Deploy your app to Firebase Hosting by running the following command:

firebase deploy
This command will upload your app's build files to Firebase Hosting and make your app live.

And that's it! Your React app should now be deployed and live on Firebase Hosting. You can view your app by navigating to the hosting URL provided by Firebase.
