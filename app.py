import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Gym Membership Recommendation System",
    page_icon="🏋️",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #F5F7FA;
}

.title {
    font-size: 40px;
    font-weight: bold;
    color: #FF4B4B;
    text-align: center;
}

.subtitle {
    font-size: 18px;
    text-align: center;
    color: gray;
}

.stButton > button {
    width: 100%;
    background: #FF4B4B;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    "<p class='title'>🏋 Gym Membership Recommendation System</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Find the Best Membership Plan According to Your Fitness Goals</p>",
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# SIDEBAR - USER INFORMATION
# =========================================================

st.sidebar.title("👤 User Information")

age = st.sidebar.slider(
    "Age",
    18,
    60,
    25
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

height = st.sidebar.number_input(
    "Height (cm)",
    min_value=140,
    max_value=220,
    value=170
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=35,
    max_value=180,
    value=70
)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    [
        "Weight Loss",
        "Muscle Gain",
        "General Fitness"
    ]
)

experience = st.sidebar.selectbox(
    "Workout Experience",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

budget = st.sidebar.slider(
    "Monthly Budget (₹)",
    1000,
    5000,
    2500,
    step=500
)

days = st.sidebar.slider(
    "Workout Days / Week",
    2,
    7,
    4
)

trainer = st.sidebar.selectbox(
    "Need Personal Trainer?",
    [
        "Yes",
        "No"
    ]
)

swimming = st.sidebar.selectbox(
    "Need Swimming Pool?",
    [
        "Yes",
        "No"
    ]
)


# =========================================================
# BMI CALCULATION
# =========================================================

height_meter = height / 100

bmi = weight / (height_meter * height_meter)

bmi = round(bmi, 2)


if bmi < 18.5:
    bmi_status = "Underweight"

elif bmi < 25:
    bmi_status = "Normal"

elif bmi < 30:
    bmi_status = "Overweight"

else:
    bmi_status = "Obese"


# =========================================================
# DISPLAY BMI
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "BMI",
        bmi
    )

with col2:
    st.metric(
        "BMI Category",
        bmi_status
    )

with col3:
    st.metric(
        "Workout Days",
        days
    )


st.divider()


# =========================================================
# USER DETAILS
# =========================================================

st.subheader("📋 Your Details")

user = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "Height": [height],
    "Weight": [weight],
    "Goal": [goal],
    "Experience": [experience],
    "Budget": [budget],
    "Workout Days": [days],
    "Trainer": [trainer],
    "Swimming": [swimming]
})

st.dataframe(
    user,
    width="stretch",
    hide_index=True
)


# =========================================================
# RECOMMEND BUTTON
# =========================================================

recommend = st.button("🏋 Recommend Membership")


# =========================================================
# RECOMMENDATION
# =========================================================

