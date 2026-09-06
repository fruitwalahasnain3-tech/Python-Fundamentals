languages = ["Python", "Java", "C++", "JavaScript", "SQL"]

language = input("Enter a language: ")

if language in languages:
    print(language,"is available.")
else:
    print(language, "is not available.")