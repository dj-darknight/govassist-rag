# Knowledge Base Plan — Chatbot for Recently Retrenched Australian Tech Workers

**Audience:** Australian workers (citizens, PRs, and sponsored visa holders) who have recently
lost an IT/tech role through redundancy or termination.
**Jurisdiction:** Commonwealth of Australia, with Victorian state content where relevant.
**Corpus principle:** every passage traceable to a named official publisher with a retrieval date.

---

## PART A — Fifteen knowledge base subtopics

| # | Subtopic | Why it belongs | Example user question |
|---|---|---|---|
| 1 | **Redundancy rights & entitlements** | Notice periods, redundancy pay scales, genuine vs non-genuine redundancy, consultation obligations | "I was told Friday was my last day with no notice — is that legal?" |
| 2 | **Final pay & what you're owed** | Unused annual leave, long service leave, payment in lieu, timing of final pay | "My employer hasn't paid my leave balance three weeks later." |
| 3 | **Tax on redundancy payouts** | Genuine redundancy tax-free limit, ETP caps, how a payout affects your tax return | "How much of my $80k payout will I actually keep?" |
| 4 | **Unfair dismissal & disputes** | Eligibility, 21-day filing deadline, general protections, sham redundancy | "They made me redundant then advertised my job — can I do anything?" |
| 5 | **Employer insolvency (FEG)** | Fair Entitlements Guarantee when the company collapses owing you money | "The startup went into liquidation. Do I get my entitlements?" |
| 6 | **JobSeeker eligibility & claiming** | Who qualifies, myGov/CRN setup, documents, early claim up to 13 weeks ahead | "Can I claim if I have savings?" |
| 7 | **Waiting periods (LAWP & IMP)** | The single biggest gap in user understanding — a redundancy payout delays payment by weeks | "I got a payout, why is Centrelink saying no payment for 13 weeks?" |
| 8 | **Mutual obligations & Workforce Australia** | Job Plan, points target, reporting, demerits and penalties | "How many jobs do I have to apply for each month?" |
| 9 | **Other government financial support** | Rent Assistance, Health Care Card, Crisis Payment, concession cards | "Is there help with rent while I'm out of work?" |
| 10 | **Managing money without income** | Budgeting, hardship arrangements, mortgage/utility deferral, free financial counselling | "Can I pause my mortgage repayments?" |
| 11 | **Superannuation** | Early release on hardship grounds, insurance held inside super, consolidating, what happens to employer contributions | "Can I pull money out of my super to get by?" |
| 12 | **Visa implications for sponsored workers** | Condition 8607 cessation window, finding a new sponsor, switching visa classes | "I'm on a 482 and just got let go — how long do I have?" |
| 13 | **IT labour market data** | Which tech occupations are growing, shortage lists, regional demand, realistic timelines | "Is it worth staying in DevOps or should I pivot?" |
| 14 | **Reskilling & training pathways** | Free TAFE, VET, government-subsidised courses, certification funding | "What can I study for free while on JobSeeker?" |
| 15 | **Job search, scams & wellbeing** | Résumé and interview resources, recruitment scams targeting the unemployed, mental health support | "This recruiter wants my bank details before the interview." |

Fifteen is deliberate: it keeps roughly 8–12 passages per topic, which gives you a corpus of
150–200 passages — comparable in shape to Walert's 120 but broad enough that retrieval quality
actually matters.

---

## PART B — Source documents for each subtopic

**Legend:** ✅ = URL confirmed live in search results, ⚠️ = publisher and document title are
correct but I have not verified the exact URL — navigate from the site's search box rather than
trusting a guessed link.

### 1. Redundancy rights & entitlements — Fair Work Ombudsman
- ✅ https://www.fairwork.gov.au/ending-employment/redundancy
- ✅ https://www.fairwork.gov.au/ending-employment/redundancy/redundancy-pay
- ✅ https://www.fairwork.gov.au/tools-and-resources/fact-sheets/minimum-workplace-entitlements/notice-of-termination-and-redundancy-pay
- ✅ **Already a PDF** — https://www.fairwork.gov.au/sites/default/files/migration/723/Notice-of-termination-and-redundancy-pay.pdf
- ✅ https://www.fairwork.gov.au/tools-and-resources/library/K600448_Redundancy-pay-continuous-service-notice-periods

