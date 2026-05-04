# 🛡️ 90-Day Roadmap — Cybersecurity & GRC

> **Goal:** Build a solid Cybersecurity foundation, targeting a **Technical GRC Analyst** role
> **Duration:** 90 days · 12 weeks · 3 phases
> **Last updated:** 2026

---

## 📌 Overview

| | Phase | Timeline | Objective |
|---|---|---|---|
| 🔵 | System Foundations & Identity | Day 1–30 | Understand the assets worth protecting and establish first control mechanisms |
| 🟠 | Offense, Defense & AI Governance | Day 31–60 | Understand how attackers break policies to build better compliance barriers |
| 🟢 | Arsenal, Portfolio & The Hunt | Day 61–90 | Package skills into tangible evidence that recruiters can't ignore |

---

## 📊 Progress Tracker

> Update manually — change `[ ]` to `[x]` when completed

### Phase 1

- [ ] Week 1 — CIA Triad & Risk Mindset
- [ ] Week 2 — Networking & Network Segmentation
- [ ] Week 3 — Linux & Access Control
- [ ] Week 4 — Cloud Lab & Cloud Security Posture

### Phase 2

- [ ] Week 5 — OWASP Top 10 & Vulnerability Management
- [ ] Week 6 — Kill Chain & Incident Response Plan
- [ ] Week 7 — Blue Team & Continuous Auditing
- [ ] Week 8 — AI Security & AI Governance

### Phase 3

- [ ] Week 9 — Scanning Tools & Compliance Automation
- [ ] Week 10 — Active Directory & Identity Risk
- [ ] Week 11 — CTFs & Pentest Report Writing
- [ ] Week 12 — Portfolio & Positioning as "Technical GRC"

---

## 📁 Repository Structure

```
grc90/
│
├── README.md                          ← This file
│
├── policies/
│   ├── user-account-policy.md         ← Week 3 ⭐
│   └── ai-governance-policy.md        ← Week 8 ⭐
│
├── checklists/
│   └── cloud-hygiene-checklist.md     ← Week 4 ⭐
│
├── playbooks/
│   └── incident-response-playbook.md  ← Week 6 ⭐
│
├── reports/
│   ├── identity-risk-assessment.md    ← Week 10 ⭐
│   └── pentest-report-[machine].md    ← Week 11 ⭐
│
├── labs/
│   ├── week1-risk-register.xlsx
│   ├── week2-wireshark-notes.md
│   ├── week7-kql-queries.md
│   └── week9-cis-audit-report.md
│
├── weekly/
│   ├── week01-cia-nist.md             ← Ngày 1–7
│   ├── week02-networking.md           ← Ngày 8–14
│   ├── week03-linux-access.md         ← Ngày 15–21
│   ├── week04-cloud-lab.md            ← Ngày 22–30
│   ├── week05-owasp-vuln.md           ← Ngày 31–37
│   ├── week06-killchain-ir.md         ← Ngày 38–44
│   ├── week07-blueteam-audit.md       ← Ngày 45–51
│   ├── week08-ai-security.md          ← Ngày 52–60
│   ├── week09-scanning-compliance.md  ← Ngày 61–67
│   ├── week10-ad-identity.md          ← Ngày 68–74
│   ├── week11-ctf-report.md           ← Ngày 75–81
│   └── week12-portfolio-hunt.md       ← Ngày 82–90
│
└── notes/
    ├── cia-triad-analysis.md
    ├── nist-csf-summary.md
    └── mitre-attack-mapping.md
```

---

## 🎯 Personal Positioning — Technical GRC

### Elevator Pitch

> *"I'm a cybersecurity professional specializing in Technical GRC — bridging the gap between hands-on security (cloud security, vulnerability management, identity governance) and compliance frameworks like NIST CSF and ISO 27001. I also focus on AI governance, helping organizations build guardrails for responsible AI adoption."*

### What Sets You Apart

| Skill | Typical GRC Analyst | Technical GRC (you) |
|---|---|---|
| Frameworks | ✅ Knows NIST, ISO 27001 | ✅ Knows + can apply them to real systems |
| Cloud | ❌ Theoretical | ✅ Hands-on AWS labs, detects misconfigurations |
| Pentesting | ❌ None | ✅ Understands attacks to write better controls |
| AI Governance | ❌ Very few have this | ✅ Real policy templates, hands-on experience |
| Evidence | CV with words only | ✅ GitHub portfolio anyone can review |

---

## 📚 Master Resource List

### Frameworks & Standards

