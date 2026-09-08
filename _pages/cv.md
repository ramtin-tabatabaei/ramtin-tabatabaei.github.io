---
layout: academic
title: "Curriculum vitae"
permalink: /cv/
intro: "Ramtin Tabatabaei · Human–robot interaction researcher"
redirect_from:
  - /resume
---

<nav class="project-index" aria-label="CV sections">
  <a href="#education">Education</a>
  <a href="#experience">Research experience</a>
  <a href="#teaching">Teaching</a>
  <a href="#skills">Technical skills</a>
  <a href="#recognition">Awards</a>
</nav>

<section class="academic-section" id="education">
  <h2>Education</h2>
  <div class="cv-entry">
    <p class="cv-date">Dec 2023 – Present</p>
    <div><h3>Ph.D., Computing &amp; Information Systems</h3><p class="cv-institution">University of Melbourne</p><p><strong>Thesis:</strong> Exploring and Exploiting Human Behavioural Responses to Robot Failures in Human-Robot Interaction</p><p><strong>Supervisors:</strong> Wafa Johal and Vassilis Kostakos</p></div>
  </div>
  <div class="cv-entry">
    <p class="cv-date">Sep 2021 – Jun 2023</p>
    <div><h3>MSc, Mechanical Engineering</h3><p class="cv-institution">Sharif University of Technology</p><p><strong>Thesis:</strong> Empirical motion-time pattern for human gaze behaviour in social situations using DNNs</p><p><strong>Supervisors:</strong> Alireza Taheri and Ali Meghdari</p><p><strong>GPA:</strong> 18.10/20 (3.87/4.00)</p></div>
  </div>
  <div class="cv-entry">
    <p class="cv-date">Sep 2017 – Sep 2021</p>
    <div><h3>BSc, Mechanical Engineering</h3><p class="cv-institution">University of Tehran</p><p><strong>Thesis:</strong> Controller design for a refrigerator using Peltier modules</p><p><strong>Supervisor:</strong> Ehsan Hosseinian</p><p><strong>GPA:</strong> 17.45/20 (3.80/4.00)</p></div>
  </div>
</section>

<section class="academic-section" id="experience">
  <h2>Research experience</h2>
  <div class="cv-entry">
    <p class="cv-date">Dec 2023 – Present</p>
    <div><h3>Researcher</h3><p class="cv-institution">Interactive Technologies Lab (IXT), University of Melbourne</p>
      <ul>
        <li>Built ROS-based collaborative tasks on Tiago with diverse failure conditions and conducted controlled user studies with more than 50 participants.</li>
        <li>Developed pipelines integrating eye tracking, ROS synchronisation, and real-time gaze feature extraction for human-centred failure detection.</li>
        <li>Designed a simulation-based failure detection framework in NVIDIA Isaac using behaviour trees and vision–language model reasoning for autonomous detection and recovery.</li>
        <li>Developed emotional expressions on Furhat using facial action units, with VLM- and user-based evaluation.</li>
        <li>Contributed to live robotics demonstrations for academic and public audiences.</li>
      </ul>
    </div>
  </div>
  <div class="cv-entry">
    <p class="cv-date">Sep 2021 – Sep 2023</p>
    <div><h3>Research Assistant</h3><p class="cv-institution">CEDRA, Sharif University of Technology</p><ul><li>Programmed and ran HRI experiments with Nao and Opo robots to study gaze behaviour in children and young adults.</li><li>Built deep learning models for lip reading and facial emotion recognition from video data.</li></ul></div>
  </div>
</section>

