import re

def count_syllables(word):
    word = word.lower()
    # Common suffixes to remove or adjust for
    if word.endswith(("es", "ed")) and len(word) > 4: # e.g. 'created' vs 'red'
        word = word[:-2]
    elif word.endswith("e") and len(word) > 3 and word[-2] not in "aeiou": # e.g. 'manage' vs 'see'
         if len(word) > 1 and word[-2] != 'l': # handle 'able', 'ible'
            word = word[:-1]


    if not word:
        return 0

    # Count vowel groups
    syllable_count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        syllable_count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            syllable_count += 1
    
    # Adjustments for common cases
    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels: # e.g. 'able', 'turtle'
        if word[-3:] != 'ble' and word[-3:] != 'cle' and word[-3:] != 'dle' and word[-3:] != 'fle' and word[-3:] != 'gle' and word[-3:] != 'kle' and word[-3:] != 'ple' and word[-3:] != 'tle' and word[-3:] != 'zle': # common -le endings
             pass # already handled by vowel counting
        else: # for 'able', 'ible' like endings if 'e' was not removed
            pass


    if syllable_count == 0 and len(word) > 0: # for short words like "the"
        syllable_count = 1
        
    return syllable_count

def calculate_gunning_fog(text_content):
    # Clean markdown: remove headers, list markers, image tags
    text_content = re.sub(r'^#+\s+', '', text_content, flags=re.MULTILINE) # Headers
    text_content = re.sub(r'^\s*[\*\-]\s+', '', text_content, flags=re.MULTILINE) # List items
    text_content = re.sub(r'!\[.*?\]\(.*?\)', '', text_content) # Image tags
    text_content = re.sub(r'\*\*|\*', '', text_content) # Bold markers
    text_content = re.sub(r'`', '', text_content) # Code ticks

    # Basic statistics
    words = re.findall(r'\b\w+\b', text_content)
    word_count = len(words)
    
    # Sentence count (approximate)
    sentences = re.split(r'[.!?]+', text_content)
    # Filter out empty strings that might result from multiple delimiters
    sentences = [s for s in sentences if len(s.strip()) > 0]
    sentence_count = len(sentences)

    if word_count == 0 or sentence_count == 0:
        return 0, word_count, sentence_count, 0

    # Complex word count
    complex_word_count = 0
    proper_nouns_heuristics = ["tesla", "motors", "inc", "model", "musk", "elon", 
                               "roadster", "california", "u.s.", "texas", "north", "carolina",
                               "bmw", "nissan", "panasonic", "nummi", "gigafactory",
                               "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec",
                               "h1", "q1", "q2", "q3", "q4", "kwh", "asp", "r&d", "ev", "evs", "cogs", "sg&a"]

    for word in words:
        # Skip proper nouns (very heuristic) and short words
        if word.lower() in proper_nouns_heuristics or len(word) < 5: # short words are unlikely to be complex
            continue
        
        # Skip common suffixes like -es, -ed, -ing for syllable counting, handled in count_syllables
        # Skip if it's a number
        if word.isdigit():
            continue

        syllables = count_syllables(word)
        if syllables >= 3:
            # print(f"Complex word: {word}, Syllables: {syllables}") # For debugging
            complex_word_count += 1
            
    # Gunning Fog formula
    # GFI = 0.4 * ( (words / sentences) + 100 * (complex_words / words) )
    average_words_per_sentence = word_count / sentence_count
    percentage_complex_words = 100 * (complex_word_count / word_count)
    
    gunning_fog_index = 0.4 * (average_words_per_sentence + percentage_complex_words)
    
    return gunning_fog_index, word_count, sentence_count, complex_word_count

