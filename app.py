import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='Startup Analysis')

df = pd.read_csv('startup_cleaned4.csv')


def load_overall_analysis():
    st.title('Overall Analysis')
    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = round(df.groupby('startup')['amount'].sum().mean())
    # total funded startup
    num_startups = df['startup'].nunique()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Total',str(total)+' Cr')
    with col2:
        st.metric('Total',str(max_funding)+' Cr')
    with col3:
        st.metric('Avg',str(avg_funding)+' Cr')
    with col4:
        st.metric('Funded Startups',num_startups)

    st.header('MOM graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig, ax = plt.subplots()
    ax.plot(temp_df['x_axis'], temp_df['amount'])
    st.pyplot(fig)

def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # biggest investments
    with col1:
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)
        st.subheader('Biggest Investments')
        # st.dataframe(big_series)
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()

        st.subheader('Sectors Invested In')
        fig1, ax1 = plt.subplots(figsize=(10, 10))
        ax1.pie(vertical_series, labels=vertical_series.index, autopct='%0.01f%%')
        st.pyplot(fig1)

    with col3:
        round_series = df[df['investors'].str.contains('investor')].groupby('round')['amount'].sum()

        st.subheader('Invested In the Stage')
        fig3, ax3 = plt.subplots(figsize=(10, 10))
        ax3.pie(round_series, labels=round_series.index, autopct='%0.01f%%')
        st.pyplot(fig3)
    with col4:
        city_series = df[df['investors'].str.contains('investor')].groupby('city')['amount'].sum()

        st.subheader('Invested In the City')
        fig4, ax4 = plt.subplots(figsize=(10, 10))
        ax4.pie(city_series, labels=city_series.index, autopct='%0.01f%%')
        st.pyplot(fig4)

    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum().head(10)
    st.subheader('YOY Investments')

    fig5, ax5 = plt.subplots(figsize=(8, 4))
    ax5.plot(year_series.index, year_series.values)
    st.pyplot(fig5)


# st.dataframe(df)
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    # btn0 = st.sidebar.button('Show Overall Analysis')
    # if btn0:
    load_overall_analysis()
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')
else:
    st.title('Investor Analysis')
    selected_investor = st.sidebar.selectbox("Select Investor", sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)

    # st.title('Investor Analysis')
