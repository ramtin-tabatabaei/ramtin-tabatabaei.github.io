---
title: "Where Did You Look?"
subtitle: "Gaze-guided vision-language verification of robot failures in human-robot collaboration"
permalink: /research/where-did-you-look/
order: 0.5
featured_project: true
video_heading: "Video"
thumbnail: "/images/projects/where-did-you-look.jpg"
preview: "/files/projects/where-did-you-look/preview.mp4"
project_context: "Gaze + vision-language models · Failure detection"
short_summary: "Human gaze acts as a cheap, always-on lookout for robot failures. Only when gaze raises an alert does a vision-language model inspect the scene and decide whether something really went wrong."
summary: "Robots that pick and place objects often fail without noticing. People working alongside them usually notice first, and their eyes show it. In this project, gaze acts as a lightweight screen that watches every robot action, and a vision-language model (VLM) is called only when gaze raises an alert. The VLM then checks the visual evidence and names the failure."
video: "/files/projects/where-did-you-look/where-did-you-look.mp4"
video_poster: "/images/projects/where-did-you-look-poster.jpg"
video_captions: "/files/projects/where-did-you-look/where-did-you-look.vtt"
tags: ["Eye tracking", "Vision-language models", "51 participants", "1,182 robot actions"]
takeaways:
  - "Gaze alone catches most failures but is noisy: tuned to catch 90% of failures, it raised 456 alerts, and about 7 in 10 were false alarms."
  - "Letting a VLM verify gaze alerts removed almost every false alarm: of 322, only 3 survived, and precision rose from 29.5% to 97.5%."
  - "Gaze-guided verification needed 61% fewer VLM calls than checking every action (F1 0.880 vs 0.921). Checked stage by stage, it needed 75% fewer calls, and 68.7% of failures were confirmed before the robot finished its move."
  - "The trade-off is recall, which fell from 89.9% to 80.1%, because some failures slipped past the gaze screen or were rejected by the VLM."
related_publications:
  -
    title: "Gazing at Failure: Investigating Human Gaze in Response to Robot Failure in Collaborative Tasks"
    venue: "ACM/IEEE HRI 2025"
    url: "/publication/HRI2025-RobotFailure/"
  -
    title: "Real-Time Detection of Robot Failures Using Gaze Dynamics in Collaborative Tasks"
    venue: "ACM/IEEE HRI 2025"
    url: "/publication/real-time-gaze-failure-detection/"
---

<section class="paper-showcase__panel paper-showcase__panel--overview">
  <h2>The Problem</h2>
  <p>Pick-and-place robots rely on sensing, planning and movement, and when one of them fails the robot often carries on as if nothing happened. In our study the robot failed in three ways. It <strong>froze</strong> mid-transport while still holding a piece, it placed a piece in the <strong>wrong location</strong>, or it closed its gripper on nothing and <strong>continued without the piece</strong>. When people work side by side with a robot, a missed failure stalls the task, breaks the rhythm of the collaboration and costs trust.</p>
</section>

<section class="paper-showcase__panel paper-showcase__panel--method">
  <h2>Study and Method</h2>
  <p>Fifty-one participants solved six Tangram puzzles with a TIAGo robot, taking turns to place pieces while wearing eye-tracking glasses that recorded their gaze at 200&nbsp;Hz. We captured 1,182 robot actions, 149 of which were failures.</p>
  <p>The scene was divided into six regions: the board, the gripper, the robot's head and body, and the two piece trays. From these we computed dwell time, transitions between regions, transition entropy and long fixations. Each feature was also compared with that participant's own history. Lightweight classifiers score these features at three checkpoints in each action: after transport, after placement and after the robot returns.</p>
  <p>When the gaze classifier raises an alert, a vision-language model inspects a grid of scene and gripper images from that action. It decides whether a failure happened and, if so, which kind.</p>
</section>

<section class="paper-showcase__panel paper-showcase__panel--results">
  <h2>What We Found</h2>
  <p>On its own, gaze is a sensitive but noisy alarm, because eyes also move when people prepare their own turn, react to a surprising but correct move, or glance at the robot's face. Used as a screen for the VLM, it kept most of the VLM's accuracy at a fraction of the cost. The strongest gaze cues were long, fixed stares at the gripper and the board, and looking at the board more or less than that person usually did.</p>
</section>

<section class="paper-showcase__panel paper-showcase__panel--discussion">
  <h2>Why It Matters</h2>
  <p>A robot doesn't need to check everything all the time. By paying attention to where its human partner looks, it can spend expensive visual reasoning only on the moments that matter. Next we are testing whether this carries over to unseen puzzles and to an entirely different task.</p>
</section>
