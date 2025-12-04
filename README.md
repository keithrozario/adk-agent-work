# Julian & Gregory - The Calendar assistants

## What does it do?

The Calendar assistants can help:

1. Summarize the days meetings
2. Summarize the weeks meetings
3. Reschedule a meeting
4. Book trainings into your calendar
5. Adjust the trainings on your calendar (e.g. move everything by a week)
6. Automatically cancel meetings if you're on emergencies

## How does it do it?

We cannot rely on Gemini Enterprise Assistant capability we instead of have to create a custom agent that oAuths into the Google Calendar and GMail Apis. Will have to figure out the oAuth works for Gemini Enterprise.

## Tech Stack

Adk-Python

## Why the name?

There is a batman villian called Calendar Man, whose real-life name is Julian Gregory Day, named after the Julian and Gregorian calendars. I'm a big batman fan. ;)


## Creation

## Steps

1. Create a simple custom agent and publish to Gemini Enterprise
2. Check if we can call the Google calendar/mail APIs with just the oAuth token 
3. Check how to pass the oAuth token from Gemini Enterprise to the custom agent (in theory we don't require oAuth, as the user is already logged on with the right identity)
4. Build it out!


