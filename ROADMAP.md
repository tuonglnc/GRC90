# 📍 ROADMAP — 90-Day Cybersecurity & GRC

> Checkboxes here are **auto-updated** by GitHub Actions when all daily tasks in the corresponding `weekly/weekXX.md` are completed.  
> You can also tick manually as a fallback.

---

## 📊 Overall Progress

<!-- ROADMAP_PROGRESS_START -->
**0 / 12 weeks completed (0%)**

```
Phase 1 [🔵] ░░░░ 0/4
Phase 2 [🟠] ░░░░ 0/4
Phase 3 [🟢] ░░░░ 0/4
```
<!-- ROADMAP_PROGRESS_END -->

---

## 🔵 Phase 1: System Foundations & Identity (Day 1–30)

| Week | Topic | Status | Daily Log |
|---|---|---|---|
| Week 1 | CIA Triad & Risk Mindset | <!-- W01_STATUS -->🔄 In progress (10/26)<!-- /W01_STATUS --> | [→ week01](./weekly/week01-cia-nist.md) |
| Week 2 | Networking & Network Segmentation | <!-- W02_STATUS -->⬜ Not started<!-- /W02_STATUS --> | [→ week02](./weekly/week02-networking.md) |
| Week 3 | Linux & Access Control | <!-- W03_STATUS -->⬜ Not started<!-- /W03_STATUS --> | [→ week03](./weekly/week03-linux-access.md) |
| Week 4 | Cloud Lab & Cloud Security Posture | <!-- W04_STATUS -->⬜ Not started<!-- /W04_STATUS --> | [→ week04](./weekly/week04-cloud-lab.md) |

**Phase 1 Deliverables:**
- [ ] `policies/user-account-policy.md`
- [ ] `checklists/cloud-hygiene-checklist.md`

> 🏆 **Milestone:** GitHub has 2 first GRC documents: User Account Policy + Cloud Hygiene Checklist

---

## 🟠 Phase 2: Offense, Defense & AI Governance (Day 31–60)

| Week | Topic | Status | Daily Log |
|---|---|---|---|
| Week 5 | OWASP Top 10 & Vulnerability Management | <!-- W05_STATUS -->⬜ Not started<!-- /W05_STATUS --> | [→ week05](./weekly/week05-owasp-vuln.md) |
| Week 6 | Kill Chain & Incident Response Plan | <!-- W06_STATUS -->⬜ Not started<!-- /W06_STATUS --> | [→ week06](./weekly/week06-killchain-ir.md) |
| Week 7 | Blue Team & Continuous Auditing | <!-- W07_STATUS -->⬜ Not started<!-- /W07_STATUS --> | [→ week07](./weekly/week07-blueteam-audit.md) |
| Week 8 | AI Security & AI Governance | <!-- W08_STATUS -->⬜ Not started<!-- /W08_STATUS --> | [→ week08](./weekly/week08-ai-security.md) |

**Phase 2 Deliverables:**
- [ ] `playbooks/incident-response-playbook.md`
- [ ] `policies/ai-governance-policy.md`

> 🏆 **Milestone:** GitHub has IR Playbook + AI Policy. At least 1 attack mapped to MITRE ATT&CK.

---

## 🟢 Phase 3: Arsenal, Portfolio & The Hunt (Day 61–90)

| Week | Topic | Status | Daily Log |
|---|---|---|---|
| Week 9 | Scanning Tools & Compliance Automation | <!-- W09_STATUS -->⬜ Not started<!-- /W09_STATUS --> | [→ week09](./weekly/week09-scanning-compliance.md) |
| Week 10 | Active Directory & Identity Risk | <!-- W10_STATUS -->⬜ Not started<!-- /W10_STATUS --> | [→ week10](./weekly/week10-ad-identity.md) |
| Week 11 | CTFs & Pentest Report Writing | <!-- W11_STATUS -->⬜ Not started<!-- /W11_STATUS --> | [→ week11](./weekly/week11-ctf-report.md) |
| Week 12 | Portfolio & Positioning as Technical GRC | <!-- W12_STATUS -->⬜ Not started<!-- /W12_STATUS --> | [→ week12](./weekly/week12-portfolio-hunt.md) |

**Phase 3 Deliverables:**
- [ ] `reports/identity-risk-assessment.md`
- [ ] `reports/pentest-report-[machine].md`
- [ ] GitHub portfolio polished
- [ ] LinkedIn optimized

> 🏆 **Milestone:** Full portfolio on GitHub. LinkedIn optimized. Ready to apply for GRC/Security Analyst roles.

---

## 📋 Week Details

### Week 1 — CIA Triad & Risk Mindset
**Day 1–7 · Technical + GRC**

**What to learn:**
- Analyze SolarWinds, Equifax breaches through CIA Triad lens
- Learn `Risk = Likelihood × Impact`, distinguish Threat / Vulnerability / Asset
- Read NIST CSF 2.0 — 6 Functions: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER
- Business Impact Analysis (BIA), RTO and RPO

