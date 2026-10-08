---
title: "**Second Report Chapter** (Team 9)"

geometry: "margin=1in"
author: |
  \begin{tabular}{ll}
  Tadouanla Guetchuin Billy   & 28177 \\
  Taosif Wasi Eshan           & 38607 \\
  Tifang Ngan Tata            & 38181  \\
  Muhammad Abubakar           & \\
  \end{tabular}
date: "July 17 , 2026"
header-includes: |
  \usepackage{amsfonts}
  \usepackage{circuitikz}
  \usepackage{amsmath}
  \usepackage{mathtools}
  \usepackage{xcolor}
  \newcommand{\blue}[1]{\textcolor{blue}{#1}}
  \newcommand{\red}[1]{\textcolor{red}{#1}}
  \makeatletter
  \renewcommand{\maketitle}{
    {\Large \@title \par}
    \vskip 0.5em
    {\normalsize \@author \par}
    \vskip 0.25em
    {\small \@date \par}
    \vskip 1em
  }
  \makeatother
format: pdf
documentclass: article
classoption: 10pt
---
## 1. Functional Design

### Core Principles
Functional Design defines **what** a system must do before establishing physical solutions or technical mechanisms.

* **Solution Neutrality:** Functions are defined without committing prematurely to specific technologies or physical components.
* **System Boundaries & Flows:** The overall function maps system inputs into outputs across three primary categories:
  * **Energy ($E$):** Electrical, mechanical, or thermal energy transfers.
  * **Signal ($S$):** Control inputs, sensor data, or status feedback.
  * **Mass / Matter ($M$):** Materials, fluids, or workpieces passing through the system.
* **Function Categories:** Core operational actions used to structure sub-functions:
  * *Conversion* (changing input form to output form)
  * *Varying* (amplifying, stepping down, or modulating)
  * *Connecting/Disconnecting* (switching, coupling, or mixing)
  * *Channeling* (directing or transferring power, signals, or mass)
  * *Storing* (holding energy, signals, or mass)

  ## 2. Utility Value Analysis (*Nutzwertanalyse*)

### Methodology
Utility Value Analysis is a quantitative multi-criteria decision-making framework used to evaluate, rank, and select competing design variants.

### The 5-Step Evaluation Process

1. **Define Alternatives:** Identify concept variants generated during conceptual design.
2. **Select Evaluation Criteria:** Derive criteria directly from the system requirements list (e.g., performance, safety, manufacturability).
3. **Weight Criteria:** Assign relative weight factors ($w_i$) to criteria such that $\sum w_i = 1.0$ (or $100\%$).
4. **Score Alternatives:** Rate performance ($v_i$) of each concept against each criterion using a standardized rating scale.
5. **Calculate Overall Utility Value:** Compute total weighted utility:
   $$\text{Utility Score} = \sum_{i=1}^{n} (v_i \cdot w_i)$$

### Evaluation Scale Systems

* **Standard Use-Value Analysis (0 to 10 Scale):** Evaluates performance on an 11-point continuum where 0 represents *Useless*, 5 represents *Satisfactory*, and 10 represents *Ideal*.
* **VDI 2225 Guideline (0 to 4 Scale):** Standardizes rating across 5 discrete levels: 0 (*Unsatisfactory*), 1 (*Just tolerable*), 2 (*Adequate*), 3 (*Good*), and 4 (*Ideal* / *Very good*).

### Methodological Limitations
* **Subjectivity:** Rating scores can be influenced by team bias or subjective interpretations.
* **False Precision:** Mathematical scoring creates an illusion of objective accuracy.
* **Sensitivity:** Final rankings can shift significantly with minor changes to weighting distributions.

---

## 3. Key Takeaways

* **Solution-neutral modeling** prevents premature design bias and clarifies fundamental system transformations.
* **Multi-criteria evaluation** transforms qualitative, multi-variable design trade-offs into structured, documentable decisions.