# The text content will be passed here when the tool is called
markdown_text = """
# Tesla Motors: Strategic Analysis and Future Outlook

## 1. Executive Summary

This brief provides a strategic analysis of Tesla Motors, Inc., based on the provided case study. As of early 2013, Tesla had achieved initial profitability with its Model S, a significant milestone in the challenging automotive industry. The company's innovative approach to electric vehicle (EV) design, its direct-to-consumer sales model, and its ambitious long-term "Master Plan" position it as a disruptive force. However, Tesla faces substantial challenges, including scaling manufacturing, managing a complex cost structure with high R&D and capital expenditures, navigating restrictive dealership laws, and achieving sustained profitability as it aims for mass-market vehicle production (Gen 3). Key opportunities lie in declining battery costs, technological leadership, strong brand recognition, and the growing EV market.

## 2. Key Findings

*   **Profitability Achieved, But Scalability is Key:** Tesla demonstrated initial profitability with the Model S (H1 2013 Gross Margin: ~20.35%), but R&D expenses remained high (H1 2013: ~11.08% of sales), indicating a continued focus on innovation over short-term profit maximization. Sustaining and scaling this profitability with future, higher-volume models is critical.
*   **Disruptive Sales Model Faces Legal Hurdles:** Tesla's direct sales and service model offers brand control and a unique customer experience but directly conflicts with existing dealership franchise laws in many U.S. states, leading to ongoing legal battles (e.g., Texas, North Carolina).
*   **Battery Economics are Central to Competitiveness:** Battery costs are a significant portion of EV production costs. Tesla's strategy of using commodity cells (18650) and aiming for scale (e.g., Gigafactory concept, though not fully detailed in this period) is crucial. Modeled projections show a 10% annual decline in battery costs could significantly improve future vehicle margins.
*   **The "Master Plan" Guides Long-Term Vision:** Tesla's strategy, as articulated by Elon Musk, involves entering the market with high-end vehicles (Roadster, Model S) to fund the development of more affordable, mass-market EVs (the "Gen 3" vehicle).
*   **Manufacturing and Cost Management are Critical:** While Tesla acquired the NUMMI plant and equipment at favorable terms, scaling production efficiently and managing the high costs associated with vehicle design, R&D, and in-house component manufacturing are ongoing challenges.

## 3. Analysis of Tesla's Strategy Components

### Cost Structure

Tesla's cost structure is characterized by significant R&D investments, high initial manufacturing setup costs, and a strategy of vertical integration for key components like powertrains and battery packs.
*   **Historical Performance:**
    *   Gross Profit Margin (Tesla):
        *   H1 2013: 20.35%
        *   2012: 7.28%
        *   2011: 30.16% (likely influenced by lower volume/Roadster sales)
        *   2010: 26.32%
    *   R&D as % of Sales (Tesla):
        *   H1 2013: 11.08%
        *   2012: 66.30%
        *   2011: 102.32%
        *   2010: 79.66%
    *   This contrasts with established automakers like BMW, which had a Gross Profit Margin of 29.53% and R&D at 6.97% of sales in 2012.
*   **Key Cost Drivers:** Vehicle design (estimated $0.5 billion for Model S), battery pack production (estimated $15,000-$18,000 for a 60kWh Model S pack, though significantly lower per kWh than competitors like the Leaf), and scaling up manufacturing operations.
*   **Cost Management Efforts:** Acquiring the NUMMI plant and production equipment at discounted prices helped reduce initial capital outlay. Bringing parts production in-house (e.g., 90% of Model S plastic parts) aims for control but adds complexity for a low-volume plant.

### Sales Model

Tesla employs a direct-to-consumer sales and service model, bypassing traditional independent dealerships.
*   **Approach:** Company-owned stores and galleries, often in high-traffic retail locations, with salaried salespeople. Service is provided through separate service centers, mobile "Tesla Rangers," and valet services.
*   **Rationale:** Elon Musk argued that traditional dealers have a conflict of interest when selling EVs alongside gasoline cars and that a direct model allows Tesla to better educate consumers and control the customer experience.
*   **Advantages:** Full control over branding, pricing, and customer interaction; ability to educate consumers directly about EV technology.
*   **Challenges:** Significant legal opposition from dealership associations and state laws prohibiting direct manufacturer sales. This has led to sales restrictions in states like Texas.

### Battery Economics

Battery technology and cost are fundamental to Tesla's strategy and competitiveness.
*   **Technology:** Tesla utilized commodity 18650 lithium-ion cells for its battery packs (e.g., nearly 7000 cells in the Roadster, over 7000 in the 85kWh Model S), cooperating with Panasonic for cell supply and modification. This approach differed from competitors developing special-purpose cells.
*   **Cost Reduction:** The case notes that Tesla's battery pack cost per kWh for the Model S was estimated to be less than half that of the Nissan Leaf. Battery costs were generally declining by about 10% per year between 2009-2012.
*   **Modeled Cost Decline:** A 10% annual decline from an assumed baseline of $150/kWh is projected as follows:
    ![Modeled Battery Cost Decline](../fig/battery_cost_decline.png)
    This decline is critical for making future models, especially the Gen 3, more affordable and profitable.

### Dealership Law

Tesla's direct sales model faces significant opposition from state franchise laws designed to protect independent auto dealers.
*   **Conflict:** Many states have laws requiring manufacturers to sell new vehicles through franchised dealerships. Tesla's company-owned store model directly violates these laws.
*   **Impact:** Tesla has faced legal battles and sales restrictions in several states (e.g., Texas, North Carolina). This creates uncertainty and operational complexity, potentially limiting market access.
*   **Tesla's Argument:** The company argues that its unique product and sales process necessitate a direct model, and that existing laws are anti-competitive in the context of EVs.

### Master Plan

Tesla's long-term strategy, famously outlined by Elon Musk in a 2006 blog post, is to:
1.  Build a sports car (Roadster).
2.  Use that money to build an affordable car (Model S).
3.  Use that money to build an even more affordable car (the future "Gen 3" vehicle, targeted around $35,000).
The overarching goal is to accelerate the advent of sustainable transport by bringing compelling mass-market electric cars to market as quickly as possible. The profits from higher-margin vehicles are reinvested into R&D and scaling production for subsequent, more affordable models.

## 4. Financial Outlook & Projections

### Historical Financial Ratios (from Case Exhibits)

*   **Tesla Motors (US$ thousands, except percentages/ratios):**
    *   Gross Profit Margin: 20.35% (H1 2013), 7.28% (2012), 30.16% (2011)
    *   R&D as % of Sales: 11.08% (H1 2013), 66.30% (2012), 102.32% (2011)
    *   Asset Turnover: 1.02 (Jun-13, based on annualized H1 Rev), 0.37 (Dec-12, based on FY Rev)
*   **BMW Group (million Euros, except percentages):**
    *   Gross Profit Margin: 29.53% (2012), 30.51% (2011)
    *   R&D as % of Sales: 6.97% (2012), 7.04% (2011)

These figures highlight Tesla's improving gross margin by H1 2013 but also its historically high R&D spending relative to revenue, a characteristic of its growth and innovation phase. Asset turnover indicates improving capital efficiency.

### Updated 2024 Ratios (Illustrative - Based on Hypothetical Data)

*Actual 2024 10-K data was not available. The following are based on illustrative assumptions for demonstration:*
*   Hypothetical 2024 Revenue: $85,000,000 (thousands)
*   Hypothetical 2024 Gross Margin: 20.00%
*   Hypothetical 2024 R&D Intensity: 5.88%
*   Hypothetical 2024 Capital Employed: $80,000,000 (thousands)
*   Hypothetical 2024 Capital Efficiency (Revenue / Capital Employed): 1.06

These hypothetical figures would suggest Tesla achieving significant revenue scale, maintaining a solid gross margin (comparable to H1 2013), reducing R&D intensity as revenues grow, and improving capital efficiency. *These are not actual forecasts.*

### Gen 3 Margin Simulation

The successful launch of a mass-market "Gen 3" vehicle is a cornerstone of Tesla's Master Plan. Assuming a target sale price (ASP) of $35,000, a non-battery production cost of $18,000/unit (assumption), a 60 kWh battery pack, and the modeled 10% annual battery cost decline (from a $150/kWh baseline), the gross margin for the Gen 3 vehicle could evolve significantly:

*   **Year 0 (Baseline Battery Cost $150/kWh):**
    *   Battery Cost per Vehicle: $9,000
    *   Total Cost per Vehicle: $27,000
    *   Gross Profit per Vehicle: $8,000
    *   **Gross Margin: ~22.86%**
*   **Year 5 (Battery Cost ~$88.57/kWh):**
    *   Battery Cost per Vehicle: ~$5,314
    *   Total Cost per Vehicle: ~$23,314
    *   Gross Profit per Vehicle: ~$11,686
    *   **Gross Margin: ~33.39%**
*   **Year 10 (Battery Cost ~$52.30/kWh):**
    *   Battery Cost per Vehicle: ~$3,138
    *   Total Cost per Vehicle: ~$21,138
    *   Gross Profit per Vehicle: ~$13,862
    *   **Gross Margin: ~39.61%**

The simulation illustrates the critical role of continued battery cost reduction in achieving target profitability for mass-market EVs.

![Simulated Gen 3 Gross Margin Over Time](../fig/gen3_gross_margin_simulation.png)

## 5. Strategic Challenges & Opportunities

### Challenges:
*   **Manufacturing Scale-Up:** Transitioning from relatively low-volume production of the Roadster and Model S to mass-market production of the Gen 3 vehicle presents enormous manufacturing, supply chain, and quality control challenges.
*   **Cost Control & Profitability:** Achieving sustained profitability while investing heavily in R&D, expanding production capacity (e.g., Gigafactory), and entering a more price-sensitive mass market requires stringent cost control.
*   **Dealership Law Conflicts:** Ongoing legal battles with state dealership associations could hinder market access and sales growth in key U.S. states.
*   **Competition:** Established automakers are increasingly entering the EV market, leveraging their scale, manufacturing expertise, and existing distribution networks.
*   **Capital Requirements:** Expansion, R&D, and potential new ventures (like the Gigafactory) will continue to require significant capital.

### Opportunities:
*   **Technological Leadership:** Tesla has established itself as a leader in EV technology, particularly in battery management, powertrain engineering, and vehicle software.
*   **Brand Strength:** The Tesla brand commands significant aspirational value and customer loyalty.
*   **Battery Cost Reduction:** Continued declines in battery costs, partly driven by Tesla's own initiatives (e.g., Gigafactory), can significantly improve vehicle affordability and margins.
*   **Execution of Master Plan:** Successfully launching an affordable, high-volume Gen 3 vehicle could solidify Tesla's position as a dominant player in the automotive industry.
*   **Growing EV Market:** Increasing consumer adoption of EVs, driven by environmental concerns, performance benefits, and government incentives, provides a tailwind for Tesla's growth.
*   **Vertical Integration:** Control over key components, from software to powertrain and potentially battery cells, can offer advantages in innovation speed and cost management if executed effectively.

## 6. Conclusion & Recommendations

Tesla Motors is a pioneering company that has fundamentally altered the trajectory of the automotive industry by making electric vehicles desirable, high-performing, and increasingly viable. Its innovative spirit, strong leadership, and ambitious vision are core strengths. However, the company operates in a capital-intensive industry and faces significant hurdles in scaling its operations, managing costs, and navigating a complex regulatory and competitive landscape.

**Recommendations:**

1.  **Focus on Battery Leadership:** Continue to aggressively pursue battery cost reductions through R&D, strategic partnerships (like Panasonic), and scaling initiatives like the Gigafactory. This is paramount for Gen 3 success.
2.  **Strategic Navigation of Legal Landscape:** Proactively engage with policymakers and explore alternative retail and service models to mitigate the impact of restrictive dealership laws, while defending the right to direct sales where feasible.
3.  **Master Mass-Market Manufacturing:** Prioritize operational excellence and efficiency in manufacturing to meet Gen 3 volume and cost targets. Learn from past production challenges and build robust supply chains.
4.  **Sustained Innovation:** Maintain investment in R&D to stay ahead in EV technology, autonomous driving capabilities, and software integration, which are key differentiators.
5.  **Prudent Financial Management:** Balance ambitious growth plans with disciplined capital allocation and a clear path to sustained profitability to maintain investor confidence.

Tesla's journey is a high-stakes endeavor. Success hinges on its ability to execute its ambitious Master Plan, particularly the transition to a mass-market automaker, while effectively managing the associated financial, operational, and legal complexities.
"""

if __name__ == "__main__":
    fog_index, wc, sc, cwc = calculate_gunning_fog(markdown_text)
    print(f"Gunning Fog Index: {fog_index:.2f}")
    print(f"Word Count: {wc}")
    print(f"Sentence Count: {sc}")
    print(f"Complex Word Count: {cwc}")
