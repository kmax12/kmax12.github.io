---
title: "Analyzing Marathon Race Data"
date: 2022-10-01
draft: true
summary: "To believe I can run a faster race by crunching numbers at my computer is probably nothing more than wishful thinking. Regardless, it was fun to explore this data, and I hope to present some novel ways of analyzing marathon race data."
og_image: /images/posts/solar-economics/cash-flows-summary.jpg
---

I'll be at the starting line of the Chicago marathon in less than a week. With so little time left, I am now reducing my mileage so my body will be fresh for the race.

Since I can't do any more training to improve my fitness, the only thing left to do is think about my strategy for the race. This will be my first marathon, so it's hard to know what to expect.

Fortunately for me, all the times from last year's Chicago marathon are available [online](https://results.chicagomarathon.com/2021/), and with a small amount of effort, I downloaded the data for all 26,000 people who ran the race.

![Data Sample](/marathon/data_sample.png "A sample of the five fastest runners in 2021 Chicago Marathon")

While exploring how to run faster is fun, it isn't my only goal. Honestly, I'm primarily focused on finishing the race without injuring myself.

Nonetheless, I was curious if I could learn anything to improve my chances of running a good race using data. So with that being said, let's dive in.

_Note: if you'd like to recreate or run this analysis with your own data, check out the code here: [kmax12/marathon_analysis](https://github.com/kmax12/marathon_analysis)_

## Pacing Strategy

In some sense, the race strategy is simple. To hit my goal of running sub-4 hours, I need an average pace of 9 minutes and 9 seconds per mile.

