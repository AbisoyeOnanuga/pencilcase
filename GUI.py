import taipy.gui
import html

# Create a Gui object
gui = taipy.gui.Gui()

# Create an Html page with the custom search engine code
html_page = taipy.gui.Html("Search Page")
html_page.load_html("<div class=\"gcse-search\"></div><script async src=\"https://cse.google.com/cse?cx=c6456045664d54b97\"></script>")

# Add the page to the Gui object
gui.add_page(html_page)

# Run the Gui object
gui.run()

import taipy.gui

# Create a Gui object
gui = taipy.gui.Gui()

# Create a Markdown page with the custom search engine code
md_page = taipy.gui.Markdown("<div class=\"gcse-search\"></div><script async src=\"https://cse.google.com/cse?cx=c6456045664d54b97\"></script>")

# Add the page to the Gui object
gui.add_page(md_page)

# Run the Gui object
gui.run()