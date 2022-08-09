op=model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])
