
import streamlit as st
import matplotlib.pyplot as plt
import math
import random

st.set_page_config(
    page_title="HeartAlchemy",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ HeartAlchemy")
st.subheader("Where simple lines transform into love ✨")

st.write("Create your own colourful mathematical heart!")

# Sidebar settings
st.sidebar.title("🎨 Customize Your Heart")

lines = st.sidebar.slider(
    "Number of Lines", 40, 240, 120
)

size = st.sidebar.slider(
    "Heart Size", 5, 25, 15
)

theme = st.sidebar.selectbox(
    "Choose Colour Theme",
    [
        "Pink & Purple",
        "Green Garden",
        "Red Romance",
        "Rainbow",
        "Ocean Blue",
        "Golden Glow",
        "Custom Colours"
    ]
)

# Colour themes
color_themes = {
    "Pink & Purple": [
        "#ff69b4", "#ff1493", "#da70d6",
        "#ba55d3", "#dda0dd"
    ],

    "Green Garden": [
        "#008000", "#90ee90", "#32cd32",
        "#00fa9a", "#adff2f"
    ],

    "Red Romance": [
        "#ff0000", "#dc143c", "#ff4d6d",
        "#ff69b4", "#ffb6c1"
    ],

    "Rainbow": [
        "#ff0000", "#ff9900", "#ffff00",
        "#00ff00", "#00bfff", "#8a2be2",
        "#ff00ff"
    ],

    "Ocean Blue": [
        "#0000ff", "#00bfff", "#40e0d0",
        "#1e90ff", "#87ceeb"
    ],

    "Golden Glow": [
        "#ffd700", "#ffaa00", "#ff8c00",
        "#fff0a5", "#f5deb3"
    ]
}

# Custom colour selection
if theme == "Custom Colours":
    st.sidebar.write("Pick your favourite colours:")

    custom_colors = []

    for i in range(3):
        color = st.sidebar.color_picker(
            f"Colour {i+1}",
            ["#ff1493", "#00ff00", "#8a2be2"][i]
        )
        custom_colors.append(color)

    colors = custom_colors

else:
    colors = color_themes[theme]

# Background selection
background = st.sidebar.selectbox(
    "Background Colour",
    ["Black", "White", "Navy Blue", "Dark Purple"]
)

background_colors = {
    "Black": "black",
    "White": "white",
    "Navy Blue": "#071426",
    "Dark Purple": "#160b25"
}

bg = background_colors[background]

# Draw button
if st.button("❤️ Create My Heart"):

    fig, ax = plt.subplots(figsize=(8, 8))

    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    for i in range(lines):

        angle = i * (math.pi * 2) / lines

        # Mathematical heart formula
        x = 16 * (math.sin(angle) ** 3) * size

        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        ) * size

        color = random.choice(colors)

        # Draw main line
        ax.plot(
            [0, x],
            [40, y],
            color=color,
            linewidth=1
        )

        # Draw decorative star lines
        for j in range(8):

            star_angle = -j * (math.pi / 4)

            x2 = x + 6 * math.cos(star_angle)
            y2 = y + 6 * math.sin(star_angle)

            ax.plot(
                [x, x2],
                [y, y2],
                color=color,
                linewidth=1
            )

    ax.axis("off")
    ax.set_aspect("equal")

    st.pyplot(fig, use_container_width=True)

    # Download artwork
    fig.savefig(
        "heartalchemy.png",
        facecolor=bg,
        bbox_inches="tight",
        dpi=200
    )

    with open("heartalchemy.png", "rb") as file:
        st.download_button(
            "⬇️ Download Your Heart",
            data=file,
            file_name="HeartAlchemy.png",
            mime="image/png"
        )

    plt.close(fig)

    st.success("Your beautiful HeartAlchemy is ready! ❤️")

st.markdown("---")

st.markdown(
    "<h4 style='text-align:center;'>"
    "Made with Python, Mathematics & Love ❤️"
    "</h4>",
    unsafe_allow_html=True
)
