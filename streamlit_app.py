
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Sovelluksen otsikko
st.title("Anti-strategia: Interaktiivinen simulaatio")

# Parametrien säätimet
num_accounts = st.slider("Tilien määrä", 10, 1000, 100, step=10)
num_rounds = st.slider("Kierrosten määrä", 10, 1000, 220, step=10)
win_prob = st.slider("Voiton todennäköisyys", 0.01, 0.5, 0.0625, step=0.005)
win_multiplier = st.slider("Voiton kerroin", 1.0, 5.0, 2.0, step=0.1)
loss_multiplier = st.slider("Tappion kerroin", 0.90, 1.0, 0.9867, step=0.001)

# Simulaatiofunktio
def simulate_strategy(num_accounts, num_rounds, win_prob, win_multiplier, loss_multiplier):
    final_balances = []
    for _ in range(num_accounts):
        balance = 1.0
        for _ in range(num_rounds):
            if np.random.random() < win_prob:
                balance *= win_multiplier
            else:
                balance *= loss_multiplier
        final_balances.append(balance)
    return final_balances

# Simulointi ja visualisointi
if st.button("Suorita simulaatio"):
    final_balances = simulate_strategy(num_accounts, num_rounds, win_prob, win_multiplier, loss_multiplier)
    st.subheader("Lopullisten saldojen jakauma")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(final_balances, bins=30, color='orchid', edgecolor='black')
    ax.set_xlabel("Lopullinen saldo")
    ax.set_ylabel("Tilien määrä")
    ax.set_title("Simulaatiotulos")
    st.pyplot(fig)

    st.write(f"**Keskimääräinen saldo:** {np.mean(final_balances):,.2f}")
    st.write(f"**Mediaani:** {np.median(final_balances):,.2f}")
    st.write(f"**Kuinka moni tili päätyi alle 1:** {(np.array(final_balances) < 1).sum()} / {num_accounts}")
    st.write(f"**Kuinka moni tili ylitti 1 000 000:** {(np.array(final_balances) > 1_000_000).sum()} / {num_accounts}")
