import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def month_lookup(month):
	year_month={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return year_month[month]

def main():
	while True:
		CSV_FILENAME = input('Please enter the time period in the format sales-YYYYMM: ')
		CSV_NAME=CSV_FILENAME+'.csv'
		csv_filepath = os.path.join("data/", CSV_NAME)
		if not os.path.isfile(csv_filepath):
		 	print("The file does not exist, please make sure to enter a file with correct format, e.g:'sales-201803'")
		else:
		 	break

	df = pd.read_csv(csv_filepath)
	products=df['product'].unique()
	products.sort()
	sales_price=df.groupby(df['product']).sum()
	sales_price_col=list(sales_price['sales price'])
	total_price_by_prod=pd.DataFrame({'products':products,'sales_price':sales_price_col})
	total_price_by_prod=total_price_by_prod.sort_values(by=['sales_price'],ascending=False)
	total_price=round(sales_price[['sales price']].sum()[0],2)
	price=[round(a,2) for a in list(total_price_by_prod['sales_price'])]
	print("-----------------------")
	print("MONTH: "+ month_lookup(CSV_FILENAME[-2:])+' '+ str(CSV_FILENAME[6:10]))
	print("-----------------------")
	print("ANALYZING")
	print("TOTAL MONTHLY SALES: "+"${0:,.2f}".format(total_price))
	print('\n')
	print("TOP SELLING PRODUCTS:")
	for i in range(len(total_price_by_prod)):
		print(str(i+1)+') '+str(total_price_by_prod.iloc[i][0])+' ' "${0:,.2f}".format(total_price_by_prod.iloc[i][1])
			)
	total_price_by_prod=pd.DataFrame({'products':products,'sales_price':sales_price_col})
	fig, ax = plt.subplots()
	fig.set_figheight(5)
	fig.set_figwidth(20)
	ax.barh(total_price_by_prod['products'],total_price_by_prod['sales_price'])
	fmt = '${x:,.2f}'
	tick = mtick.StrMethodFormatter(fmt)
	ax.set_xlabel("USD")
	ax.set_ylabel("products")
	ax.xaxis.set_major_formatter(tick)
	ax.set_title('Total sales')
	for i, v in enumerate(total_price_by_prod['sales_price']):
	    ax.text(v , i , "${0:,.2f}".format(v))
	plt.show()

if __name__ == '__main__':
	main()
