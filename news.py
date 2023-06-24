import requests
import smtplib
import ssl

category = "entertainment"
language = "en"
# Getting news from newsapi, use your own API key in place of APIKEY
api_key = "APIKEY"
url = "https://newsapi.org/v2/top-headlines?" \
      "country=us&" \
      f"category={category}&" \
      "sortBy=publishedAt&" \
      "apiKey=APIKEY&" \
      f"language={language}"

# Secure connection to Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 465

# Username of Google account (mail), recipient email address
# IMPORTANT: Password requires 2FA on Google account and *has* to be a 16-char app password that is generated by Google
# Can't use regular password, Google deems it as unsecure
username = ""
password = "e.g. sdfn owom maaw plim"
# Array of recipient email addresses
recipient_address = [""]

# Make a request
response = requests.get(url)

# Convert data to dictionary
content = response.json()

# Putting news content into a single string
# Subject line, includes news category
message = f"Subject: This week's latest {category} news" + 2*"\n"
# Max 25 news articles
for article in content["articles"][:25]:
    if article["title"] is not None:
        message += article["title"] + "\n"
        if article["description"] is not None:
            message += article["description"] + "\n"
        message += article["url"] + 2* "\n"

message += "\n" + "Updated news courtesy of kzfan1227"
# Self plug

# sends the email on a secure connection, encoded as utf-8 instead of ascii to ensure proper encoding
context1 = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context1) as server:
    server.login(username, password)
    server.sendmail(username, recipient_address, message.encode("utf-8"))
