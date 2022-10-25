---
editor_options:
  markdown:
    wrap: 72
---

# Descriptive Statistics and Probability for Data Science

------------------------------------------------------------------------

### Notations

| Symbol | Definition                  |
|--------|-----------------------------|
| $\cap$ | Intersection, AND           |
| $\cup$ | Union, OR                   |
| $X$    | Random variable, Estimation |
| $x$    | Observed sample             |

------------------------------------------------------------------------

# (1) Probability

### Law of Total Probability

Probabilities of all events add up to one:

$$1 = P(A) + P(A^c)$$

------------------------------------------------------------------------

### Inclusion-Exclusion Principle

For two events: $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

For three events:
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(B \cap C) - P(A \cap C) + P(A \cap B \cap C)$$

------------------------------------------------------------------------

### Odds

**odds** are the comparison of two probabilities.

$$o = \frac{p}{1-p}$$

$$p = \frac{o}{o+1}$$

------------------------------------------------------------------------

# Probability Distribution Functions

Probabilities themselves have uncertainty. The probability distribution
characterizes the full spectrum of all possible probabilities of an
event.

-   Continuous random variables have a **probability DENSITY function**
    (PDF)

-   Discrete random variables have a **probability MASS function** (PMF)

------------------------------------------------------------------------

## Central Tendency

-   Central tendency = "typical" value of a random variable
    -   mode = measured as an outcome (not as a probability)
    -   mean = expected value
        -   For discrete $X$ with PMF $P(X = X)$
            -   $\mathbb{E}(X) = \displaystyle\sum_{x}x \cdot P(X = x)$
        -   For continuous X with PDF $f_{X}(x)$
            -   $\mathbb{E}(X) = \displaystyle\int_{x}x \cdot f_{X}(x)$
        -   Sample mean
            -   $\overline{X} = \frac{1}{n} \displaystyle\sum_{i=1}^{n} X_{i}$

------------------------------------------------------------------------

### Linear properties of expected values

How the expected value is affected by the transformation of random
variables.

-   $\mathbb{E}(aX) = a\mathbb{E}(X)$
-   $\mathbb{E}(X + Y) = \mathbb{E}(X) + \mathbb{E}(Y)$
-   $\mathbb{E}(XY) \neq \mathbb{E}(X)\mathbb{E}(Y)$
-   $\mathbb{E}(X^{2}) \neq [\mathbb{E}(X)]^{2}$

------------------------------------------------------------------------

## Uncertainty

-   Uncertainty = the "variability" of a variable
-   Cannot be negative
-   0 means no randomness

------------------------------------------------------------------------

### Entropy

$$H(Y) = - \displaystyle\sum_{x} P( X = x) log[P(X = x)]$$

