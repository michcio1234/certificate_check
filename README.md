# Certificate validation app

A simple web app to check authenticity of a certificated issues on paper or as a PDF file.

## What is it?

It's a web application which lets the users input an alphanumeric code, checks if this code is present in a database, and if it is, it outputs the name assigned to this code.

It can be used to validate authenticity of certificates issued after attending an online course, a webinar, or real-life event. An organiser can include unique codes on issued certificates, and allow validating them on a website.

I created this app as an exercise - to learn FastAPI and a bit of CSS.

## Example

See a demo here: https://simple-certificate-validation.herokuapp.com/xyz123

Another valid code is `abcd1234`. You don't have to include a code in the URL.

## How to use it?

1. Clone the repository
2. Replace the file `attcert/data/attendees.csv` with an actual CSV file containing names and codes. Keep the header line.
3. Deploy it. The easiest way to do it is to use Heroku:
   1. Commit the changes. (Be careful not to push sensitive data to Github!)
   2. Register on Heroku and create a new app: https://dashboard.heroku.com/new-app
   3. Install `heroku cli`: https://devcenter.heroku.com/articles/heroku-cli
   4. Add Heroku remote to your repository. Inside the root repo folder execute: `heroku git:remote <your app name>`
   5. Push the code to Heroku: `git push heroku`.

That's it. Your app is live at <your-app-name>.herokuapp.com.
