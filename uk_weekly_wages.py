import sys
import datetime 


import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns 


from matplotlib.font_manager import FontProperties
#dir_fonts=FontProperties(fname='/System/Library/Fonts/Menlo.ttc', size=12, style='oblique', variant='normal'); 
font_hiraginoProNW4='/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc';
dir_fonts=FontProperties(fname=font_hiraginoProNW4, size=12, style='oblique', variant='normal'); 
plt.rcParams['font.family'] = dir_fonts.get_name()

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import matplotlib as mpl 
#import matplotlib.style 
mpl.style.use('seaborn-dark-palette'); # classic, seaborn-pastel 
#mpl.style.use('tableau-colorblind10')

CB91_Blue = '#2CBDFE'
CB91_Green = '#47DBCD'
CB91_Pink = '#F3A0F2'
CB91_Purple = '#9D2EC5'
CB91_Violet = '#661D98'
CB91_Amber = '#F5B14C'

class weekly_wages():
	def __init__(self):
		print('calling constructor');
		
	def looked_at(self):
		f_path0='weekly_earnings_by_sectors.csv';
		df0=pd.read_csv(f_path0, encoding='utf-8', header='infer');
		df_stacked=pd.DataFrame([]);
		for jrow in df0.itertuples():
			df_temp=pd.DataFrame({
			'date':[
			jrow.year,
			jrow.year,
			jrow.year,
			jrow.year],
			'weekly_earnings':[
			jrow.Services,
			jrow.Finance_and_business_services,
			jrow.Manufacturing,
			jrow.Construction],
			'industry':[
			'Services',
			'Finance and business services',
			'Manufacturing',
			'Construction']
			})
			df_stacked=pd.concat([df_stacked,df_temp],axis=0);

		df_stacked['date']=pd.to_datetime(df_stacked['date'],format='%b %y')
		print('stacked=\n', df_stacked, ' \n', df_stacked.dtypes);
		fig0,ax0=plt.subplots(figsize=(9,5));
		sns.lineplot(data=df_stacked,x='date', y='weekly_earnings',hue='industry', ax=ax0,lw=2.5);
		ax0.set_xlabel('');
		ax0.set_ylabel('週給 ポンド', fontsize=14);
		ax0.tick_params(axis='both', which='major', labelsize=14)
		
		ax0.set_title('４つの業種の週給（週給は月平均）', fontsize=16)
		handles0, labels0 = ax0.get_legend_handles_labels()
		ggz=ax0.legend(handles=handles0[1:], labels=labels0[1:], loc='upper left', fancybox=True, framealpha=0.35)
		for jlg in ggz.legendHandles:
			jlg.set_linewidth(3);
		plt.setp(ax0.get_legend().get_texts(), fontsize=14)
		#ax0.set_xlim(['2010-01-01', '2020-12-31'])
		ax0.grid();
		plt.tight_layout();
		plt.show();


if __name__=='__main__':
	ww0=weekly_wages();
	ww0.looked_at();