- [NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)
- [NIST AI Risk Management Framework](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [EU AI Act](https://artificialintelligenceact.eu/the-act/)

### Practice Platforms

- [TryHackMe](https://tryhackme.com/) — start here
- [HackTheBox](https://www.hackthebox.com/) — once you have a foundation
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — web security
- [Gandalf by Lakera](https://gandalf.lakera.ai/) — AI security

### Tools

- [Wireshark](https://www.wireshark.org/) · [Nmap](https://nmap.org/) · [Burp Suite](https://portswigger.net/burp) · [BloodHound](https://github.com/SpecterOps/BloodHound) · [Prowler](https://github.com/prowler-cloud/prowler)

---
## 🔵 PHASE 1: System Foundations & Identity (Day 1–30)

### Week 1 — CIA Triad & Risk Mindset (GRC Mindset)

**Day 1–7 · Technical + GRC**

#### What to Learn

- Analyze 2–3 major breaches (SolarWinds, Equifax) through the CIA Triad lens
- Learn `Risk = Likelihood × Impact`, distinguish Threat / Vulnerability / Asset
- Read NIST CSF 2.0 — understand the 6 Functions: **GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER**
- Read Section 3: understand Current Profile vs Target Profile, 4 Tiers (Partial → Adaptive)
- Learn Business Impact Analysis (BIA), RTO and RPO

#### Daily Checklist

| Day | Task |
|---|---|
| Day 1 | Study CIA Triad, learn Risk = Likelihood × Impact, analyze Equifax breach through CIA |
| Day 2 | Analyze SolarWinds 2020 through CIA lens, compare with Equifax |
| Day 3 | Read NIST CSF 2.0 PDF — Sections 1, 2, 3. Summarize all 6 Functions in your own words |
| Day 4 | Map Equifax breach to NIST CSF — which Functions did they FAIL at? Start TryHackMe Pre-Security |
| Day 5 | Build a 5×5 Risk Matrix, create a simple Risk Register in Excel (5 security risks) |
| Day 6 | Study BIA, RTO, RPO — apply to Equifax case ($575M fine, reputational damage…) |
| Day 7 | Week review, create GitHub repo `cybersec-grc-journey`, upload Risk Register + notes |

#### Week 1 Deliverables

- [ ] GitHub repo created
- [ ] Risk Register Excel file (5 risks with Likelihood + Impact + Risk Score)
- [ ] Analysis notes on 2 breaches through CIA & NIST CSF

#### Resources

- 📄 [NIST CSF 2.0 — Official PDF](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)
- 🌐 [nist.gov/cyberframework — Quick Start Guides](https://www.nist.gov/cyberframework)
- 🎓 [TryHackMe — Pre-Security Path](https://tryhackme.com/path/outline/presecurity)
- 📖 [Wikipedia: Equifax Data Breach 2017](https://en.wikipedia.org/wiki/2017_Equifax_data_breach)
- 📖 [CISA: SolarWinds Emergency Directive](https://www.cisa.gov/news-events/news/emergency-directive-21-01)

#### End-of-Week Self-Check

> Answer all of these = ready for Week 2 ✅

1. What is the CIA Triad? Give a real-world example for each pillar.
2. What is Risk? Explain it in language a CEO would understand.
3. How many Functions does NIST CSF 2.0 have? Name and briefly describe each.
4. Which Function is **new** in CSF 2.0 compared to v1.1?
5. Which CIA pillar(s) did the Equifax breach violate?

---

### Week 2 — Networking Through the Lens of Control

**Day 8–14 · Technical + GRC**

#### What to Learn

- Master OSI 7 layers, TCP/IP, IP addressing, common Ports & Protocols (80, 443, 22, 3389)
- Practice Wireshark: capture and analyze basic network traffic
- Understand Network Segmentation, VLAN, DMZ — read PCI DSS requirements on network segmentation
- GRC angle: understand why Network Segmentation is a mandatory control in PCI DSS

#### Week 2 Deliverables

- [ ] Wireshark lab notes (capture at least 1 HTTP/HTTPS session)
- [ ] Simple network diagram with segmentation: Internet → DMZ → Internal Network

#### Resources

- 🎓 [TryHackMe Pre-Security — Networking section](https://tryhackme.com/path/outline/presecurity)
- 🎥 [Professor Messer Network+ (YouTube, free)](https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-training-course/)
- 🛠️ [Wireshark — Download](https://www.wireshark.org/download.html)

---

### Week 3 — Linux & Access Control

**Day 15–21 · Technical + GRC**

#### What to Learn

- Master the terminal: navigation, file permissions (`chmod`/`chown`), user management
- Practice basic Privilege Escalation on TryHackMe
- Apply the **Least Privilege** principle
- Write a User Account Management Policy (1 page)

#### Week 3 Deliverables ⭐

- [ ] `📄 policies/user-account-policy.md` — User Account Management Policy

#### Resources

- 🎓 [TryHackMe — Linux Privilege Escalation](https://tryhackme.com/room/linprivesc)

---

### Week 4 — Cloud Lab & Cloud Security Posture

**Day 22–30 · Lab + GRC**

#### What to Learn

- Set up AWS Free Tier lab: create IAM roles, S3 bucket, EC2 instance
- Enable CloudTrail logging, connect Wazuh SIEM (or AWS Security Hub)
- Practice Misconfiguration Assessment: check for public buckets, overly permissive security groups
- Read CIS Benchmark for AWS — understand what a "benchmark" means in GRC context

#### Week 4 Deliverables ⭐

- [ ] `📄 checklists/cloud-hygiene-checklist.md` — Cloud Hygiene Checklist based on CIS

#### Resources

- 🌐 [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- 🛠️ [CloudGoat — Rhino Security Labs (intentionally vulnerable AWS lab)](https://github.com/RhinoSecurityLabs/cloudgoat)
- 🌐 [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

### 🏆 Phase 1 Milestone

> GitHub has **2 first GRC documents**: User Account Policy + Cloud Hygiene Checklist

---

## 🟠 PHASE 2: Offense, Defense & AI Governance (Day 31–60)

### Week 5 — OWASP Top 10 & Vulnerability Management

**Day 31–37 · Technical + GRC**

#### What to Learn

- Practice SQL Injection, XSS, IDOR on DVWA or PortSwigger Web Security Academy
- Learn CVSS scoring: Critical (9.0+), High (7.0–8.9), Medium (4.0–6.9), Low (0.1–3.9)
- Build a Vulnerability Management SLA:
  - 🔴 Critical = remediate within 24 hours
  - 🟠 High = remediate within 7 days
  - 🟡 Medium = remediate within 30 days
  - 🟢 Low = remediate within 90 days
- Prioritize vulnerabilities by business impact, not just CVSS score

#### Week 5 Deliverables

- [ ] Vulnerability Management SLA framework document
- [ ] Practice notes for SQLi and XSS on PortSwigger

#### Resources

- 🎓 [PortSwigger Web Security Academy (free)](https://portswigger.net/web-security)
- 📖 [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- 🌐 [NVD — CVSS Calculator](https://nvd.nist.gov/vuln-metrics/cvss)

---

### Week 6 — Cyber Kill Chain & Incident Response Plan

**Day 38–44 · Technical + GRC**

#### What to Learn

- Practice the full Kill Chain: Recon → Weaponization → Delivery → Exploitation → Reverse Shell
- Learn MITRE ATT&CK framework: map attack techniques to tactics
- Build an Incident Response Playbook with 6 steps:
  1. **Preparation** — before an incident occurs
  2. **Detection & Analysis** — identify and analyze the incident
  3. **Containment** — prevent further spread
  4. **Eradication** — remove the root cause
  5. **Recovery** — restore systems to normal
  6. **Lessons Learned** — post-incident review
- Add: breach notification procedures (GDPR 72h, NIS2) and escalation matrix

#### Week 6 Deliverables ⭐

- [ ] `📄 playbooks/incident-response-playbook.md` — Complete IR Playbook

#### Resources

- 🌐 [MITRE ATT&CK Framework](https://attack.mitre.org/)
- 🎓 [TryHackMe — Jr Penetration Tester Path](https://tryhackme.com/path/outline/jrpenetrationtester)

---

### Week 7 — Blue Team & Continuous Auditing

**Day 45–51 · Technical + Lab**

#### What to Learn

- Write KQL queries (Microsoft Sentinel) and SPL queries (Splunk) to detect anomalies in logs
- Practice threat hunting: identify signs of Lateral Movement and Privilege Escalation in event logs
- Treat log analysis as **Continuous Auditing**: map findings to control violations
- Use AI (Claude/ChatGPT) to summarize policy violations from raw log data

#### Week 7 Deliverables

- [ ] Basic KQL/SPL query library (saved to repo)

#### Resources

- 🎓 [Microsoft Learn — KQL (free)](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)
- 🎓 [TryHackMe — SOC Level 1 Path](https://tryhackme.com/path/outline/soclevel1)

---

### Week 8 — AI Security & AI Governance

**Day 52–60 · Technical + GRC**

#### What to Learn

- Practice Prompt Injection on Gandalf (lakera.ai) and study OWASP Top 10 for LLMs
- Study the EU AI Act: 4-tier risk classification:
  - 🚫 **Unacceptable Risk** — prohibited entirely
  - 🔴 **High Risk** — strict oversight required
  - 🟡 **Limited Risk** — transparency obligations
  - 🟢 **Minimal Risk** — no specific requirements
- Build an AI Usage Policy for an enterprise: data classification, approved tools, guardrails

#### Week 8 Deliverables ⭐

- [ ] `📄 policies/ai-governance-policy.md` — AI Governance Policy template

> 💡 **Note:** This is a major differentiator — very few GRC professionals have an AI Security background

#### Resources

- 🎮 [Gandalf — Lakera AI (Prompt Injection game)](https://gandalf.lakera.ai/)
- 📖 [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- 🌐 [NIST AI Risk Management Framework](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- 📖 [EU AI Act — Summary](https://artificialintelligenceact.eu/the-act/)

### 🏆 Phase 2 Milestone

> GitHub has **IR Playbook + AI Policy**. At least 1 attack mapped to MITRE ATT&CK.

---

## 🟢 PHASE 3: Arsenal, Portfolio & The Hunt (Day 61–90)

### Week 9 — Scanning Tools & Compliance Automation

**Day 61–67 · Lab + GRC**

#### What to Learn

- Practice Nmap (port scanning), Nikto (web scanner), Burp Suite Community (manual testing)
- Use Scout Suite or Prowler to automatically audit AWS against CIS Benchmarks
- Compare scan results with CIS Benchmarks — document findings as a compliance report
- Understand the difference: vulnerability scan vs compliance scan

#### Week 9 Deliverables

- [ ] CIS Benchmark audit report (AWS)

#### Resources

- 🛠️ [Kali Linux — Download](https://www.kali.org/get-kali/)
- 🎓 [HackTheBox Starting Point](https://app.hackthebox.com/starting-point)
- 🌐 [CIS Benchmarks (cisecurity.org)](https://www.cisecurity.org/cis-benchmarks)
- 🛠️ [Prowler — AWS Security Tool](https://github.com/prowler-cloud/prowler)

---

### Week 10 — Active Directory & Identity Risk

**Day 68–74 · Technical + GRC**

#### What to Learn

- Set up an Active Directory lab (Windows Server on VirtualBox)
- Use BloodHound to map attack paths — "Attack Paths to Domain Admin"
- Each attack path = a control gap that needs remediation
- Connect to Identity Governance concepts: PAM, JIT Access, Tiered Admin Model
- Propose technical controls to block each identified attack path

#### Week 10 Deliverables ⭐

- [ ] `📄 reports/identity-risk-assessment.md` — Identity Risk Assessment with recommended controls

#### Resources

- 🎓 [TryHackMe — Active Directory Basics](https://tryhackme.com/room/winadbasics)
- 🛠️ [BloodHound Community Edition](https://github.com/SpecterOps/BloodHound)

---

### Week 11 — CTFs & Pentest Report Writing

**Day 75–81 · Technical + Output**

#### What to Learn

- Solve 2–3 machines on TryHackMe (Easy/Medium) or HackTheBox Starting Point
- For each machine: write a full pentest report — **not just capture the flag**
- Professional pentest report structure:

```
1. Executive Summary     — non-technical summary for leadership
2. Scope & Methodology   — what was tested and how
3. Findings              — list of vulnerabilities, each including:
   - Description
   - CVSS Score
   - Evidence (screenshot/payload)
   - Remediation (how to fix)
4. Risk Rating Summary   — table of Critical/High/Medium/Low counts
5. Conclusion            — overall assessment and recommendations
```

#### Week 11 Deliverables ⭐

- [ ] `📄 reports/pentest-report-[machine-name].md` — Complete pentest report

#### Resources

- 🎓 [TryHackMe](https://tryhackme.com/)
- 🎓 [HackTheBox Starting Point](https://app.hackthebox.com/starting-point)

---

### Week 12 — Portfolio & Positioning as "Technical GRC"

**Day 82–90 · Output + Career**

#### What to Learn

- Consolidate GitHub portfolio: labs + policy templates + risk reports + pentest report + AI governance doc
- Optimize LinkedIn with the right keywords
- Write 1–2 LinkedIn posts about your learning journey (builds visibility with recruiters)
- Consider next certification
- Start applying

#### LinkedIn Keywords

```
Cloud Compliance · AI Risk Assessment · Identity Governance
Vulnerability Management · NIST CSF · ISO 27001 · PCI DSS
GRC Analyst · Security Analyst · Cloud Security · MITRE ATT&CK
SIEM · KQL · Threat Modeling · CSPM
```

#### Recommended Certifications (post 90 days)

| Certification | Fit | Notes |
|---|---|---|
| **CompTIA Security+** | ⭐⭐⭐⭐⭐ | Best entry-level cert, widely recognized |
| **ISC² CC** | ⭐⭐⭐⭐ | Free, GRC-friendly, great for beginners |
| **AWS Security Specialty** | ⭐⭐⭐ | After obtaining Security+ |

#### Week 12 Deliverables ⭐

- [ ] Polished GitHub portfolio with a clean README
- [ ] LinkedIn profile optimized with target keywords
- [ ] Applied to at least 5 roles: GRC Analyst / Compliance Analyst / Security Analyst (Junior)

### 🏆 Phase 3 Milestone

> Full portfolio on GitHub. LinkedIn optimized. Ready to apply for GRC/Security Analyst positions.

---

*This roadmap was built for personal learning. Update and adjust as needed along the way.*
