import wikipedia

# Set language for Wikipedia (e.g., 'en' for English)
wikipedia.set_lang("en")

user_input = input("Enter a page title or search phrase (blank to exit): ")
while user_input != "":
    try:
        page_title = wikipedia.search(user_input)[0]

        page = wikipedia.page(page_title)

        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")

    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation page. Please specify your query:")
        options = e.options
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        choice = input("Enter the number of your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            user_input = options[int(choice) - 1]
        else:
            print("Invalid choice. Exiting...")
            break
    user_input = input("Enter a page title or search phrase (blank to exit): ")

print("Goodbye!")
