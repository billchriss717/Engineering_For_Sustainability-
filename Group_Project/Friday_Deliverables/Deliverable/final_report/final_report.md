---
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
documentclass: article
classoption: 10pt

toc: true
toc-depth: 3
number-sections: true

format:
  pdf:
    include-before-body: titlepage.tex
---

\pagebreak  
# Introduction
## Background & Statement of Problem

## Background 
Water is the most valuable natural resource and plays a vital role in mainly maintaining a healthy
ecosystem,  supporting biodiversity. Freshwater bodies such as **rivers**, **lakes**, and 
**canals** are home to numerous aquatic organisms. However, these water bodies are increasingly 
threathened by pollution, climate change, and excessive nutrient inputs, which can lead to 
environmental problems such as harmful algal growth.

Algae are naturally occuring photosynthetic organisms found in freshwater and marine ecosystems.
Under normal conditions, they are an essential part of aquatic ecosystems because they produce 
oxygen through photosynthesis and form the base of many aquatic food chains. However, when 
Nutirents such as **Nitrogen** and **Phosphorus** become excessively avalable due to agricultural 
**runoff**, **wastewater discharge**, **urban stormwater**  or other human activities, algae can 
multiply rapidly. Combined with warm temperatures, suffcient sunlight, and slow-moving water, 
these conditions often result in excessive algal growth, commonly known as **algal blooms**.

Excessive algae growth has many negative **environmental**, **social** and **economic 
consequences**. Thick ayers of algae reduce the penetration of sunlight into the water, preventing
submerged aquatic plants from carrying out photosynthesis. As algae die and decompose, 
microorganisms consume large amounts of dissolved oxygen, leading to oxygen with depletion that 
can stress or kill fish and other aquatic organisms. In severe cases, algal blooms may produce 
**unpleasant odours**, **reduce water clarity**, **clog waterways**, **interfere with recreational
activities**, and significantly decrease the aesthetic value of natural environments.

The **Spoy Canal in Kleve, Germany**, Germany, experiences recurring algae growth, making it an 
important environmental challenge for the city. Besides being part of hte local drainage and water
management system, the canal is an attractive feature of residents and visitors and contributes to
the city's landscape. Because the canal passes through public areas, maintaining its **ecological 
health and visual appearance is essential**

As part of this initiative, **Hochschule Rhein-Waal (HSRW)** collaborates with the city of kleve 
by  involving engineering students in solving real-world sustainability challenges. Instead of 
simply  proposing theoritical ideas, students apply the **VDI2221 Engineering design methodology**
as well as the **VDI2220 Engineering design methodology**, which emphasizes systematic product 
developement. The design process begins by understanding the ***problem***, ***analysing*** 
***stakeholders***, ***identifying customer needs***, and translating these needs into measurable
engineering requirements before generateing design concepts.

In this project, students are expected to develop a **sustainable  engineering solution**  capable
of reducing algae accumulation  in the **Spoy Canal** while balancing technical ***performance, 
environmental protection, economic feasibility, safety, maintainability, and sustainability.***

## Statement of Problem
The Spoy Canal currently experiences recurring algae accumulation, which negatively affects the 
ecological conditions and visual quality  of the waterway. Excessive algae reduce water quality, 
decrease dissolved oxygen concentrations, interfere with aquatic ecosystems, and create an 
unpleaseant environment for both residents and visitors. The Problem also increases maintenance 
efforts and cost of the local authorities responsible for managing the canal.

As Kleve prepares for **LaGa 2029**, the existing algae problem presents additional challenges.
A canal covered with algae is inconsistent with the objectives of **LaGa**, which seeks to promote
**environmental sustainability, biodiversity and attractive urban landscape.** Therefore, an 
effective and sustainable solution is required to improve the condition of the canal before and 
during the event. 

Traditional algae removeal methods often require consdierable **manual labour, repeated 
maintenance, and operational costs.** Some methods may also disturb aquatic habitats or consume
significant amounts of energy. Consequently, there is a need for an innovative engineering 
solution that removes algae efficiently while minimizing environmental impacts.

