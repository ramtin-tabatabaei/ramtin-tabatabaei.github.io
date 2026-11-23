---
title: "CoMET"
subtitle: "Condition-Based Monitoring of Execution with Behaviour Trees for Failure Detection in Robotic Manipulation"
permalink: /research/comet/
order: 0
featured_project: true
thumbnail: "/images/projects/comet.jpg"
project_context: "Robot manipulation · Execution monitoring"
short_summary: "Did the robot actually grasp the ball? CoMET checks what should be true at each stage of a manipulation task. I use AHA’s FailGen to test how the monitor responds when an action goes wrong."
summary: "CoMET turns a manipulation task into a behaviour tree with explicit conditions. In the basketball task, for example, the ball should still be in the gripper on the way to the hoop. CoMET checks camera views at waypoints and monitors robot signals between them to identify when a condition stops holding."
video: "/files/projects/comet/comet-demo.mp4"
video_poster: "/images/projects/comet.jpg"
links:
  - label: "Code on GitHub"
    url: "https://github.com/ramtin-tabatabaei/CoMET"
---

## How AHA fits into the evaluation

I use FailGen from the [AHA project](https://github.com/NVlabs/AHA) to introduce failures into RLBench demonstrations. This lets me compare a successful run with one in which the robot misses a grasp or drops an object. The video compares CoMET with AHA-based baselines across 78 manipulation tasks.
