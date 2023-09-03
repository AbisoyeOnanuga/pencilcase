import taipy.gui
import requests

# Create a Gui object
gui = taipy.gui.Gui()

# Create a text box for entering the search query
search_box = taipy.gui.TextBox("Search Pencil Case for a learning topic")

# Create a button for triggering the search
search_button = taipy.gui.Button("Search")

# Create a label for displaying the search results
result_label = taipy.gui.Label("Pencil search")

# Define a function that performs the search and updates the result label
def search():
    # Get the query from the text box
    query = search_box.get_text()
    
    # Set the URL and parameters for the Google Programmable Search Engine API
    url = "https://cse.google.com/cse.js?cx=c6456045664d54b97"
    params = {
        "key": "AIzaSyAL3XfxAUvvv8rjNdClR0lAAZxsJUZSnTg", # Replace with your API key
        "cx": "c6456045664d54b97", # Replace with your search engine ID
        "q": query # The query to search
    }
    
    # Send a GET request to the API and get the JSON response
    response = requests.get(url, params=params)
    results = response.json()
    
    # Check if there are any items in the results
    if results.get("items"):
        # Create an empty list to store the result links
        links = []
        
        # Loop through each item in the results
        for item in results["items"]:
            # Get the title and link of the item
            title = item["title"]
            link = item["link"]
            
            # Format the title and link as HTML code with a hyperlink
            html = f"<a href='{link}'>{title}</a>"
            
            # Append the HTML code to the list of links
            links.append(html)
        
        # Join the list of links with line breaks as HTML code
        html = "<br>".join(links)
        
        # Set the result label to display the HTML code
        result_label.set_html(html)
    
    else:
        # If there are no items in the results, set the result label to display a message
        result_label.set_text("No results found")

# Set the button to call the search function when clicked
search_button.set_on_click(search)

# Add the text box, button, and label to the Gui object
gui.add_element(search_box)
gui.add_element(search_button)
gui.add_element(result_label)

# Run the Gui object
gui.run()

# to test the python app, open a terminal and navigate to the repository folder. Run the script using << python pencilcase.py >>
# a window should popup with your pencil case app. 

# You can use the search box to enter a query and get results from the custom google search created for pencil case
# You can also use the button to add the results to your playlist and use the listbox to play the links using Pygame.

# To close the app, you can click on the X button on the top right corner of the window 
# or press Ctrl+C on your terminal or command prompt.