**Resources:**
- 📄 [NIST CSF 2.0 PDF](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)
- 🌐 [nist.gov/cyberframework](https://www.nist.gov/cyberframework)
- 🎓 [TryHackMe Pre-Security](https://tryhackme.com/path/outline/presecurity)

**Self-check:** Can you answer these without notes?
1. What is the CIA Triad? Real-world example for each pillar.
2. Risk = ? Explain it to a CEO.
3. How many Functions in NIST CSF 2.0? Name them all.
4. Which Function is new in CSF 2.0 vs v1.1?
5. Which CIA pillar(s) did Equifax violate?

---

### Week 2 — Networking & Network Segmentation
**Day 8–14 · Technical + GRC**

**What to learn:**
- OSI 7 layers, TCP/IP, common Ports (80, 443, 22, 3389)
- Wireshark: capture and analyze basic traffic
- Network Segmentation, VLAN, DMZ — PCI DSS requirements

**Resources:**
- 🎥 [Professor Messer Network+](https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-training-course/)
- 🎓 [TryHackMe Pre-Security — Networking](https://tryhackme.com/path/outline/presecurity)

---

### Week 3 — Linux & Access Control
**Day 15–21 · Technical + GRC**

**What to learn:**
- Terminal: `chmod`, `chown`, user management
- Privilege Escalation basics
- Least Privilege principle
- Write User Account Management Policy

**Resources:**
- 🎓 [TryHackMe Linux PrivEsc](https://tryhackme.com/room/linprivesc)

**Output ⭐:** `policies/user-account-policy.md`

---

### Week 4 — Cloud Lab & Cloud Security Posture
**Day 22–30 · Lab + GRC**

**What to learn:**
- AWS Free Tier: IAM, S3, EC2
- CloudTrail + Wazuh/Security Hub
- Misconfiguration Assessment
- CIS Benchmark for AWS

**Resources:**
- 🌐 [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- 🛠️ [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat)

**Output ⭐:** `checklists/cloud-hygiene-checklist.md`

---

### Week 5 — OWASP Top 10 & Vulnerability Management
**Day 31–37 · Technical + GRC**

**What to learn:**
- SQLi, XSS, IDOR on PortSwigger
- CVSS scoring
- Vulnerability SLA: Critical=24h, High=7d, Medium=30d, Low=90d

**Resources:**
- 🎓 [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- 🌐 [NVD CVSS Calculator](https://nvd.nist.gov/vuln-metrics/cvss)

---

### Week 6 — Kill Chain & Incident Response Plan
**Day 38–44 · Technical + GRC**

**What to learn:**
- Full Kill Chain: Recon → Reverse Shell
- MITRE ATT&CK framework
- IR Playbook 6 steps + GDPR 72h notification

**Resources:**
- 🌐 [MITRE ATT&CK](https://attack.mitre.org/)
- 🎓 [TryHackMe Jr Penetration Tester](https://tryhackme.com/path/outline/jrpenetrationtester)

**Output ⭐:** `playbooks/incident-response-playbook.md`

---

### Week 7 — Blue Team & Continuous Auditing
**Day 45–51 · Technical + Lab**

**What to learn:**
- KQL (Microsoft Sentinel) + SPL (Splunk)
- Threat hunting: Lateral Movement, PrivEsc
- Continuous Auditing mindset

**Resources:**
- 🎓 [Microsoft Learn KQL](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)
- 🎓 [TryHackMe SOC Level 1](https://tryhackme.com/path/outline/soclevel1)

---

### Week 8 — AI Security & AI Governance
**Day 52–60 · Technical + GRC**

**What to learn:**
- Prompt Injection on Gandalf
- OWASP Top 10 for LLMs
- EU AI Act: 4-tier risk classification
- Build AI Usage Policy

**Resources:**
- 🎮 [Gandalf by Lakera](https://gandalf.lakera.ai/)
- 🌐 [NIST AI RMF](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- 📖 [EU AI Act](https://artificialintelligenceact.eu/the-act/)

**Output ⭐:** `policies/ai-governance-policy.md`

---

### Week 9 — Scanning Tools & Compliance Automation
**Day 61–67 · Lab + GRC**

**What to learn:**
- Nmap, Nikto, Burp Suite Community
- Prowler / Scout Suite — CIS Benchmark audit on AWS

**Resources:**
- 🛠️ [Prowler](https://github.com/prowler-cloud/prowler)
- 🌐 [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

---

### Week 10 — Active Directory & Identity Risk
**Day 68–74 · Technical + GRC**

**What to learn:**
- AD lab + BloodHound attack path mapping
- PAM, JIT Access, Tiered Admin Model
- Propose controls for each attack path

**Resources:**
- 🛠️ [BloodHound Community Edition](https://github.com/SpecterOps/BloodHound)
- 🎓 [TryHackMe Active Directory](https://tryhackme.com/room/winadbasics)

**Output ⭐:** `reports/identity-risk-assessment.md`

---

### Week 11 — CTFs & Pentest Report Writing
**Day 75–81 · Technical + Output**

**What to learn:**
- Solve 2–3 machines on TryHackMe/HTB
- Write full pentest report (not just capture flags)
- Structure: Exec Summary → Findings (CVSS) → Evidence → Remediation

**Output ⭐:** `reports/pentest-report-[machine].md`

---

### Week 12 — Portfolio & Positioning as Technical GRC
**Day 82–90 · Output + Career**

**Actions:**
- Polish GitHub portfolio
- Optimize LinkedIn keywords
- Write 1–2 LinkedIn posts
- Consider: CompTIA Security+ or ISC² CC
- Apply to 5+ junior GRC/Security Analyst roles

**LinkedIn Keywords:**
`Cloud Compliance` · `AI Risk Assessment` · `Identity Governance` · `Vulnerability Management` · `NIST CSF` · `ISO 27001` · `GRC Analyst` · `MITRE ATT&CK`