<section class="academic-section" id="teaching">
  <h2>Teaching &amp; supervision</h2>
  <div class="cv-entry">
    <p class="cv-date">2024 – Present</p>
    <div><h3>University of Melbourne</h3><ul><li><strong>Elements of Data Processing</strong> — Tutor, Semester 2, 2025 and Semester 1, 2026.</li><li><strong>Machine Learning</strong> — Tutor, Semester 1, 2026.</li><li><strong>Master's project supervision</strong> — March–July 2024. Supervised development of a web application for annotating ROSBag data.</li></ul></div>
  </div>
  <div class="cv-entry">
    <p class="cv-date">2022 – 2023</p>
    <div><h3>Sharif University of Technology</h3><ul><li><strong>Social Cognitive Robotics</strong> — Tutor, January–June 2023.</li><li><strong>Advanced Math 1</strong> — Tutor, September–December 2022.</li></ul></div>
  </div>
</section>

<section class="academic-section">
  <div class="section-heading"><h2>Publications</h2><a href="{{ '/publications/' | relative_url }}">Publication details <span aria-hidden="true">↗</span></a></div>
  {% assign cv_papers = site.publications | where_exp: 'paper', 'paper.hidden != true' | where_exp: 'paper', 'paper.paper_year != nil' | sort: 'paper_year' | reverse %}
  {% for paper in cv_papers %}{% include publication-entry.html paper=paper %}{% endfor %}
</section>

<section class="academic-section" id="skills">
  <h2>Technical skills</h2>
  <dl class="cv-skills">
    <div><dt>Robotics</dt><dd>ROS, Tiago, Furhat, Nao, Opo, collaborative task design, interaction behaviours, NVIDIA Isaac, behaviour trees.</dd></div>
    <div><dt>Perception &amp; programming</dt><dd>Python, OpenCV, Pupil Labs, eye tracking, computer vision, LLM/VLM reasoning, OpenAI APIs, API integration.</dd></div>
    <div><dt>Research methods</dt><dd>Experimental design, controlled user studies, trust measurement, multimodal behavioural analysis, annotation workflows, linear mixed-effects and cumulative link mixed models.</dd></div>
    <div><dt>Modelling</dt><dd>Unity and SolidWorks.</dd></div>
  </dl>
</section>

<section class="academic-section">
  <h2>Demonstrations &amp; public engagement</h2>
  <ul class="academic-records">
    <li><span>Sep 2025</span><div><strong>Innovation Week.</strong> Designed and delivered a Furhat social interaction demonstration with rapid behaviour scripting and multi-party interaction.</div></li>
    <li><span>Sep 2025</span><div><strong>University of Melbourne Showcase.</strong> Presented an interactive robotics pipeline combining real-time perception, behaviour control, and HRI.</div></li>
    <li><span>Mar 2025</span><div><strong>Post-HRI academic visit.</strong> Demonstrated an office assistant robot on Tiago with autonomous navigation and interaction.</div></li>
    <li><span>Oct 2024</span><div><strong>CIS Doctoral Colloquium.</strong> Poster presentation: <em>Gazing at Failure: Investigating Human Gaze in Response to Robot Failure in Collaborative Tasks.</em></div></li>
    <li><span>Sep 2024</span><div><strong>Ubicomp demo session.</strong> Live demonstration of robot failures in human–robot collaboration using Tiago.</div></li>
    <li><span>Aug 2024</span><div><strong>University Open Day.</strong> Public demonstration of autonomous social robotics.</div></li>
  </ul>
</section>

<section class="academic-section" id="recognition">
  <h2>Awards &amp; honours</h2>
  <ul class="academic-records">
    <li><span>Mar 2024</span><div><strong>Winner, HRI24 Robot Challenge.</strong> Office Assistant on Tiago, Team Melbourne.</div></li>
    <li><span>Aug 2021</span><div>Top 0.2% in the national master's entrance examination.</div></li>
    <li><span>Jun 2021</span><div>Top 15% of graduating class.</div></li>
    <li><span>Jul 2017</span><div>Top 1% in the national bachelor's entrance examination.</div></li>
  </ul>
</section>

<section class="academic-section">
  <h2>Languages</h2>
  <p><strong>Persian:</strong> Native. <strong>English:</strong> IELTS 7.0 (Listening 7.0, Reading 7.5, Writing 6.5, Speaking 6.5).</p>
</section>
