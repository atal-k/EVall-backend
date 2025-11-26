import os
import django
import json
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from blogs.models import BlogPost

# Your JS data here (paste all 6 entries)
blogs_data = [
    { 
       "id": 5,
       "title": "EV Charging Summit 2025 — Key Takeaways for City Planners",
       "slug": "ev-charging-summit-2025-city-planners-takeaways",
       "meta_description": "Top takeaways from EV Charging Summit 2025: zoning for chargers, financing micro-hubs, and public-private partnerships for equitable access.",
       "excerpt": "Top takeaways from EV Charging Summit 2025: zoning for chargers, financing micro-hubs, and public-private partnerships for equitable access.",
       "author": "ChargeGrid Team",
       "category": "events",
       "category_name": "Events",
       "tag_list": [
           "events",
           "EV charging summit",
           "city planning",
           "public policy",
           "micro-hubs"
       ],
       "content": {
        "time": 1763189400000,
        "version": "2.25.0",
        "blocks": [
            {
                "type": "Header",
                "id": "h1",
                "data": {
                    "text": "EV Charging Summit 2025: Practical Takeaways for Cities",
                    "level": 2
                }
            },
            {
                "type": "paragraph",
                "id": "p1",
                "data": {
                    "text": "The EV Charging Summit 2025 focused on scalable policy and deployment patterns. City planners, utilities and operators left with specific steps to reduce friction for charging rollouts — here are the ones you can implement quickly."
                }
            },
            {
                "type": "Header",
                "id": "h2",
                "data": {
                    "text": "Six action items that move the needle",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l1",
                "data": {
                    "style": "ordered",
                    "items": [
                        "Embed charger-ready electrical capacity in new building codes",
                        "Create fast-track permitting for public chargers",
                        "Use blended finance (grants + private capital) for micro-hubs",
                        "Mandate open roaming and payment interoperability",
                        "Coordinate grid capacity planning with utilities",
                        "Target underserved neighborhoods for public chargers"
                    ]
                }
            },
            {
                "type": "Quote",
                "id": "q1",
                "data": {
                    "text": "“Policy clarity reduces investment risk — that is what we heard most from private deployers.”",
                    "caption": "— Priya Nair, Municipal Infrastructure Director"
                }
            },
            {
                "type": "Header",
                "id": "h3",
                "data": {
                    "text": "Financing models discussed",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l2",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Concession models with minimum guaranteed revenue",
                        "Green municipal bonds for public charger pools",
                        "Usage-based subsidies for fleet customers in early years"
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h4",
                "data": {
                    "text": "Measuring success",
                    "level": 3
                }
            },
            {
                "type": "Table",
                "id": "t1",
                "data": {
                    "withHeadings": True,
                    "content": [
                        [
                            "Metric",
                            "Why it matters",
                            "Target"
                        ],
                        [
                            "Charger Utilization",
                            "Reflects demand and site selection",
                            "30–60% in early years"
                        ],
                        [
                            "Average Session Time",
                            "Indicates throughput",
                            "15–40 minutes depending on charger type"
                        ],
                        [
                            "Equitable Coverage",
                            "Ensures access across neighborhoods",
                            "Proportionate to population density"
                        ]
                    ]
                }
            },
            {
                "type": "paragraph",
                "id": "p2",
                "data": {
                    "text": "The Summit was pragmatic: align incentives, simplify rules, and measure results. Where cities move fastest is where local governments made a single office responsible for coordinating permits, utility requests and funding."
                }
            }
        ]
    },
       "featured_image_url": "/images/blog_featured/2025/11/ev-charging-summit.webp",
       "featured_image_alt": "Panel discussion at an EV infrastructure conference",
       "is_featured": False,
       "reading_time": 1,
       "views_count": 37,
       "status": "published",
       "published_at": "2025-11-24T05:46:51Z",
       "created_at": "2025-11-24T05:46:51.858991Z"
   },
   {
       "id": 4,
       "title": "Solid-State Batteries: A Practical Guide for Urban Fleets and Policymakers",
       "slug": "solid-state-batteries-urban-evs-next-leap",
       "meta_description": "Solid-state batteries promise higher energy density, faster charging and improved safety — what fleets and cities must plan for today.",
       "excerpt": "Solid-state batteries promise higher energy density, faster charging and improved safety — what fleets and cities must plan for today.",
       "author": "ChargeGrid Tech",
       "category": "technological-advancements",
       "category_name": "Technological Advancements",
       "tag_list": [
           "solid-state",
           "battery tech",
           "fast charging",
           "EV innovation",
           "energy density"
       ],
       "content": {
        "time": 1763016600000,
        "version": "2.25.0",
        "blocks": [
            {
                "type": "Header",
                "id": "h1",
                "data": {
                    "text": "Solid-State Batteries: A Practical Guide for Urban Fleets and Policymakers",
                    "level": 2
                }
            },
            {
                "type": "paragraph",
                "id": "p1",
                "data": {
                    "text": "Solid-state batteries (SSBs) are framed as a transformative leap for electric vehicles. For cities and fleet operators the promise is attractive: smaller packs for the same range, quicker opportunity charging, simpler depot safety requirements and a step change in vehicle packaging. But between lab promise and street-scale benefits sits a complex mix of materials science, manufacturing scale, standards and policy. This guide breaks the noise into practical signals: what to expect, how to pilot, and the strategic choices that matter."
                }
            },
            {
                "type": "Header",
                "id": "h2",
                "data": {
                    "text": "Why SSBs are different (short primer)",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l1",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Solid electrolyte replaces liquid — reducing risk of leakage and thermal runaway.",
                        "Higher theoretical energy density — enabling smaller or lighter battery packs.",
                        "Potentially faster charge acceptance — making short, high-power top-ups more useful.",
                        "New manufacturing flows — which require different supply chains and capital investments."
                    ]
                }
            },
            {
                "type": "Quote",
                "id": "q1",
                "data": {
                    "text": "“Solid-state is less a single product and more a family of chemistries — each with different tradeoffs for fleets.”",
                    "caption": "— Dr. Elena Rossi, Materials Scientist"
                }
            },
            {
                "type": "Header",
                "id": "h3",
                "data": {
                    "text": "What fleets and cities actually gain",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l2",
                "data": {
                    "style": "ordered",
                    "items": [
                        "Smaller pack volume or higher range for the same footprint — useful for compact urban vehicles and cargo vans.",
                        "Improved depot safety profile — fewer thermal incidents reduces insurance and regulatory friction for multi-tenant garages.",
                        "Higher charge-acceptance windows — opportunity charging at micro-hubs becomes more viable.",
                        "Potential lifecycle benefits — if cycle life and calendar degradation meet expectations, replacement costs fall."
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h4",
                "data": {
                    "text": "Where SSBs may matter most first",
                    "level": 3
                }
            },
            {
                "type": "Table",
                "id": "t1",
                "data": {
                    "withHeadings": True,
                    "content": [
                        [
                            "Use case",
                            "Why SSB helps",
                            "Early feasibility"
                        ],
                        [
                            "Compact urban delivery vans",
                            "Higher energy density without heavier packs",
                            "High"
                        ],
                        [
                            "Shared mobility / e-taxis",
                            "Fast top-ups and safer depot parking",
                            "Medium"
                        ],
                        [
                            "Heavy-duty buses and trucks",
                            "Requires very large cell formats and proven cycle life",
                            "Low–Medium"
                        ],
                        [
                            "Multi-tenant parking & residential garages",
                            "Improved thermal safety lowers regulatory barriers",
                            "High"
                        ]
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h5",
                "data": {
                    "text": "Technical risks and the questions to ask",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l3",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Manufacturing scale: Can the supplier commit to steady volume and quality control?",
                        "Interface degradation: How does the solid electrolyte behave after thousands of real drive cycles?",
                        "Temperature sensitivity: What are performance limits across your local climate range?",
                        "Repairability and recycling: Are there established pathways for end-of-life reuse and separation?"
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h6",
                "data": {
                    "text": "A practical fleet pilot — step by step",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l4",
                "data": {
                    "style": "ordered",
                    "items": [
                        "Select a duty-cycle match: choose routes with predictable range needs (e.g., urban delivery loops).",
                        "Choose a small, controlled vehicle cohort (5–20 units) with compatible chargers.",
                        "Instrument heavily: record temperature, charge acceptance, cycle depth and degradation monthly.",
                        "Run a parallel control group on Li-ion for direct comparative metrics.",
                        "Agree success criteria up front: TCO horizon, cycle retention %, and safety incidents."
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h7",
                "data": {
                    "text": "Policy levers cities should adopt now",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l5",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Fund pilot de-risking: grants that cover part of pilot costs accelerate validation.",
                        "Update codes for depot safety: recognize SSBs’ different failure modes and adjust inspection frameworks.",
                        "Support local manufacturing: incentives for pilot production plants reduce supply chain risk.",
                        "Mandate recycling plans: require early evidence of end-of-life management from suppliers."
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h8",
                "data": {
                    "text": "Simple decision framework for procurement teams",
                    "level": 3
                }
            },
            {
                "type": "Table",
                "id": "t2",
                "data": {
                    "withHeadings": True,
                    "content": [
                        [
                            "Question",
                            "If yes →",
                            "If no →"
                        ],
                        [
                            "Is the route duty cycle predictable and within single-shift range?",
                            "Proceed to pilot cohorts",
                            "Defer until variability reduces"
                        ],
                        [
                            "Can the supplier provide a multi-year warranty with degradation guarantees?",
                            "Negotiate pricing with warranty milestones",
                            "Require stronger test data or prefer Li-ion"
                        ],
                        [
                            "Is local service and spare-parts support available?",
                            "Pilot with local service SLA",
                            "Add service readiness as a contract condition"
                        ]
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h9",
                "data": {
                    "text": "Cost and TCO considerations (what changes and what doesn’t)",
                    "level": 3
                }
            },
            {
                "type": "paragraph",
                "id": "p2",
                "data": {
                    "text": "SSBs may reduce per-vehicle battery weight and space requirements, but initial cell costs are likely higher. Early adopters should model both battery capex and operational savings from reduced charging time, lower insurance and deferred depot upgrades. Use sensitivity analysis: vary cycle life, energy price and warranty buy-back to understand break-even timelines."
                }
            },
            {
                "type": "Header",
                "id": "h10",
                "data": {
                    "text": "Realistic roadmap (what to expect by phase)",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l6",
                "data": {
                    "style": "ordered",
                    "items": [
                        "2025–2026: Pilots in controlled urban fleets and premium models — learning and materials validation.",
                        "2027–2028: Scaling production lines, early commercial models; costs begin to fall with volume.",
                        "Post-2028: Wider adoption where lifecycle economics are proven and recycling infrastructure exists."
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h11",
                "data": {
                    "text": "Case study (illustrative): City courier pilot",
                    "level": 3
                }
            },
            {
                "type": "paragraph",
                "id": "p3",
                "data": {
                    "text": "A hypothetical 20-vehicle pilot fitted with SSB packs ran on short urban loops (avg 80 km/day). After 12 months the pilot reported: 8% energy savings from smaller ancillary weight, average opportunity charge windows cut by 25% (reducing route downtime), and no thermal incidents in depot operations. The supplier provided a 5-year degradation warranty with staged buy-back terms — a key factor that made the economics acceptable."
                }
            },
            {
                "type": "Header",
                "id": "h12",
                "data": {
                    "text": "Common pitfalls and how to avoid them",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l7",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Relying on vendor hype: demand independent test data and third-party validation.",
                        "Skipping service readiness: require local spares and certified technicians.",
                        "Assuming instant cost parity: build TCO models with conservative cycle life assumptions.",
                        "Neglecting recycling: require suppliers to commit to EOL management."
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h13",
                "data": {
                    "text": "Checklist for procurement teams (ready to pilot?)",
                    "level": 3
                }
            },
            {
                "type": "Checklist",
                "id": "chk1",
                "data": {
                    "items": [
                        {
                            "text": "Defined duty cycles and baseline Li-ion comparator data",
                            "checked": True
                        },
                        {
                            "text": "Supplier provides multi-year degradation and safety data",
                            "checked": False
                        },
                        {
                            "text": "Local maintenance and spares plan in place",
                            "checked": False
                        },
                        {
                            "text": "Clear metrics for pilot success (TCO, downtime, incidents)",
                            "checked": True
                        }
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h14",
                "data": {
                    "text": "Conclusion — how to think about SSBs strategically",
                    "level": 3
                }
            },
            {
                "type": "paragraph",
                "id": "p4",
                "data": {
                    "text": "Solid-state batteries are not an immediate universal replacement for lithium-ion — they are a strategic opportunity. For cities and fleets, the sensible path is targeted pilots, firm procurement conditions (warranty, service, recycling) and close coordination with local policy to de-risk deployment. When SSBs deliver on cycle life and manufacturability, they will reshape vehicle packaging, depot design and charging strategies — but that future is built on careful, data-driven work today."
                }
            },
            {
                "type": "paragraph",
                "id": "cta",
                "data": {
                    "text": "Want a pilot checklist or TCO template tailored to your fleet? Ask for a sample pilot deck and a spreadsheet model to evaluate SSBs vs Li-ion in your routes."
                }
            }
        ]
    },
       "featured_image_url": "/images/blog_featured/2025/11/solid-state-batteries.webp",
       "featured_image_alt": "Concept render of a solid-state battery cell and urban delivery van silhouette",
       "is_featured": False,
       "reading_time": 1,
       "views_count": 37,
       "status": "published",
       "published_at": "2025-11-24T05:46:05Z",
       "created_at": "2025-11-24T05:46:05.760358Z"
   },
   {
       "id": 2,
       "title": "Why Compact Electric Cargo Trucks Will Dominate Urban Deliveries",
       "slug": "compact-electric-cargo-trucks-urban-delivery-future",
       "meta_description": "Compact electric cargo trucks reduce operating costs, improve curb access, and simplify charging for last-mile delivery in dense cities.",
       "excerpt": "Compact electric cargo trucks reduce operating costs, improve curb access, and simplify charging for last-mile delivery in dense cities.",
       "author": "Urban EV Insights",
       "category": "electronic-vehicles",
       "category_name": "Electronic Vehicles",
       "tag_list": [
           "EV",
           "compact trucks",
           "last-mile",
           "fleet electrification",
           "urban logistics"
       ],
       "content": {
        "time": 1762843800000,
        "version": "2.25.0",
        "blocks": [
            {
                "type": "Header",
                "id": "h1",
                "data": {
                    "text": "Small Trucks, Big Impact: The Case for Compact Electric Cargo Vehicles",
                    "level": 2
                }
            },
            {
                "type": "paragraph",
                "id": "p1",
                "data": {
                    "text": "Last-mile delivery in dense urban cores has a new best fit: compact electric cargo trucks. Their smaller footprint, lower operational cost and ease of access to restricted streets make them an attractive option for operators, regulators and citizens alike."
                }
            },
            {
                "type": "Header",
                "id": "h2",
                "data": {
                    "text": "Top operational advantages",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l1",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Easier curb access and faster deliveries in narrow streets",
                        "Lower energy and maintenance costs compared to larger EV trucks",
                        "Simplified depot charging and opportunity charging workflows"
                    ]
                }
            },
            {
                "type": "Quote",
                "id": "q1",
                "data": {
                    "text": "“Compact EVs shrink congestion impact while expanding fleet uptime.”",
                    "caption": "— Maria Chen, Logistics Strategy Lead"
                }
            },
            {
                "type": "Header",
                "id": "h3",
                "data": {
                    "text": "Fleet design patterns that work",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l2",
                "data": {
                    "style": "ordered",
                    "items": [
                        "Micro-hub distribution with short-range last-mile legs",
                        "Mixed-fleet approach: compact trucks for high-frequency routes, larger units for bulk loads",
                        "Telematics-driven duty cycle matching to avoid under/over-spec vehicles"
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h4",
                "data": {
                    "text": "Payload vs. route: a quick table",
                    "level": 3
                }
            },
            {
                "type": "Table",
                "id": "t1",
                "data": {
                    "withHeadings": True,
                    "content": [
                        [
                            "Metric",
                            "Compact EV Truck",
                            "Medium EV Van"
                        ],
                        [
                            "Typical Payload (kg)",
                            "800-1,200",
                            "1,200-2,000"
                        ],
                        [
                            "Urban Manoeuvrability",
                            "High",
                            "Medium"
                        ],
                        [
                            "Typical Depot Charging",
                            "Opportunity + overnight",
                            "Overnight bulk charging"
                        ]
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h5",
                "data": {
                    "text": "Implementation checklist for fleet managers",
                    "level": 3
                }
            },
            {
                "type": "Checklist",
                "id": "chk1",
                "data": {
                    "items": [
                        {
                            "text": "Map routes by parcel density and curb constraints",
                            "checked": True
                        },
                        {
                            "text": "Pilot 5–10 compact trucks on mixed routes",
                            "checked": False
                        },
                        {
                            "text": "Install at least one micro-depot with opportunity charging",
                            "checked": False
                        }
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h6",
                "data": {
                    "text": "Risks and mitigations",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l3",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Payload limits → use mixed fleets for heavy routes",
                        "Driver retraining → operator training on regenerative braking and cargo handling",
                        "Charging access → coordinate with micro-hub and public charging operators"
                    ]
                }
            },
            {
                "type": "paragraph",
                "id": "p2",
                "data": {
                    "text": "Compact electric cargo trucks are a strategic complement to bigger vehicles — not a replacement. Smart deployment reduces congestion and cost while improving delivery speed in dense cities."
                }
            }
        ]
    },
       "featured_image_url": "/images/blog_featured/2025/11/customer-stories-hero.webp",
       "featured_image_alt": "Compact electric cargo truck parked on a busy city street",
       "is_featured": True,
       "reading_time": 1,
       "views_count": 36,
       "status": "published",
       "published_at": "2025-11-21T09:09:25Z",
       "created_at": "2025-11-21T09:09:25.007557Z"
   },
   {
       "id": 6,
       "title": "2025 Portable EV Chargers Review: Which Ones Work for Urban Fleets?",
       "slug": "review-portable-ev-chargers-2025-urban-fleets",
       "meta_description": "A practical 2025 review of portable EV chargers suitable for urban fleets, comparing cost, charging speed, durability, and fleet usability.",
       "excerpt": "A practical 2025 review of portable EV chargers suitable for urban fleets, comparing cost, charging speed, durability, and fleet usability.",
       "author": "Fleet Tech Review",
       "category": "reviews",
       "category_name": "Reviews",
       "tag_list": [
           "portable chargers",
           "fleet charging",
           "urban EVs",
           "AC charging",
           "EV review"
       ],
       "content": {
        "time": 1763138400000,
        "version": "2.25.0",
        "blocks": [
            {
                "type": "Header",
                "data": {
                    "text": "2025 Portable EV Chargers Review: Which Ones Work for Urban Fleets?",
                    "level": 2
                }
            },
            {
                "type": "paragraph",
                "data": {
                    "text": "Portable EV chargers are no longer niche gear for individual drivers. In dense cities, where fleets face limited depot space and unpredictable charging access, these compact devices are becoming insurance against downtime. But not all portable chargers are fleet-ready. This 2025 review focuses on durability, speed, and real operational usability — not marketing claims."
                }
            },
            {
                "type": "Header",
                "data": {
                    "text": "Who Actually Needs Portable Chargers?",
                    "level": 3
                }
            },
            {
                "type": "List",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Last-mile delivery fleets without guaranteed depot charging",
                        "Shared mobility operators with dynamic rebalancing",
                        "Service vans operating in mixed rural/urban routes",
                        "Taxi fleets relying on opportunity charging at public plazas"
                    ]
                }
            },
            {
                "type": "Quote",
                "data": {
                    "text": "“Portable chargers won’t replace fast charging, but they prevent operational breakdowns.”",
                    "caption": "— M. Narayan, Fleet Manager, UrbanRide Logistics"
                }
            },
            {
                "type": "Header",
                "data": {
                    "text": "Top Portable EV Chargers in 2025 (Fleet Edition)",
                    "level": 3
                }
            },
            {
                "type": "Table",
                "data": {
                    "withHeadings": True,
                    "content": [
                        [
                            "Model",
                            "Power Rating",
                            "Durability",
                            "Avg Fleet Cost",
                            "Best Use Case"
                        ],
                        [
                            "ChargeFlex Pro 7.2kW",
                            "7.2 kW AC",
                            "High (IP66)",
                            "$640",
                            "Urban delivery vans"
                        ],
                        [
                            "VoltCarry X10",
                            "10 kW AC",
                            "Medium (IP54)",
                            "$890",
                            "Taxi & shared mobility"
                        ],
                        [
                            "RoadCharge Mini 3.6",
                            "3.6 kW AC",
                            "Very High (IP67)",
                            "$410",
                            "Maintenance vans, low-usage fleets"
                        ],
                        [
                            "SmartGrid Pocket 11",
                            "11 kW AC",
                            "Medium (IP55)",
                            "$1,120",
                            "Premium executive EV fleets"
                        ]
                    ]
                }
            },
            {
                "type": "Header",
                "data": {
                    "text": "Fleet-Focused Evaluation Criteria",
                    "level": 3
                }
            },
            {
                "type": "List",
                "data": {
                    "style": "ordered",
                    "items": [
                        "Charge reliability on low-voltage urban grids",
                        "Ingress protection during monsoon and dusty conditions",
                        "Connector support (Type-2, CCS extension support)",
                        "Weight & cable tolerance for daily handling",
                        "Warranty and rapid replacement availability"
                    ]
                }
            },
            {
                "type": "Header",
                "data": {
                    "text": "The Hidden Metric: Cable Durability",
                    "level": 3
                }
            },
            {
                "type": "paragraph",
                "data": {
                    "text": "The weakest point in most portable chargers isn’t electronics — it’s the cable. Heavy fleet usage means pulling, bending, dragging on concrete and exposure to puddles. In our assessment, flexible, multi-layer insulated cables extend lifespan by ~40% for busy courier fleets. Avoid cloth-sheath cables marketed for home garages; they fail early outdoors."
                }
            },
            {
                "type": "Header",
                "data": {
                    "text": "Which Charger Should My Fleet Choose?",
                    "level": 3
                }
            },
            {
                "type": "Table",
                "data": {
                    "withHeadings": True,
                    "content": [
                        [
                            "Fleet Type",
                            "Best Charger",
                            "Reason"
                        ],
                        [
                            "Urban delivery vans",
                            "ChargeFlex Pro 7.2kW",
                            "Balanced weight, rugged IP rating"
                        ],
                        [
                            "Taxi fleets",
                            "VoltCarry X10",
                            "Higher power reduces queue downtime"
                        ],
                        [
                            "Small service fleets",
                            "RoadCharge Mini 3.6",
                            "Low cost, extreme durability"
                        ],
                        [
                            "Premium shuttle services",
                            "SmartGrid Pocket 11",
                            "Fastest AC charging option"
                        ]
                    ]
                }
            },
            {
                "type": "Header",
                "data": {
                    "text": "Cost Reality Check: Portable vs Charging Depots",
                    "level": 3
                }
            },
            {
                "type": "paragraph",
                "data": {
                    "text": "Portable units won’t eliminate depot investments. But they avoid short-term breakdown costs. For fleets with fluctuating routes or depot delays due to real-estate constraints, a handful of portable chargers can cut unplanned downtime by up to 15–22%. Think of them as operational insurance rather than a primary charging strategy."
                }
            },
            {
                "type": "Header",
                "data": {
                    "text": "Checklist Before Buying a Portable Charger (Fleet)",
                    "level": 3
                }
            },
            {
                "type": "Checklist",
                "data": {
                    "items": [
                        {
                            "text": "Works with your vehicles’ connectors (Type-2/CCS adapters)",
                            "checked": True
                        },
                        {
                            "text": "IP65 or higher for all-weather operations",
                            "checked": False
                        },
                        {
                            "text": "Minimum 2-year warranty with fast replacement terms",
                            "checked": False
                        },
                        {
                            "text": "Cable protection sleeve or reinforced insulation",
                            "checked": True
                        },
                        {
                            "text": "Weight below 7.5 kg for driver handling",
                            "checked": False
                        }
                    ]
                }
            },
            {
                "type": "Header",
                "data": {
                    "text": "Final Verdict",
                    "level": 2
                }
            },
            {
                "type": "paragraph",
                "data": {
                    "text": "Portable EV chargers are becoming essential for city-scale fleets. They can’t replace fast-charging hubs, but they dramatically reduce revenue loss caused by charging unpredictability. The winning choice depends on fleet size, route type and grid access — not maximum power rating alone."
                }
            },
            {
                "type": "paragraph",
                "data": {
                    "text": "Want a fleet-focused comparison spreadsheet with TCO estimates? Request a downloadable calculator for your vehicle mix."
                }
            }
        ]
    },
       "featured_image_url": "/images/blog_featured/2025/11/portable-ev-charger-review.webp",
       "featured_image_alt": "Technician using a portable EV charger on a city delivery van",
       "is_featured": False,
       "reading_time": 1,
       "views_count": 16,
       "status": "published",
       "published_at": "2025-11-20T05:47:33Z",
       "created_at": "2025-11-24T05:47:33.578968Z"
   },
   {
       "id": 7,
       "title": "Managed Charging as a Service: The Practical Playbook for Fleet Operators",
       "slug": "managed-charging-as-a-service-playbook-fleets",
       "meta_description": "A practical, step-by-step playbook to evaluate, procure and run Managed Charging as a Service (MCaaS) for fleets — contracts, KPIs and rollout.",
       "excerpt": "A practical, step-by-step playbook to evaluate, procure and run Managed Charging as a Service (MCaaS) for fleets — contracts, KPIs and rollout.",
       "author": "GridOps Services",
       "category": "services",
       "category_name": "Services",
       "tag_list": [
           "managed charging",
           "fleet services",
           "V2G",
           "energy management",
           "charging-as-a-service"
       ],
       "content": {
        "time": 1763967000000,
        "version": "2.25.0",
        "blocks": [
            {
                "type": "Header",
                "id": "h1",
                "data": {
                    "text": "Managed Charging as a Service: The Practical Playbook for Fleet Operators",
                    "level": 2
                }
            },
            {
                "type": "paragraph",
                "id": "p1",
                "data": {
                    "text": "Electric fleets change the nature of operations: fueling becomes load management, maintenance becomes software-driven, and energy becomes a strategic input. Managed Charging as a Service (MCaaS) packages these complexities into an operator-managed offering — but success depends on how you choose the provider, define the contract, and phase the rollout. This playbook walks you through the decisions that matter, supported by tactical checklists and measurable KPIs."
                }
            },
            {
                "type": "Header",
                "id": "h2",
                "data": {
                    "text": "1. What is MCaaS — and what isn’t it?",
                    "level": 3
                }
            },
            {
                "type": "paragraph",
                "id": "p2",
                "data": {
                    "text": "At its core, MCaaS is an outsourced service where a vendor supplies, operates and optimizes charging infrastructure on behalf of a fleet. Typical components include charger hardware (sometimes), network operations, load scheduling, billing and reporting. What it is not: a one-size-fits-all guarantee that eliminates operational responsibility. The fleet still owns route planning, vehicle specification and must remain accountable for service-level outcomes."
                }
            },
            {
                "type": "Quote",
                "id": "q1",
                "data": {
                    "text": "“Think of MCaaS as hiring a power-operator — not a black box. The better the data you feed it, the better the outcome.”",
                    "caption": "— Daniel Ruiz, Head of Fleet Electrification, GridOps"
                }
            },
            {
                "type": "Header",
                "id": "h3",
                "data": {
                    "text": "2. Why fleets choose MCaaS (the tangible benefits)",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l1",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Operational simplicity: the provider handles day-to-day charger operations and grid interactions.",
                        "CapEx to OpEx: convert heavy upfront station costs into predictable recurring fees.",
                        "Access to optimization: pooled intelligence across clients reduces energy cost and increases uptime.",
                        "Faster scale: providers already have supply chains and field service teams, shortening deployment time."
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h4",
                "data": {
                    "text": "3. Business models you’ll encounter",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l2",
                "data": {
                    "style": "ordered",
                    "items": [
                        "Full MCaaS (hardware + operations): the provider owns chargers and operations; you pay a bundled fee.",
                        "Operations-only (capex retained): fleet buys hardware; provider operates and optimizes.",
                        "Revenue-share concessions: provider builds and operates in exchange for a share of revenue.",
                        "Performance-based contracts: fees linked to SLA attainment, energy savings or uptime targets."
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h5",
                "data": {
                    "text": "4. Contract essentials — the clauses that protect you",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l3",
                "data": {
                    "style": "ordered",
                    "items": [
                        "Clear SLAs: define uptime %, fault response time, and remedy windows (e.g., 95% uptime, 4-hour hotspot response).",
                        "Data ownership & access: telematics and usage data must be exportable in open formats on request.",
                        "Transparent pricing: fixed subscription + per-kWh + explicit demand pass-throughs; avoid hidden balancing fees.",
                        "Exit & transition: defined hardware transfer terms or buyout formula and a minimum 90-day transition plan.",
                        "Liability & insurance: clarify who bears responsibility for fire, theft, and regulatory non-compliance."
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h6",
                "data": {
                    "text": "5. KPIs that actually matter (and how to measure them)",
                    "level": 3
                }
            },
            {
                "type": "Table",
                "id": "t1",
                "data": {
                    "withHeadings": True,
                    "content": [
                        [
                            "KPI",
                            "Why it matters",
                            "Suggested target / cadence"
                        ],
                        [
                            "Charger uptime (%)",
                            "Directly impacts operations and revenue",
                            ">= 98% monthly"
                        ],
                        [
                            "Average energy cost per km",
                            "Operational cost control",
                            "Track monthly; trend down quarter-on-quarter"
                        ],
                        [
                            "Peak demand reduction (%)",
                            "Avoids high tariff charges",
                            ">= 10% vs unmanaged baseline"
                        ],
                        [
                            "Time to repair (hours)",
                            "Service responsiveness",
                            "<= 8 hours for critical faults"
                        ],
                        [
                            "Data latency (secs)",
                            "Real-time control and visibility",
                            "<= 60 seconds"
                        ]
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h7",
                "data": {
                    "text": "6. A pragmatic implementation roadmap (phased and reversible)",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l4",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Phase 0 — Discovery (2–4 weeks): collect duty cycles, peak power constraints and building/utility data.",
                        "Phase 1 — Pilot (3 months): 10–20% of vehicles, 1–2 depots or sites, validate scheduling and billing.",
                        "Phase 2 — Iterate (2 months): adjust SLAs, fine-tune energy profiles and tariff optimization logic.",
                        "Phase 3 — Scale (6–12 months): full roll-out with staged hardware delivery and training.",
                        "Phase 4 — Advanced (optional): enable V2G, renewable scheduling and aggregated grid services."
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h8",
                "data": {
                    "text": "7. Quick cost illustration (simple, conservative example)",
                    "level": 3
                }
            },
            {
                "type": "paragraph",
                "id": "p3",
                "data": {
                    "text": "Numbers below are illustrative. Always model with your local tariffs and duty cycles. Example for a 50-vehicle depot:"
                }
            },
            {
                "type": "Table",
                "id": "t2",
                "data": {
                    "withHeadings": True,
                    "content": [
                        [
                            "Item",
                            "Assumption / unit",
                            "Monthly cost (USD)"
                        ],
                        [
                            "Energy (per km)",
                            "50 vehicles × 100 km/day × 0.2 kWh/km × $0.12/kWh",
                            "≈ 36,000"
                        ],
                        [
                            "MCaaS fee (example)",
                            "$300 per vehicle per month (bundled ops + support)",
                            "15,000"
                        ],
                        [
                            "Network & comms",
                            "Site connectivity & telemetry",
                            "1,200"
                        ],
                        [
                            "Total monthly (rough)",
                            "Energy + MCaaS + network",
                            "≈ 52,200"
                        ]
                    ]
                }
            },
            {
                "type": "paragraph",
                "id": "p4",
                "data": {
                    "text": "Interpretation: MCaaS fees convert capital and people costs into a predictable monthly line item. Savings can come from demand-charge mitigation, scheduled charging into lower tariffs, and fewer in-house service hours."
                }
            },
            {
                "type": "Header",
                "id": "h9",
                "data": {
                    "text": "8. Real-world considerations & common pitfalls",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l5",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Vendor lock-in: negotiate exportable data and step-out hardware transfer terms.",
                        "Over-optimistic uptime promises: require financial remedies or service credits when SLAs aren’t met.",
                        "Misaligned incentives: avoid contracts that reward providers for increasing energy volume.",
                        "Hidden fees: require a full schedule of fees in the contract (installation, spare parts, emergency response)."
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h10",
                "data": {
                    "text": "9. Short case study — urban transit operator (hypothetical)",
                    "level": 3
                }
            },
            {
                "type": "paragraph",
                "id": "p5",
                "data": {
                    "text": "A 120-bus city transit operator switched to an MCaaS provider for depot charging. Over 12 months the operator reported: charger uptime improved from 92% to 99.2%, peak-demand charges reduced by 18% through managed scheduling, and in-house charger staffing fell by two full-time equivalents (FTEs). The operator retained ownership of vehicle data and used it to reduce unscheduled downtime by 12%."
                }
            },
            {
                "type": "Header",
                "id": "h11",
                "data": {
                    "text": "10. Negotiation checklist (what to ask in the vendor RFP)",
                    "level": 3
                }
            },
            {
                "type": "Checklist",
                "id": "chk1",
                "data": {
                    "items": [
                        {
                            "text": "Provide sample SLAs and credits for missed targets",
                            "checked": True
                        },
                        {
                            "text": "Demonstrate field service coverage and spare parts inventory",
                            "checked": True
                        },
                        {
                            "text": "Show data export formats and access APIs",
                            "checked": True
                        },
                        {
                            "text": "Disclose full fee schedule (installation, maintenance, emergency response)",
                            "checked": True
                        },
                        {
                            "text": "Outline step-out / buy-out terms and timelines",
                            "checked": False
                        }
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h12",
                "data": {
                    "text": "11. Final recommendations — how to get started this quarter",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l6",
                "data": {
                    "style": "ordered",
                    "items": [
                        "Run a 4- to 8-week discovery to capture duty cycles and tariff profiles.",
                        "Issue a competitive RFP including the negotiation checklist above.",
                        "Start a 3-month pilot covering 10–20% of vehicles and 1 depot.",
                        "Measure against the KPIs in this playbook and include SLA remedies."
                    ]
                }
            },
            {
                "type": "paragraph",
                "id": "p6",
                "data": {
                    "text": "MCaaS can remove many barriers to electrification — but it is not a shortcut. Treat the vendor relationship as a strategic partnership, insist on data transparency, and phase deployments so you can learn and adjust. Done well, MCaaS turns charging from an operational headache into a managed asset that reduces cost, risk and time to scale."
                }
            },
            {
                "type": "paragraph",
                "id": "cta",
                "data": {
                    "text": "Ready to evaluate MCaaS for your fleet? Use this playbook as your RFP backbone: run discovery, pilot fast, measure carefully, and keep data ownership non-negotiable."
                }
            }
        ]
    },
       "featured_image_url": "/images/blog_featured/2025/11/managed-charging-services.webp",
       "featured_image_alt": "Fleet manager reviewing managed charging dashboard with depot chargers in background",
       "is_featured": True,
       "reading_time": 2,
       "views_count": 14,
       "status": "published",
       "published_at": "2025-11-19T05:47:57Z",
       "created_at": "2025-11-24T05:47:57.400132Z"
   },
   {
       "id": 3,
       "title": "How Fast-Charging Infrastructure Will Transform EV Adoption in Developing Cities",
       "slug": "fast-charging-infrastructure-developing-cities-ev-adoption",
       "meta_description": "Fast-charging networks are becoming the cornerstone of mass EV adoption. Discover how smart charging, public stations",
       "excerpt": "Fast-charging networks are becoming the cornerstone of mass EV adoption. Discover how smart charging, public stations",
       "author": "ChargeGrid Team",
       "category": "news",
       "category_name": "News",
       "tag_list": [
           "EV charging",
           "fast chargers",
           "urban mobility",
           "energy policy",
           "smart grid"
       ],
       "content": {
        "time": 1763794200000,
        "version": "2.25.0",
        "blocks": [
            {
                "type": "Header",
                "id": "h1",
                "data": {
                    "text": "Fast-Charging Will Decide the Future of EVs — Not Vehicles",
                    "level": 2
                }
            },
            {
                "type": "paragraph",
                "id": "p1",
                "data": {
                    "text": "EV adoption isn’t limited by the engineering of electric vehicles — it’s limited by the *speed, access, and reliability* of charging. In many fast-growing cities, consumers delay EV purchases not due to pricing, but due to charging anxiety. When public fast-chargers become as common as fuel stations, EV adoption becomes inevitable."
                }
            },
            {
                "type": "Quote",
                "id": "q1",
                "data": {
                    "text": "“Charging determines the fate of electric mobility more than batteries do.”",
                    "caption": "— Arun Patel, Urban Energy Policy Analyst"
                }
            },
            {
                "type": "Header",
                "id": "h2",
                "data": {
                    "text": "What Makes Fast Charging a Game Changer?",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l1",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Enables EV usage for people without home parking or chargers",
                        "Reduces waiting anxiety with 15–40 minute charge times",
                        "Unlocks commercial fleet electrification at scale",
                        "Potential to integrate with renewable energy storage"
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h3",
                "data": {
                    "text": "EV Charging Pyramid: A Future Ready City",
                    "level": 3
                }
            },
            {
                "type": "Table",
                "id": "t1",
                "data": {
                    "withHeadings": True,
                    "content": [
                        [
                            "Layer",
                            "Purpose",
                            "Examples"
                        ],
                        [
                            "Home & Workplace Charging",
                            "Daily use charging",
                            "Slow AC chargers, rooftop solar chargers"
                        ],
                        [
                            "Public Fast Charging",
                            "On-the-go rapid charging",
                            "DC fast chargers at malls, highways"
                        ],
                        [
                            "Fleet Depots & Hubs",
                            "Commercial mass charging",
                            "Logistics hubs, taxi stands, e-bus depots"
                        ],
                        [
                            "Smart Energy Storage",
                            "Grid load balancing",
                            "Battery banks, renewable micro-grids"
                        ]
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h4",
                "data": {
                    "text": "Where Should Developing Cities Install Fast-Chargers?",
                    "level": 3
                }
            },
            {
                "type": "Checklist",
                "id": "chk2",
                "data": {
                    "items": [
                        {
                            "text": "Transport hubs (metros, bus stations)",
                            "checked": True
                        },
                        {
                            "text": "Business districts & malls",
                            "checked": True
                        },
                        {
                            "text": "Public parking zones",
                            "checked": False
                        },
                        {
                            "text": "High-traffic highways & toll areas",
                            "checked": True
                        },
                        {
                            "text": "Residential clusters",
                            "checked": False
                        }
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h5",
                "data": {
                    "text": "The Business Side: Who Profits?",
                    "level": 3
                }
            },
            {
                "type": "paragraph",
                "id": "p2",
                "data": {
                    "text": "EV charging networks open scalable revenue models far beyond selling energy. Advertising screens, retail partnerships, subscription models for fleets, and dynamic pricing based on grid load make fast-charging hubs profitable ecosystem centers rather than simple utilities."
                }
            },
            {
                "type": "List",
                "id": "l2",
                "data": {
                    "style": "ordered",
                    "items": [
                        "Energy sales (per kWh)",
                        "Tiered subscription plans",
                        "Real-estate & retail collaborations",
                        "Integrated battery swapping hubs",
                        "Smart-grid storage partnerships"
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h6",
                "data": {
                    "text": "Barriers to Fast-Charging Expansion (and Solutions)",
                    "level": 3
                }
            },
            {
                "type": "List",
                "id": "l3",
                "data": {
                    "style": "unordered",
                    "items": [
                        "High installation costs → Government incentives + PPP infrastructure",
                        "Grid stress during peak hours → Smart scheduling + local battery storage",
                        "Land acquisition challenges → Repurpose parking lots, malls, office space",
                        "Low utilization in early years → Fleet contracts to guarantee baseline demand"
                    ]
                }
            },
            {
                "type": "Header",
                "id": "h7",
                "data": {
                    "text": "Conclusion: The Grid Is the New Highway",
                    "level": 2
                }
            },
            {
                "type": "paragraph",
                "id": "p3",
                "data": {
                    "text": "Developing cities are at a turning point. Electric mobility will not be shaped by car manufacturers alone — but by grid innovators, city planners, and energy entrepreneurs. Fast-charging infrastructure will determine which nations lead the EV revolution and which ones lag behind it."
                }
            },
            {
                "type": "paragraph",
                "id": "cta",
                "data": {
                    "text": "The future is not about building more EVs. It’s about building cities ready to charge them."
                }
            }
        ]
    },
       "featured_image_url": "/images/blog_featured/2025/11/charging-infra-banner.webp",
       "featured_image_alt": "Fast-charging station network in a developing city",
       "is_featured": True,
       "reading_time": 1,
       "views_count": 41,
       "status": "published",
       "published_at": "2025-11-17T09:49:48Z",
       "created_at": "2025-11-21T09:49:48.009743Z"
   }
   ]

for blog in blogs_data:
    BlogPost.objects.create(
        title=blog['title'],
        slug=blog['slug'],
        meta_description=blog.get('meta_description', ''),
        author=blog['author'],
        category=blog['category'],
        tags=','.join(blog.get('tag_list', [])),
        content=blog['content'],
        featured_image_alt=blog.get('featured_image_alt', ''),
        status=blog['status'],
        is_featured=blog.get('is_featured', False),
        reading_time=blog.get('reading_time', 1),
        views_count=blog.get('views_count', 0),
        published_at=blog.get('published_at'),
    )
    print(f"✅ Imported: {blog['title']}")

print("Done!")