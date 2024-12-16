import pandas as pd
import mysql.connector
import streamlit as st 
from streamlit_option_menu import option_menu  #used for selecting an option from list of options in a menu
import plotly.express as px 
import plotly.graph_objects as go
from tabulate import tabulate
import altair as alt

#each bus we have to filter
#now we have to take route_name from each dataframe and then append to list

#kerala bus
kerala=[]
df_k=pd.read_csv("df_k.csv")
for i,r in df_k.iterrows():  #traverse through each row
    kerala.append(r['Route_name'])   # add that row in new list


#Andhra bus
andhra=[]
df_a=pd.read_csv("df_a.csv")
for i,r in df_a.iterrows():
    andhra.append(r['Route_name'])

#Assam bus
assam=[]
df_as=pd.read_csv("df_as.csv")
for i,r in df_as.iterrows():
    assam.append(r['Route_name'])


#goa bus
goa=[]
df_g=pd.read_csv("df_g.csv")
for i,r in df_g.iterrows():
    goa.append(r['Route_name'])
    
#telungana
telungana=[]
df_t=pd.read_csv("df_t.csv")
for i,r in df_t.iterrows():
    telungana.append(r['Route_name'])

#haryana
haryana=[]
df_h=pd.read_csv("df_h.csv")
for i,r in df_h.iterrows():
    haryana.append(r['Route_name'])

#punjab bus
punjab=[]
df_pb=pd.read_csv("df_pb.csv")
for i,r in df_pb.iterrows():
    punjab.append(r["Route_name"])

#rajasthan bus
rajasthan=[]
df_r=pd.read_csv("df_r.csv")
for i,r in df_r.iterrows():
    rajasthan.append(r['Route_name'])
    
#south bengal bus
sbengal=[]
df_s=pd.read_csv("df_s.csv")
for i,r in df_s.iterrows():
    sbengal.append(r["Route_name"])
    
#uttar pradesh bus
up=[]
df_u=pd.read_csv("df_up.csv")
for i,r in df_u.iterrows():
    up.append(r['Route_name'])

#west bengal bus
wbengal=[]
df_wb=pd.read_csv("df_wb.csv")
for i,r in df_wb.iterrows():
    wbengal.append(r['Route_name'])

###############################################

# ---------------> STREAMLIT PART ------------>

###############################################



