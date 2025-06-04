1. Create a view called `practice_dtl`.
2. Render a html template called `practice-dtl.html`
3. Pass these variables to the template:
    - username (set it to a username of your choice). Display "Hello, {username}". Replace username with the username.
    - no_of_messages (set it to 5). Display "You have {no_of_messages} messages"
    - messages (set it to a list ["hello", "free to chat?", "when can we talk?"])
    - is_logged_in (set it to True)
    - if the user is logged in, display all their messages in a numbered list (use a for loop)
    - if they are not logged in (i.e. is_logged_in is False), display in a p tag, "You need to log in to view your messages".
4. The user should see the html template by going to `127.0.0.1:8000/messages` in their browser.