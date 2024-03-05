import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts_10 = nba_2010[nba_2010.fran_id == 'Knicks']['pts']
nets_pts_10 = nba_2010[nba_2010.fran_id == 'Nets']['pts']

diff_means_2010 = knicks_pts_10.mean() - nets_pts_10.mean()
print(diff_means_2010)

plt.hist(knicks_pts_10, color="blue", label="Knicks", alpha=0.5)
plt.hist(nets_pts_10, color="red", label="Nets", alpha=0.5)
plt.legend()
plt.title("2010 Season")
plt.show()

# 4
knicks_pts_14 = nba_2014.pts[nba.fran_id=="Knicks"]
nets_pts_14 = nba_2014.pts[nba.fran_id=="Nets"]

knicks_mean_14 = np.mean(knicks_pts_14)
nets_mean_14 = np.mean(nets_pts_14)
diff_means_2014 = knicks_mean_14 - nets_mean_14
print(diff_means_2014)

plt.hist(knicks_pts_14, color="blue", label="Knicks", normed=True, alpha=0.5)
plt.hist(nets_pts_14, color="red", label="Nets", normed=True, alpha=0.5)
plt.legend()
plt.title("2014 Season")
plt.show()

# 5
sns.boxplot(data=nba_2010, x='fran_id', y='pts')
plt.show()

# 6
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

# 7
location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)

# 8
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

# 9
point_diff_forecast_cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_cov)

# 10
point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

# 11
plt.scatter(x='forecast', y='point_diff', data=nba_2010)
plt.xlabel('Forecast Win Prob')
plt.ylabel('Point Diff')
plt.show()