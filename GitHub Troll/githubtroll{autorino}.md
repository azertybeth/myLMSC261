GitHub lurker project notes

Project Chosen: Lawnchair (Android FOSS Launcher based on Launcher3 [android’s default launcher] written in Kotlin and Java)

I actively use this launcher because it retains a lot of the stock android aesthetic while not bundling any Google-specific code like the default launcher does. There are also more customization options added into it.

11/24:
All release versions published by the same user despite many users collaborating on the project. Commits have been made by multiple users, however. There are 21 total branches with 5 active branches:
* 12-dev-localization (updated today)
* 12-alpha
* 11-dev-localization
* 11-dev
* 11-alpha

The naming schemes are derived from Android version numbers, with the current being Android 12. This is because this project is directly related to stock releases of the default Android launcher.

The crowd-sourcing contribution guidelines say that Kotlin is preferred over Java, but 92% of the code is Java according to GitHub.

From cursory Googling it looks like Kotlin is its own language that is designed to interact with Java seamlessly, as opposed to being entirely based on Java.

There are some “jobs” listed in GitHub under the project page. I don’t entirely understand what the terminology means to GitHub, so I should probably educate myself about that later.


11/26:
Okay, so after doing some googling on the actions tab in GitHub, it seems like “Jobs” are cloud-hosted tasks that can be called upon by an application and don’t actually have anything to do with breaking down jobs and assigning tasks within a development team.


11/27: a user (not part of the dev team) submitted an issue 6 minutes ago: “navigation bar is blocking the ‘add to home screen’ button”.

3 days ago a member of the dev team closed an issue because it had already been fixed; linked to a specific commit containing the fix (Rachel was really right about the importance of concise commit titling being helpful). I wish/wonder if there were a way to see which .apk release package correlates to code changes…

I still can’t quite tell whether the actions tab in GitHub are development tools for sending crash info etc. or if they’re actual jobs to incorporate into a release version of the program. Maybe Rachel has some helpful insights (since all the google explanations seem tailored to people who already understand the vague concept).

It looks like the majority of the social aspect/team communication takes place under the GitHub "issues" tab. While it looks like non-dev
users are able to submit their own issues, there are some issues that have been pinned by the dev team. One such issue is about preparing
a release of the app for the FOSS distribution platform "F-Droid". It looks like one of the head developers "self-assigned" the issue,
and also tagged it as 'enhancements' and 'help wanted', which seems like a helpful indirect way to communicate. There follows more direct
discussion in the comments on the issue posting in which there are back-and-forths between various collaborators proposing ideas and
solutions.

At a second glance, it seems this issue is no longer relevant and was posted over a year ago, however the insight is still valuable and
interesting.


Link to article I read about GitHub actions:
https://gabrieltanner.org/blog/an-introduction-to-github-actions

Link to project repo:
https://github.com/LawnchairLauncher/lawnchair
