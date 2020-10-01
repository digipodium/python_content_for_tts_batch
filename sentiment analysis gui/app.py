import streamlit as st
from textblob import TextBlob

st.title("sentiment analysis app")

msg = st.text_area('Please add some english data here')
isclicked = st.button('analyse this data')

if isclicked and msg:
    with st.spinner('analysing'):
        blob = TextBlob(msg)
        results = {'positive':{},'negative':{},'neutral':{}}
        total_pol = []
        for sentence in blob.sentences:
            pol = sentence.sentiment.polarity
            total_pol.append(pol)
            if pol > 0:
                results['positive'][str(sentence)]= pol
            elif pol < 0:
                results['negative'][str(sentence)]= pol
            else:
                results['neutral'][str(sentence)]= pol
            

    # st.write(results)
    avg_pol = sum(total_pol)/len(total_pol)
    if avg_pol>0:
        answer = 'positive'
    elif avg_pol<0:
        answer = 'negative'
    else:
        answer='neutral' 
    st.success(f'your data has {avg_pol} which makes it {answer}')
# streamlit run app.py