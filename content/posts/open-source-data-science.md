---
title: "You cannot do data science without open source"
subtitle: "But you cannot do open source without a sustainable plan"
date: 2020-07-18
draft: false
summary: While I had a strong feeling back in 2017 when I made my first open source library, it’s even more clear today that you cannot do data science without open source.

---
When I joined [Alteryx](https://www.alteryx.com/) last year, one of the first things I heard from our CEO Dean Stoeker was a quote inspired by the inventor Buckminster Fuller. It went along the lines of:

> We are building all the right technologies for all the wrong reasons. We will not be able to operate Spaceship Earth very well nor for much longer unless we see it as a common cause. It has to be none of us or all of us.

This idea resonated with me because for the past several years I have been building open source technology with the goal of enabling as many people as possible to solve problems using data science and machine learning. 

While I had a strong feeling back in 2017 when we made our [first open source release](https://innovation.alteryx.com/open-sourcing-featuretools/), it’s even more clear today that **you cannot do data science without open source**.



## Ordinary people building extraordinary things

Literally speaking, “open source” refers to software where the source code is licensed for anyone to freely use for any purpose. There are notable differences among the common licenses like MIT, GPL, Apache 2.0, or BSD, but they are more similar than different. 

Despite the source code being out in the open, only a small fraction of open source software users ever look at the source code of most data science tools ([I'd estimate under 1%](https://twitter.com/maxk/status/1264582887967535104?s=20)). So, why is it so important to make the source code free for someone to see and use?

The reason lies in what Buckminster Fuller highlighted. Solving big problems is about working towards a common cause. Open source is the mechanism in which a group of ordinary people can work together to create something extraordinary.

That is what I’ve experienced working on [Featuretools](https://github.com/FeatureLabs/featuretools), a data science library that is downloaded thousands of times a day by people all over the world. We have seen it used by banks to issue loans to small businesses who don’t have access to capital, school districts to identify students who are having problems at home by predicting school absences, and technology startups trying to identify what a customer will buy next. 


## Data Science is Collaborative

The biggest lie in data science is that it is the [Sexiest Job of the 21st Century](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century). It fetishizes the idea that data science is only composed of exciting work driven by individual data scientists. 

The truth is that data science is about working through the nitty gritty details of transforming big ideas into concrete solutions. Along the way it requires building on the ideas of *others*, leverage statistics developed by *others*, or asking *others* for ideas while debugging or improving solution that doesn’t work as expected. Put simply, most of the time it isn't a sexy job.

Building tools that enable data scientists similarly benefits from the help by other people. With open source development you can scalably work through complex technical details with thousands of people to figure out details like

* What is the single API that works across different use cases?
* How do we handle missing values when trying to calculate the standard deviation?
* Why does this software work on linux but not windows? 
* How can a user process a terabyte of data without running out of memory? 

These are just some of the most interesting technical challenges. In reality, there have been over [400 “issues”](https://github.com/FeatureLabs/featuretools/issues) with our software. I should point out these are not all bugs, but also feature requests and discussions. Some we took, while others we had to say no to even though we appreciated the input that made us think. 

It took me a few years, but ultimately I am proud, not embarrassed, of the bugs people reported in our software. Every bug we fix is indisputable evidence that our software just got that much better for our users. 

If you’re making critical decisions for your business or organization, would you rather use proprietary software where the author make unverifiable [claims](https://www.datarobot.com/blog/next-generation-automated-feature-engineering/) their software is the best, or an open source option that clearly shares what the software can and cannot do? 

I can't answer definitively why more data science and machine learning companies don’t go open source, but I’ll highlight one theory I have through this quote from Commissioner Pravin Lal in the video game “Sid Meier’s Alpha Centauri”: 

> Beware of he who would deny you access to information, for in his heart he dreams himself your master.

## Open Source Needs to be a Two Way Street 
In the 4 years building my company Feature Labs, the role of open source in data science became obvious for the reasons above. 

However, despite all the strengths of open source, we were less than a dozen full time people. It became painstakingly apparent that in order to continue to grow required money. Unfortunately, software engineers and data scientists aren’t cheap. 

So, therein lies the fundamental challenge we need to solve. The beauty of open source is that it is the best way to accumulate the knowledge of the world in a reusable form for everyone's benefit. However, how do you do that in a sustainable way?

The answer used to create many companies is to restrict access, but as you do that, you restrict progress. 

In order for open source to work, you need to not only give back to the community, but to find a way to share in the profit you create in the community. 

## Journey to sustainable innovation 

Bill Gates has said

> Most people overestimate what they can do in one year and underestimate what they can do in ten years.

Open source is a mechanism to solve big problems in data science and machine learning on step a time. But, how can it be done in a sustainable way over an extended period of time? 

