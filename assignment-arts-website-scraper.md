# Arts Website Scraper

## Objective:
The objective of this assignment is to introduce beginning Python students to web scraping using the Beautiful Soup library, with a focus on an arts-related website. Students will be required to extract specific information related to the visual or performing arts from the provided website.

## Instructions:
1. Select an arts-related website that includes information about visual or performing arts, such as art galleries, theater productions, music events, etc.
2. Use Beautiful Soup to scrape the selected website and extract the required information.
3. Display the extracted information to the user in a structured format.

## Requirements:
1. The program should scrape an arts-related website of your choice. Feel free to explore websites related to art galleries, theater productions, music events, or any other form of visual or performing arts.
2. The program should extract at least three different types of information related to the arts (e.g., event titles, artist names, exhibition descriptions, performance schedules, etc.).
3. The extracted information should be displayed to the user in a readable and well-organized format.

**Note:** To complete this assignment, you will need to install the `beautifulsoup4` library if it is not already installed. You can install it using the following command:
```python
pip install beautifulsoup4
```

Make sure to import the necessary libraries (`requests` and `bs4`) at the beginning of your code.

## Example Output:
```
Scraping an Arts Website...

----- Extracted Information -----

Upcoming Art Exhibitions:
- Exhibition Name: "Artistic Impressions"
  Description: Explore a collection of vibrant and expressive artworks that capture the essence of the human experience.
  Date: 24th June 2023 - 15th July 2023
  Location: ABC Art Gallery

- Exhibition Name: "Abstract Expressions"
  Description: Immerse yourself in the world of abstract art with this thought-provoking exhibition featuring works by contemporary artists.
  Date: 2nd July 2023 - 31st July 2023
  Location: XYZ Art Space

Theater Performances:
- Performance Name: "Romeo and Juliet"
  Description: Experience Shakespeare's timeless tragedy performed by a talented cast of actors in a stunning outdoor setting.
  Date: 28th June 2023 - 10th July 2023
  Location: City Theater

- Performance Name: "The Nutcracker Ballet"
  Description: Delight in the magical holiday classic brought to life by graceful dancers and enchanting music.
  Date: 5th December 2023 - 24th December 2023
  Location: Grand Opera House

----------------------------------
```

**Note:** The above example output is for illustration purposes only. The actual output will vary based on the arts website you choose to scrape.

## Grading Criteria:
- Successful scraping of the selected arts website (30%)
- Proper extraction of relevant information (40%)
- Displaying the extracted information in a structured format (20%)
- Code structure, organization, and readability (10%)

Have fun exploring the arts and happy coding!