if recommend:

    # -----------------------------------------------------
    # Membership Recommendation
    # -----------------------------------------------------

    if budget <= 1500:

        membership = "🥉 Basic Membership"
        price = "₹1,500 / Month"

    elif budget <= 2500:

        membership = "🥈 Standard Membership"
        price = "₹2,500 / Month"

    elif budget <= 4000:

        membership = "🥇 Premium Membership"
        price = "₹4,000 / Month"

    else:

        membership = "💎 Elite Membership"
        price = "₹5,000 / Month"


    # -----------------------------------------------------
    # Trainer Requirement
    # -----------------------------------------------------

    if trainer == "Yes" and budget >= 3000:

        membership = "🥇 Premium Membership"
        price = "₹4,000 / Month"


    # -----------------------------------------------------
    # Swimming Requirement
    # -----------------------------------------------------

    if swimming == "Yes" and budget >= 5000:

        membership = "💎 Elite Membership"
        price = "₹5,000 / Month"


    # -----------------------------------------------------
    # Recommendation Result
    # -----------------------------------------------------

    st.success("Recommendation Generated Successfully!")

    st.header("🏆 Recommended Plan")

    col1, col2 = st.columns(2)


    # -----------------------------------------------------
    # PLAN DETAILS
    # -----------------------------------------------------

    with col1:

        st.info(f"### {membership}")

        st.write(
            f"**Monthly Cost:** {price}"
        )

        st.write(
            f"**BMI:** {bmi}"
        )

        st.write(
            f"**BMI Category:** {bmi_status}"
        )


    # -----------------------------------------------------
    # MEMBERSHIP BENEFITS
    # -----------------------------------------------------

    with col2:

        st.write("### Membership Benefits")


        if "Basic" in membership:

            st.write("✅ Gym Access")
            st.write("✅ Cardio Area")
            st.write("❌ Personal Trainer")
            st.write("❌ Swimming Pool")


        elif "Standard" in membership:

            st.write("✅ Gym Access")
            st.write("✅ Cardio Area")
            st.write("✅ Group Classes")
            st.write("❌ Swimming Pool")


        elif "Premium" in membership:

            st.write("✅ Gym Access")
            st.write("✅ Personal Trainer")
            st.write("✅ Group Classes")
            st.write("✅ Nutrition Guidance")


        else:

            st.write("✅ All Premium Features")
            st.write("✅ Swimming Pool")
            st.write("✅ Sauna")
            st.write("✅ VIP Lounge")
            st.write("✅ Personal Diet Coach")


    st.divider()


    # =====================================================
    # WORKOUT PLAN
    # =====================================================

    st.subheader("💪 Workout Plan")


    if goal == "Weight Loss":

        workout = [
            "🏃 30 mins Cardio",
            "🚴 Cycling",
            "🔥 HIIT Training",
            "🧘 Stretching"
        ]


    elif goal == "Muscle Gain":

        workout = [
            "🏋 Chest",
            "💪 Back",
            "🦵 Legs",
            "💥 Shoulders",
            "💪 Arms"
        ]


    else:

        workout = [
            "🚶 Walking",
            "🏃 Jogging",
            "🏋 Strength Training",
            "🧘 Yoga"
        ]


    for item in workout:

        st.write(item)


    st.divider()


    # =====================================================
    # DIET RECOMMENDATION
    # =====================================================

    st.subheader("🥗 Diet Recommendation")


    if goal == "Weight Loss":

        st.write("🥚 Egg Whites")
        st.write("🥗 Green Vegetables")
        st.write("🍎 Fruits")
        st.write("🥛 Low Fat Milk")
        st.write("🚰 Drink 3-4 Liters Water")


    elif goal == "Muscle Gain":

        st.write("🍗 Chicken Breast")
        st.write("🥚 Eggs")
        st.write("🍚 Rice")
        st.write("🥛 Milk")
        st.write("🥜 Dry Fruits")


    else:

        st.write("🥗 Balanced Diet")
        st.write("🍎 Fruits")
        st.write("🥛 Milk")
        st.write("🥩 Protein")
        st.write("🥦 Vegetables")


    st.divider()


    # =====================================================
    # MEMBERSHIP COMPARISON
    # =====================================================

    st.subheader("📊 Membership Comparison")


    # IMPORTANT:
    # प्रत्येक row मध्ये समान number of columns आहेत.
    # त्यामुळे "All arrays must be of the same length"
    # हा error येणार नाही.

    comparison_data = [

        {
            "Plan": "Basic",
            "Price": "₹1500",
            "Trainer": "❌",
            "Swimming": "❌",
            "Sauna": "❌"
        },

        {
            "Plan": "Standard",
            "Price": "₹2500",
            "Trainer": "❌",
            "Swimming": "❌",
            "Sauna": "❌"
        },

        {
            "Plan": "Premium",
            "Price": "₹4000",
            "Trainer": "✅",
            "Swimming": "❌",
            "Sauna": "❌"
        },

        {
            "Plan": "Elite",
            "Price": "₹5000",
            "Trainer": "✅",
            "Swimming": "✅",
            "Sauna": "✅"
        }

    ]


    table = pd.DataFrame(comparison_data)


    st.dataframe(
        table,
        width="stretch",
        hide_index=True
    )


    st.divider()


    # =====================================================
    # FITNESS OVERVIEW
    # =====================================================

    st.subheader("📈 Your Fitness Overview")


    chart = pd.DataFrame({

        "Category": [
            "BMI",
            "Workout Days",
            "Water Intake"
        ],

        "Value": [
            bmi,
            days,
            3
        ]

    })


    st.bar_chart(
        chart.set_index("Category")
    )


    # =====================================================
    # FINAL MESSAGE
    # =====================================================

    st.success(
        "🎉 Thank you for using the Gym Membership Recommendation System!"
    )