---
title:
permalink: /
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

<div class="home-page">
  <section class="home-hero">
    <p class="home-hero__eyebrow">Ph.D. Candidate | University of Melbourne</p>
    <h1 class="home-hero__title">
      <span class="home-hero__title-line">Human-Robot Interaction Researcher</span>
      <span class="home-hero__title-line">Building Reliable Robot Systems</span>
    </h1>
    <div class="home-hero__copy">
      <p class="home-hero__lead">I build and study robot behaviours that remain understandable, adaptive, and trustworthy when things go wrong. My work combines human-robot interaction, robotics engineering, perception, and behavioral data analysis.</p>
      <p class="home-hero__lead home-hero__lead--secondary">Across controlled user studies, live robotics demonstrations, and real-time perception pipelines, I investigate how people notice robot failures, how trust changes after those failures, and how robots should communicate and recover. I work with ROS-based systems, gaze and eye-tracking data, collaborative task design, and social robot platforms to turn research questions into practical robotic systems.</p>
    </div>
    <div class="home-hero__actions">
      <a class="btn" href="{{ base_path }}/cv/">View CV</a>
      <a class="btn btn--inverse" href="{{ base_path }}/publications/">Publications</a>
    </div>
    <div class="home-hero__chips">
      <span class="home-chip">ROS</span>
      <span class="home-chip">Human-Robot Interaction</span>
      <span class="home-chip">Gaze Analytics</span>
      <span class="home-chip">Robot Failure Recovery</span>
      <span class="home-chip">Behavioral Data Analysis</span>
    </div>
  </section>

  <section class="home-summary-grid">
    <article class="home-card">
      <p class="home-card__label">Current role</p>
      <h2>Ph.D. candidate in HRI</h2>
      <p>I am based in the School of Computing and Information Systems at the University of Melbourne, working with <a href="https://wafa.johal.org/">A/Prof. Wafa Johal</a> and Prof. Vassilis Kostakos in the Human-Computer Interaction Group and the <a href="https://chri-lab.github.io/">Human-Robot Interaction Lab</a>.</p>
    </article>

    <article class="home-card">
      <p class="home-card__label">Research question</p>
      <h2>What happens when robots fail?</h2>
      <p>I study how people interpret robot failures, how trust changes across repeated failures, and how robots should detect, communicate, and recover from mistakes during collaboration.</p>
    </article>

    <article class="home-card">
      <p class="home-card__label">Hands-on systems</p>
      <h2>From experiments to live demos</h2>
      <p>I have built and evaluated collaborative robot behaviours on Tiago and Furhat, combining user studies, gaze sensing, and real-time analysis in both research and public-facing demonstrations.</p>
    </article>
  </section>

  <section class="home-section">
    <div class="home-section__header">
      <p class="home-section__eyebrow">Research</p>
      <h2 class="home-section__title">Selected Research and Engineering Work</h2>
      <p class="home-section__intro">My work challenges the assumption that robots and AI systems are flawless. I focus on failure detection, trust calibration, and recovery strategies for human-robot collaboration.</p>
    </div>

    <div class="home-research-carousel" data-home-research-carousel>
      <div class="home-research-carousel__controls">
        <button type="button" class="home-research-carousel__button" data-slide-direction="-1" aria-label="Show previous study">&#8592;</button>
        <p class="home-research-carousel__status">Study <span data-current-slide>1</span> / <span data-total-slides>2</span></p>
        <button type="button" class="home-research-carousel__button" data-slide-direction="1" aria-label="Show next study">&#8594;</button>
      </div>

      <article class="home-research-slide home-research-card is-active" data-home-research-slide>
        <p class="home-research-card__index">01</p>
        <h3>Gaze-Based Robot Failure Detection</h3>
        <p>For robots, detecting and predicting failures as early as possible is vital to prevent damage and negative user experiences. I studied user non-verbal behaviour, especially gaze patterns, to identify cues that indicate when a failure is about to occur.</p>
        <ul class="home-list">
          <li>User gaze behaviour can signal the onset of a robot failure.</li>
          <li>Gaze patterns are related to the type of failure the robot makes.</li>
          <li>A random forest classifier showed strong potential for detecting failures within a few seconds after they occur.</li>
        </ul>
        <div class="home-video">
          <iframe data-video-src="https://www.youtube.com/embed/wHYsmDMllyY" title="Gaze-based robot failure detection video" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
      </article>

      <article class="home-research-slide home-research-card" data-home-research-slide hidden>
        <p class="home-research-card__index">02</p>
        <h3>Trust Dynamics Across Multiple Robot Failures</h3>
        <p>Robot failures often happen more than once during collaboration, and their effects on user trust can accumulate. I examine how repeated failures change trust, perceived robot intelligence, and the value of showing failure awareness.</p>
        <ul class="home-list">
          <li>User trust is influenced by both the current failure and the failures that came before it.</li>
          <li>Different failure sequences with similar severity can produce different trust and intelligence judgments.</li>
          <li>Failure awareness helps after serious failures, but it can reduce trust when the failure is minor or barely noticeable.</li>
        </ul>
        <div class="home-video">
          <iframe data-video-src="https://www.youtube.com/embed/4mW9Y5JS5RM" title="Trust dynamics across robot failures video" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
      </article>
    </div>
  </section>

  <section class="home-section home-section--compact">
    <div class="home-section__header">
      <p class="home-section__eyebrow">Capabilities</p>
      <h2 class="home-section__title">Technical Strengths</h2>
    </div>

    <div class="home-strength-grid">
      <article class="home-mini-card">
        <h3>Robotics and HRI</h3>
        <ul class="home-mini-list">
          <li>ROS</li>
          <li>Collaborative task design</li>
          <li>Social robotics</li>
          <li>Behavior design</li>
          <li>User studies</li>
        </ul>
      </article>
      <article class="home-mini-card">
        <h3>Perception and Data</h3>
        <ul class="home-mini-list">
          <li>Eye tracking</li>
          <li>Gaze analytics</li>
          <li>Computer vision</li>
          <li>Annotation workflows</li>
          <li>Statistical modeling</li>
        </ul>
      </article>
      <article class="home-mini-card">
        <h3>Programming</h3>
        <ul class="home-mini-list">
          <li>Python</li>
          <li>Machine learning workflows</li>
          <li>Data processing</li>
          <li>API integration</li>
        </ul>
      </article>
      <article class="home-mini-card">
        <h3>Prototyping and Simulation</h3>
        <ul class="home-mini-list">
          <li>Unity</li>
          <li>SolidWorks</li>
          <li>Interactive prototyping</li>
          <li>Experimental system design</li>
        </ul>
      </article>
    </div>
  </section>

  <section class="home-section home-section--compact">
    <div class="home-section__header">
      <p class="home-section__eyebrow">Background</p>
      <h2 class="home-section__title">Education and Teaching</h2>
    </div>

    <div class="home-two-column">
      <article class="home-panel">
        <h3>Education</h3>
        <ul class="home-list">
          <li><strong>Ph.D. (Ongoing)</strong> - School of Computing and Information Systems, University of Melbourne</li>
          <li><strong>M.Sc. in Applied Design</strong> - Sharif University of Technology, 2021-2023</li>
          <li><strong>B.Sc. in Mechanical Engineering</strong> - University of Tehran, 2017-2021</li>
        </ul>
      </article>

      <article class="home-panel">
        <h3>Teaching</h3>
        <ul class="home-list">
          <li><strong>Elements of Data Processing</strong>, Semester 2, 2025 - University of Melbourne</li>
        </ul>
      </article>
    </div>
  </section>
</div>