The proposed solution should not only reomve algae effectively but also operate safely in public 
areas. Consume little energy, protect aquativ organims, resist corrosion in freshwater 
environments, require minimal maintenance, and comply with environmental and safety regulations.
Since the machine will potentially operate in areas visited by the pubilc during **LaGa 2029**, it
should also have an **aesthetically acceptable appearance and produce minimal noise.**

Following the engineering design methodology, the first stage of the project is not to select a 
specific but to define what the product must achieve. This involves identifying stakeholder needs 
and translating them into measurable engineering requirements that will guide concept generation 
and evaluation in the following stages of the project.

## Requirements and Stakeholders

The overall engineering challange is therefore to design a sustainable, reliable, safe, and 
efficient algae-removal machine capcable of improving the ecological condition of visual quality 
of the **Spoy Canal** while satisfying technical, environmental, economic, and stakeholder 
requirements. Such a solution would contribute to the long-term management of the canal and 
support the environmental objectives of **LaGa 2029**.

Identifying the different stakeholders, their interests, their relationship to the project, and 
their respective priorities and categories is essential for effective project planning and 
management.

[\blue{Figure 1} ](#stakeholder-list) presents the stakeholders considered in the project and 
provides an overview of their respective interests, estimated project impact, and priority.

Based on the identified stakeholders, a set of project requirements is established. These 
requirements relate to both the characteristics of the final product and the project development
process. A weight is assigned to each requirements based on the degree of importance it is for 
the  project and the total sum of all weights must equal  **100%**. 2 revisions of this table 
exist. The final revision identifies the requirements seen on [\blue{Figure 2}](#req-list).

The differences between these revisions are pointed out below:

### 1. Additions (Revision 2)
-  **Itemized Legal Framework (ID 17-19)** Replaced the generic local compliance entry with three 
distinct legal permits: Federal Waterway Permit (Strom- und Schifffahrtpolizeiliche Genehmigung,
4% weight), Water Use Permit (Wasserrechtliche Erlaubnis, 4% weight), and Biodiversity & Habitat 
Protection (Naturschutzrecht, 3% weight).

-  **Canal Navigation Preservation (ID 22):** Added a safety requirement mandating that operation 
must not disrupt waterway navigation, evaluated via allowable traffic stoppage time (Demand, 3% 
weight).

- **Infrastructure Protection (ID 23)** Introduced an ergonomics requirement barring any physical
alteration, reconstruction, or destruction of existing canal walls or bank infrastructure 
(Demand, 5% weight).

-  **Weather Resistance (ID 24)** Added a performance requirement demanding continuous system 
operability under hot, sunny, moist, and rainy conditions during peak algal bloom periods 
(Demand, 2% weight).

### 2. Changes & Modifications (Revision 1 $\rightarrow$ Revision 2)
**Technical & Operational Scale-up**
-  **algae Removal Rate (ID 1):** Target extraction rate increased from 20–30 kg/h to 120–200 
kg/h.  
- **Storage Capacity (ID 7):** Onboard holding capacity expanded from 40 kg to 200–250 kg.  
- **Machine Mass (ID 8):** Maximum mass threshold increased from < 80 kg to < 500 kg.  
- **Surface Footprint (ID 12):** Maximum envelope area expanded from 1 m² to < 5 m².  
- **Operating Speed (ID 3):** Reduced from ~5 km/h to ~1 km/h to optimize harvesting efficiency.  
- **Energy Limit (ID 5):** Refined from nominal 500 W to an explicit ceiling of < 500 W.  

![Stakeholder List](/home/chriss/Desktop/Engineering_For_Sustainability/Group_Project/Pictures/stakeholder-list.png){#stakeholder-list}

![Requirements List](/home/chriss/Desktop/Engineering_For_Sustainability/Group_Project/Pictures/requirements_list.png){#req-list}


# 1. Design
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
  
Below is the Functional design  diagram showcasing the different functions, sub-functions, 
signals, Matter(mass), and Energy flowing into the system.

![Functional Design Revision 1](/home/chriss/Desktop/Engineering_For_Sustainability/Group_Project/Pictures/Functional-diagram-1.jpeg)

The diagram above shows the initial design of system itself. After some more analysis, we came up
with a better design which ended up being our final design of the system shown seen on the figure
below.

![Functional Design Revision 2](/home/chriss/Desktop/Engineering_For_Sustainability/Group_Project/Pictures/Function-diagram.png)

Below the functional design diagram is a table explaining the various changes and modifications done to generate the final functional diagram.

| Feature | Initial Diagram | Current Diagram | Reason for Change |
|---------|-----------------|-----------------|-------------------|
| Navigation | Not clearly defined | **Navigate to Algae Area** | Ensures the machine reaches the correct cleaning location before starting the cleaning process. |
| System Positioning | Not included | **System Positioned** | Confirms that the machine is correctly positioned before algae collection begins. |
| Collection Process | General algae collection | **Collect Algae–Water–Debris Mixture** | Represents the actual operating condition where algae, water, and floating debris are collected together. |
| Separation Process | General separation process | **Separate Algae–Debris from Water** | Makes the separation process more specific and realistic by distinguishing water from solid materials. |
| Water Output | Not clearly represented | **Water Returned to Canal** | Indicates that filtered water is discharged back into the canal after separation. |
| Thermal Loss | Not shown | **Heat (Thermal Loss)** | Represents energy losses generated during the separation process. |
| Storage Function | Simple storage block | **Store Collected Algae–Debris** | Clarifies that both algae and debris are temporarily stored before further processing. |
| Storage Monitoring | Not available | **Monitor Storage Level** | Allows continuous monitoring of the storage tank to prevent overflow. |
| Tank Full Signal | Not included | **Alarm / Stop Collection** and **Signal: Tank Full** | Automatically stops the collection process when the storage tank reaches its maximum capacity. |
| Debris Separation | Not included | **Separation of Algae from Debris** | Separates useful algae from unwanted waste materials before finBecause this functional sketch is AI-generated, it serves as an illustrative abstraction and does not fully represent the finalized mechanical architecture or intended technical details of the concept.al storage or disposal. |
| Waste Handling | Not included | **Remove Waste & Debris** | Introduces a dedicated process for removing non-organic waste such as plastics and stones. |
| Waste Output | Not specified | **Waste/Debris** | Clearly defines the waste stream leaving the system after separation. |
| Energy Output | Not represented | **Energy Loss (Heat)** | Completes the system's energy flow by identifying energy losses. |
| Signal Flow | Limited control signals | **Start Signal**, **System Positioned Signal**, and **Tank Full Signal** | Improves system automation and provides better operational control. |
| Material Flow | Simple material flow | Separate **Algae**, **Water**, and **Debris** flows | Makes the functional model easier to understand by distinguishing the different material streams. |


## 2. Morphological Box Synthesis
The Morphological Box decomposes the AlgaNova system into nine technical sub-functions to 
synthesize three distinct concept variants across a spectrum of automation:

- **Concept 1(Manual Base):** Relies on manual paddling, visual navigation, a harvest trident, 
perforated basket separation, and manual dumping.

-  **Concept 2 (Hybrid Power):** Combines pedal/battery propulsion with an electrically assisted 
conveyor, perforated belt filtration, and strain-gauge load monitoring.

-  **Concept 3(Conveyor System):** Features submerged electric propellers, sensor/camera 
navigation, a powered conveyor, IP67 ultrasonic volume monitoring, and an articulated rear-tipping hopper.

*NOTE: All three variants converge on coarse screening/sedimentation for secondary algae debris 
separation.*

[\blue{Figure 5}](#Morph) is the developed morphological box:

![Morphological Box:](/home/chriss/Desktop/Engineering_For_Sustainability/Group_Project/Pictures/Morphological_Box.png){#Morph}


## 3. Utility Value Analysis (*Nutzwertanalyse*)

![Value analysis](/home/chriss/Desktop/Engineering_For_Sustainability/Group_Project/Pictures/value_analysis-1.png)
![Value analysis](/home/chriss/Desktop/Engineering_For_Sustainability/Group_Project/Pictures/value_analysis-2.png)

### Methodology
To determine the optimal system architecture, a weighted value analysis (utility analysis) evaluates the three synthesized concept variants against the 23 functional, physical, and regulatory requirements. Each requirement is assigned a weighting factor ($t_i$) totaling 1.00 ($100\%$). Individual concepts are rated on a degree of fulfillment scale ($v_i \in [0, 10]$), yielding a weighted utility score ($w_i = t_i \cdot v_i$) per parameter.

$$
\sum W_{concept 1} = \mathbf{7.81}\quad | \sum W_{concept 2} = \mathbf{7.89}\quad |
\sum W_{concept 3} = \mathbf{7.53}\quad
$$

### Analytical Comparison

- **Concept 2(Hybrid power collection)** Achieves the highest utility score by establishing an optimal balance between operational performance and system efficiency. It yields superior ratings in operating depth coverage ($0\text{--}0.5\text{ m}$, rating 5), storage capacity ($100\text{ kg}$, rating 7), and low maintenance costs ($100\text{ Euros}$, rating 10), while maintaining full compliance across all legal and safety indicators.

- **Concept 1(Human Base Collection)** Performs strongly in energy independence ($0\text{ W}$, rating 9), weight ($210\text{ kg}$, rating 10), and low maintenance costs ($10\text{ Euros}$, rating 10). However, its utility is constrained by limited operational depth ($0\text{--}0.2\text{ m}$, rating 2) and reduced storage capacity ($80\text{ kg}$, rating 2).

- **Concept 3(Conveyor System)**: Delivers robust functional performance but receives penalties due to elevated power consumption ($450\text{ W}$, rating 6), higher noise emissions ($60\text{--}80\text{ dB}$, rating 4), and increased maintenance expenditure ($150\text{ Euros}$, rating 8).

### Conclusion
**Concept 2** is selected as the primary design baseline for detailed technical development based
on its maximum overall utility score.

# Functional Sketch Analysis: Concept 2 (Dual-Paddle Algae Collection Machine)
[\blue{Figure 6}](sketch) shows the functional sketch 

![Functional Sketch](/home/chriss/Desktop/Engineering_For_Sustainability/Group_Project/Pictures/sketch.jpeg){#sketch}

## System Architecture & Structural Layout
The design features a floating catamaran hull equipped with dual lateral paddle wheels for propulsion and fluid guidance, a central inclined perforated conveyor, an elevated twin-seat control cabin with a signaling beacon, and a high-capacity rear storage hopper.

## Operational Workflow:
1. Collect: Dual paddle wheels direct surface algae and debris into the central intake.

2. Separate: The perforated conveyor lifts solid biomass while gravity-draining clean water back into the canal.

3. Store: Screened algae-debris deposits into the rear storage hopper.

4. Monitor & Alarm: Level sensors monitor fill status, triggering an audio-visual alarm and system stop upon reaching full capacity.

5. Separate & Remove: Secondary screening isolates excess moisture before the waste is offloaded onshore.

**Design Notes:** Because this functional sketch is AI-generated, it serves as an illustrative abstraction and does not fully represent the finalized mechanical architecture or intended technical details of the concept.

# Conclusion & Future Outlook
The conceptual design and value analysis successfully established Concept 2 as the optimal baseline for the AlgaNova system, striking the best balance between performance, operational feasibility, and regulatory compliance.

Moving forward, several overarching challenges must be addressed during detailed development:

- **Operational & Environmental Variability:** Managing unpredictable canal conditions, such as varying water currents, floating debris types, and fluctuating algal density.

- **System Integration & Efficiency:** Optimizing the trade-offs between battery weight, drive-system power consumption, and total structural payload.

- **Durability & Regulatory Adherence:** Maintaining long-term material resilience against corrosion while meeting all local environmental and waterway navigation standards.

Future work will transition the project from conceptual evaluation to detailed mechanical engineering, component sizing, and physical prototype testing.


# REFERENCES
### Berndsen, D. (2026). *Engineering for Sustainability: Impulse Funding and Business Model*. Hochschule Rhein-Waal.
Source of information:
- Business model and financial planning.
- Funding opportunities and stakeholder value.

### Berndsen, D. (2026). *Engineering for Sustainability: Sustainability Analysis for Concept Refinement*. Hochschule Rhein-Waal.
Source of information:
- Sustainability framework.
- Environmental and social evaluation.

### Gebauer, J. (2026). *Planting Diversity: HSRW goes LaGa*. Hochschule Rhein-Waal.
Source of information:
- LaGa 2029 project context.
- Biodiversity and sustainability goals.

### Hochschule Rhein-Waal. (2026). *Potential and Opportunities for our Region*.
Source of information:
- Regional development.
- Project motivation.

### Megill, W. M. (2023). *The Problem of Algae in the Spoy Canal*. Hochschule Rhein-Waal.
Source of information:
- Algae problem overview.
- Canal characteristics.

### Megill, W. M. (2026). *Introduction to Limnology*. Hochschule Rhein-Waal.
Source of information:
- Freshwater ecosystems.
- Algae growth processes.

### Umweltbüro Essen. (2021). *Konzept zur Lösung der Algenproblematik im Spoykanal Kleve*. Stadt Kleve.
Source of information:
- Scientific background.
- Existing algae management methods.

### Hochschule Rhein-Waal. (2026). *VDI2220 Engineering Design Course Materials.*
Source of information:
- Engineering design methodology.
- Project workflow.

### Hochschule Rhein-Waal. (2026). *Week 1 Deliverable – Background and Statement of Problem.*
Source of information:
- Project definition.
- Problem formulation.

### Hochschule Rhein-Waal. (2026). *Week 1 Deliverable – Stakeholder Analysis.*
Source of information:
- Stakeholder identification.
- Project requirements.

### Hochschule Rhein-Waal. (2026). *VDI2220 Requirements List Template.*
Source of information:
- Requirements engineering.
- Design specifications.

### Hochschule Rhein-Waal. (2026). *Functional Design and Morphological Analysis.*
Source of information:
- Functional decomposition.
- Concept development.

### International Electrotechnical Commission. (2013). *IEC 60529: Degrees of Protection Provided by Enclosures (IP Code).*
Source of information:
- IPX6 waterproof requirement.
- Equipment protection standards.

### United Nations. (2023). *Recommendations on the Transport of Dangerous Goods: Manual of Tests and Criteria (UN 38.3).*
Source of information:
- Battery safety requirements.
- Lithium battery certification.

### United Nations. (2015). *Transforming Our World: The 2030 Agenda for Sustainable Development.*
Source of information:
- Sustainable Development Goals.
- Sustainability principles.

### Bundesministerium der Justiz. *Bundesnaturschutzgesetz (Federal Nature Conservation Act).*
Source of information:
- Biodiversity protection.
- Environmental regulations.

### Bundesministerium der Justiz. *Wasserhaushaltsgesetz (German Water Resources Act).*
Source of information:
- Water management regulations.
- Environmental compliance.

### Authors (Team 9). (2026). *Photographs of the Spoy Canal and Prototype Development.*
Source of information:
- Site observations.
- Original project photographs.

### Authors (Team 9). (2026). *Original Project Work.*
Source of information:
- Engineering analyses.
- Team-generated diagrams and models.

### OpenAI. (2026). *ChatGPT (GPT-5.5).* https://chatgpt.com
Source of information:
- Prototype development and refinement.
- Technical writing and engineering support.