### 2. Final pay & what you're owed — Fair Work Ombudsman
- ⚠️ Fair Work Ombudsman, "Final pay" (under Ending employment)
- ⚠️ Fair Work Ombudsman, "Notice and Redundancy Calculator" — capture the explanatory text, not the calculator itself
- ✅ Useful plain-language state summary: https://www.nsw.gov.au/employment/if-you-lose-your-job/understand-your-rights/notice-pay-and-entitlements

### 3. Tax on redundancy payouts — ATO
- ✅ https://www.ato.gov.au/individuals-and-families/jobs-and-employment-types/working-as-an-employee/leaving-your-job/genuine-redundancy-payments
- ✅ https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/employment-termination-payments
- ✅ https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments
- ✅ https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement

**Watch out:** the tax-free base and service amounts are indexed every 1 July. Any passage
containing a dollar figure needs a `valid_for_financial_year` metadata field or your bot will
confidently quote last year's threshold.

### 4. Unfair dismissal & disputes — Fair Work Commission
- ⚠️ Fair Work Commission, "Unfair dismissal" and the unfair dismissal eligibility quiz (fwc.gov.au)
- ⚠️ Fair Work Commission, "General protections" application guide
- ⚠️ Fair Work Ombudsman, "Dismissal" and "Who doesn't get redundancy pay"

The 21-day time limit for lodging is the highest-stakes fact in your whole corpus. Consider a
hard-coded escalation for anything matching dismissal-dispute intent rather than a generated answer.

### 5. Employer insolvency (FEG) — Dept of Employment and Workplace Relations
- ⚠️ DEWR, "Fair Entitlements Guarantee" (dewr.gov.au) — FEG Hotline 1300 135 040
- ✅ Context on FEG income treatment: https://guides.dss.gov.au/social-security-guide/4/3/3/70

### 6. JobSeeker eligibility & claiming — Services Australia
- ✅ https://www.servicesaustralia.gov.au/jobseeker-payment
- ✅ https://www.servicesaustralia.gov.au/who-can-get-jobseeker-payment
- ✅ https://www.servicesaustralia.gov.au/how-to-claim-jobseeker-payment
- ✅ https://www.servicesaustralia.gov.au/when-to-claim-jobseeker-payment
- ✅ https://www.servicesaustralia.gov.au/starting-your-claim-for-jobseeker-payment
- ✅ https://my.gov.au/en/services/work/recently-unemployed/payments-to-help-if-you-re-unemployed/jobseeker-payment

Services Australia pages print with a "This information was printed [date] from [URL]" footer —
keep it, it's free provenance metadata.

### 7. Waiting periods — Services Australia + DSS Social Security Guide
- ✅ https://www.servicesaustralia.gov.au/when-youll-get-your-first-jobseeker-payment
- ✅ https://www.servicesaustralia.gov.au/liquid-assets-waiting-period
- ✅ https://guides.dss.gov.au/social-security-guide/3/1/2/20 (liquid assets test waiting period)
- ✅ https://guides.dss.gov.au/social-security-guide/4/3/4/10 (income maintenance period)

The DSS Social Security Guide is the policy-level source behind the Services Australia pages —
denser and better for inferred-answer questions where the customer-facing page is too shallow.

### 8. Mutual obligations & Workforce Australia — DEWR
- ✅ https://www.dewr.gov.au/points-based-activation-system-pbas-workforce-australia
- ✅ https://www.dewr.gov.au/newsroom/articles/explainer-mutual-obligation-requirements
- ✅ **Already a PDF** — https://www.dewr.gov.au/employment-services-data/resources/workforce-australia-user-journey-overview-points-based-activation-system
- ✅ https://guides.dss.gov.au/social-security-guide/3/11
- ⚠️ Services Australia, "Demerits and penalties for not meeting mutual obligation requirements"

### 9. Other government financial support — Services Australia
- ⚠️ Services Australia: "Rent Assistance", "Low Income Health Care Card", "Crisis Payment",
  "Income and assets tests for JobSeeker Payment", "Employment Separation Certificate"
- ⚠️ Victorian Government: utility relief grant scheme, energy concessions (energy.vic.gov.au)

### 10. Managing money without income — ASIC Moneysmart
- ✅ https://moneysmart.gov.au/work-and-tax/losing-your-job
- ⚠️ Moneysmart: "Budget planner", "Problems paying your mortgage", "Urgent help with money"
- ⚠️ National Debt Helpline (ndh.org.au) — free financial counselling, 1800 007 007

### 11. Superannuation — ATO + Moneysmart
- ⚠️ ATO, "Early access to super — severe financial hardship" and "Compassionate release of super"
- ⚠️ Moneysmart, "Getting your super" and "Insurance through super"
- ⚠️ ATO, "Keeping track of your super" / consolidating accounts

