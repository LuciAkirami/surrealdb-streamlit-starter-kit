import streamlit as st
import asyncio
from utils.db_connector import add_data, get_data, update_data, delete_data

async def main():
    st.title("Social Media Feed Application")

    # Add data section
    st.header("Add Data to Media Table")
    name = st.text_input("Name:")
    post = st.text_area("Post:")
    if st.button("Add"):
        if name and post:
            try:
                await add_data(name, post)
                st.success("Data added successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a name and post.")

    # Update data section
    st.header("Update Data in Media Table")
    update_name = st.text_input("Name to update:")
    new_post = st.text_area("Updated Post:")
    if st.button("Update"):
        if update_name and new_post:
            try:
                await update_data(update_name, new_post)
                st.success("Data updated successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a name and new post.")

    # Delete data section
    st.header("Delete Data from Media Table")
    delete_name = st.text_input("Name to delete:")
    if st.button("Delete"):
        if delete_name:
            try:
                await delete_data(delete_name)
                st.success("Data deleted successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a name to delete.")

    # Get data section
    st.header("Feed from Media Table")
    data = await get_data()
    data = data[0]['result']
    if data:
        st.subheader("Data in Media Table:")
        for row in data:
            name = '-'+row['name']
            post = row['post']

            # Styling the Post
            color1 = '#1AA3FF'

            st.markdown(f'\
            <div style = "border:2px solid {color1};border-radius:15px;padding: 10px;"> \
            <p style = "font-size:20px;">{post}</p>\
            <p style = "font-size:12px;">{name}</p>      \
            </div> \
                        ',unsafe_allow_html=True)
            st.markdown(f'<br>',unsafe_allow_html=True)
    else:
        st.warning("No data found in the Media table.")

if __name__ == "__main__":
    asyncio.run(main())
