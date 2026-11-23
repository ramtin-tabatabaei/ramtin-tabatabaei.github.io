---
layout: academic
title:
permalink: /
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="academic-intro" aria-labelledby="intro-name">
  <div class="academic-intro__copy">
    <p class="academic-kicker">Human–robot interaction</p>
    <h1 id="intro-name">Ramtin <span>Tabatabaei</span></h1>
    <p class="academic-affiliation">Ph.D. candidate, University of Melbourne<br><span>School of Computing and Information Systems</span></p>
    <p class="academic-lead">I study what happens when robots make mistakes. How do people respond, how does trust change, and how can robots recognise and recover from failure?</p>
    <div class="intro-links" aria-label="Contact and academic profiles">
      <a class="btn-link btn-link--primary" href="mailto:{{ site.author.email }}"><i class="far fa-envelope" aria-hidden="true"></i> Email me</a>
      <a class="btn-link" href="{{ site.author.googlescholar }}">Google Scholar <span aria-hidden="true">↗</span></a>
      <a class="btn-link" href="https://www.linkedin.com/in/{{ site.author.linkedin }}/">LinkedIn <span aria-hidden="true">↗</span></a>
      <a class="btn-link btn-link--ghost" href="{{ '/cv/' | relative_url }}">CV</a>
    </div>
  </div>
  <figure class="academic-portrait">
    <picture>
      <source srcset="{{ '/images/ramtin-portrait.webp' | relative_url }}" type="image/webp">
      <img src="{{ '/images/ramtin-portrait.jpg' | relative_url }}" alt="Ramtin Tabatabaei standing beside a Pepper robot in the robotics lab" width="1000" height="1250" fetchpriority="high">
    </picture>
    <figcaption>With Pepper in the robotics lab</figcaption>
  </figure>
</section>

<section class="academic-section academic-section--projects" id="projects" aria-labelledby="projects-heading">
  <div class="section-heading">
    <h2 id="projects-heading">Selected research</h2>
    <a href="{{ '/projects/' | relative_url }}">All projects <span aria-hidden="true">→</span></a>
  </div>
  <div class="project-grid">
    {% include research-cards.html %}
  </div>
</section>

<section class="academic-section" aria-labelledby="selected-heading">
  <div class="section-heading"><h2 id="selected-heading">Selected publications</h2><a href="{{ '/publications/' | relative_url }}">All publications <span aria-hidden="true">→</span></a></div>
  {% assign selected_papers = site.publications | where: 'featured', true | where_exp: 'paper', 'paper.hidden != true' | sort: 'paper_year' | reverse %}
  {% for paper in selected_papers limit:2 %}
    {% include publication-entry.html paper=paper %}
  {% endfor %}
</section>

<section class="academic-section" id="research" aria-labelledby="research-heading">
  <div class="section-heading"><h2 id="research-heading">Research focus</h2><a href="{{ '/publications/' | relative_url }}">Publications <span aria-hidden="true">→</span></a></div>
  <p>I combine real-robot experiments, eye tracking, and controlled user studies to understand how people notice, interpret, and respond to robot mistakes. I also develop machine learning methods that combine vision–language models with robot-state monitoring to detect failures and guide recovery. My work connects human behaviour with robot intelligence to make human–robot collaboration more reliable.</p>
  <p>I am supervised by <a href="https://wafa.johal.org/">Wafa Johal</a> and Vassilis Kostakos. My work is part of the Human-Computer Interaction Group and the <a href="https://chri-lab.github.io/">Human-Robot Interaction Lab</a>.</p>
  <dl class="research-directions">
    <div><dt>Behavioural signals</dt><dd>Using gaze and interaction patterns to detect when something goes wrong.</dd></div>
    <div><dt>Trust &amp; recovery</dt><dd>Understanding how repeated failures and robot awareness shape collaboration.</dd></div>
    <div><dt>Robotic systems</dt><dd>Building and evaluating detection and recovery methods on real robots and in simulation.</dd></div>
  </dl>
</section>

<section class="academic-section" aria-labelledby="teaching-heading">
  <div class="section-heading"><h2 id="teaching-heading">Teaching &amp; supervision</h2><a href="{{ '/cv/#teaching' | relative_url }}">Teaching history <span aria-hidden="true">→</span></a></div>
  <p>In Semester 2, 2026, I am a lab tutor for <em>Intelligent Robotics (ECE4078)</em> at Monash University and a marker for <em>Usability Evaluation Methods (INFO20004)</em> at the University of Melbourne. Previously, I tutored <em>Elements of Data Processing</em> (Semester 2, 2025 and Semester 1, 2026) and <em>Machine Learning</em> (Semester 1, 2026) at Melbourne.</p>
  <p>I also supervised a master's project developing a web application for annotating ROSBag data from March to July 2024.</p>
</section>
