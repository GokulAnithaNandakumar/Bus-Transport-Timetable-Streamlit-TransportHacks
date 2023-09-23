import streamlit as st
import pandas as pd

#Transportation data can add many routes
transportation_data = {
    'Chennai-Bangalore': {
        'Stops': [
            'Chennai Central Bus Station',
            'Tambaram',
            'Chengalpattu',
            'Kanchipuram',
            'Vellore',
            'Krishnagiri',
            'Hosur',
            'Electronic City',
            'Silk Board',
            'Koramangala',
            'Majestic Bus Station',
            'Yeshwantpur',
            'Bangalore International Airport'
        ],
        'Departure Times': [
            '07:00 AM',
            '07:30 AM',
            '08:15 AM',
            '09:00 AM',
            '10:00 AM',
            '11:15 AM',
            '12:30 PM',
            '01:45 PM',
            '02:30 PM',
            '03:15 PM',
            '04:00 PM',
            '05:30 PM',
            '06:45 PM'
        ]
    },
    'Bangalore-Chennai': {
        'Stops': [
            'Bangalore International Airport',
            'Yeshwantpur',
            'Majestic Bus Station',
            'Koramangala',
            'Silk Board',
            'Electronic City',
            'Hosur',
            'Krishnagiri',
            'Vellore',
            'Kanchipuram',
            'Chengalpattu',
            'Tambaram',
            'Chennai Central Bus Station'
        ],
        'Departure Times': [
            '08:00 PM',
            '08:30 PM',
            '09:15 PM',
            '10:00 PM',
            '11:00 PM',
            '12:15 AM',
            '01:30 AM',
            '02:45 AM',
            '03:30 AM',
            '04:15 AM',
            '05:00 AM',
            '06:30 AM',
            '07:45 AM'
        ]

    },
    'Vellore-Chennai': {
        'Stops': ['Vellore', 'Kanchipuram', 'Chengalpattu', 'Tambaram', 'Chennai Central Bus Station'],
        'Departure Times': ['08:30 AM', '09:15 AM', '10:00 AM', '10:45 AM', '11:30 AM']
    },
    'Chennai to Vellore': {
        'Stops': ['Chennai Central Bus Station', 'Tambaram', 'Chengalpattu', 'Kanchipuram', 'Vellore'],
        'Departure Times': ['07:00 AM', '07:45 AM', '08:30 AM', '09:15 AM', '10:00 AM']
    },

    'Hyderabad-Chennai': {
        'Stops': [
            'Hyderabad Central Bus Station', 'Shamshabad', 'Mahbubnagar', 'Raichur', 'Yadgir', 'Gulbarga', 'Solapur',
            'Vijayapura', 'Bagalkot', 'Hubli', 'Dharwad', 'Belgaum', 'Kolhapur', 'Sangli', 'Satara', 'Karad', 'Pune',
            'Shirwal', 'Khed', 'Chakan', 'Talegaon', 'Lonavala', 'Kamshet', 'Vadgaon', 'Khandala', 'Karjat', 'Neral',
            'Bhivpuri Road', 'Shelu', 'Neral'
        ],
        'Departure Times': [
            '08:00 PM', '08:30 PM', '09:15 PM', '10:00 PM', '11:00 PM', '12:15 AM', '01:30 AM', '02:45 AM', '03:30 AM',
            '04:15 AM', '05:00 AM', '06:30 AM', '07:45 AM', '08:30 AM', '09:15 AM', '10:00 AM', '11:00 AM', '12:15 PM',
            '01:30 PM', '02:45 PM', '03:30 PM', '04:15 PM', '05:00 PM', '06:30 PM', '07:45 PM', '08:30 PM', '09:15 PM',
            '10:00 PM', '11:00PM', '12:00PM'
        ]
    },

    'Chennai-Hyderabad': {
        'Stops': [
            'Chennai Central Bus Station', 'Tambaram', 'Chengalpattu', 'Kanchipuram', 'Vellore', 'Chittoor', 'Tirupati',
            'Kadapa', 'Mydukur', 'Proddatur', 'Yerraguntla', 'Muddanur', 'Tadipatri', 'Gooty', 'Guntakal', 'Adoni',
            'Mantralayam Road', 'Raichur', 'Sindhnur', 'Gangawati', 'Koppal', 'Kushtagi', 'Hosapete', 'Hampi',
            'Kamalapur',
            'Hospet Junction', 'Munirabad', 'Koppal', 'Gadag Junction'
        ],
        'Departure Times': [
            '08:00 PM', '08:30 PM', '09:15 PM', '10:00 PM', '11:00 PM', '12:15 AM', '01:30 AM', '02:45 AM', '03:30 AM',
            '04:15 AM', '05:00 AM', '06:30 AM', '07:45 AM', '08:30 AM', '09:15 AM', '10:00 AM', '11:00 AM', '12:15 PM',
            '01:30 PM', '02:45 PM', '03:30 PM', '04:15 PM', '05:00 PM', '06:30 PM', '07:45 PM', '08:30 PM', '09:15 PM',
            '10:00 PM', '11:00PM'
        ]
    },

    'Madurai-Chennai': {
        'Stops': [
            'Madurai', 'Dindigul', 'Tiruchirappalli', 'Ariyalur', 'Perambalur', 'Thittakudi', 'Chidambaram', 'Sirkazhi',
            'Mayiladuthurai', 'Kuthalam', 'Aduthurai', 'Thanjavur', 'Tiruverumbur', 'Tiruchirappalli', 'Srirangam',
            'Valadi', 'Manaparai', 'Chatrapatti', 'Kulithalai', 'Musiri', 'Srirangam', 'Tiruchirappalli', 'Tirupattur',
            'Villupuram', 'Melmaruvathur', 'Chengalpattu', 'Tambaram', 'Chennai fussil Bus Terminus', 'Broadway',
            'Chennai Central Railway Station'
        ],
        'Departure Times': [
            '08:00 PM', '08:30 PM', '09:15 PM', '10:00 PM', '11:00 PM', '12:15 AM', '01:30 AM', '02:45 AM', '03:30 AM',
            '04:15 AM', '05:00 AM', '06:30 AM', '07:45 AM', '08:30 AM', '09:15 AM', '10:00 AM', '11:00 AM', '12:15 PM',
            '01:30 PM', '02:45 PM', '03:30 PM', '04:15 PM', '05:00 PM', '06:30 PM', '07:45 PM', '08:30 PM', '09:15 PM',
            '10:00 PM', '11:00 PM','12:00PM'
        ]
    },
    'Chennai-Madurai': {
        'Stops': [
            'Chennai Central Railway Station', 'Broadway', 'Chennai Mofussil Bus Terminus', 'Tambaram', 'Chengalpattu',
            'Melmaruvathur', 'Villupuram', 'Tirupattur', 'Tiruchirappalli', 'Srirangam', 'Musiri', 'Kulithalai',
            'Chatrapatti', 'Manaparai', 'Valadi', 'Srirangam', 'Tiruchirappalli', 'Thanjavur', 'Aduthurai', 'Kuthalam',
            'Mayiladuthurai', 'Sirkazhi', 'Chidambaram', 'Thittakudi', 'Perambalur', 'Ariyalur', 'Tiruchirappalli',
            'Dindigul', 'Madurai'
        ],
        'Departure Times': [
            '08:00 PM', '08:30 PM', '09:15 PM', '10:00 PM', '11:00 PM', '12:15 AM', '01:30 AM', '02:45 AM', '03:30 AM',
            '04:15 AM', '05:00 AM', '06:30 AM', '07:45 AM', '08:30 AM', '09:15 AM', '10:00 AM', '11:00 AM', '12:15 PM',
            '01:30 PM', '02:45 PM', '03:30 PM', '04:15 PM', '05:00 PM', '06:30 PM', '07:45 PM', '08:30 PM', '09:15 PM',
            '10:00 PM', '11:00 PM''12:00PM'
        ]
    },

    'Route': {
        'Stops': ['Stop 1', 'Stop 3', 'Stop 5','...'],
        'Departure Times': ['08:10 AM', '08:40 AM', '09:10 AM','...']
    }
}


