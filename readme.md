# Artist Investments vs. Streaming Success  
**A Data-Driven Look at ROI for Independent Musicians**

*December, 2020*

## Overview

The recorded music industry has undergone radical changes in the past two decades, with per-listen royalties replacing revenue from physical media and paid downloads. This transition dramatically reduced artist income while competition from exploding content catalogs increased.

This project explores the effectiveness of different artist investments in driving streaming performance, attempting to quantify how spending on production and promotion is associated with differing stream counts. The aim is guide artists towards prioritizing costs that provide a measurable return.

## Summary of Findings
Production investments were positively associated with increased stream counts up to ~$9,500, after which returns diminished. Modest increases in stream counts were also associated with higher ad spending. In contrast, PR campaigns, high-quality video production, and label affiliation showed no measurable positive effect on streaming popularity. Additional singles and EPs were more strongly associated with higher stream counts than full-length albums.

## Data

The original data came from 42 artists who volunteered their 2020 digital stream reports and completed a detailed survey about their promotional and production investments. After excluding two outlier artists with unreplicable paths to exposure, the final dataset included 40 artists representing 2.9 million streams across 28 platforms. This public repo uses an anonymized version of the dataset (`artist_streams_anonymized.csv`).

### Summary Statistics (n = 40)

| Variable      | Mean    | Std. Dev. | Min   | Median | Max       |
|---------------|---------|-----------|-------|--------|-----------|
| StreamCount   | 59,668  | 212,641   | 20    | 2,241  | 1,062,833 |
| NumAlbums     | 3.1     | 3.2       | 0     | 2      | 19        |
| SinglesEPs    | 1.6     | 2.8       | 0     | 0      | 12        |
| AdSpend ($100s) | 6.63  | 20.19     | 0     | 1      | 120       |
| PR Campaigns  | 1.2     | 1.2       | 0     | 1      | 4         |
| ProdCost ($1000s) | 4.917 | 4.256   | 0     | 3.75   | 18        |
| HQVid Count   | 2.0     | 3.5       | 0     | 0      | 14        |


## Methodology

A log-linear regression model was used to estimate the relationship between various artist investments and stream counts, controlling for catalog size and label affiliation.

**Model:**

`Ln(StreamCount) = b0 + b1*ProdCost + b2*ProdCost^2 + b3*AdSpend + b4*NumPR + b5*NumHQVid + b6*NumAlbums + b7*SinglesEPs + b8*DLabel`

- **Dependent Variable:** Log of total artist stream count 
- **Key Regressors:** Production cost, ad spend, number of PR campaigns, and number of HQ music videos  
- **Controls:** Number of albums/singles/EPs on Spotify, label affiliation

## Results

- Production investment had the strongest positive relationship with stream counts, up to approximately $9,500.
- Ad spending was associated with a modest increase in stream counts, roughly 5 percent per $100.
- PR campaigns were negatively associated with stream counts across all specifications.
- High-quality video production showed no statistically significant effect on stream counts.
- Additional singles and EPs were more positively correlated with streams than full-length albums.
- No statistically significant difference in stream performance was observed between artists with and without label affiliation.

Regression specification (5), which excluded statistically insignificant variables such as HQ videos and label affiliation, explained over 60% of the variation in stream counts (Adjusted R² = 0.604).

### OLS Regression Results  
**Dependent Variable:** Log of stream quantity (Jan 1 – Aug 31, 2020)  

| Regressors       | (1)         | (2)         | (3)         | (4)         | (5)         | (6)¹        |
|------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| **ProdCost** ($1000s)    | 0.219**     | 0.909***    | 1.090***    | 1.159***    | 1.085***    | 1.113***    |
|                  | (0.081)     | (0.192)     | (0.243)     | (0.289)     | (0.259)     | (0.256)     |
| **ProdCost²** ($1000s) |  | –0.047***   | –0.057***   | –0.060***   | –0.057***   | –0.057***   |
|                  | |(0.012)     | (0.015)     | (0.017)     | (0.016)     | (0.015)     |
| **AdSpend** ($100s)      |             |             | 0.045***    | 0.048***    | 0.050***    | 0.079*      |
|                  |             |             | (0.010)     | (0.011)     | (0.011)     | (0.046)     |
| **PR**           |             |             | –0.668*     | –0.715*     | –0.639*     | –0.618      |
|                  |             |             | (0.339)     | (0.374)     | (0.369)     | (0.367)     |
| **HQVid**        |             |             |             | –0.073      |             |             |
|                  |             |             |             | (0.089)     |             |             |
| **NumAlbums**    | 0.006       | 0.024       | 0.143**     | 0.160**     | 0.184***    | 0.186***    |
|                  | (0.094)     | (0.072)     | (0.066)     | (0.077)     | (0.063)     | (0.061)     |
| **SinglesEPs**   | 0.346***    | 0.383***    | 0.315***    | 0.347***    | 0.290***    | 0.317***    |
|                  | (0.113)     | (0.105)     | (0.063)     | (0.073)     | (0.062)     | (0.065)     |
| **DLabel**       | 1.434       | 1.372       | 1.059       | 1.034       |             |             |
|                  | (1.071)     | (0.953)     | (0.801)     | (0.757)     |             |             |
| **Intercept**    | 5.946***    | 4.423***    | 4.238***    | 4.126***    | 4.308***    | 4.076***    |
|                  | (0.552)     | (0.528)     | (0.530)     | (0.563)     | (0.515)     | (0.510)     |
| **Model Fit**    |-------------|-------------|-------------|-------------|-------------|
| Standard Error (SER)   | 1.906 | 1.617 | 1.441 | 1.446 | 1.479 | 1.458 |
| Adjusted R²            | 0.342 | 0.527 | 0.624 | 0.621 | 0.604 | 0.541 |

¹ Two Ad Spend outliers removed, n = 38  
*** 1%, ** 5%, * 10% significance level  

### F-Statistics and p-Values on Joint Hypotheses

| Hypothesis                          | (1)   | (2)       | (3)       | (4)       | (5)       | (6)       |
|------------------------------------|-------|-----------|-----------|-----------|-----------|-----------|
| ProdCost, ProdCost² = 0            |      | 14.082    | 13.087 | 9.495 | 10.870 | 12.037 |
|                                    |      | (<0.001) | (<0.001)  | (<0.001)  | (<0.001)  | (<0.001)  |           
| AdSpend, PR = 0                    |      |          | 9.710     | 11.186    | 11.138    | 3.267     |
|                                    |      |          | (<0.001)  | (<0.001)  | (<0.001)  | (0.052)   |
| AdSpend, PR, HQVid = 0             |      |          |          | 7.794     |          |          |
|                                    |      |          |          | (<0.001)  |          |          |
| All investment variables = 0       |      | | 10.934 | 10.029    | 11.991    | 10.691    |
|                                    |      | | (<0.001)| (<0.001)  | (<0.001)  | (<0.001)  |

## Limitations

This analysis has several limitations:

- **Sample bias:** Artists were volunteers, skewing the sample toward jazz/instrumental musicians in the Pacific Northwest.
- **Measurement error:** Spending data is self-reported and often rounded, as many artists don't keep detailed records.
- **Simultaneous causality:** Success might drive further investment rather than the reverse.
- **Omitted variables:** Touring, sync placements, cultural relevance, and playlist algorithm dynamics were not captured but likely impact results.
- **Generalizability:** The results are unlikely to hold for a randomly selected or genre-diverse group of artists.

## Reproduction

To reproduce the analysis:

1. Clone the repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
