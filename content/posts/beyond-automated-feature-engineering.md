---
title: "Beyond Automated Feature Engineering to Feature Stores"
date: 2022-03-02
draft: false
summary: While automating human intelligence is exciting, the core challenge is providing machine learning-ready data for developers who don't want to do feature engineering.
---

I love programming because I get to tell the computer what to do. Using lines of code, I can automate any task that can be described algorithmically.

Many years ago, I noticed myself repeatedly writing scripts to transform raw data into explanatory variables (aka "features") for machine learning algorithms. So, it was only natural to write a program that could automate that process.

Much to my delight, it worked better than I expected. As a result, the code I wrote became [Featuretools][1], one of the first libraries for automated feature engineering.

There were two distinct problems in machine learning and data science Featuretools solved

1.  **The status quo had a missing API** — In many data pipelines, developers had to write custom code to transform the relational and/or temporal storage format of raw data to the single-table, feature matrix representation used by machine learning models.
2.  **Developers weren't domain experts** — To make machine learning models work, humans had to brainstorm which transformations to apply, often requiring domain expertise. Developers could copy and paste Featuretools code and get a "good enough" model for most tabular data problems.

Featuretools addresses both these problems through "automated feature engineering." As a developer, you only had to supply your data model and connect some APIs. Featuretools made the iterative and roundabout process of doing machine learning a little bit more like using an SDK to build a mobile app.

With automated feature engineering, developers could spend time on all the other activities required to make machine learning successful. So I quickly hopped on the bandwagon that automating feature engineering was critical for machine learning success.

However, what matters in machine learning is having the right features, not how you get them. So while the automation of human intelligence is exciting, the core value of Featuretools is providing machine learning-ready data for developers who didn't want to do feature engineering rather than automation.

So, what's beyond automation?

The most important thing isn't the automation but a ready-to-use machine learning features repository. The time savings from automation frequently don't matter as much for feature engineering as other parts of the machine learning process [^1].

The reason is that most models and problems can reuse brilliant feature engineering ideas. In other words, an organization can get a lot of leverage out of feature engineering. Compare this to the topic of hyperparameter optimizing (i.e., libraries like [EvalML][2]). That needs to be automated because the right set of hyperparameters is generally only relevant for training on the specific dataset. Even more, it's nearly impossible for a human to outperform algorithmic hyperparameter tuning, unlike feature engineering.

Ultimately, most organizations should create a "repository of machine learning ready features" to curate the best features for each "entity" that matters — customers, trucks, factories, stores, patients, loans, etc.

Perhaps unsurprisingly, a database of reusable features that fits this description naturally emerges in many architectures if you ask people who build machine learning systems. As a result, the machine learning tooling world [seems to agree][3] to call such a database a "feature store."

Feature stores won't replace automated feature engineering tools like Featuretools [^2]. In fact, their most significant benefit is storing the best features from many different sources[^3].

Doing data science and machine learning today still feels like a battle with tooling. However, architectures that include a feature store will simplify things.

[^1]: As an aside, automation still plays a critical role for machine learning platforms where you don't know the shape or form of the data ahead of time. In these cases, you need to automate making the data machine learning ready without human involvement. Fortunately, that isn't the case for most companies using machine learning on their datasets.

[^2]: A library like Featuretools can be handy in a feature store. It stores complete provenance information about each feature that wouldn't be easily accessible by looking at a script written by a data scientist. So, for example, it's easy to trace the data types, columns, relationships, and functions used to generate any feature.

[^3]: A feature store has numerous other benefits, such as feature serving or historical snapshotting. However, the specifics of the use case will dictate which of that functionality is necessary, so it's harder to say which functionality is required to be a feature store.

[1]: https://github.com/alteryx/featuretools
[2]: https://github.com/alteryx/evalml
[3]: https://www.featurestore.org/