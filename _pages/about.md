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
      <span class="home-hero__title-line">Human–Robot Interaction Researcher</span>
      <span class="home-hero__title-line home-hero__title-line--secondary">Designing Failure-Aware and Trustworthy Robotic Systems</span>
    </h1>
    <div class="home-hero__copy">
    <p class="home-hero__lead">
      I investigate robot behavior under failure, with a focus on maintaining transparency, adaptability, and trust in human–robot interaction. My research integrates robotics systems, perception, and vision–language/large language model (VLM/LLM)-based reasoning to study failure detection and recovery in collaborative settings.
    </p>
    <p class="home-hero__lead home-hero__lead--secondary">
      I examine how humans perceive and respond to robot failures, how trust evolves across repeated interactions, and how behavioral signals (e.g., gaze and interaction patterns) can inform failure detection. In parallel, I develop external reasoning frameworks that enable robots to autonomously detect failures and select appropriate recovery strategies.
    </p>
    <p class="home-hero__lead home-hero__lead--secondary">
      My work is grounded in end-to-end system development and validated through real-robot experiments, simulation environments, and controlled user studies.
    </p>
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
      <p>I study how people interpret robot failures, how trust evolves across repeated interactions, and how robots can detect, communicate, and recover from errors during collaboration through both human behavioral signals and external reasoning systems (e.g., LLMs/VLMs).</p>
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


 <section class="cv-section cv-section--capabilities">
    <div class="cv-section__header">
      <p class="cv-section__eyebrow">Capabilities</p>
      <h2 class="cv-section__title">Technical Strengths</h2>
    </div>
    <div class="cv-grid cv-grid--2">
      <article class="cv-card">
        <h3>Robotics & HRI</h3>
        <ul class="cv-list">
          <li><strong>Robotics systems:</strong> ROS workflows, Tiago (PAL Robotics), Furhat social robot, collaborative task design, interaction behaviors</li>
          <li><strong>Human studies:</strong> experimental design, study execution, trust measurement, multimodal behavioral analysis</li>
          <li><strong>Demonstration work:</strong> live showcases, public-facing robotics demos, rapid prototyping for interaction scenarios</li>
        </ul>
      </article>
      <article class="cv-card">
        <h3>Perception, Programming & Analysis</h3>
        <ul class="cv-list">
          <li><strong>Perception and data:</strong> Pupil Labs, gaze tracking and processing, annotation workflows, OpenCV, computer vision pipelines</li>
          <li><strong>Programming and systems:</strong> Python, ROS, LLM- and VLM-based reasoning via OpenAI APIs, API integration</li>
          <li><strong>Modeling and analysis:</strong> Unity, SolidWorks, statistical modeling (linear mixed-effects models, cumulative link mixed models)</li>
        </ul>
      </article>
    </div>
  </section>

  <section class="cv-section cv-section--experience">
    <div class="cv-section__header">
      <p class="cv-section__eyebrow">Career</p>
      <h2 class="cv-section__title">Experience</h2>
    </div>
    <div class="cv-timeline cv-timeline--experience">
      <article class="cv-timeline__item">
        <div class="cv-timeline__meta">Melbourne, Australia</div>
        <h3>University of Melbourne</h3>
        <div class="cv-role-stack">
          <section class="cv-role-card">
            <div class="cv-role-card__header">
              <h4>Researcher</h4>
              <span>Dec 2023 – Present</span>
            </div>
            <p class="cv-role-card__subhead">Interactive Technologies Lab (IXT)</p>
            <ul class="cv-list">
              <li><strong>Tiago Robot</strong></li>
                <ul>
                  <li>Built ROS-based collaborative tasks with diverse failure conditions and conducted controlled user studies with <strong>50+ participants</strong> on real robots.</li>
                  <li>Developed pipelines integrating <strong>eye tracking, ROS synchronization, and real-time gaze feature extraction</strong> for human-centered failure detection.</li>
                  <li>Designed a simulation-based failure detection framework in NVIDIA Isaac using <strong>behavior trees and VLM-based reasoning</strong> for autonomous detection and recovery.</li>
                </ul>

                <li><strong>Furhat Robot</strong></li>
                <ul>
                  <li>Developed complex emotional expressions using <strong>facial action units</strong>, with VLM- and user-based evaluation to identify appropriate responses.</li>
                  <li>Contributed to live robotics showcases and demos for academic and public audiences.</li>
                </ul>
            </ul>
          </section>
          <section class="cv-role-card">
            <div class="cv-role-card__header">
              <h4>Tutor & Project Supervisor</h4>
              <span>Mar 2024 – Present</span>
            </div>
            <p class="cv-role-card__subhead">Teaching and supervision</p>
            <ul class="cv-list">
              <li><strong>Elements of Data Processing</strong> · Tutor · Semester 2, 2025 and Semester 1, 2026</li>
              <li><strong>Machine Learning</strong> · Tutor · Semester 1, 2026</li>
              <li><strong>Master's Project</strong> · Supervisor · Mar 2024 – Jul 2024 · Supervised development of a web app for annotating ROSBag data.</li>
            </ul>
          </section>
        </div>
      </article>
      <article class="cv-timeline__item">
        <div class="cv-timeline__meta">Tehran, Iran</div>
        <h3>Sharif University of Technology</h3>
        <div class="cv-role-stack">
          <section class="cv-role-card">
            <div class="cv-role-card__header">
              <h4>Research Assistant</h4>
              <span>Sep 2021 – Sep 2023</span>
            </div>
            <p class="cv-role-card__subhead">CEDRA</p>
            <ul class="cv-list">
              <li>Programmed and ran HRI experiments with <strong>Nao and Opo robots</strong> to study gaze behavior in children and young adults.</li>
              <li>Built deep learning models for <strong>lip reading</strong> and <strong>facial emotion recognition</strong> from video data.</li>
            </ul>
          </section>
          <section class="cv-role-card">
            <div class="cv-role-card__header">
              <h4>Tutor</h4>
              <span>Sep 2022 – Jun 2023</span>
            </div>
            <p class="cv-role-card__subhead">Teaching roles</p>
            <ul class="cv-list">
              <li><strong>Social Cognitive Robotics</strong> · Jan 2023 – Jun 2023</li>
              <li><strong>Advanced Math 1</strong> · Sep 2022 – Dec 2022</li>
            </ul>
          </section>
        </div>
      </article>
    </div>
  </section>

  <section class="cv-section cv-section--education">
    <div class="cv-section__header">
      <p class="cv-section__eyebrow">Academic Path</p>
      <h2 class="cv-section__title">Education</h2>
    </div>
    <div class="cv-timeline">
      <article class="cv-timeline__item">
        <h3>University of Melbourne</h3>
        <div class="cv-role-card__header cv-role-card__header--education">
          <h4>Ph.D., Computing & Information Systems</h4>
          <span>Dec 2023 – Present</span>
        </div>
        <p><strong>Thesis:</strong> <em>Exploring and Exploiting Human Behavioural Responses to Robot Failures in Human-Robot Interaction</em></p>
        <p><strong>Supervisors:</strong> Dr. Wafa Johal & Prof. Vassilis Kostakos</p>
      </article>
      <article class="cv-timeline__item">
        <h3>Sharif University of Technology</h3>
        <div class="cv-role-card__header cv-role-card__header--education">
          <h4>MSc, Mechanical Engineering</h4>
          <span>Sep 2021 – Jun 2023</span>
        </div>
        <p><strong>GPA:</strong> 18.10/20 (= 3.87/4.00)</p>
        <p><strong>Thesis:</strong> <em>Empirical motion-time pattern for human gaze behaviour in social situations using DNNs</em></p>
        <p><strong>Supervisors:</strong> Dr. Alireza Taheri & Prof. Ali Meghdari</p>
      </article>
      <article class="cv-timeline__item">
        <h3>University of Tehran</h3>
        <div class="cv-role-card__header cv-role-card__header--education">
          <h4>BSc, Mechanical Engineering</h4>
          <span>Sep 2017 – Sep 2021</span>
        </div>
        <p><strong>GPA:</strong> 17.45/20 (= 3.80/4.00)</p>
        <p><strong>Thesis:</strong> <em>Controller design for a refrigerator using Peltier modules</em></p>
        <p><strong>Supervisor:</strong> Dr. Ehsan Hosseinian</p>
      </article>
    </div>
  </section>

  <section class="cv-section cv-section--engagement">
    <div class="cv-section__header">
      <p class="cv-section__eyebrow">Engagement</p>
      <h2 class="cv-section__title">Demos & Public Engagement</h2>
    </div>
    <article class="cv-card">
      <ul class="cv-list">
        <li><strong>Innovation Week (Sep 2025):</strong> designed and delivered a Furhat robot social interaction demo with rapid behavior scripting and multi-party interaction.</li>
        <li><strong>University of Melbourne Showcase Event (Sep 2025):</strong> presented an interactive robotics pipeline combining real-time perception, behavior control, and HRI concepts.</li>
        <li><strong>Post-HRI Academic Visit (Mar 2025):</strong> demonstrated an office assistant robot on Tiago with autonomous navigation and interaction.</li>
        <li><strong>CIS Doctoral Colloquium (Oct 2024):</strong> poster presentation, <em>Gazing at Failure: Investigating Human Gaze in Response to Robot Failure in Collaborative Tasks</em>.</li>
        <li><strong>Ubicomp 2025 Demo Session (Sep 2024):</strong> live demo, <em>Robot Failures in Human-Robot Collaboration Using the Tiago Robot</em>.</li>
        <li><strong>University Open Day (Aug 2024):</strong> public demo, <em>Autonomous Social Robotics</em>.</li>
      </ul>
    </article>
  </section>

  <section class="cv-section cv-section--publications">
    <div class="cv-section__header">
      <p class="cv-section__eyebrow">Research Output</p>
      <h2 class="cv-section__title">Selected Publications</h2>
    </div>
    <article class="cv-card">
      <ol class="cv-publication-list">
       <li><strong>Tabatabaei</strong>, Kostakos, Johal. <em>Oops, I Did It Again (But I Know It): Robot Failure Consistency and Awareness in Human-Robot Collaboration.</em> ACM CHI 2026.</li>
        <li><strong>Tabatabaei</strong>, Kostakos, Johal. <em>Gazing at Failure: Investigating Human Gaze in Response to Robot Failure in Collaborative Tasks.</em> ACM/IEEE HRI 2025.</li>
        <li><strong>Tabatabaei</strong>, Kostakos, Johal. <em>Real-Time Detection of Robot Failures Using Gaze Dynamics in Collaborative Tasks.</em> ACM/IEEE HRI 2025.</li>
        <li>Zhang, Li, <strong>Tabatabaei</strong>, Johal. <em>ROSAnnotator: A Web Application for ROSBag Data Analysis in Human-Robot Interaction.</em> ACM/IEEE HRI 2025.</li>
        <li>Pan, Schömbs, Zhang, <strong>Tabatabaei</strong>, Bilal, Johal. <em>OfficeMate: Pilot Evaluation of an Office Assistant Robot.</em> ACM/IEEE HRI 2025.</li>
        <li><strong>Tabatabaei</strong>, Kostakos, Johal. <em>Oops, I Did It Again (But I Know It): Robot Failure Consistency and Awareness in Human-Robot Collaboration.</em> CHI 2026.</li>
      </ol>
    </article>
  </section>

  <section class="cv-section cv-section--details">
    <div class="cv-grid cv-grid--2">
      <article class="cv-card">
        <div class="cv-section__header cv-section__header--tight">
          <p class="cv-section__eyebrow">Recognition</p>
          <h2 class="cv-section__title">Awards & Honors</h2>
        </div>
        <ul class="cv-list">
          <li><strong>Winner, HRI24 Robot Challenge, Office Assistant on Tiago (Team Melbourne)</strong> · Mar 2024</li>
          <li><strong>Top 0.2% National Entrance Exam (Master's)</strong> · Aug 2021</li>
          <li><strong>Top 15% of graduating class</strong> · Jun 2021</li>
          <li><strong>Top 1% National Entrance Exam (Bachelor's)</strong> · Jul 2017</li>
        </ul>
      </article>
      <article class="cv-card">
        <div class="cv-section__header cv-section__header--tight">
          <p class="cv-section__eyebrow">Languages</p>
          <h2 class="cv-section__title">Languages</h2>
        </div>
        <ul class="cv-list">
          <li><strong>English:</strong> IELTS 7.0 (L 7.0, R 7.5, W 6.5, S 6.5)</li>
          <li><strong>Persian:</strong> Native</li>
        </ul>
      </article>
    </div>
  </section>
</div>