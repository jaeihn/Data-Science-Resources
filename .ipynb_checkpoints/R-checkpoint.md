---
layout: default
title:  "R"
---


# R

## Reading data files

- Look at the data file first, to choose appropriate function arguments. 
  - Does it have headers?
  - Does it have index names? 
  - Does it have meta data? 
  - What delimiter does it use?


```R
# For plain text files
library(readr)
```


```R
# Default
# data <- read_csv("")
```


```R
# Skipping rows

## At the beginning
# can_lang2 <- read_csv("data/can_lang-meta-data.csv", skip = 2)

## At the end
```


```R
# For Microsoft Excel files
library(readxl)
```

## Documentation using R Markdown

In R Markdown, you can name code chunks and add options. 

`{r name-of-code-chunk options=TRUE}`

Options can be set globally for all chunks at the beginning of document. Local options override the global options.

```
# Put this inside the first r code chunk. 
# Write options in (...), separated with commas.

knitr::opts_chunk$set(...)
```

| Option | Default | Description |
|--------|---------|-------------|
| <code>eval</code> | TRUE | evaluate code and display results |
| <code>echo</code> | TRUE | display code and results; when false, hides code and only shows output |
| <code>warning</code> | TRUE | display warnings |
| <code>error</code> | FALSE | display errors |
| <code>message</code> | TRUE | display messages |
| <code>tidy</code> | FALSE | reformat code in tidy way |
| <code>cache</code> | FALSE | cache results for future renders |
| <code>fig.width</code> | TRUE | set width of plot |
| <code>fig.height</code> | TRUE | set height of plot | 

More options can be found in [R Markdown Reference Guide](https://www.rstudio.com/wp-content/uploads/2015/03/rmarkdown-reference.pdf).


- supports inline evaluated code
- supports LaTex math equationsb

### Citing R 


```R
citation()
```


    
    To cite R in publications use:
    
      R Core Team (2022). R: A language and environment for statistical
      computing. R Foundation for Statistical Computing, Vienna, Austria.
      URL https://www.R-project.org/.
    
    A BibTeX entry for LaTeX users is
    
      @Manual{,
        title = {R: A Language and Environment for Statistical Computing},
        author = {{R Core Team}},
        organization = {R Foundation for Statistical Computing},
        address = {Vienna, Austria},
        year = {2022},
        url = {https://www.R-project.org/},
      }
    
    We have invested a lot of time and effort in creating R, please cite it
    when using it for data analysis. See also ‘citation("pkgname")’ for
    citing R packages.


