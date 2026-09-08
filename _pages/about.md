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
    <h1 id="intro-name">Ramtin Tabatabaei</h1>
    <p class="academic-affiliation">Ph.D. candidate · University of Melbourne</p>
    <p>I study what happens when robots make mistakes: how people respond, how trust changes, and how robots can recognise and recover from failure.</p>
    <p>I am a Ph.D. candidate in the School of Computing and Information Systems, supervised by <a href="https://wafa.johal.org/">Wafa Johal</a> and Vassilis Kostakos. My work is part of the Human-Computer Interaction Group and the <a href="https://chri-lab.github.io/">Human-Robot Interaction Lab</a>.</p>
    <div class="text-links intro-links" aria-label="Contact and academic profiles">
      <a href="mailto:{{ site.author.email }}">Email</a>
      <a href="{{ site.author.googlescholar }}">Google Scholar</a>
      <a href="https://www.linkedin.com/in/{{ site.author.linkedin }}/">LinkedIn</a>
      <a href="{{ '/cv/' | relative_url }}">Curriculum vitae</a>
    </div>
  </div>
  <figure class="academic-portrait">
    <img src="{{ '/images/Me.png' | relative_url }}" alt="Ramtin Tabatabaei" width="230" height="280" fetchpriority="high">
    <figcaption>Melbourne, Australia</figcaption>
  </figure>
</section>

<section class="academic-section" id="research" aria-labelledby="research-heading">
  <div class="section-heading"><h2 id="research-heading">Research</h2><a href="{{ '/projects/' | relative_url }}">Explore projects <span aria-hidden="true">↗</span></a></div>
  <p>My research combines real-robot experiments, eye tracking, and controlled user studies. I use human behavioural signals to investigate robot failures, and develop vision–language model reasoning for failure detection and recovery.</p>
  <dl class="research-directions">
    <div><dt>Behavioural signals</dt><dd>Using gaze and interaction patterns to detect when something goes wrong.</dd></div>
    <div><dt>Trust &amp; recovery</dt><dd>Understanding how repeated failures and robot awareness shape collaboration.</dd></div>
    <div><dt>Robotic systems</dt><dd>Building and evaluating detection and recovery methods on real robots and in simulation.</dd></div>
  </dl>
</section>

<section class="academic-section" aria-labelledby="selected-heading">
  <div class="section-heading"><h2 id="selected-heading">Selected publications</h2><a href="{{ '/publications/' | relative_url }}">All publications <span aria-hidden="true">↗</span></a></div>
  {% assign selected_papers = site.publications | where: 'featured', true | where_exp: 'paper', 'paper.hidden != true' | sort: 'paper_year' | reverse %}
  {% for paper in selected_papers limit:2 %}
    {% include publication-entry.html paper=paper %}
  {% endfor %}
</section>

<section class="academic-section" aria-labelledby="teaching-heading">
  <div class="section-heading"><h2 id="teaching-heading">Teaching &amp; supervision</h2><a href="{{ '/cv/#teaching' | relative_url }}">Teaching history <span aria-hidden="true">↗</span></a></div>
  <p>At the University of Melbourne, I tutor <em>Elements of Data Processing</em> and <em>Machine Learning</em>. I have also supervised a master's project developing a web application for annotating ROSBag data.</p>
</section>