Insurance inside super is the underrated one — people cancel a super account after redundancy and
silently lose income protection and TPD cover.

### 12. Visa implications — Dept of Home Affairs
- ⚠️ Home Affairs, Skills in Demand (subclass 482) visa page and the Visa Conditions list at
  immi.homeaffairs.gov.au — navigate from the site, don't trust a guessed deep link
- ⚠️ Home Affairs, condition 8607 in the visa conditions finder
- ⚠️ Federal Register of Legislation, Migration Regulations 1994 Schedule 8 (authoritative text)

**This topic is a landmine and you should treat it as your headline evaluation case.** From
1 July 2024 the cessation window for 482/457/494 holders changed from 60 consecutive days to
180 consecutive days (365 cumulative). Half the pages currently on the open web still say 60 days.
If you scrape indiscriminately, your bot will tell someone they have two months when they have six,
or vice versa — a wrong answer that could cost them their visa. Only take this from Home Affairs
or the Register of Legislation, date-stamp it, and consider having the bot answer visa questions
with a pointer to Home Affairs plus a registered migration agent rather than a substantive answer.

### 13. IT labour market data — Jobs and Skills Australia
- ✅ https://www.jobsandskills.gov.au/data/employment-projections/occupation
- ✅ https://www.jobsandskills.gov.au/data/occupation-and-industry-profiles
- ✅ https://www.jobsandskills.gov.au/publications/australian-jobs-2026
- ✅ https://www.jobsandskills.gov.au/data (Internet Vacancy Index, Occupation Shortage List)
- ⚠️ ABS Labour Force Survey releases (abs.gov.au) for headline unemployment context

### 14. Reskilling & training — Victorian and Commonwealth
- ⚠️ Victorian Government, "Free TAFE for Priority Courses" (vic.gov.au / skills.vic.gov.au)
- ⚠️ My Skills / Your Career (yourcareer.gov.au) — National Careers Institute
- ⚠️ Services Australia, "Approved Program of Study" and study while on JobSeeker rules
- ✅ Skills-shortage framing: https://www.jobsandskills.gov.au/news/cyber-security-skills-demand-labour-market-evolves

### 15. Job search, scams & wellbeing
- ⚠️ Services Australia, "Job hunting" pages
- ⚠️ Workforce Australia (workforceaustralia.gov.au) — résumé and interview resources
- ⚠️ Scamwatch / National Anti-Scam Centre (scamwatch.gov.au) — employment and recruitment scams
- ⚠️ Beyond Blue — mental health during unemployment; Lifeline 13 11 14

**Do not let the model generate on mental-health queries.** If a user expresses distress, the right
behaviour is a fixed, hand-written response with crisis contacts, not a retrieved-and-summarised
passage. Build this as a routing rule ahead of retrieval, and say so in your report — it is a
concrete safety design decision that will read well in assessment.

---

## Building the corpus

**Capture method.** Print to PDF from the browser (Ctrl/Cmd+P → Save as PDF) rather than
screenshotting. Text stays selectable, so extraction is clean, and government pages carry a
printed-on date in the footer.

**Naming convention.** `NN_topic_publisher_YYYY-MM-DD.pdf`, e.g.
`07_waiting-periods_services-australia_2026-08-23.pdf`. The leading number maps to the taxonomy
above so provenance survives chunking.

**Metadata per passage.** Carry at minimum: `passage_id`, `subtopic_id`, `publisher`,
`source_url`, `retrieved_date`, `jurisdiction` (Cth / VIC), and `contains_indexed_figures`
(boolean — flip it true for anything with a dollar threshold or rate).

**Chunking.** Government pages are heavily nested with headings and bullets. Chunk on heading
boundaries rather than fixed token windows, or you will split a threshold away from the condition
it applies to — which is exactly how a bot ends up saying "$5,500" with no mention that it only
applies to a single person with no dependants.

**Deliberately build out-of-KB questions.** The natural ones here are questions the corpus
genuinely cannot answer: "how much will *my* payout be", "should I take the redundancy or fight
it", "will I get the job". These are the abstention cases, they map straight onto Walert's
out-of-KB category, and they let you reuse the evaluation design.

**Scope statement for your report.** This is a domain where a fluent wrong answer causes financial
and legal harm. Write into your project scope that the chatbot provides *information and
signposting, not financial, legal, tax, or migration advice*, and that it always surfaces the
source document. That framing justifies weighting abstention heavily in your evaluation instead of
optimising BERTScore alone.
