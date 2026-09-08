---
title: "Ramtin Tabatabaei — Robotics & AI Engineer"
layout: hire
permalink: /hire/
author_profile: false
---

<section class="hire-hero">
  <div class="hire-hero__glow" aria-hidden="true"></div>
  <div class="hire-hero__inner">
    <p class="hire-hero__eyebrow">Robotics &amp; AI Engineer · Human–Robot Interaction</p>
    <h1 class="hire-hero__title">
      I build robots that <span class="hire-grad">detect, communicate, and recover</span> from failure.
    </h1>
    <p class="hire-hero__lead">
      Ph.D. researcher and full-stack robotics engineer. I design end-to-end systems on real
      robots — from ROS control and perception pipelines to LLM/VLM-based reasoning — and validate
      them through real-world experiments with 50+ users.
    </p>
    <div class="hire-hero__actions">
      <a class="hire-btn hire-btn--primary" href="{{ base_path }}/cv/">View Résumé</a>
      <a class="hire-btn" href="#projects">See Projects</a>
      <a class="hire-btn hire-btn--ghost" href="mailto:{{ site.author.email }}">Get in touch</a>
    </div>
    <ul class="hire-chips">
      <li>ROS</li>
      <li>Python</li>
      <li>LLMs / VLMs</li>
      <li>Computer Vision</li>
      <li>NVIDIA Isaac</li>
      <li>Behavior Trees</li>
      <li>Unity</li>
      <li>Statistical Modeling</li>
    </ul>
  </div>
</section>

<section class="hire-stats" data-reveal>
  <div class="hire-stats__inner">
    <div class="hire-stat">
      <span class="hire-stat__num">50<span class="hire-stat__plus">+</span></span>
      <span class="hire-stat__label">participants in real-robot user studies</span>
    </div>
    <div class="hire-stat">
      <span class="hire-stat__num">4</span>
      <span class="hire-stat__label">robot platforms shipped on (Tiago, Furhat, Nao, Opo)</span>
    </div>
    <div class="hire-stat">
      <span class="hire-stat__num">5<span class="hire-stat__plus">+</span></span>
      <span class="hire-stat__label">peer-reviewed publications (CHI, HRI)</span>
    </div>
    <div class="hire-stat">
      <span class="hire-stat__num">#1</span>
      <span class="hire-stat__label">Winner, HRI'24 Robot Challenge</span>
    </div>
  </div>
</section>

<section class="hire-section" id="skills">
  <div class="hire-section__head" data-reveal>
    <p class="hire-section__eyebrow">What I do</p>
    <h2 class="hire-section__title">Engineering strengths</h2>
    <p class="hire-section__intro">I work across the full stack of a robotics system — hardware integration, perception, reasoning, and the human studies that prove it works.</p>
  </div>
  <div class="hire-grid hire-grid--skills">
    <article class="hire-card" data-reveal>
      <div class="hire-card__icon" aria-hidden="true">🤖</div>
      <h3>Robotics systems</h3>
      <p>ROS workflows, real-time control, and collaborative task design on Tiago (PAL Robotics) and the Furhat social robot. End-to-end systems that run live, not just in simulation.</p>
    </article>
    <article class="hire-card" data-reveal>
      <div class="hire-card__icon" aria-hidden="true">👁️</div>
      <h3>Perception &amp; data</h3>
      <p>Eye tracking with Pupil Labs, OpenCV computer-vision pipelines, ROS synchronization, and real-time feature extraction. Built annotation workflows for multimodal interaction data.</p>
    </article>
    <article class="hire-card" data-reveal>
      <div class="hire-card__icon" aria-hidden="true">🧠</div>
      <h3>AI reasoning</h3>
      <p>LLM- and VLM-based reasoning via OpenAI APIs, integrated with behavior trees in NVIDIA Isaac for autonomous failure detection and recovery. Python throughout.</p>
    </article>
    <article class="hire-card" data-reveal>
      <div class="hire-card__icon" aria-hidden="true">📊</div>
      <h3>Studies &amp; analysis</h3>
      <p>Experimental design, study execution with 50+ participants, and rigorous analysis — linear mixed-effects and cumulative link mixed models — to turn behavior into evidence.</p>
    </article>
  </div>
</section>

