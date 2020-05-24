# Pages Auto Publish

It'd be cool if Github Pages automatically made future posts visible when their time came without you having to add a commit when you're using Jekyll as a static site generator. They also seem to need the published state changed to true.

I'm intending that this action will use a cron schedule to look at the date on posts in the \_posts directory and if the date is after the last run, check to see if it's published status is true. If not, set it to true, make a commit, and hopefully your post will be automatically published!
