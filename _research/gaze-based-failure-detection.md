---
thumbnail: "/images/papers/hri2025-robotfailure/Areas Of Interest.jpg"
project_context: "Gaze & behavioural sensing · HRI 2025"
short_summary: "Investigating how gaze changes when a robot makes a mistake, and whether those changes can support early failure detection during collaborative tasks."
title: "Gaze-Based Robot Failure Detection"
subtitle: "Reading human non-verbal behaviour to detect and anticipate robot failures"
permalink: /research/gaze-based-failure-detection/
research_index: "01"
order: 1
summary: "For robots, detecting and predicting failures as early as possible is vital to prevent damage and negative user experiences. I study human non-verbal behaviour — especially gaze patterns — to identify cues that signal when a robot failure is about to occur or has just occurred."
video: "https://www.youtube.com/embed/wHYsmDMllyY"
takeaways:
  - "User gaze behaviour can signal the onset of a robot failure."
  - "Gaze patterns are related to the type of failure the robot makes."
  - "A random forest classifier showed strong potential for detecting failures within a few seconds after they occur."
links:
  -
    label: "Related paper"
    url: "/publication/HRI2025-RobotFailure/"
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
  <h2>Overview</h2>
  <p>This line of work investigates the relationship between human gaze behaviour and robot failures. Using robot-assisted collaborative tasks (such as tangram puzzles), I explore how different failure types affect human perception and gaze dynamics, presenting gaze as a potential signal for robot error detection and recovery.</p>
</section>

<section class="paper-showcase__panel paper-showcase__panel--method">
  <h2>Method and System</h2>
  <p>Participants work with a robot on collaborative tasks while experiencing both <strong>executional</strong> and <strong>decisional</strong> failures at different task stages. Eye tracking (Pupil Labs) is synchronised with ROS, and real-time gaze features are extracted to characterise how people look at the robot, the workspace, and the task before, during, and after a failure.</p>
</section>

<section class="paper-showcase__panel paper-showcase__panel--results">
  <h2>What I Found</h2>
  <p>Executional failures led to increased gaze shifts toward the robot, while decisional failures resulted in less variability in gaze transitions — especially when occurring at the end of a task. These differences make gaze a reliable indicator of <em>whether</em> a failure occurred and <em>what kind</em> of failure it was, which in turn can inform appropriate recovery actions.</p>
</section>

<section class="paper-showcase__panel paper-showcase__panel--discussion">
  <h2>Why It Matters</h2>
  <p>Human-centred failure detection lets robots notice when something has gone wrong even when the failure is not directly observable from their own sensors. By reading the human's reaction, a robot can recover faster and preserve user trust during collaboration.</p>
</section>