#setting streamlit page
st.set_page_config(layout="wide",page_icon=":material/directions_bus:",page_title="RedBus Project",initial_sidebar_state="expanded")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.hdqwalls.com/wallpapers/bus-retro-56.jpg");
        background-size: cover; /* Ensures the image covers the entire container */
        background-position: center; /* Centers the image */
        background-repeat: no-repeat; /* Prevents the image from repeating */
        background-attachment: fixed; /* Fixes the image in place when scrolling */
        height: 100vh; /* Sets the height to 100% of the viewport height */
        width: 100vw; /* Sets the width to 100% of the viewport width */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] {{
        background-color: #60191900; /* Replace with your desired color */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Ensure font size does not change on hover */
    .nav-link {
        font-size: 18px !important;
    }
    .nav-link:hover {
        font-size: 18px !important;
        color: #32789e !important; /* Change only the color on hover */
    }
    .nav-link-selected {
        font-size: 20px !important;
    }
    </style>
    """,unsafe_allow_html=True
)




# Theme button in the sidebar



with st.sidebar:
    #THEME CONTROL  OPERATIONAL IN SIDEBAR
    
    
    menu = option_menu(
        "Main Menu", 
        ["Home", 'Bus Routes'], 
        icons=['house', 'map'], 
        menu_icon="cast", 
        default_index=0,
        styles={
            "icon":{"font-size":"21px"},
            # "nav-link-selected": {"background-color": "#0b0bdd","font-size":"20px"}
        }
    )


if menu=="Home":
    st.title(":red[:material/analytics:] :green[Redbus Data Scraping with Selenium  & Dynamic Filtering using Streamlit]")
    st.text("")
    st.subheader(" ")
    st.markdown(""" ### :violet[:material/tooltip:] :red[*Objective of the Project*]

                To Scrape the Data from Redbus Website and to create a user interface and 
     dynamic filtration of data using streamlit and SQL 
    """)
    
    dfbus=pd.read_csv("dfbus.csv")
    
    fig = px.scatter(dfbus, 
                 x='Price', 
                 y='Ratings', 
                 color='Bus_type',
                 size='Seats_Available',
                 hover_name='Bus_name',
                 title='Bus Price vs Ratings',
                 labels={'Price': 'Ticket Price', 'Ratings': 'Bus Ratings'})

    # Display the plot in Streamlit
    st.plotly_chart(fig)
    
    st.markdown("""
                <br><br>""",unsafe_allow_html=True)
    
    labels = dfbus['Seats_Available']
    values = dfbus['Ratings']

    # Create the Pie chart
    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.1)])
    fig2.update_layout(
        title_text="distribution",
        title_x=0.45
    )
    st.plotly_chart(fig2)
    
    st.markdown("""
                <br><br>""",unsafe_allow_html=True)
    
    
    
    dfbus = pd.read_csv("dfbus.csv")

    # Create an Altair chart
    chart = alt.Chart(dfbus).mark_circle().encode(
        y='Price:Q',               # 'Price' as a quantitative (float) field
        x='Total_duration:N',      # 'total_duration' as a nominal (string) field
        color='Route_name:N',          # Adjust this to the appropriate categorical column in your data
    ).interactive()

        # Display the chart
    st.altair_chart(chart,use_container_width=True)
        
    #altair
    # Top panel is a scatter plot of Total_duration vs Price
    brush = alt.selection_interval(encodings=['x'])

# Define the click selection for interactivity
    click = alt.selection_single(encodings=['y'])

    # Top panel is a scatter plot of Total_duration vs Price
    points = (
        alt.Chart(dfbus)
        .mark_point()
        .encode(
            alt.X("Total_duration:N", title="Total Duration"),
            alt.Y("Price:Q", title="Price"),
            color=alt.condition(brush, "Bus_type:N", alt.value("lightgray")),
            size=alt.Size("Price:Q", scale=alt.Scale(range=[5, 200])),
        )
        .properties(width=550, height=300)
        .add_selection(brush)
        .transform_filter(click)
    )

    # Bottom panel is a bar chart of Bus_type
    bars = (
        alt.Chart(dfbus)
        .mark_bar()
        .encode(
            y="Bus_type:N",
            x="count():Q",
            color=alt.condition(click, alt.Color('Bus_type:N', legend=None), alt.value("lightgray")),
        )
        .transform_filter(brush)
        .properties(width=300, height=700)
        .add_selection(click)
    )
        # Combine the charts
    chart = alt.vconcat(points, bars, title="Bus Data Analysis")

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)
    

# ALL Datas from table

def fetching_all_data():

    conn=mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="R!sh!raj00ty",
                                    database="redbus")          
    my_cursor=conn.cursor()

    sql_query_all = "SELECT * FROM busdetail;"

    my_cursor.execute(sql_query_all)
    table=my_cursor.fetchall()
    conn.commit()

    df=pd.DataFrame(table,columns=["ID","Bus_name","Route_name","Bus_type","Start_time",
                                "Duration","End_time","Ratings","Price","Seats_Available",
                                "Route_link","State"])
    
    st.dataframe(df)
    return df
    
if menu=="Bus Routes":
    
    st.title(":green[:material/filter_alt:]    :blue[Dynamic Filtering of Data]")

    #all_data_df = pd.read_csv(r"D:\Vignesh\My Files\Client Projects\R\dfbus.csv")
    
    st.title("Bus Routes")

    all_data_df = fetching_all_data()

    st.subheader("FILTERS")

    col1, col2, col3 = st.columns(3)

    # state filtering
    with col1:

        state_list = list(sorted(all_data_df["State"].unique()))

        state = st.selectbox("Select the State", state_list)

        df_state = all_data_df[all_data_df["State"] == state]

    # price availability
    with col2:
        price_min = df_state["Price"].min()
        price_max = df_state["Price"].max()

        price_values = st.slider("Select a Price range", int(price_min), int(price_max), (int(price_min), int(price_max)))
        
        price_start = price_values[0]
        price_end = price_values[1]
        
        df_price = df_state[(df_state["Price"]>= price_start) & (df_state["Price"]<= price_end)]

    # seat availability

    with col3:

        seat_list = list(sorted(df_price["Seats_Available"].unique()))

        seat_available = st.selectbox("Select the Seat Availability",seat_list)

        df_seat_avai = df_price[df_price["Seats_Available"] >= seat_available]

    # Second columns
    col1, col2, col3 =  st.columns(3)

    with col1:

        star_rating_min = df_seat_avai["Ratings"].min()
        star_rating_max = df_seat_avai["Ratings"].max()

        if star_rating_min == star_rating_max:
            
            df_rating = df_seat_avai[df_seat_avai["Ratings"] == star_rating_min]

        elif star_rating_min != star_rating_max:

            rating_values = st.slider("Select a rating range", star_rating_min, star_rating_max, (star_rating_min, star_rating_max))

            rating_start = rating_values[0]
            rating_end = rating_values[1]

            df_rating = df_seat_avai[(df_seat_avai["Ratings"] >= rating_start) & (df_seat_avai["Ratings"] <= rating_end)]

    with col2:

        route_name_list = sorted(df_rating["Route_name"].unique())

        route_name = st.selectbox("Select the Route Name", route_name_list)

        df_route_name = df_rating[df_rating["Route_name"] == route_name]

    with col3:
        
        bustype_list = sorted(df_route_name["Bus_type"].unique())

        bustype = st.selectbox("Select the Bus Type", bustype_list)

        df_bustype = df_route_name[df_route_name["Bus_type"] == bustype]
        df_bustype.reset_index(drop = True, inplace = True)

    
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        
    st.dataframe(df_bustype,use_container_width=True)
    
    