st.title('Intercity Transportation Timetable')

#User input
selected_route = st.selectbox('Select a Route', list(transportation_data.keys()))


#retrieve timetable data for the route
def get_timetable(route):
    return transportation_data[route]


#Display timetable for route
if selected_route:
    timetable = get_timetable(selected_route)
    st.subheader(f'Timetable - {selected_route}')

    #Display stops and departure times in a table coulumns
    timetable_df = pd.DataFrame(timetable)
    st.table(timetable_df)

#User input Route Planning
st.sidebar.subheader('Route Planning')

all_stops = set()
for route_data in transportation_data.values():
    all_stops.update(route_data['Stops'])

start_stop = st.sidebar.selectbox('Starting Stop', sorted(all_stops), key='start')
end_stop = st.sidebar.selectbox('Ending Stop', sorted(all_stops), key='end')

if start_stop and end_stop:
    selected_stops = [start_stop, end_stop]
    st.sidebar.success(f'Planned Route: {start_stop} to {end_stop}')
    st.sidebar.write(f'Start: {start_stop}')
    st.sidebar.write(f'End: {end_stop}')
    st.sidebar.write('Intermediate Stops:')
    for stop in sorted(all_stops):
        if start_stop < stop < end_stop:
            st.sidebar.write(stop)

#Search Function
search_term = st.sidebar.text_input('Search for a Stop:')
if search_term:
    st.sidebar.subheader('Results:')
    for route, data in transportation_data.items():
        stops = data['Stops']
        if any(search_term.lower() in stop.lower() for stop in stops):
            st.sidebar.write(f'Route: {route}')
            st.sidebar.write(f'Stops: {", ".join(stops)}')