-   entropy = measured as transformation of probabilities = measure of
    **SURPRISE**
    -   [[Youtube] Entropy (for data science) Clearly
        Explained](https://www.youtube.com/watch?v=YtebGVx-Fxw)
    -   The more homogeneous a population is, the lower the entropy.
    -   The more random a population (equally distributed), the higher
        the entropy.
    -   [[Youtube] Introduction to Entropy for Data
        Science](https://www.youtube.com/watch?v=IPkRVpXtbdY)

------------------------------------------------------------------------

### Variance

| $\text{Var} (X) = \mathbb{E}{[X - \mathbb{E}(X)]^{2}}$ | $\text{Var} (X) = \mathbb{E}(X^{2}) - [\mathbb{E}(X)]^{2}$ |
|-----------------------------------|-------------------------------------|

-   Variance = squared deviation from the mean

-   $X^{2}=Z$ is a random variable transformation. It is a new variable
    containing the squares of the values of $X$ while maintaining the
    corresponding probabilities. $Z$ and $X$ have [**different
    distributions**]{.underline}.

-   sample variance:

$$S^{2} = \frac{1}{n-1} \displaystyle\sum_{i=1}^{n} (X_{i} - \overline{X})^{2}
$$

------------------------------------------------------------------------

### Standard Deviation

-   standard deviation = sqrt of variance

------------------------------------------------------------------------

## Random Variable Transformations

What is the point of this transformation? To make the bins more extreme
Emphasize polarity? Differentiate distributions with same mean. Mean is
sensitive to outliers.

anova = mean squared chi-square distributions to make more meaningful
manipulations.

To make your life easier in hypothesis testing and statistical modelling

-   Chart of [Univariate Distribution
    Relationships](http://www.math.wm.edu/~leemis/chart/UDR/UDR.html)

------------------------------------------------------------------------

# (2) Parametric Families of Distributions

Parametric, as in, can be defined using parameters. There are several
ways to parameterize a distribution family--the choice will depend on
what information is accessible.

-   [Wikipedia's list of probability
    distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions)

------------------------------------------------------------------------

## Binomial Distribution

<http://www.math.wm.edu/~leemis/chart/UDR/PDFs/Binomial.pdf>

![](https://img.shields.io/badge/R-dbinom()-inactive?style=flat-square&logo=R&logoColor=blue&labelColor=white)
![](https://img.shields.io/badge/Python-scipy.stats.binom()-inactive?style=flat-square&logo=python&logoColor=blue&labelColor=yellow)

$$X \sim \text{Binomial}(n,\pi)$$

-   $X$ is the distribution of outcomes of $n$ games with winning
    probability of $\pi$.
-   $\sim$ = "distributed as"
-   $\pi$ = probability parameter, not pi.

### Binomial PMF

$$ P(X=x|n, \pi) = {n \choose x} \pi^{x} (1- \pi)^{n-x} \text{  for  } x = 0, 1, \ldots , n $$
where $$ {n \choose x} = \frac{n!}{x!(n-x)!} $$

### Expected Value

$$E(X) = n \pi$$

### Variance

$$ \text{Var}(X) = n \pi (1- \pi) $$

------------------------------------------------------------------------

## Geometric Distribution

![](https://img.shields.io/badge/R-dgeom()-inactive?style=flat-square&logo=R&logoColor=blue&labelColor=white)
![](https://img.shields.io/badge/Python-scipy.stats.geom()-inactive?style=flat-square&logo=python&logoColor=blue&labelColor=yellow)

$$X \sim \text{Geometric}(\pi)$$

-   $X$ demonstrates the outcome of a game with win rate $\pi$ played
    $n$ times before a win. Check the definition--X may or may not
    include the winning attempt.
-   Geometric distribution has infinitely many possible outcomes.

`(Something about "infinite support" that I don't understand..)`

### Geometric PMF

$$P(X = x | \pi) = \pi (1 - \pi)^{x} \text{  for  } x=0,1,\ldots$$

### Expected Value

$$E(X) = \frac{1- \pi}{\pi}$$

### Variance

$$ \text{Var}(X) = \frac{1- \pi}{\pi^{2}} $$

------------------------------------------------------------------------

## Negative Binomial (= Pascal) Distribution

![](https://img.shields.io/badge/R-dnbinom()-inactive?style=flat-square&logo=R&logoColor=blue&labelColor=white)
![](https://img.shields.io/badge/Python-scipy.stats.nbinom()-inactive?style=flat-square&logo=python&logoColor=blue&labelColor=yellow)

$$X \sim \text{Negative Binomial}(k, \pi)$$

-   $X$ is the number of losses at a game with win rate $\pi$ before
    experiencing $k$ wins.
-   When $k=1$, this becomes a Geometric distribution.

### Negative Binomial PMF

$$P(X = x | k, \pi) = {x \choose k-1+x} \pi^{k} (1- \pi)^{x} \text{  for  } x=0,1,\ldots$$

### Expected Value

$$E(X) = \frac{k(1- \pi)}{\pi}$$

### Variance

$$ \text{Var}(X) = \frac{k(1- \pi)}{\pi^{2}} $$

------------------------------------------------------------------------

## Poisson Distribution

![](https://img.shields.io/badge/R-dpois()-inactive?style=flat-square&logo=R&logoColor=blue&labelColor=white)
![](https://img.shields.io/badge/Python-scipy.stats.poisson()-inactive?style=flat-square&logo=python&logoColor=blue&labelColor=yellow)

$$X \sim \text{Poisson}(\lambda)$$

-   $X$ is the total that accumulated over a period of time with an
    average rate $\lambda$.

### Negative Binomial PMF

$$P(X = x | \lambda) = \frac{\lambda^{x} \text{exp}(-\lambda)}{x!} \text{  for  } x=0,1,\ldots$$

### Expected Value

$$E(X) = \lambda$$

### Variance

$$ \text{Var}(X) = \lambda$$

------------------------------------------------------------------------

## Bernoulli (= Binary) Distribution

$$X \sim \text{Bernoulli}(\pi)$$

-   $X$ is the number of losses at a game with win rate $\pi$ before
    experiencing $k$ wins.
-   Bernoulli is a special case of Binomial with $n=1$.

### Negative Binomial PMF

$$P(X = x | \pi) = \pi^{x}(1-p)^{1-x} \text{  for  } x=0,1$$

### Expected Value

$$E(X) = \pi$$

### Variance

$$ \text{Var}(X) = \pi(1-\pi)$$

------------------------------------------------------------------------

# (3) Joint Probability

## Joint Distributions

Joint distributions = working with multiple random variables

Covariance = the variables are not independent; they are related

copula = take correlations from different marginal distributions into
normal modelling

-   Gaussian copula

-   There is more than one way to obtain a joint distribution. Any
    specific procedure will depend on factors such as the existing
    correlation between a given set of random var.

marginal distribution = within a system of many variables, the
standalone distribution of an indivdual variable; variable is considered
in isolation from other related variables within the same system

how to go from joint to marginal? = adding up the probabilities
corresponding to relevant outcomes

------------------------------------------------------------------------

## Dependence Concepts

### Independence

-   $X$ and $Y$ are independent, if knowing something about one of them
    tell us nothing about the other. They can still happen at the same
    time, hence IS NOT MUTUALL EXCLUSIVE. If these two random variables
    are independent, you only need the correseponding marginal
    probabilities associated with their joint distribution. Independence
    is a CONDITION of the random variables.

-   How to check if independent? 1) Find marginal; 2) Use them to check
    whether the distribution satisfies definition of independence

$$
P(X=x \cap Y=y) = P(X=x) \cdot P(Y=y)
$$

Measures of Dependence "strength" of dependence

------------------------------------------------------------------------

### Covariance

[Covariance and correlation
(video)](https://www.youtube.com/watch?v=KDw3hC2YNFc)

[How would you explain covariance
\...](https://stats.stackexchange.com/questions/18058/how-would-you-explain-covariance-to-someone-who-understands-only-the-mean)

Covariance = dependence between two NUMERIC random variables

-   Only measures linear relationships

-   Unlike variance, there can be NEGATIVE covariance

-   Positive covariance = an increase in one variable is associated with
    an increase in the other variable

-   Zero covariance = no LINEAR trends found (but may be related in
    other ways)

-   Covariance by itself is not very interpretable, because it depends
    on the spread of X and Y.

-   The "scale problem" in covariance is fixed by **Pearson's
    correlation**.

    -   standardize = subtract the mean, divide by ...

    -   normalization

    -   standard deviation = 1

$$
\text{Corr}(X,Y)=\mathbb{E}[(\frac{X-\mu_{X}}{\sigma_{X}})(\frac{Y-\mu_{Y}}{\sigma_{Y}})]
$$

"correlation coefficient" usually refers to Pearson's

$$
-1 \leq \text{Corr}(X,Y) \leq 1
$$

------------------------------------------------------------------------

### Kendall's Tau $\tau_{K}$

-   pair by pair of rows

-   strength of relationship

-   can capture nonlinear relationships, but relationships MUST BE
    MONOTONIC - as you increase one, the other increases as well

------------------------------------------------------------------------

### Mutual Information

-   Measures dependence in categorical variables

------------------------------------------------------------------------

# Resources

### Textbook

-   [Daniel Kunin - Seeing Theory (visualized
    textbook)](https://seeing-theory.brown.edu/index.html)

-   [Chris Piech - Stanford University Course Reader for
    CS109](https://chrispiech.github.io/probabilityForComputerScientists/en/index.html)

-   [Alex Tsun - Probability & Statistics with Applications to
    Computing](https://www.alextsun.com/files/Prob_Stat_for_CS_Book.pdf)

-   [Stanley H. Chan - Introduction to Probability for Data
    Science](https://probability4datascience.com/)

-   [Ian Goodfellow & Yoshua Bengio & Aaron Courville - Deep
    Learning](https://www.deeplearningbook.org/)

-   [H. Pishro-Nik - Introduction to Probability, Statistics and Random
    Processes](https://www.probabilitycourse.com/)

-   [Joseph K. Blitzstein & Jessica Hwang - Harvard University
    Introduction to
    Probability](https://drive.google.com/file/d/1VmkAAGOYCTORq1wxSQqy255qLJjTNvBI/edit)

### Cheatsheets

-   <https://github.ubc.ca/MDS-2022-23/DSCI_551_stat-prob-dsci_students/blob/master/cheatsheet/DSCI_551_Cheatsheet.pdf>

-   <https://github.com/wzchen/probability_cheatsheet>

-   <http://web.cs.elte.hu/~mesti/valszam/kepletek>

### Courses

-   [contour
    plots](https://www.khanacademy.org/math/multivariable-calculus/thinking-about-multivariable-function/visualizing-scalar-valued-functions/v/contour-plots?modal=1)
    / [surface plots](https://plotly.com/r/3d-surface-plots/)

-   [JBstatistics](http://www.jbstatistics.com/) /
    [YouTube](https://www.youtube.com/channel/UCiHi6xXLzi9FMr9B0zgoHqA)

-   [Harvard STAT 110 course](https://projects.iq.harvard.edu/stat110) /
    [YouTube
    videos](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo)

-   [Word problems for conditional
    probability](https://www.math.kth.se/matstat/gru/sf1901/TCOMK/exercises.pdf)

\
