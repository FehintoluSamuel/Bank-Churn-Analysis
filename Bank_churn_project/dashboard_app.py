# Set wide layout for screenshot friendliness
st.set_page_config(layout='wide')
st.title('📊 Bank Churn Full Dashboard')
# Load cleaned data
csv_path = csv_path = r'C:\Users\fehin\schlscrape_project\\Bank_churn_project\data_folder\cleaned_bank_churn_analysis.csv'
df = pd.read_csv(csv_path)
# ------------------- SECTION 1: Demographics -------------------
st.header('🌍 Gender & Country Distribution of Customers')
demographics_gender = df.groupby(['Geography', 'Gender']).size().reset_index(name='Number of Customers')
fig1 = px.bar(demographics_gender, x='Geography', y='Number of Customers', color='Gender', barmode='group',
              title='Gender Distribution across Countries')
st.plotly_chart(fig1, use_container_width=True)
country_counts = df['Geography'].value_counts().reset_index()
country_counts.columns = ['Country', 'Number of Customers']
fig2 = px.bar(country_counts, x='Country', y='Number of Customers', text='Number of Customers', color='Country',
              title='Number of Customers per Country')
st.plotly_chart(fig2, use_container_width=True)
# ------------------- SECTION 2: Age & Tenure Distributions -------------------
st.header('📈 Customers Age and Tenure Distributions by Country')
for country in country_counts['Country']:
    subset = df[df['Geography'] == country] 
    st.subheader(f"{country} - Age Distribution")
    st.plotly_chart(px.histogram(subset, x='Age', nbins=30, marginal="box",
                                  title=f'Age Distribution in {country}',
                                  color_discrete_sequence=['steelblue']), use_container_width=True)
    st.subheader(f"{country} - Tenure Distribution")
    st.plotly_chart(px.histogram(subset, x='Tenure', nbins=11,
                                  title=f'Tenure Distribution in {country}',
                                  color_discrete_sequence=['teal']), use_container_width=True)
# ------------------- SECTION 3: Customer Account Behaviour -------------------
st.header('💳 Customer Account Behaviour by Country')
for country in country_counts['Country']:
    subset = df[df['Geography'] == country]
    st.subheader(f"📍 {country}")
    st.plotly_chart(px.histogram(subset, x='Balance', nbins=30, title='Balance Distribution',
                                  color_discrete_sequence=['darkorange']), use_container_width=True)
    st.plotly_chart(px.histogram(subset, x='NumOfProducts', title='Number of Products Distribution',
                                  color_discrete_sequence=['royalblue']), use_container_width=True)
    st.plotly_chart(px.histogram(subset, x='HasCrCard', title='Credit Card Ownership',
                                  category_orders={'HasCrCard':[0,1]},
                                  labels={'HasCrCard':'Has Credit Card (0=No, 1=Yes)'},
                                  color_discrete_sequence=['purple']), use_container_width=True)
    st.plotly_chart(px.histogram(subset, x='IsActiveMember', title='Active Membership',
                                  category_orders={'IsActiveMember':[0,1]},
                                  labels={'IsActiveMember':'Active Member (0=No, 1=Yes)'},
                                  color_discrete_sequence=['green']), use_container_width=True)
    st.plotly_chart(px.histogram(subset, x='EstimatedSalary', nbins=30, title='Estimated Salary',
                                  color_discrete_sequence=['crimson']), use_container_width=True)
#
# ------------------- SECTION 4: Churn Comparison -------------------
st.header('🚪 Churners vs Non-Churners')

df['ChurnLabel'] = df['Exited'].map({0: 'Stayed', 1: 'Exited'})

fig_age = px.histogram(df, x='Age', color='ChurnLabel', barmode='overlay',
                       nbins=30, opacity=0.5, histnorm='density', title='Age: Churners vs Non-Churners')
st.plotly_chart(fig_age, use_container_width=True)

fig_balance = px.histogram(df, x='Balance', color='ChurnLabel', barmode='overlay',
                           nbins=30, opacity=0.5, histnorm='density', title='Balance: Churners vs Non-Churners')
st.plotly_chart(fig_balance, use_container_width=True)

fig_prods = px.histogram(df, x='NumOfProducts', color='ChurnLabel', barmode='group',
                         title='Products: Churners vs Non-Churners')
st.plotly_chart(fig_prods, use_container_width=True)

fig_cc = px.histogram(df, x='HasCrCard', color='ChurnLabel', barmode='group',
                      category_orders={'HasCrCard': [0, 1]},
                      labels={'HasCrCard':'Has Credit Card (0=No, 1=Yes)'},
                      title='Credit Card: Churners vs Non-Churners')
st.plotly_chart(fig_cc, use_container_width=True)
#
fig_active = px.histogram(df, x='IsActiveMember', color='ChurnLabel', barmode='group',
                          category_orders={'IsActiveMember':[0,1]},
                          labels={'IsActiveMember':'Active Member (0=No, 1=Yes)'},
                          title='Activity Level: Churners vs Non-Churners')
st.plotly_chart(fig_active, use_container_width=True)

fig_salary = px.histogram(df, x='EstimatedSalary', color='ChurnLabel', barmode='overlay',
                          nbins=30, opacity=0.5, histnorm='density',
                          title='Estimated Salary: Churners vs Non-Churners')
st.plotly_chart(fig_salary, use_container_width=True)
#
# ------------------- SECTION 5: Churn Feature Importance -------------------
st.header('🧠 Feature Importance (Random Forest)')
#
df_model = df.copy()
df_model['Gender'] = LabelEncoder().fit_transform(df_model['Gender'])
df_model = pd.get_dummies(df_model, columns=['Geography'], drop_first=True)
#
X = df_model.drop(columns=['Exited', 'ChurnLabel'])
y = df_model['Exited']
X_scaled = StandardScaler().fit_transform(X)
#
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_scaled, y)
#
feat_imp = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
fig_importance = px.bar(feat_imp, x=feat_imp.values, y=feat_imp.index, orientation='h',
                        title='Feature Importance in Predicting Churn',
                        labels={'x':'Importance', 'y':'Feature'})
st.plotly_chart(fig_importance, use_container_width=True)