<section class="hire-section hire-section--tint" id="projects">
  <div class="hire-section__head" data-reveal>
    <p class="hire-section__eyebrow">Selected work</p>
    <h2 class="hire-section__title">Projects &amp; systems</h2>
    <p class="hire-section__intro">A sample of systems I designed, built, and evaluated on real robots.</p>
  </div>
  <div class="hire-grid hire-grid--projects">
    <article class="hire-project" data-reveal>
      <span class="hire-project__tag">Perception · ML</span>
      <h3>Gaze-based failure detection</h3>
      <p>A pipeline that fuses eye tracking, ROS synchronization, and real-time gaze features to detect robot failures from human reactions — with a random-forest classifier flagging failures within seconds.</p>
      <ul class="hire-project__stack">
        <li>Pupil Labs</li><li>ROS</li><li>OpenCV</li><li>Python</li>
      </ul>
      <a class="hire-project__link" href="{{ base_path }}/research/gaze-based-failure-detection/">Read the case study →</a>
    </article>
    <article class="hire-project" data-reveal>
      <span class="hire-project__tag">Autonomy · VLM</span>
      <h3>Autonomous failure recovery</h3>
      <p>A simulation-based failure detection framework in NVIDIA Isaac combining behavior trees with VLM-based reasoning, enabling a robot to autonomously detect and recover from errors.</p>
      <ul class="hire-project__stack">
        <li>NVIDIA Isaac</li><li>Behavior Trees</li><li>VLM</li><li>Python</li>
      </ul>
    </article>
    <article class="hire-project" data-reveal>
      <span class="hire-project__tag">HRI · Trust</span>
      <h3>Trust under repeated failure</h3>
      <p>A collaborative Tangram system on Tiago that scripts controlled robot failures and awareness behaviors, used in a 54-participant study on how trust evolves across repeated errors.</p>
      <ul class="hire-project__stack">
        <li>Tiago</li><li>ROS</li><li>Study design</li><li>Mixed models</li>
      </ul>
      <a class="hire-project__link" href="{{ base_path }}/research/trust-dynamics-robot-failures/">Read the case study →</a>
    </article>
    <article class="hire-project" data-reveal>
      <span class="hire-project__tag">Social robots</span>
      <h3>Furhat emotional expressions</h3>
      <p>Complex emotional expressions built from facial action units on the Furhat robot, evaluated with both VLM-based and user-based methods — and demoed live for public audiences.</p>
      <ul class="hire-project__stack">
        <li>Furhat</li><li>FACS</li><li>VLM eval</li>
      </ul>
    </article>
    <article class="hire-project" data-reveal>
      <span class="hire-project__tag">Award-winning</span>
      <h3>OfficeMate assistant on Tiago</h3>
      <p>An office-assistant robot with autonomous navigation and interaction on Tiago — winner of the HRI'24 Robot Challenge with Team Melbourne.</p>
      <ul class="hire-project__stack">
        <li>Tiago</li><li>Navigation</li><li>ROS</li>
      </ul>
      <a class="hire-project__link" href="{{ base_path }}/publication/officemate/">Read more →</a>
    </article>
    <article class="hire-project" data-reveal>
      <span class="hire-project__tag">Tooling · Web</span>
      <h3>ROSAnnotator</h3>
      <p>A web application for analyzing ROSBag data in human-robot interaction, making multimodal interaction logs searchable and annotatable. Supervised through to delivery.</p>
      <ul class="hire-project__stack">
        <li>Web app</li><li>ROSBag</li><li>Annotation</li>
      </ul>
      <a class="hire-project__link" href="{{ base_path }}/publication/rosannotator/">Read more →</a>
    </article>
  </div>
</section>

<section class="hire-section" id="experience">
  <div class="hire-section__head" data-reveal>
    <p class="hire-section__eyebrow">Track record</p>
    <h2 class="hire-section__title">Experience</h2>
  </div>
  <div class="hire-timeline">
    <article class="hire-timeline__item" data-reveal>
      <div class="hire-timeline__when">Dec 2023 – Present</div>
      <div class="hire-timeline__body">
        <h3>Researcher &amp; Engineer — University of Melbourne</h3>
        <p class="hire-timeline__where">Interactive Technologies Lab (IXT) · Melbourne, Australia</p>
        <ul>
          <li>Built ROS-based collaborative tasks with diverse failure conditions and ran controlled studies with <strong>50+ participants</strong> on real robots.</li>
          <li>Developed pipelines integrating eye tracking, ROS synchronization, and real-time gaze feature extraction.</li>
          <li>Designed a simulation-based failure detection framework in NVIDIA Isaac using behavior trees and VLM-based reasoning.</li>
          <li>Delivered live robotics showcases and public demos.</li>
        </ul>
      </div>
    </article>
    <article class="hire-timeline__item" data-reveal>
      <div class="hire-timeline__when">Sep 2021 – Sep 2023</div>
      <div class="hire-timeline__body">
        <h3>Research Assistant — Sharif University of Technology</h3>
        <p class="hire-timeline__where">CEDRA · Tehran, Iran</p>
        <ul>
          <li>Programmed and ran HRI experiments with Nao and Opo robots studying gaze behavior.</li>
          <li>Built deep-learning models for lip reading and facial emotion recognition from video.</li>
        </ul>
      </div>
    </article>
  </div>
</section>

<section class="hire-cta" id="contact" data-reveal>
  <div class="hire-cta__inner">
    <h2>Let’s build something that works in the real world.</h2>
    <p>I’m open to robotics, ML, and AI engineering roles. Happy to talk through any of the projects above.</p>
    <div class="hire-hero__actions hire-hero__actions--center">
      <a class="hire-btn hire-btn--primary" href="mailto:{{ site.author.email }}">Email me</a>
      {% if site.author.linkedin %}<a class="hire-btn" href="https://www.linkedin.com/in/{{ site.author.linkedin }}/">LinkedIn</a>{% endif %}
      <a class="hire-btn hire-btn--ghost" href="{{ base_path }}/cv/">Full résumé</a>
    </div>
  </div>
</section>
