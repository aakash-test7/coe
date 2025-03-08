### README Summary

This project is a Streamlit-based web application named **ChickpeaOmicsExplorer**, designed to explore and analyze omics data related to chickpea. The application provides various functionalities for searching, visualizing, and analyzing gene and protein data, along with user authentication and data management features.

---

### **File Structure and Functionality**

#### **1. `app.py`**
- **Purpose**: Main entry point for the Streamlit application.
- **Key Features**:
  - Sets up the page configuration and navigation bar.
  - Manages session state for page navigation and user authentication.
  - Integrates with `pages` module to load different pages based on user selection.
  - Provides a sidebar with external links and logout functionality.
  - Handles user authentication and redirects to appropriate pages.

#### **2. `backend.py`**
- **Purpose**: Backend logic for data processing, retrieval, and analysis.
- **Key Functions**:
  - **`generate_signed_url(blob_name)`**: Generates signed URLs for accessing files stored in Google Cloud Storage (GCS).
  - **`read_excel_from_gcs(bucket_name, blob_name, header=0)`**: Reads Excel files from GCS and returns them as pandas DataFrames.
  - **`normalize_data(data)`**: Normalizes data using log2 transformation.
  - **`format_sequence(seq)`**: Formats DNA/RNA sequences for display.
  - **`get_string_network_link(protein_transcript)`**: Fetches protein-protein interaction (PPI) network links from the STRING database.
  - **`filter_orthologs(tid)`** and **`filter_paralogs(tid)`**: Filters orthologs and paralogs based on transcript ID.
  - **`web_driver()`**: Initializes a headless Chrome web driver for web automation.
  - **`automate_Cultivated_task(tid)`** and **`automate_Wild_task(tid)`**: Automates SNP calling tasks for cultivated and wild chickpea varieties.
  - **`transcriptid_info(tid)`**: Displays detailed information about a transcript ID, including sequences, protein data, and SNP information.
  - **`user_input_menu(tid)`** and **`multi_user_input_menu(mtid)`**: Handles single and multiple transcript ID inputs, respectively, and displays relevant data.
  - **`process_locid(locid)`** and **`process_mlocid(mlocid)`**: Converts NCBI IDs to transcript IDs.
  - **`perf_chart(selected_tissues)`**: Displays performance charts for different tissues/stages.
  - **`svm_charts()`**: Visualizes SVM model performance metrics.
  - **`tsi_plot()`**: Plots Tissue Specificity Index (TSI) analysis.
  - **`img_to_base64()`** COnverts images to Base64 encodes strings.

#### **3. `__init__.py`**
- **Purpose**: Imports and makes available all page modules (e.g., `About_Us`, `Tutorials`, `Glossary`, etc.) for use in the main application.

#### **4. `About_Us.py`**
- **Purpose**: Displays information about the application and its developers.
- **Key Features**:
  - Provides a contact form with a mailto link for inquiries.

#### **5. `Citations.py`**
- **Purpose**: Displays citations and references used in the application.
- **Key Features**:
  - Lists sources and citations in a structured format.

#### **6. `Glossary.py`**
- **Purpose**: Provides a glossary of key terms and definitions related to chickpea omics.
- **Key Features**:
  - Allows users to search for terms used in the application and view their definitions.

#### **7. `footer_all.py`**
- **Purpose**: Defines the footer for all pages.
- **Key Features**:
  - Displays contact information and institutional logos.

#### **8. `home_page.py`**
- **Purpose**: Displays the home page of the application.
- **Key Features**:
  - Provides a brief introduction to the application.

#### **9. `login.py`**
- **Purpose**: Handles user login and registration.
- **Key Features**:
  - Provides interfaces for login and registration.
  - Validates user credentials and stores user information in a MySQL database.
  - Manages session state for authenticated users.

#### **10. `metadata.py`**
- **Purpose**: Displays meta-data and analytics from the backend.
- **Key Features**:
  - Visualizes performance and analysis plots.
  - Displays heatmaps and functional annotation plots.

#### **11. `search.py`**
- **Purpose**: Handles the search functionality for gene and protein data.
- **Key Features**:
  - Allows users to search by gene ID, multiple gene IDs, NCBI ID, or multiple NCBI IDs.
  - Displays detailed information about the searched genes, including sequences, protein data, and SNP information.
  - Logs search history for authenticated users.

#### **12. `security_login.py`**
- **Purpose**: Manages user authentication and database initialization.
- **Key Features**:
  - Initializes the MySQL database and creates necessary tables.
  - Validates user credentials during login.
  - Registers new users and stores their information in the database.
  - Provides basic statistics about the number of users and searches.

#### **13. `tutorials.py`**
- **Purpose**: Provides video tutorials on how to use the application.
- **Key Features**:
  - Displays video tutorials for navigation, single task, multi-task, glossary, and contact features.
  - Uses signed URLs to stream videos from GCS.

#### **14. `home.py`**
- **Purpose**: Strcutural components for `home_page.py`
- **Key Features**:
  - Customization options for headings, text and body.

#### **15. `gallery.py`**
- **Purpose**: Strcutural components for `home_page.py`
- **Key Features**:
  - Customization options for gallery and images.

#### **15. `about_us_html.py`**
- **Purpose**: Strcutural components for `about_us.py`
- **Key Features**:
  - Customization options for division containers and boxes.
  
---

### **Major Connections and Workflows**

1. **User Authentication**:
   - Users can log in or register through the `login.py` interface.
   - User credentials are stored in a MySQL database, and session state is managed using Streamlit's `st.session_state`.

2. **Data Retrieval and Processing**:
   - Data is stored in Google Cloud Storage (GCS) and retrieved using signed URLs generated by the `generate_signed_url` function.
   - The `backend.py` file handles data processing, including sequence formatting, SNP calling, and PPI network retrieval.

3. **Search Functionality**:
   - Users can search for gene or protein data using transcript IDs or NCBI IDs.
   - The `search.py` file handles the search logic, displaying detailed information about the searched genes and logging the search history for authenticated users.

4. **Visualization**:
   - The application provides various visualizations, including performance charts, heatmaps, and TSI plots, through the `metadata.py` and `backend.py` files.

5. **Navigation and Page Management**:
   - The `app.py` file manages page navigation and integrates with the `pages` module to load different pages based on user selection.

6. **Tutorials and Help**:
   - The `tutorials.py` file provides video tutorials to help users navigate and use the application effectively.

---

### **Dependencies**
- **Streamlit**: For building the web application.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Selenium**: For web automation tasks like SNP calling.
- **Google Cloud Storage**: For storing and retrieving data files.
- **MySQL**: For user authentication and search history management.
- **BeautifulSoup**: For parsing HTML content.

---

### **Workflow Summary**
1. **User Interaction**: Users interact with the application through the Streamlit interface, logging in or registering, and navigating through different pages.
2. **Data Retrieval**: Data is fetched from GCS and processed in the backend.
3. **Search and Analysis**: Users can search for specific genes or proteins, and the application displays detailed information and visualizations.
4. **Visualization**: The application provides various charts and plots to help users analyze the data.
5. **Tutorials**: Users can access video tutorials to learn how to use the application effectively.

---

This README provides a high-level overview of the application's structure, functionality, and workflows. For more detailed information, refer to the individual files and their respective comments.
