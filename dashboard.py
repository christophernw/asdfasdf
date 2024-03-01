import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
import requests
from io import StringIO

st.header("🔍📊 Christo's E-Commerce Analysis 💻🛍️")
st.caption('By: Christopher Nathanael Wijaya')

# min_date = all_df["order_date"].min()
# max_date = all_df["order_date"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://cdn.discordapp.com/attachments/1197482797577809961/1213195950277918800/shopping-bag.png?ex=65f497c6&is=65e222c6&hm=34c43a22ca88a5fbc3773909607422740af8e31ecb6f7674db246b08895e1b29&")
    st.subheader("Welcome to Christo's Dashboard 📚")
    # Mengambil start_date & end_date dari date_input
    # start_date, end_date = st.date_input(
    #     label='Rentang Waktu',min_value=min_date,
    #     max_value=max_date,
    #     value=[min_date, max_date]
    # )
# Fetch the CSV data from the GitHub URL
url = "https://raw.githubusercontent.com/christophernw/testingdata/main/all_data.csv"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Read the CSV data using StringIO
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)


st.header("After going through these steps ...")
col1, col2, col3 = st.columns([1, 1, 1])
 
with col1:
    st.subheader("Wrangling 1️⃣") 
    st.image("https://cdn.discordapp.com/attachments/1197482797577809961/1213206220366938142/folders.png?ex=65f4a157&is=65e22c57&hm=0eead0428f175f2108ae34762cc48f31cc6fcd0592ea03304a23db1f2a1c6c8c&", width=200)
with col2:
    st.subheader("EDA 2️⃣")
    st.image("https://cdn.discordapp.com/attachments/1197482797577809961/1213208031869800498/exploration_2.png?ex=65f4a307&is=65e22e07&hm=fc8e3d83f6f2ec59f61e88a0736fd7c755126d5cde6428c9d52299161641b692&", width=200)
with col3:
    st.subheader("Visualization 3️⃣")
    st.image("https://cdn.discordapp.com/attachments/1197482797577809961/1213207673625907290/pie-chart.png?ex=65f4a2b1&is=65e22db1&hm=0e13b6d18adc19c7b2958e88b01c69c13d91ce7efa0927b645e700253f0519e9&", width=200)
    
st.header('These are my findings:')
top_10_cities = df['customer_city'].value_counts().head(10)
top = top_10_cities[0]
st.title('1. Top 10 Cities🏅')

fig, ax = plt.subplots(figsize=[10, 6])
sns.barplot(x=top_10_cities.values, y=top_10_cities.index, palette='crest_r')
plt.title('Top 10 Customers Capacity Cities')
sns.despine()
st.pyplot(fig)
st.text("Sau Paulo 🥶")

top_10_states = df['customer_state'].value_counts().head(10)
st.title('2. Top 10 States 🏆')
fig, ax = plt.subplots(figsize=[10, 6])
sns.barplot(x=top_10_states.values, y=top_10_states.index, palette='crest_r')
plt.title('Top 10 Customers Capacity States')
sns.despine()
st.pyplot(fig)

st.title('3. Product Review Score ✏️')
plt.figure(figsize=[15, 8])
review_score_index = [str(i) for i in df.review_score.value_counts().index]
sns.barplot(x=review_score_index, y=df.review_score.value_counts().values, palette='crest_r')
plt.title('Review Scores')
sns.despine()
st.pyplot(plt)
st.text("That's preety good 👍")

st.title('4. Category Distribution 📊')
def classify_cat(x):
    if x in ['office_furniture', 'furniture_decor', 'furniture_living_room', 'kitchen_dining_laundry_garden_furniture', 'bed_bath_table', 'home_comfort', 'home_comfort_2', 'home_construction', 'garden_tools', 'furniture_bedroom', 'furniture_mattress_and_upholstery']:
        return 'Furniture'
    elif x in ['auto', 'computers_accessories', 'musical_instruments', 'consoles_games', 'watches_gifts', 'air_conditioning', 'telephony', 'electronics', 'fixed_telephony', 'tablets_printing_image', 'computers', 'small_appliances_home_oven_and_coffee', 'small_appliances', 'audio', 'signaling_and_security', 'security_and_services']:
        return 'Electronics'
    elif x in ['fashio_female_clothing', 'fashion_male_clothing', 'fashion_bags_accessories', 'fashion_shoes', 'fashion_sport', 'fashion_underwear_beach', 'fashion_childrens_clothes', 'baby', 'cool_stuff', ]:
        return 'Fashion'
    elif x in ['housewares', 'home_confort', 'home_appliances', 'home_appliances_2', 'flowers', 'costruction_tools_garden', 'garden_tools', 'construction_tools_lights', 'costruction_tools_tools', 'luggage_accessories', 'la_cuisine', 'pet_shop', 'market_place']:
        return 'Home & Garden'
    elif x in ['sports_leisure', 'toys', 'cds_dvds_musicals', 'music', 'dvds_blu_ray', 'cine_photo', 'party_supplies', 'christmas_supplies', 'arts_and_craftmanship', 'art']:
        return 'Entertainment'
    elif x in ['health_beauty', 'perfumery', 'diapers_and_hygiene']:
        return 'Beauty & Health'
    elif x in ['food_drink', 'drinks', 'food']:
        return 'Food & Drinks'
    elif x in ['books_general_interest', 'books_technical', 'books_imported', 'stationery']:
        return 'Books & Stationery'
    elif x in ['construction_tools_construction', 'construction_tools_safety', 'industry_commerce_and_business', 'agro_industry_and_commerce']:
        return 'Industry & Construction'

df['product_category'] = df.product_category_name_english.apply(classify_cat)
plt.figure(figsize=[10, 6])
sns.barplot(x=df.product_category.value_counts().values, y=df.product_category.value_counts().index, palette='crest_r')
plt.title('Number of orders per each Category')
plt.xticks(rotation=45)
sns.despine()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
st.text("The Electronics are going crazy nowadays 💥🤯")

st.title('5. Favs Payment Method 💸💸')
fig, ax = plt.subplots(figsize=[10, 10])
ax.pie(df.payment_type.value_counts().values, explode=(0.05, 0.05, 0.05, 0.05), labels=df.payment_type.value_counts().index, autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title('Payment Types Distribution')
st.pyplot(fig)
st.text("Credit Card 💳😍")


st.subheader("That's all for now, thank you gais 🤩🙏🏻")