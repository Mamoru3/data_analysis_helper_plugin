# stats_helper.py
# Stats helper, copyright Alessandro Loddo

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats import multitest


# ------------------------------------------------------------------ #
# 1.  CATEGORICAL × CATEGORICAL  ------------------------------------ #
# ------------------------------------------------------------------ #
def chi_square(df: pd.DataFrame, row_var: str, col_var: str):
    """
    Chi-square test of independence + Cramér’s V + standardised residuals.

    Returns
    -------
    dict   {table, chi2, p, dof, cramers_v, residuals}
    """
    table = pd.crosstab(df[row_var], df[col_var])
    chi2, p, dof, expected = stats.chi2_contingency(table)
    n = table.values.sum()
    cramers_v = np.sqrt(chi2 / (n * (min(table.shape) - 1)))
    residuals = (table - expected) / np.sqrt(expected)
    return {
        "table": table,
        "chi2": chi2,
        "p": p,
        "dof": dof,
        "cramers_v": cramers_v,
        "residuals": residuals,
    }


def fisher_exact_2x2(df: pd.DataFrame, row_var: str, col_var: str):
    """
    Fisher exact test (only valid on a 2 × 2 contingency table).

    Returns
    -------
    odds_ratio, p_value
    """
    table = pd.crosstab(df[row_var], df[col_var]).iloc[:2, :2]
    return stats.fisher_exact(table)


# ------------------------------------------------------------------ #
# 2.  NUMERIC × TWO GROUPS  ----------------------------------------- #
# ------------------------------------------------------------------ #
def t_test(
    df: pd.DataFrame,
    numeric: str,
    group: str,
    group0=None,
    group1=None,
    equal_var=False,
):
    """
    Welch (default) or Student t-test for two independent groups.

    Parameters
    ----------
    equal_var : bool
        False (default) = Welch’s t, robust to unequal variances.

    Returns
    -------
    statistic, p_value
    """
    if group0 is None or group1 is None:
        levels = df[group].dropna().unique()
        if len(levels) != 2:
            raise ValueError("Need exactly two groups or specify group0/group1")
        group0, group1 = levels
    a = df.loc[df[group] == group0, numeric].dropna()
    b = df.loc[df[group] == group1, numeric].dropna()
    return stats.ttest_ind(a, b, equal_var=equal_var)


def mann_whitney(
    df: pd.DataFrame,
    numeric: str,
    group: str,
    group0=None,
    group1=None,
):
    """Non-parametric alternative to the two-sample t-test."""
    if group0 is None or group1 is None:
        levels = df[group].dropna().unique()
        if len(levels) != 2:
            raise ValueError("Need exactly two groups or specify group0/group1")
        group0, group1 = levels
    a = df.loc[df[group] == group0, numeric].dropna()
    b = df.loc[df[group] == group1, numeric].dropna()
    return stats.mannwhitneyu(a, b, alternative="two-sided")


# ------------------------------------------------------------------ #
# 3.  NUMERIC × >2 GROUPS  ------------------------------------------ #
# ------------------------------------------------------------------ #
def anova(df: pd.DataFrame, numeric: str, factor: str, welch: bool = False):
    """
    One-way ANOVA.  Set `welch=True` for Welch’s (unequal-variance) ANOVA.

    Returns
    -------
    statsmodels ANOVA table
    """
    formula = f"{numeric} ~ C({factor})"
    model = smf.ols(formula, data=df).fit()
    if welch:
        return sm.stats.anova_lm(model, typ=2, robust="hc3")
    return sm.stats.anova_lm(model, typ=2)


def kruskal(df: pd.DataFrame, numeric: str, factor: str):
    """Non-parametric alternative to one-way ANOVA (Kruskal-Wallis)."""
    groups = [g.dropna() for _, g in df.groupby(factor)[numeric]]
    return stats.kruskal(*groups)


def tukey_hsd(df: pd.DataFrame, numeric: str, factor: str):
    """Tukey’s HSD post-hoc test after a significant ANOVA."""
    return pairwise_tukeyhsd(df[numeric], df[factor])


# ------------------------------------------------------------------ #
# 4.  REGRESSION MODELS  ------------------------------------------- #
# ------------------------------------------------------------------ #
def linear_regression(df: pd.DataFrame, formula: str):
    """
    Ordinary Least Squares via Patsy formula.
    Example:  'Y ~ X1 + X2 + C(CatVar)'
    """
    return smf.ols(formula, data=df).fit()


def logistic_regression(df: pd.DataFrame, formula: str):
    """
    Binary logistic regression (dependent variable must be 0/1 or bool).
    """
    return smf.logit(formula, data=df).fit()


# ------------------------------------------------------------------ #
# 5.  MULTIPLE-TEST CORRECTIONS  ------------------------------------ #
# ------------------------------------------------------------------ #
def adjust_pvalues(pvals, method: str = "fdr_bh"):
    """
    Correct a list/array of p-values (FDR, Bonferroni, …).

    Returns
    -------
    numpy.ndarray  –  corrected p-values
    """
    _, p_adj, _, _ = multitest.multipletests(pvals, method=method)
    return p_adj
