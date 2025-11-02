import streamlit as st
import time
from datetime import datetime

def fibonacci_generator(limit=None):
    """Generate Fibonacci sequence"""
    a, b = 0, 1
    count = 0
    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1

def main():
    # Page configuration
    st.set_page_config(
        page_title="Fibonacci Generator",
        page_icon="🔢",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for beautiful styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    .info-box {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header Section
    st.markdown('<h1 class="main-header">🔢 Fibonacci Sequence Generator by SURAJ </h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/1968/1968126.png", width=100)
        st.title("Navigation")
        st.markdown("---")
        
        st.header("📊 Statistics")
        if 'generation_count' not in st.session_state:
            st.session_state.generation_count = 0
        st.metric("Total Generations", st.session_state.generation_count)
        
        st.header("ℹ️ About Fibonacci")
        st.markdown("""
        The Fibonacci sequence is a famous series where each number is the sum of the two preceding ones:
        
        **0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...**
        
        **Mathematical Formula:**
        F(n) = F(n-1) + F(n-2)
        
        Found in nature, art, and computer science!
        """)
    
    # Main Content Area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("⚙️ Configuration")
        st.markdown("---")
        
        # Generation options
        option = st.radio(
            "**Select Generation Method:**",
            ["First N numbers", "Up to maximum value"],
            index=0
        )
        
        if option == "First N numbers":
            n = st.slider(
                "**How many Fibonacci numbers?**",
                min_value=1,
                max_value=50,
                value=10,
                help="Select how many numbers to generate from the sequence"
            )
        else:
            max_val = st.slider(
                "**Maximum value limit**",
                min_value=1,
                max_value=1000,
                value=100,
                help="Generate numbers up to this maximum value"
            )
        
        # Additional options
        st.subheader("🎨 Display Options")
        show_formula = st.checkbox("Show mathematical formula", value=True)
        show_stats = st.checkbox("Show sequence statistics", value=True)
    
    with col2:
        st.header("🚀 Generate & Results")
        st.markdown("---")
        
        # Generate button with cool animation
        if st.button("✨ Generate Fibonacci Sequence", use_container_width=True):
            with st.spinner("Calculating the magic of mathematics..."):
                time.sleep(1)  # For dramatic effect
                
                # Track generations
                st.session_state.generation_count += 1
                
                # Generate sequence
                if option == "First N numbers":
                    sequence = []
                    for i, num in enumerate(fibonacci_generator(n)):
                        sequence.append((i, num))
                    
                    # Display results
                    st.balloons()  # Celebration animation!
                    
                    with st.container():
                        st.markdown('<div class="result-box">', unsafe_allow_html=True)
                        st.subheader(f"📈 First {n} Fibonacci Numbers")
                        
                        # Show in columns for better layout
                        cols = st.columns(2)
                        with cols[0]:
                            for i, num in sequence[:len(sequence)//2]:
                                st.code(f"F({i:2d}) = {num:>8}")
                        with cols[1]:
                            for i, num in sequence[len(sequence)//2:]:
                                st.code(f"F({i:2d}) = {num:>8}")
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Statistics
                    if show_stats:
                        with st.container():
                            st.markdown('<div class="info-box">', unsafe_allow_html=True)
                            st.subheader("📊 Sequence Statistics")
                            col_stat1, col_stat2, col_stat3 = st.columns(3)
                            
                            with col_stat1:
                                st.metric("Total Numbers", n)
                            with col_stat2:
                                st.metric("Largest Number", sequence[-1][1])
                            with col_stat3:
                                st.metric("Sum", sum(num for _, num in sequence))
                            st.markdown('</div>', unsafe_allow_html=True)
                
                else:  # Up to maximum value
                    sequence = []
                    for num in fibonacci_generator():
                        if num > max_val:
                            break
                        sequence.append(num)
                    
                    st.balloons()
                    
                    with st.container():
                        st.markdown('<div class="result-box">', unsafe_allow_html=True)
                        st.subheader(f"📊 Fibonacci Numbers up to {max_val}")
                        
                        # Display sequence in a nice format
                        st.write("**Sequence:**")
                        sequence_text = ", ".join(map(str, sequence))
                        st.info(sequence_text)
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Statistics
                    if show_stats:
                        with st.container():
                            st.markdown('<div class="info-box">', unsafe_allow_html=True)
                            st.subheader("📊 Sequence Statistics")
                            col_stat1, col_stat2 = st.columns(2)
                            
                            with col_stat1:
                                st.metric("Total Numbers", len(sequence))
                                st.metric("Largest Number", sequence[-1])
                            with col_stat2:
                                st.metric("Sum", sum(sequence))
                                st.metric("Average", f"{sum(sequence)/len(sequence):.2f}")
                            st.markdown('</div>', unsafe_allow_html=True)
                
                # Mathematical formula
                if show_formula and len(sequence) > 2:
                    with st.container():
                        st.markdown("---")
                        st.subheader("🧮 Mathematical Formula")
                        st.latex(r"F(n) = F(n-1) + F(n-2)")
                        st.latex(r"F(0) = 0, \quad F(1) = 1")
                        
                        # Show last calculation
                        if option == "First N numbers" and n >= 3:
                            last_num = sequence[-1][1]
                            prev1 = sequence[-2][1]
                            prev2 = sequence[-3][1]
                            st.write(f"**Example:** {last_num} = {prev1} + {prev2}")
        
        # Instructions when no generation yet
        else:
            st.info("👆 Click the button above to generate your Fibonacci sequence!")
            st.image("https://media.giphy.com/media/3o7aCTPPm4OHfRLSH6/giphy.gif", width=300)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "Made by SURAJ MAURYA using Streamlit | "
        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()