However, even though the Chicago marathon course is [relatively flat](https://runnersconnect.net/wp-content/uploads/2012/10/chicago-marathon-course-pro.png), I can see in the data it's unlikely I'll run each mile split at a perfectly even pace.

The published data contains the total elapsed time for each runner after every 5 kilometers and the half marathon distance. Using these times, I can calculate split paces for each runner at various points in the race.

I wanted to focus on casual runners like myself, so I filtered down to runners who finished the race with 8:40/mi - 9:20/mi splits and plotted their average pace per split.

{{< plotly "average_split_pace" >}}

<div class="use-desktop-message">Psst..view on a desktop for interactive graphs!</div>

This plot shows that, on average, the pace stays relatively flat (and below a 4-hour finishing pace) for the race's first half but increases afterward. In particular, **the rate at which runners slow down starts accelerating around 25km (approx. 15.5 mi).**

While seeing this trend helps me understand what to expect, it doesn't provide direct guidance on running a better race. Instead, we must look at what separates runners who ran "good" or "bad" races to develop actionable strategy ideas.

## Who Ran a Good Race?

One challenge with analyzing this data is that it's hard to know each individual runner's goal.

For example, a 3-hour 45-minute finish is good someone trying to break 4 hours but bad for someone trying to break 3.5 hours. Without knowing a runner's goal, it's hard to determine if they ran a "good" or "bad" race [^1].

Perhaps, if we get creative, we can devise a way of labeling some runners.

Let's revisit the premise of this analysis: I am trying to break 4 hours. More generally, it's safe to say few people run a marathon intending to run slightly above a round number.

With that in mind, let's look at the Finish Times Distribution. I also added vertical lines at round finish times in the graph below.

{{< plotly "finish_time_distribution_with_lines" >}}

What clearly stands out is that **more people finish right before a round time relative to right after it**. This substantiates the idea that people run the race with the explicit goal of beating a round time.

Based on this observation, I extracted 1576 runners who "closely missed" or "closely beat" a 4-hour finish time.

<figure class="table-figure">
<table class="table table-hover">
   <thead>
      <tr>
         <th></th>
         <th># Runners</th>
         <th>Finish Time</th>
         <th>Mean Finish Time</th>
         <th>Mean Pace</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><b>Close Beat</b></td>
         <td>868</td>
         <td>3:55 - 4:00</td>
         <td>3:57:34</td>
         <td>09:03</td>
      </tr>
      <tr>
         <td><b>Close Miss</b></td>
         <td>708</td>
         <td>4:00 - 4:05</td>
         <td>4:02:33</td>
         <td>09:14</td>
      </tr>
   </tbody>
</table>
<figcaption>Summary of Close Beat and Close Miss Runners</figcaption>
</figure>

I now have a group of runners that all set out with the same goal as me - to run a sub-4-hour marathon - along with whether or not they accomplished that goal.

**Focusing on the close-to-the-goal finishers makes sense because they are people for whom slight changes to the strategy might be big enough to make a difference.**

## How to be a Close Beat Runner?

Throughout my training, I did numerous runs of half marathon distance. For each of those runs, I would reflect on how I felt at the end because I knew I'd eventually be running a second back-to-back in the process of completing the full marathon.

So, I first wanted to look at the distribution of half marathon times for each group.

{{< plotly "first_half_distribution" >}}

While the Close Beat group ran an average of 1 minute 30 seconds faster than the Close Miss group, **the distributions look very similar**.

Furthermore, the majority of both groups ran the first half in under 2 hours, meaning they were on pace to break 4 hours.

Here's a way to see how similar both groups run the first half of the race: if you picked a random Close Miss runner, there is a 44% probability they ran faster than a random Close Beat Runner.

Put another way, **if you run the first half in slightly under 2 hours, it's hard to predict if you will be a Close Beat or Close Miss runner**.

My takeaway? The difference between these two groups is how they run the race's second half.

## What Happens in the Second Half?

Earlier, we looked at the average pace at each split. Now, let's look at the _difference_ in pace at each split between Close Beat and Close Miss runners. In the graph below, each bar represents the pace difference between close beat and miss runners.

{{< plotly "pace_difference" >}}

Across the entire race, Close Miss runners have an average pace of 11 seconds slower than Close Beat runners (grey horizontal line). However, the individual splits tell a different story.

**The Close Miss runners run faster than expected for the race's first half. But, for the race's second half, they are running slower than expected** relative to the Close Beat runners.

We know from earlier that most people slow down around the 35km mark (21.5mi). Still, the Close Miss group slows a disproportionate amount compared to the Close Beat group because their difference in pace is greater than other splits.

**This suggests to me that the Close Miss group ran too fast at the beginning of the race** and potentially "[hit the wall](https://www.runnersworld.com/uk/training/marathon/a774858/how-to-avoid-the-wall-and-cope-if-you-hit-it/)".

## Second Half Slow Down

Finally, let's dig deeper into the correlation between the second-half slowdown and finish time by looking across all runners.

In the plot below, I graph the percentage slower each runner completes the second half vs. their overall finish time, along with the best fit trendline.

{{< plotly "finish_time_vs_percent_slowdown" >}}

It's hard to prove causation, but the correlation is clear. **On average, the more you slow down in the race's second half, the slower your finish time.**

## My Race Strategy

Overall, this analysis reaffirms that conventional wisdom is correct. The best pacing strategy is to avoid slowing down later in the race by not starting too fast.

Unfortunately, acting on this is tricky because setting an initial pace depends on my ultimate finishing time, and I've never run a marathon before.

However, if my main goal is to break 4 hours, it translates into a simple strategy: **run the first half a bit 2 hours and then slow down as little as possible**

To help me achieve that, 3 ideas come to mind.

1. At the beginning of the race, I don't need to run faster to put "time in the bank." Instead, I should focus on energy-efficient running to have "energy in the bank." So, for example, I shouldn't waste energy weaving around runners unless I'm running significantly slower than a 9:09 pace.
2. Focus on fueling correctly during the race to have energy for the race's second half.
3. Be mentally prepared to push starting around 30km (~19miles) when many runners' paces spike slower.

## Improving Analysis

This analysis only looked at a subset of good/bad race times. There are definitely runners who had good races whose strategies I didn't analyze. Additionally, my labeling of good and bad races may be incorrect. In particular, the people who just broke 4 hrs might not consider it a good race but rather "good enough."

Along those lines, the best strategy may be contained in runners who solidly beat 4 hrs rather than closely beat it. However, I couldn't consider these people because I could not tell if someone between two round numbers had a good or bad race.

## Final thoughts

To believe I can run a faster race by crunching numbers at my computer is probably nothing more than wishful thinking. Regardless, it was enjoyable to explore this data, and I hope I presented some novel ways of analyzing marathon race data.

I'll close out with an animation I made to visualize the results. The Close Beat (Green) and Close Miss (Red) runners running around the course:

![Race Animation](/marathon/race.gif)

[^1]: In Chicago, like many other marathons, you are assigned a starting time based on your self-selected estimated finish time. The dataset doesn't contain this data, but I did have the time of day each runner started, which likely could be used to reverse out what starting corral a runner was a part of. I chose not to do this because I figured it was less generalizable to other marathons than the close beat / close miss method.
